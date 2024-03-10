import cv2
import numpy as np


THRESHOLD = 40

def detect_tomatoes(frame):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    is_tomat_exist = False
    # Define range of red color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Apply morphological operations to remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((20,20),np.uint8))

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    coor = [640, 480]
    # Check if there are any contours
    if len(contours) == 0:
        cv2.putText(frame, 'No tomatoes detected', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        # Iterate through contours and draw bounding boxes around tomatoes
        for contour in contours:
            # Get the bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            coor = [x, y]

            # Draw the bounding box around the tomato
            if ((w > THRESHOLD) and (h > THRESHOLD)):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                is_tomat_exist = True
            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                is_tomat_exist = False

        if is_tomat_exist:
            cv2.putText(frame, 'Tomatoes detected', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, 'No tomatoes detected', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return frame, is_tomat_exist, coor

# Initialize video capture from the camera