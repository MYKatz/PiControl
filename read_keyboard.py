import time
import uuid
import requests

import sys
import os

import struct

import RPi.GPIO as GPIO

struct_format = "LI0LHHI"

reader = open('/dev/input/event0','rb')

endpoint = "https://picontrol.treehacks.com/" #where picontrol server is hosted
if os.environ.get("API_ENDPOINT"):
    endpoint = os.environ.get("API_ENDPOINT")

##Rpi i/o stuff

#GPIO.cleanup()

LED_PIN = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

def blink():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED_PIN, GPIO.LOW)



log = open("log.txt","a") 

pi_address = str(uuid.getnode()) #48-bit integer string, Mac address


register = requests.post(endpoint + "/api/pis/register/" + pi_address)

while register.status_code != 200:
    register = requests.post(endpoint + "/api/pis/register/" + pi_address)
    time.sleep(15)

if register.status_code == 200:
    print("pi is registered :)")


scancodes = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'q', 17: u'w', 18: u'e', 19: u'r',
    20: u't', 21: u'y', 22: u'u', 23: u'i', 24: u'o', 25: u'p', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'a', 31: u's', 32: u'd', 33: u'f', 34: u'g', 35: u'h', 36: u'j', 37: u'k', 38: u'l', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'z', 45: u'x', 46: u'c', 47: u'v', 48: u'b', 49: u'n',
    50: u'm', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
}


scannedCode = ""
while True: #always be readin'

    buffer = reader.read(struct.calcsize(struct_format))
    (tv_sec, tv_usec, type, code, value) = struct.unpack(struct_format, buffer)
    #print(tv_sec, tv_usec, type, code, value)
    
    if type == 1: # keypress type for yarongtech scanner
        if code == 28:
            if len(scannedCode) < 4: #hacky fix for random enters after scanning card
                scannedCode = ""
                continue
            #enter
            print(scannedCode)

            log.write(str(scannedCode) + "\n")

            sendReq = requests.post("%s/api/scanticket/%s?serial=%s" % (endpoint, pi_address, scannedCode))
            if sendReq.status_code != 200:
                print("something went wrong")

            scannedCode = ""

            #TODO: maybe make this run concurrently so it doesn't block the main loop
            #But this is relatively low priority I think cause 
            blink() 

        elif value == 1:
            scannedCode += str(scancodes[code])

GPIO.cleanup()
