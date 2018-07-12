# -*- coding: utf-8 -*-
import cv2
import time
from ..submodules.facedetector import FaceDetector

class IsFaceExist(object):
    def __init__(self):
        self.fd = FaceDetector()
    
    def __call__(self, observation):
        facerect = self.fd.getFacerect(observation)
        if str(facerect) == "None": return
        if len(facerect) > 0:
            return 1.0
        else:
            return 0.0
