# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:56:33 2018

@author: Andrius
"""

import cv2
import timeit

# Formats:
# http://www.fourcc.org/codecs.php

videoCapture = cv2.VideoCapture('sample_MPEG4_xvid.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter( 'MyOutputVid.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, size )
#videoWriter = cv2.VideoWriter( 'MyOutputVid.flv', cv2.VideoWriter_fourcc('F','L','V','1'), fps, size )
#videoWriter = cv2.VideoWriter( 'MyOutputVid.flv', cv2.VideoWriter_fourcc(*'flv1'), fps, size )
#videoWriter = cv2.VideoWriter( 'MyOutputVid2.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size )
#videoWriter = cv2.VideoWriter( 'MyOutputVid2.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size )
#videoWriter = cv2.VideoWriter( 'MyOutputVid3.avi', cv2.VideoWriter_fourcc(*'xvid'), fps, size )

# cv2.VideoWriter_fourcc(*'i420') – .avi, uncompressed YUV, 4:2:0. 
# cv2.VideoWriter_fourcc(*'pim1') – .avi, MPEG-1
# cv2.VideoWriter_fourcc(*'xvid') – .avi, MPEG-4, good compression
# cv2.VideoWriter_fourcc(*'theo') – .ogv, Ogg Vorbis.
# cv2.VideoWriter_fourcc(*'flv1') – .flv, Flash video.
# cv2.VideoWriter_fourcc(*'mjpg') - .avi, 
# cv2.VideoWriter_fourcc(*'divx') - .avi,
# cv2.VideoWriter_fourcc(*'mp4v') - .mp4,

start = timeit.timeit()
success, frame = videoCapture.read()
while success: # Loop until there are no more frames.
    videoWriter.write(frame)
    success, frame = videoCapture.read()

videoWriter.release()
end = timeit.timeit()
print("Finished in %.4f s" % (end - start)) 