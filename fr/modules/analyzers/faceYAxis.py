# -*- coding: utf-8 -*-
import cv2
from .facedetector import FaceDetector

class FaceYAxis(object):
    def __init__(self):
        self.fd = FaceDetector()
    
    def analyze(self, observation):
        _, y = self.fd.biggestFaceRectPosNormalized(observation)
        return y
