#import libraries of python opencv
import cv2

# capture video/ video path
cap = cv2.VideoCapture('trees.mp4')


#use trained trees XML classifiers
tree_cascade = cv2.CascadeClassifier('haarcascade_trees.xml')


#read until video is completed
while True:
    #capture frame by frame
    ret, frame = cap.read()
    #convert video into gray scale of each frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect Trees in the video
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)
    #cv2.im_write(trees)

    #to draw a rectangle in each trees 
    for (x,y,w,h) in trees:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('video', frame)
        crop_img = frame[y:y+h,x:x+w]

     #press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


#release the video-capture object
cap.release()
#close all the frames
cv2.destroyAllWindows()
