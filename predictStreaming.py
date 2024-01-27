import cv2
import tensorflow as tf
import numpy as np
import serial
import time

# Set the serial port and baud rate
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace '/dev/ttyUSB0' with your Arduino's serial port

# Load the saved TFLite model
interpreter = tf.lite.Interpreter(model_path="./model/model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Define class labels
class_labels = ["Tomat Busuk", "Tomat Matang", "Tomat Mentah", "Tomat Setengah Matang"]


# Open video capture
cap = cv2.VideoCapture(0)  # Change 0 to the desired video device index

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame
    resized_frame = cv2.resize(frame, (256, 256))  # Adjust size as needed
    input_data = np.expand_dims(resized_frame, axis=0)
    input_data = input_data.astype(np.float32) / 255.0  # Normalize

    # Set the input tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Perform inference
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Get the predicted class
    predicted_class_index = np.argmax(output_data)
    predicted_score = output_data[0][predicted_class_index] * 100

    # Display the predicted class on the frame
    class_label = f"Class: {class_labels[predicted_class_index]} | {predicted_score:.2f}"
    cv2.putText(frame, class_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('Frame', frame)
    
    ser.write(predicted_class_index.encode())
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
