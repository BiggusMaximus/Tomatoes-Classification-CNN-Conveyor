import serial
import time
import random
import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="./model/model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


port = '/dev/ttyUSB1'

try:    
    ser = serial.Serial(port, 115200)
    ser.reset_input_buffer()
    print("Succesfully Connected")
    
    while True:
        line = ser.readline().decode("ISO-8859-1").rstrip()
        print(line)
        whichClass = random.randint(0, 3)
        whichClass = str(whichClass) + "\n"
        ser.write(whichClass.encode())
except:
    print("Error cant connect to Arduino")


