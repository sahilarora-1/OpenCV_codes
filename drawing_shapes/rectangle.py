import cv2
image=cv2.imread("C:/opencv/sample_images/resized_car.jpg")
if image is None:
    print("check path image not found")
else:
    print("image loaded")
    #rectangle=cv2.rectangle(image,pt1(left starting points),pt2(right ending point of fig),color,thickness)
    rectangle=cv2.rectangle(image,(50,50),(300,350),(0,255,0),3)
    cv2.imshow('rectangle drawn',rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()