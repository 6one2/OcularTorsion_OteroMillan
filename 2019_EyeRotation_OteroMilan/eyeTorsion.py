# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np


#%% read video file

readfile = '/Users/sebastienvillard/Documents/LawsonImaging/Expes/2018_EyePosition/EyeRotationVideo/GVS_2Hz.avi'

cap = cv2.VideoCapture(readfile)

#%% show video
while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    # press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything is done, release the video cap
cap.release()

# Close all the frames
cv2.destroyAllWindows()

