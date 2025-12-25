import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Clean up noise
    fgmask = cv2.medianBlur(fgmask, 5)

    # Extract only the object
    result = cv2.bitwise_and(frame, frame, mask=fgmask)

    cv2.imshow('Original', frame)
    cv2.imshow('Object Only', result)

    if cv2.waitKey(30) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
