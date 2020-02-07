import time
import uuid
import requests

import serial

#import pickledb

#Environment vars
endpoint = "http://localhost:3000" #where picontrol server is hosted

log = open("MyFile.txt","a") 

pi_address = str(uuid.getnode()) #48-bit integer string, Mac address

ser = serial.Serial('/dev/ttyUSB4',19200, timeout = 5)

'''
register = requests.post(endpoint + "/api/pis/register/" + pi_address)
if register.status_code == 200:
    print("pi is registered :)")
else:
    raise Exception("failed to register pi -- please restart")
'''

while True: #always be readin'

    nfc_uid = ser.readline() #input("card uid: ")

    log.write(nfc_uid)

    # Try again if no card is available.
    '''
    if nfc_uid is not None:

        sendReq = requests.post("%s/api/scanticket/%s?serial=%s" % (endpoint, pi_address, nfc_uid))
        if sendReq.status_code != 200:
            print("something went wrong")

        #TODO: do something with the cube's colors -- tooodooo
    '''
