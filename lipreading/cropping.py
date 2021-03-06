import dlib
import cv2
import os
import imutils
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import faceAlignment as fas

# Some constants
RESULT_PATH = './images/'       # The path that the result images will be saved

DATA_PATH = './data/'       # Dataset path
LOG_PATH = 'log_aligned.txt'            # The path for the working log file
RESIZE = (35, 35)                # Final image size
logfile = open(LOG_PATH,'w')
# Face detector and landmark detector
face_detector = dlib.get_frontal_face_detector()
landmark_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
fa = FaceAligner(landmark_detector)
angle = 270;


def shape_to_list(shape):
	coords = []
	for i in range(0, 68):
		coords.append((shape.part(i).x, shape.part(i).y))
	return coords
dir_list = os.listdir(DATA_PATH)
counter = 0
for dir_name in dir_list:
    v_path = DATA_PATH + dir_name+'/'
    res = RESULT_PATH + dir_name+'/'
    if not os.path.exists(res):  # If the directory not exists, make it.
        os.makedirs(res)

    video_list = os.listdir(v_path)     # Read video list
    for vid_name in video_list:
        vid_path = v_path+vid_name
        print(str(counter) + ": " + vid_path)

        vid = cv2.VideoCapture(vid_path)       # Read video

        directory = res + vid_name + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)
            # Parse into frames
            frame_buffer = []               # A list to hold frame images
            frame_buffer_color = []         # A list to hold original frame images
            while(True):
                # for i in range(0,24):
                success, frame = vid.read()
                if not success:
                    break                           # Break if no frame to read left
                frame = imutils.rotate(frame, angle)
                gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # Convert image into grayscale
                frame_buffer.append(gray)                  # Add image to the frame buffer
                frame_buffer_color.append(frame)
                # cv2.imshow("frame", gray)
                # key = cv2.waitKey(1)
                # if key == 27:
                #     break
            vid.release()


            # Obtain face landmark information
            landmark_buffer = []        # A list to hold face landmark information
            # Crop images
            cropped_buffer = []
            for (i, image) in enumerate(frame_buffer):          # Iterate on frame buffer
                face_rects = face_detector(image,1)             # Detect face
                if len(face_rects) < 1:                 # No face detected
                    print("No face detected: ",vid_path)
                    logfile.write(vid_path + " : No face detected \r\n")
                    break
                if len(face_rects) > 1:                  # Too many face detected
                    print("Too many face: ",vid_path)
                    logfile.write(vid_path + " : Too many face detected \r\n")
                    break
                rect = face_rects[0]                    # Proper number of face
                # (x, y, w, h) = rect_to_bb(rect)
                # faceAligned = fa.align(frame_buffer_color[i], image, rect)

                try:
                    cropped = fas.gen_align_lip_from_video(frame_buffer_color[i])
                    if cropped is None:
                        break
                    cropped = cv2.resize(cropped, (RESIZE[0], RESIZE[1]), interpolation=cv2.INTER_CUBIC)  # Resize
                    # cropped_buffer.append(cropped)
                    # for (i, image) in enumerate(cropped_buffer):

                    cv2.imwrite(directory + "%d" % (i + 1) + ".jpg", cropped)  # Write lip image
                except:
                    print("exception")
                # cv2.imwrite("./pictures/" + "%d" % (i + 1) + ".jpg", crop)
                # landmark = landmark_detector(faceAligned, rect)   # Detect face landmarks
                # landmark = shape_to_list(landmark)
                # landmark_buffer.append(landmark)

            # Crop images
            # cropped_buffer = []
            # for (i,landmark) in enumerate(landmark_buffer):
            #     lip_landmark = landmark[48:68]                                          # Landmark corresponding to lip
            #     lip_x = sorted(lip_landmark,key = lambda pointx: pointx[0])             # Lip landmark sorted for determining lip region
            #     lip_y = sorted(lip_landmark, key = lambda pointy: pointy[1])
            #     x_add = int((-lip_x[0][0]+lip_x[-1][0])*LIP_MARGIN)                     # Determine Margins for lip-only image
            #     y_add = int((-lip_y[0][1]+lip_y[-1][1])*LIP_MARGIN)
            #     crop_pos = (lip_x[0][0]-x_add, lip_x[-1][0]+x_add, lip_y[0][1]-y_add, lip_y[-1][1]+y_add)   # Crop image
            #     # (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
            #     # roi = image[y:y + h, x:x + w]

            #
            #     cropped = frame_buffer_color[i][crop_pos[2]:crop_pos[3],crop_pos[0]:crop_pos[1]]
            #     cropped = cv2.resize(cropped,(RESIZE[0],RESIZE[1]),interpolation=cv2.INTER_CUBIC)        # Resize
            #     cropped_buffer.append(cropped)


        counter=counter+1
logfile.close()
# print(counter)
