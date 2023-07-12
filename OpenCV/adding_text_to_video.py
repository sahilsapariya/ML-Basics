import cv2 as cv
import datetime 

cap = cv.VideoCapture(0)

# To capture width, number is 3 or cv2.CAP_PROP_FRAME_WIDTH
# To capture height, number is 4 or cv2.CAP_PROP_FRAME_HEIGHT
cap.set(3, 750)
cap.set(4, 900)

width = cap.get(3)
height = cap.get(4)
font = cv.FONT_HERSHEY_SIMPLEX

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        resolution_text = 'Width: ' + str(width) + ' Height: ' + str(height)
        date = str(datetime.datetime.now())
        frame = cv.putText(frame, resolution_text, (10, 50), font, 1, (0, 255, 255), 2, cv.LINE_AA)
        frame = cv.putText(frame, date, (10, 90), font, 1, (0, 255, 255), 2, cv.LINE_AA)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()