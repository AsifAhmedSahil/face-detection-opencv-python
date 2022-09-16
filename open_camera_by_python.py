import cv2
# Enable camera ***

video_cap = cv2.VideoCapture(0)
# while true is for on camera permanent time

while True :
    ret, video_data = video_cap.read()
    cv2.imshow("live_sahil",video_data)

    # if else for stop video 
    if cv2.waitKey(10) == ord("a") :
        break
video_cap.release()