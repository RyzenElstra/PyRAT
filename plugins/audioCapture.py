#!/usr/bin/python
# -*- coding: utf-8 -*-
# audioCapture.py

from alsaaudio import PCM, PCM_CAPTURE, PCM_FORMAT_S16_LE
import wave
from os import environ, mkdir, listdir
from time import strftime, gmtime
from platform import system

class AudioCapture(object):
	def __init__(self):
		os = system()
		
		if os == 'Windows':
			self.usuario = environ['USERNAME']
		else:
			self.usuario = environ['USER']
		
		try:
			self.capturarAudio()
			self.guardarAudio()
		except Exception as e:
			print e

	def capturarAudio(self):
		self.captura = PCM(PCM_CAPTURE)
		self.captura.setchannels(1) # default 2
		self.captura.setrate(44100) # default 44100
		self.captura.setformat(PCM_FORMAT_S16_LE) # default PCM_FORMAT_S16_LE
		self.captura.setperiodsize(1024) # default 32

	def guardarAudio(self):
		if not 'audio' in listdir('./'):
			mkdir('audio')

		tiempo = strftime("%d %b %Y_%H:%M:%S", gmtime())
		miAudio = './audio/' + self.usuario + '_' + tiempo + '.wav'

		audio = wave.open(miAudio, 'w')
		audio.setnchannels(1)
		audio.setsampwidth(2)
		audio.setframerate(44100)

		while True:
			try:
				length, data = self.captura.read()
				audio.writeframes(data)
			except KeyboardInterrupt:
				break

def main():
	audioCapture = AudioCapture()

if __name__ == '__main__':
	main()
