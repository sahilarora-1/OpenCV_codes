import cv2
image=cv2.imread('C:/opencv/sample_images/resized_car.jpg')
if image is None:
    print("❌ Image not found! Please check the path.")
else:
    print("image loaded")
    #cv2.circle(img,centre,radius_len,color,thickness)
    circle=cv2.circle(image,(200,200),120,(255,0,0),3)
    cv2.imshow('circle_image',circle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    