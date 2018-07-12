# -*- coding: utf-8 -*-
import cv2
from ..submodules.facedetector import FaceDetector

class FaceYAxis(object):
    def __init__(self):
        self.fd = FaceDetector()
    
    def __call__(self, observation):
        _, y = self.fd.biggestFaceRectPosNormalized(observation)
        return y
