import os
import numpy
import shutil

DIR_PATH = "./refined_images/silent/"

dir_list = os.listdir(DIR_PATH)
for folder in dir_list:
    images  = os.listdir(DIR_PATH+folder+'/')
    if(len(images)< 25):
        print(folder+" "+str(len(images)))
        # shutil.rmtree(DIR_PATH+folder)
