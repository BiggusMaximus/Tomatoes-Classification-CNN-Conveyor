import cv2


def main():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(
        0
    )  # 0 for the default camera, you can change it if you have multiple cameras

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Check if the frame is empty
        if not ret:
            break

        # Display the frame in a window
        cv2.imshow("Video Stream", frame)

        # Check for the 'q' key to quit the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the VideoCapture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
