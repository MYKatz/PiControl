import board
import busio

# Additional import needed for I2C/SPI
#from digitalio import DigitalInOut
#
# NOTE: pick the import that matches the interface being used
#
from adafruit_pn532.adafruit_pn532 import MIFARE_CMD_AUTH_B
from adafruit_pn532.i2c import PN532_I2C
import Adafruit_PN532 as PN532
#from adafruit_pn532.spi import PN532_SPI
#from adafruit_pn532.uart import PN532_UART

#These imports aren't needed for NFC
#But they are needed for what we wanna do
import time
import uuid
import pickledb

#Environment vars
endpoint = "localhost:3000" #where to send pings
delay = 0.1 #seconds, delay between scans

# GPIO 18, pin 12
CS   = 18
# GPIO 23, pin 16
MOSI = 23
# GPIO 24, pin 18
MISO = 24
# GPIO 25, pin 22
SCLK = 25


# I2C connection:
#i2c = busio.I2C(board.SCL, board.SDA)

# Non-hardware reset/request with I2C
#pn532 = PN532_I2C(i2c, debug=False)
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
pn532.SAM_configuration()

# With I2C, we recommend connecting RSTPD_N (reset) to a digital pin for manual
# harware reset
#reset_pin = DigitalInOut(board.D6)
# On Raspberry Pi, you must also connect a pin to P32 "H_Request" for hardware
# wakeup! this means we don't need to do the I2C clock-stretch thing
#req_pin = DigitalInOut(board.D12)
#pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

# SPI connection:
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#cs_pin = DigitalInOut(board.D5)
#pn532 = PN532_SPI(spi, cs_pin, debug=False)

# UART connection
#uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=100)
#pn532 = PN532_UART(uart, debug=False)

ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()

print('Waiting for RFID/NFC card to write to!')

# Afaik key is only used for authentication
# key = b'\xFF\xFF\xFF\xFF\xFF\xFF'

while True: #always be readin'

    # Check if a card is available to read
    nfc_uid = pn532.read_passive_target(timeout=0.5)
    print('.', end="")
    # Try again if no card is available.
    if nfc_uid is not None:
        print('Found card with UID:', [hex(i) for i in uid])
        nfc_uid_string = ":".join([hex(i) for i in uid]) #NFC hex address

        pi_address = str(uuid.getnode) #48-bit integer string, Mac address

        #TODO: do something with the nfc uid and the pi's mac address
        #TODO: do something with the cube's colors

        time.sleep(delay) #short delay before reading again

print("")

print('Found card with UID:', [hex(i) for i in uid])