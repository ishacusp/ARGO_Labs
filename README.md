# ARGO_Labs
This is a repository for all my work at ARGO Labs 

The goal of this project is to, by leveraging, the segmentation and classification approach as described in the [pyimagesearch blogpost](https://www.pyimagesearch.com/2018/09/03/semantic-segmentation-with-opencv-and-deep-learning), count the number of distinct objects along 2nd Avenue in Manhattan.


### To use this repository (instructions in construction)
1. First download the source code from this post: [pyimagesearch blogpost](https://www.pyimagesearch.com/2018/09/03/semantic-segmentation-with-opencv-and-deep-learning)

2. Make sure that you have OpenCV 3.4.1 or higher version and have following necessary packages installed:

   a. numpy
   
   b. argparse
   
   c. imutils
   
   d. time
   
   e. cv2
  
3. After that replace the segment.py file given through the source code **with the segment.py of this repository**

4 Follow getstreet.py or getstreet.ipynb file in this repository to download the Google Street View (GSV) images in the images folder. Get API Key for GSV images from [here](https://developers.google.com/maps/documentation/streetview/get-api-key)

5. Once the GSV images are installed, change the image file path in segment.py

6. Then Run: python segment.py --model enet-cityscapes/enet-model.net \
	--classes enet-cityscapes/enet-classes.txt \
	--colors enet-cityscapes/enet-colors.txt \
	--image images/image_name
