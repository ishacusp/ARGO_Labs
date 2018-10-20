# ARGO_Labs
This is a repository for all my work at ARGO Labs (in construction)

The goal of this project is to implement a traffic flow counter/count distinct objects for the streets of New York City
(2nd Avenue Street of NYC) using ENet Neural Network (pixel wise real-time semantic segmentation) and OpenCV. 

1. Package Requisities:

   a. OpenCV 3.4.1
    
   b. numpy
   
   c. argparse
   
   d. imutils
   
   e. time
   
   f. cv2

2. get_street_images.ipynb - jupyter notebook to download the Google Street View (GSV) images in the images folder and then turn those images to a video (MP4 file), which is saved in the videos folder(train.mp4). Get API Key for GSV images from [here](https://developers.google.com/maps/documentation/streetview/get-api-key)

3. segment.py - python file to run the segmentation algorithm on image files

4. segment_video.py - python file to run the segmentation algorithm on the train.mp4 file and count the number of distinct objects in each frame (here each video frame is a single image as the video itself is made of several images put together) of the video. The output of the segmentation is saved as "second_avenue_output_count.avi" in the output folder.

5. To run the segmentation on an image file:
   python segment.py --model enet-cityscapes/enet-model.net \
	--classes enet-cityscapes/enet-classes.txt \
	--colors enet-cityscapes/enet-colors.txt \
	--image images/image_name
	
6. To run the segmentation on the video file (mp4 in the videos folder):
   python segment_video.py --model enet-cityscapes/enet-model.net \
	--classes enet-cityscapes/enet-classes.txt \
	--colors enet-cityscapes/enet-colors.txt \
	--video videos/train.mp4 \
	--output output/second_avenue_output.avi
	
7. Legend:

![Legend](https://github.com/ishacusp/ARGO_Labs/blob/master/opencv-semantic-segmentation/legend_reference.jpg)

Reference: https://www.pyimagesearch.com/2018/09/03/semantic-segmentation-with-opencv-and-deep-learning


