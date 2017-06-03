# Raspberry Pi & PCF85748-Bit-I-O-Port-Expander
This is a test program for the PCF85748  8-Bit I/O Port-Expander.
I developed the program on a Raspberry Pi with Raspbian Jessie as OS.
I used for my test program the project from https://github.com/flyte/pcf8574 which makes the control of the PCF85748 very easy.

The picture below shows the PCF85748 and the 4-way relais.

![PCF85748-Bit-I-O-Port-Expander](https://custom-build-robots.com/wp-content/uploads/2017/06/PCF8574-test-setup-01-300x239.jpg)

## Raspberry Pi - controlling a Relais
I am using the program "RelaisControl.py" to control the switch state of my 4 way relais. The realis is connect to the pins 1 - 4 of the PCF85748 8-Bit I/O Port-Expander. I use the board in my robots to switch on / off a metal detector or an IR-flood light.

![Screenshot RelaisControl.py program](https://custom-build-robots.com/wp-content/uploads/2017/06/PCF8574-test-program-300x190.jpg)

## Setup
The picture below shows the setup with the Raspberry Pi, the 4-way relais and the PCF85748-Bit-I-O-Port-Expander on the right cardboard. On the left cardboard you see the Raspberry Pi and some other electronics I used for a different setup and test.

![PCF85748 setup with 4-way relais](https://custom-build-robots.com/wp-content/uploads/2017/06/PCF8574-test-setup-01-300x239.jpg)
