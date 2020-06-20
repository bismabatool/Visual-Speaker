import numpy as np
from keras import optimizers
import vggmodel
from tensorflow.keras.preprocessing import image as image_utils
from tensorflow.keras.models import load_model
import h5py
from keras.models import load_model
import cv2

# 15 is Next
# 16 is Previous
# 17 is start
# 18 is stop
# class_names=["Stop navigation", "Excuse me", "I am sorry", "Thank you", "Good bye", "I love this grace", "Nice to meet you",
#              "You are welcome", "How are you", "Have a good time", "Begin", "Choose", "Connection", "Navigation", "Next", "Previous", "Start", "Stop", "Hello", "Web"]
class_names = ["00", "01","02","03","04","05","06","07","08","09","slient"]
weights_path="1_rmsprop_new.h5"


model = load_model('model/model_weights_final.h5')

def predict_by_model(path):
    # example path = 'val/16/M01_words_06_01result.jpg'

    print("[INFO] loading and preprocessing image...")
    input_image = load_and_prcoess_image(path)
    # input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    prediction = model.predict(input_image)
    prediction_class = np.argmax(prediction, axis=1)
    print(class_names[prediction_class[0]])

    if(is_confidence_too_low(prediction)):
        print("Can you say again? Please")
        write_to_txt("result_lip/text.txt", "Can you say again? Please")

    else:
        print(class_names[prediction_class[0]])
        # print(prediction_class[0]+1)
        write_to_txt("result_lip/text.txt", class_names[prediction_class[0]])

    # ID of Good Bye is 5
    if(prediction_class[0]+1==5):
        return 0
    else:
        return 1

def load_and_prcoess_image(path):
    image = image_utils.load_img(path, target_size=(224,224), color_mode="grayscale")
    # image= image.reshape(224, 224, 1)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image_utils.img_to_array(image, data_format='channels_last')
    input_image = np.expand_dims(image, axis=0)/255
    return input_image

def is_confidence_too_low(prediction):
    prediction_class = np.argmax(prediction, axis=1)
    return prediction[0][prediction_class[0]]<0.5

def write_to_txt(name, words):
    with open(name, "w") as text_file:
        text_file.write(words)  

# predict_by_model("image.jpg")
