#cv2.VideoWriter("video.avi",codec(compressor),FPS,(width, height))
import cv2
#capturing video from builtin camera
camera=cv2.VideoCapture(0)
#taking height and width of the frame used
width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

#compressor 
codec=cv2.VideoWriter_fourcc(*'XVID')

#saving video using VideoWriter object
video=cv2.VideoWriter('stored_vdieo.avi',codec,30,(width,height))


while True:
    sucess,image=camera.read()
    #error handling if video is not captured
    if not sucess:
        print("Video not found !! check source")
        break
    
    video.write(image)#writing the captured video frame by frame
    cv2.imshow('video recording',image)#showing the video while recording

    #checking for stoping condition
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print('video saved! QUITING>>>>>>>>')
        break
camera.release()
video.release()
cv2.destroyAllWindows()
