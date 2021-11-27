import serial
from ast import literal_eval

ARDUINO_USB_PORT = '/dev/cu.usbserial-1410'
SPEED_USB_PORT = 9600

with serial.Serial(ARDUINO_USB_PORT, SPEED_USB_PORT, timeout=1.0) as ser:
    lst = []
    count = 0
    val = 1
    while count < 10:
        # ser.write('1'.encode())
        ser.write(str(val).encode())
        # res = ser.readline()
        res = ser.readline().decode('utf-8')

        if res:
            count += 1
            lst.append(literal_eval(res))
            # lst.append(res)
            print(res)
        else:
            print('No Data')

    print(lst)

temp = []

for i in lst:
    temp.append(i['TEMPERATURE'])
print(temp)
