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
cap = cv2.VideoCapture(1)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Camera resolution: {} x {}".format(width, height))

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
