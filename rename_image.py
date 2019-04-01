import os
import shutil
import cv2


#change the videos name here  "video_file='./video_name'

def change_frame_names(start,length,video_file='./test/', image_dir='./image/', image_file='%s.png'):
    # Delete the entire directory tree if it exists.
    if os.path.exists(image_dir):
        shutil.rmtree(image_dir)  

    # Make the directory if it doesn't exist.
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # change frame names
    s=start
    for i in range(length):

        img=cv2.imread(video_file+image_file % str(s).zfill(5))
        cv2.imwrite(image_dir+image_file % str(i).zfill(5), img)  # Save a frame
        print('Save', image_dir+image_file % str(i).zfill(5))
        s += 1

    print("Finish!")

##  change here  (start_frame_num,total_frame)
change_frame_names(27091,2400)