import os

DATA_PATH = './dataset/'       # Dataset path
counter =0
dir_list = os.listdir(DATA_PATH)


for dir_name in dir_list:
    v_path = DATA_PATH + dir_name+'/'

    video_list = os.listdir(v_path)     # Read video list
    print(v_path+" videos: "+str(len(video_list)))
    counter+=len(video_list)
    # for vid_name in video_list:

print(counter)
