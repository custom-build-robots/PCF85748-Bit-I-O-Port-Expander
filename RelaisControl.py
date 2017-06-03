#!/usr/bin/env python
# coding: latin-1
# Autor:   Ingmar Stapel
# Datum:   20170603
# Version:   1.0
# Homepage:   http://custom-build-robots.com
# Dieses Programm ist das sogenannte Test Programm fuer ein Relais.
# Es wird ueber die Konsole und Tastatur vom PC aus via SSH bedient.
# Ich habe dieses Programm fuer den Raspberry Pi entworfen.
# Verwendet habe ich Raspbian Jessie.


# Es werden verschiedene Python Klassen importiert deren Funktionen
# im Programm benoetigt werden fuer die Programmverarbeitung.
import sys, tty, termios, os, readchar, time

# Importieren der PCF8574 Bibliothek für die Ansteuerung des Chips
# Die verwendete pcf8574 ist hier erhaeltlich:
# https://github.com/flyte/pcf8574
from pcf8574 import PCF8574

# Setzen des SMB Bus
i2c_port_num = 1

# Setzen der I2C Adresse des PCF8574 Boards
pcf_address = 0x38

# Initialisieren
pcf = PCF8574(i2c_port_num, pcf_address)

# Loesche den Bildschirminhalt
os.system('clear')
   
# Diese Schleife schaltet die Ausgaenge nacheinander Aktiv und
# deaktiviert diese wieder. Die Ausgabe zeigt den Kanal und Status
# des Ausganges des PCF8574 an.
for i in range(0, 7):
   print("########### PCF8574 Test-Programm ###########")

   print("Setze den Kanal: ",i," auf den Status: True.")
   pcf.port[i] = True
   print("Lese  den Kanal: ",i," mit dem Status: ",pcf.port[i])
   time.sleep(1)
   print("Setze den Kanal: ",i," auf den Status: Flase.")
   pcf.port[i] = False
   print("Lese  den Kanal: ",i," mit dem Status: ",pcf.port[i])
   time.sleep(1)
   os.system('clear')
 
# Ende des Programmes
