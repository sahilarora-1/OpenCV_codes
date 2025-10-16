import cv2
video=cv2.VideoCapture(0)#0 to use web cam
while True:
    ret, frame=video.read()
    if not ret:
        print('unable to load video')
        break
    cv2.imshow('captured vide',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print('Quiting live feed')
        break
video.release()
cv2.destroyAllWindows()