#!/usr/bin/env python
#-*- encoding:utf-8 -*-
# screenshot.py
 
from PyQt4.QtGui import QApplication, QPixmap
from os import environ, mkdir, listdir
from sys import argv
from time import strftime, gmtime
 
class Screenshot(object):
        def __init__(self):  
                self.usuario = environ['USER']
                if not 'screenshot' in listdir('./'):
                        mkdir('screenshot')
 
        def capturarPantalla(self):
                time = strftime("%d %b %Y_%H:%M:%S", gmtime())
                imagen = './screenshot/' + self.usuario + '_' + time + '.png'
 
                app = QApplication(argv)
                winId = QApplication.desktop().winId()
                width = QApplication.desktop().screenGeometry().width()
                height = QApplication.desktop().screenGeometry().height()
 
                captura = QPixmap.grabWindow(winId, 0, 0, width, height)
 
                captura.save(imagen)
 
def main():
        ss = Screenshot()
        ss.capturarPantalla()
 
if __name__ == '__main__':
        main()