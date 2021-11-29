import serial
from ast import literal_eval
from models.database import Sensor

ARDUINO_USB_PORT = '/dev/cu.usbserial-1410'
SPEED_USB_PORT = 9600


def get_value(port, port_speed, count_values: int = 10, count_to_error: int = 20,) -> list:
    temp = []
    counter = 0
    try:
        with serial.Serial(port, port_speed, timeout=1.0) as port:
            while counter < (count_values + 1):  # first package always lost
                port.write(str(b'1').encode())  # change command
                com_data = port.readline().decode('utf-8')
                # print(counter, com_data)
                if com_data:
                    temp.append(literal_eval(com_data))
                else:
                    print('No Data')
                counter += 1
            #
            # result = []
            # for i in temp:
            #     result.append(i[attr])
            return temp

    except serial.SerialTimeoutException:
        print('Port time out!')
    except serial.SerialException:
        print('Port Not Found!')


def send_command(sensor=None, command: str = '1',) -> bool:

    try:
        with serial.Serial(ARDUINO_USB_PORT, SPEED_USB_PORT, timeout=1.0) as port:
            port.write(str(b'?').encode())  # change command
            com_data = port.readline().decode('utf-8')
            if com_data == '!':
                port.write(str(command).encode())  # change command
                if port.readline().decode('utf-8') == command:
                    print('Success')
                    return True
                print("Lost")
                return False
    except serial.SerialTimeoutException:
        print('Port time out!')
    except serial.SerialException:
        print('Port Not Found!')
