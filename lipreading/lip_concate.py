import os
import numpy as np
import cv2
import  matplotlib.pyplot as plt

RESULT_PATH = './dataset/silent/'
Image_Path = './refined_images/silent/'

if not os.path.exists(RESULT_PATH):  # If the directory not exists, make it.
        os.makedirs(RESULT_PATH)
folder_list = os.listdir(Image_Path)
for classes in folder_list:
    class_path = Image_Path + classes + '/'
    res = RESULT_PATH + classes + '/'
    # if not os.path.exists(res):  # If the directory not exists, make it.
    #     os.makedirs(res)
    video_list = os.listdir(class_path)
    image_list = []
    print(classes)
    for category in video_list:
        # print(class_path+category)
        image = cv2.imread(class_path+category, cv2.IMREAD_COLOR)
        image_list.append(image)
    layer1 = np.concatenate((image_list[0],image_list[1], image_list[2], image_list[3], image_list[4]), axis=1)
    layer2 = np.concatenate(( image_list[5], image_list[6], image_list[7], image_list[8], image_list[9]), axis=1)
    layer3 = np.concatenate(( image_list[10], image_list[11], image_list[12], image_list[13], image_list[14]), axis=1)
    layer4 = np.concatenate((image_list[15], image_list[16], image_list[17], image_list[18], image_list[19]), axis=1)
    layer5 = np.concatenate((image_list[20], image_list[21], image_list[22], image_list[23], image_list[24]), axis=1)
    output = np.concatenate((layer1, layer2, layer3, layer4, layer5), axis=0)
    # plt.imshow(output)
    # plt.show()
    # print(RESULT_PATH+classes)

    cv2.imwrite(RESULT_PATH+classes+'.jpg', output)
    # print(res+classes)




