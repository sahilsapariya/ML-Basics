import cv2

# If we want to start webcame then write 0 in VideoCaptured method
# otherwise if we pass any video path then it will open that video
cap = cv2.VideoCapture('OpenCV\\videos\\tree.avi')


while cap.isOpened():
    # isOpened method returns boolean 
    # if video is opened in cap variable then it returns true
    ret, frame = cap.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', grey)

    # we have to pass BIT mask for 64 bits machines
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release method destroies all the variable stored when video started
cap.release()
cv2.destroyAllWindows()