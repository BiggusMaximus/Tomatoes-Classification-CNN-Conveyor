import cv2


def take_picture():
    # Initialize the camera
    camera = cv2.VideoCapture(
        0
    )  # 0 represents the default camera, change it if you have multiple cameras

    if not camera.isOpened():
        print("Error: Could not open camera")
        return

    # Capture a frame
    ret, frame = camera.read()

    if not ret:
        print("Error: Failed to capture image")
        return

    # Display the captured image
    cv2.imshow("Captured Image", frame)
    cv2.waitKey(0)  # Waits indefinitely until a key is pressed
    cv2.destroyAllWindows()

    # Save the captured image
    image_name = "captured_image.jpg"
    cv2.imwrite(image_name, frame)
    print(f"Image saved as {image_name}")

    # Release the camera
    camera.release()


if __name__ == "__main__":
    take_picture()
