import cv2
import datetime

def take_picture():
    # Initialize the camera
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open camera")
        return

    taking_picture = False

    while True:
        # Capture a frame
        ret, frame = camera.read()

        if not ret:
            print("Error: Failed to capture image")
            break

        # Display the captured image
        cv2.imshow("Press 'e' to take picture or 'q' to quit", frame)

        # Check for key press
        key = cv2.waitKey(1) & 0xFF

        if key == ord('e'):
            taking_picture = True

        if taking_picture:
            # Get current date and time
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Save the captured image
            image_name = f"./setengah matang_fix/captured_image_{current_time}.jpg"
            cv2.imwrite(image_name, frame)
            print(f"Image saved as {image_name}")

            taking_picture = False

        if key == ord('q'):
            break

    # Release the camera and close windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    take_picture()
