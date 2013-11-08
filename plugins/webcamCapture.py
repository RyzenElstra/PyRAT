#!/usr/bin/env python
#-*- encoding:utf-8 -*-
# webcamCapture.py
 
from pygame.image import save
import pygame.camera as camera
from os import environ, mkdir, listdir
from time import strftime, gmtime
from platform import system
 
class WebcamCapture(object):
        def __init__(self):
                os = system()
                
                if os == 'Windows':
                        self.usuario = environ['USERNAME']
                else:
                        self.usuario = environ['USER']
 
                camera.init()
                misWebcams = camera.list_cameras()
 
                if len(misWebcams) == 0:
                        raise Exception('No hay webcam disponible.')
                        exit()
 
                elif len(misWebcams) == 1:
                        self.miWebcam = misWebcams[0]
 
                else:
                        for i in range(len(misWebcams)):
                                try:
                                        self.miWebcam = misWebcams[i]
                                        break
                                except:
                                        continue
 
        def capturar(self):
                try:
                        webcam = camera.Camera(self.miWebcam,(640,480))
                        webcam.start()
 
                        self.captura = webcam.get_image()
                        
                        webcam.stop()
                except Exception as e:
                        print e
 
        def guardarCaptura(self):
                if not 'webcam' in listdir('./'):
                        mkdir('webcam')
 
                tiempo = strftime("%d %b %Y_%H:%M:%S", gmtime())
                imagen = './webcam/' + self.usuario + '_' + tiempo + '.png'
 
                save(self.captura, imagen)
 
def main():
        wcCapture = WebcamCapture()
        wcCapture.capturar()
        wcCapture.guardarCaptura()
 
if __name__ == '__main__':
        main()
