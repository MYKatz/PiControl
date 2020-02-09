import time
import uuid
import requests

import serial

import sys

reader = open('/dev/input/event0','rb')

endpoint = "http://localhost:3000" #where picontrol server is hosted

log = open("MyFile.txt","a") 

pi_address = str(uuid.getnode()) #48-bit integer string, Mac address

'''
register = requests.post(endpoint + "/api/pis/register/" + pi_address)
if register.status_code == 200:
    print("pi is registered :)")
else:
    raise Exception("failed to register pi -- please restart")
'''

code = ""

while True: #always be readin'

    buffer = fp.read(1)
    for c in buffer:
        if c > 0:
            print(c)
            if c == 30 : code = code + '1'
            elif c == 31 : code = code + '2'
            elif c == 32 : code = code + '3'
            elif c == 33 : code = code + '4'
            elif c == 34 : code = code + '5'
            elif c == 35 : code = code + '6'
            elif c == 36 : code = code + '7'
            elif c == 37 : code = code + '8'
            elif c == 38 : code = code + '9'
            elif c == 39 : code = code + '0'
            elif c == 40 :
                print('code:' + code) # debug

                code = ''

    # Try again if no card is available.
    '''
    if nfc_uid is not None:

        sendReq = requests.post("%s/api/scanticket/%s?serial=%s" % (endpoint, pi_address, nfc_uid))
        if sendReq.status_code != 200:
            print("something went wrong")

        #TODO: do something with the cube's colors -- tooodooo
    '''
