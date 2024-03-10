import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('COM5', 115200)
    ser.reset_input_buffer()

    while True:
        ser.write(b"1\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
