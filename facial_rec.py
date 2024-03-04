import cv2
import numpy as np


#Face Structue

# cap = cv2.VideoCapture(0)
# facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# while cap.isOpened():
#     ret,frame = cap.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     faces = facecascade.detectMultiScale(gray,1.3,5)
#     for a in faces:
#         cv2.rectangle(frame,(a[0],a[1]),(a[0]+a[2],a[1]+a[3]),(0,255,255), 2)
#     cv2.imshow("Video",frame)

#     if cv2.waitKey(1) == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()

######################################################

# Eye Outline

# cap = cv2.VideoCapture(0)
# eyecascade = cv2.CascadeClassifier("haarcascade_eye.xml")
# while cap.isOpened():
#    ret,frame = cap.read()
#    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#    eyes = eyecascade.detectMultiScale(gray,1.3,5)
#    for a in eyes:
#        cv2.rectangle(frame,(a[0],a[1]),(a[0]+a[2],a[1]+a[3]),(0,255,255), 2)
#    cv2.imshow("Video",frame)

#    if cv2.waitKey(1) == ord("q"):
#        break
# cap.release()
# cv2.destroyAllWindows()



 
