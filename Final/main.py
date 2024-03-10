import cv2
import numpy as np
from dsp import *
import serial

cap = cv2.VideoCapture(1)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Camera resolution: {} x {}".format(width, height))

port = "COM6"
try:    
    ser = serial.Serial('COM6', 9600)
except:
    print("Error cant connect to Arduino")

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    is_tomat_exist = False
    if not ret:
        break

    # Detect tomatoes in the frame and draw bounding boxes
    frame_with_boxes, is_tomat_exist, coor = detect_tomatoes(frame)

    if ((is_tomat_exist) and (coor[0] < 255) and (coor[0] > 245)):
        print(f"kontol, {coor}")
        cv2.imwrite("kontol.jpg", frame)
    else:
        print(coor)

    # Display the frame with bounding boxes
    cv2.imshow('Tomato Detection', frame_with_boxes)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

if __name__ == '__main__':
    