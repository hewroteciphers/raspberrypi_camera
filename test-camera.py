#!/usr/bin/env python

import picamera

class Camera(object):
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1366,1024)
        self.camera.vflip = False
        self.camera.hflip = False
        self.camera.rotation = 90

    def snap(self, filename):
        self.camera.capture(filename)
        return filename

if __name__ == '__main__':
    cam = Camera()
    cam.snap('picam1.jpg')
