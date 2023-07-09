import cv2
cap = cv2.VideoCapture(0) # 0 for default camera
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' to exit
        break
cap.release()
cv2.destroyAllWindows()