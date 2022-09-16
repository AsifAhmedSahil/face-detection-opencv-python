import cv2
# Enable camera ***
face_cap = cv2.CascadeClassifier("C:/python/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

video_cap = cv2.VideoCapture(0)
# while true is for on camera permanent time

while True :
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor  = 1.1,
        minNeighbors = 5,
        minSize = (30,40),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data, (x,y), (x+w,y+h),(0,255,0),2)
    cv2.imshow("live_sahil",video_data)

    # if else for stop video 
    if cv2.waitKey(10) == ord("a") :
        break
video_cap.release()