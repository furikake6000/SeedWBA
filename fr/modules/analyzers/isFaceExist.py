# -*- coding: utf-8 -*-
import cv2
import time
from .facedetector import FaceDetector

class IsFaceExist(object):
    def __init__(self):
        self.fd = FaceDetector()
    
    def analyze(self, observation):
        facerect = self.fd.getFacerect(observation)
        if str(facerect) == "None": return
        if len(facerect) > 0:
            return 1.0
        else:
            return 0.0
