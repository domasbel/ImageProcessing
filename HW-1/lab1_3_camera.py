# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:56:33 2018

@author: Andrius
fps gerai veikia 10
"""

import cv2

cameraCapture = cv2.VideoCapture(0)
#fps = cameraCapture.get(cv2.CAP_PROP_FPS)
fps = 20 # an assumption
width=1280 # default: 640
height=720 # default: 480
cameraCapture.set(cv2.CAP_PROP_FPS, fps)
cameraCapture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cameraCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
size = (int(width), int(height))
videoWriter = cv2.VideoWriter('MyOutputVid4.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, size )

cnt = 0
while( cameraCapture.isOpened() ):
    # Capture frame-by-frame
    success, frame = cameraCapture.read()
    if success==True: 
        # # Convert to grayscale
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # # Convert back to BGR because players supports only BGR
        # frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)        
        videoWriter.write(frame)
        cnt = cnt + 1
            
    # Display the resulting frame
    cv2.imshow('Digital Image Processing',frame)
    if cv2.waitKey(1) & 0xFF == ord('w'): # press w to write single image
        cv2.imwrite('screenshot.png', frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cameraCapture.release()
videoWriter.release()
cv2.destroyAllWindows()


