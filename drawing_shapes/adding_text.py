import cv2
#loading image
image=cv2.imread('C:/opencv/sample_images/resized_car.jpg')
if image is None:
    print('image not found')
else:
    print('image found')
    #cv2.putText(image,text you want to insert, left bootom points from where text starts,color,scale(0.5,1,2),thickness)
    text=cv2.putText(image,'this is a car',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    cv2.imshow('text added',text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
