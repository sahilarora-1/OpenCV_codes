import cv2
image=cv2.imread('C:/opencv/sample_images/resized_car.jpg')
if image is None:
    print("❌ Image not found! Please check the path.")
else:
    print("image loaded")
    #cv2.line(image,pt1,pt2,color,thickness)
    line_drawn=cv2.line(image,(50,50),(250,50),(0,0,255),3)
    cv2.imshow('line',line_drawn)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()