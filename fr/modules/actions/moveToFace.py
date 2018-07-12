# -*- coding: utf-8 -*-
import cv2
import math
from ..submodules.facedetector import FaceDetector

class Noaction(object):
    def __init__(self):
        self.fd = FaceDetector()

    def activate(self):
        # Called when action activated
        return {}
    
    def update(self):
        act = {
            "wheelleft": 0.0,
            "wheelright": 0.0
        }
        # Called every frame while action is activated
        if str(self.fd.biggestFaceRect) != "None":
            # If face exists
            x, _ = self.fd.biggestFaceRectPosNormalized(None)
            size = self.fd.biggestFaceSizeNormalized(None)
            if abs(x) > 0.3:
                if x > 0:
                    # Rotate to left
                    act["wheelleft"] -= 0.1
                    act["wheelright"] += 0.1
                else:
                    # Rotate to right
                    act["wheelleft"] += 0.1
                    act["wheelright"] -= 0.1
            if size < 0.1:
                # Move forward
                act["wheelleft"] += 0.1
                act["wheelright"] += 0.1

    def deactivate(self):
        # Called when action deactivated
        return {}