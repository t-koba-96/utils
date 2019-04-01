import os
import shutil
import cv2


#video file →　where the video exists
#image_dir  →  where the frame are made 
#image_file →　frame name

def video_2_frames(video_file='./worker_e.mp4', image_dir='./image/', image_file='%s.png'):
    # Delete the entire directory tree if it exists.
    if os.path.exists(image_dir):
        shutil.rmtree(image_dir)  

    # Make the directory if it doesn't exist.
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Video to frames
    i = 0
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        flag, frame = cap.read()  
        if flag == False:  
            break
        cv2.imwrite(image_dir+image_file % str(i).zfill(5), frame)  # ５桁の数字で保存　例：　1 →　00001
        print('Save', image_dir+image_file % str(i).zfill(5))
        i += 1

    print("Finish!")

    cap.release()  


video_2_frames()