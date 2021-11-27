import serial
from ast import literal_eval

ARDUINO_USB_PORT = '/dev/cu.usbserial-1410'
SPEED_USB_PORT = 9600


# with serial.Serial(ARDUINO_USB_PORT, SPEED_USB_PORT, timeout=1.0) as ser:
#     lst = []
#     count = 0
#     val = 1
#     while count < 10:
#         # ser.write('1'.encode())
#         ser.write(str(val).encode())
#         # res = ser.readline()
#         res = ser.readline().decode('utf-8')
#
#         if res:
#             count += 1
#             lst.append(literal_eval(res))
#             # lst.append(res)
#             print(res)
#         else:
#             print('No Data')
#
#     print(lst)
#
# temp = []
#
# for i in lst:
#     temp.append(i['TEMPERATURE'])
# print(temp)


def get_value(sensor=None, attr: str = '1', count_values: int = 10, count_to_error: int = 20,) -> list:
    # sensor is a class in future
    temp = []
    counter = 0
    count_values += 1

    with serial.Serial(ARDUINO_USB_PORT, SPEED_USB_PORT, timeout=1.0) as port:
        while counter < count_values:
            if counter < count_values:
                port.write(str(b'1').encode())  # change command
                com_data = port.readline().decode('utf-8')
                print(counter, com_data)
                if com_data:
                    temp.append(literal_eval(com_data))
                else:
                    print('No Data')
            counter += 1

        result = []
        for i in temp:
            result.append(i[attr])
        return result


print(get_value(attr='TEMPERATURE', count_values=10))
