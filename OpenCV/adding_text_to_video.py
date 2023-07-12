import cv2 as cv
import datetime 
cap = cv.VideoCapture(0)

cap.set(3, 750)
cap.set(4, 900)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        font = cv.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        date = str(datetime.datetime.now())
        frame = cv.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv.LINE_AA)
        frame = cv.putText(frame, date, (10, 90), font, 1, (0, 255, 255), 2, cv.LINE_AA)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()