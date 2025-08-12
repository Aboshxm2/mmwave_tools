import serial
import time
import sys

seconds = 3
if (len(sys.argv) > 1):
    seconds = int(sys.argv[1])

until = time.time() + seconds

print(f'Recording for {seconds} seconds. Until: {until}')

SERIAL_PORT = 'COM13'
OUTPUT_FILE = './output'

s = serial.Serial(SERIAL_PORT, baudrate=921600, timeout=0.1)

with open(OUTPUT_FILE, 'wb') as f:
    while until > time.time():
        b = s.read(4096)
        f.write(b)
        print(b)


s.close()
