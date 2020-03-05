import numpy as np
import cv2

dessicationClassifier = cv2.CascadeClassifier(r'C:\Users\rvrah\OneDrive\Desktop\dessicationClassifier\classifier\cascade.xml')
uncutLawnClassifier = cv2.CascadeClassifier(r'C:\Users\rvrah\OneDrive\Desktop\uncutLawnClassifier\classifier\cascade.xml')
img = cv2.imread(r'C:\Users\rvrah\OneDrive\Desktop\dessicationClassifier\p\testing1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dessicationCascade = dessicationClassifier.detectMultiScale(img, 1.3, 5)
uncutLawnCascade = uncutLawnClassifier.detectMultiScale(img, 1.3, 5)
dessicationCount = 0
uncutLawncount = 0
for (x,y,w,h) in dessicationCascade:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    dessicationCount+=1
for (x,y,w,h) in uncutLawnCascade:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    uncutLawncount+=1
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(dessicationCount)
print(uncutLawncount)
