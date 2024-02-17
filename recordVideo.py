import cv2

def record_video():
    # Open default webcam
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    recording = False

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Add text to the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        if recording:
            cv2.putText(frame, 'Recording...', (10, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, 'Press \'r\' to start recording', (10, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, 'Press \'q\' to quit', (10, 100), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Start recording when 'r' is pressed
        if cv2.waitKey(1) & 0xFF == ord('r'):
            if not recording:
                print("Recording started...")
            recording = True

        # Stop recording when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording stopped...")
            recording = False

        # Write the frame if recording is enabled
        if recording:
            out.write(frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and writer
    cap.release()
    out.release()

    # Destroy all windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    record_video()
