#ROTATION
#syntax=R=cv2.getRotationMatrix2D(centre, angle, scale)
#centre=(w//2,h//2)
#angle=any angle 
#scale=1(same size),0.5(half size),2(double size)
#rotated_image=cv2.warpAffine(image,R,(w,h))
#r is the rotation matrix
import cv2
image=cv2.imread('resized_car.jpg')
if image is not None :
    print("Image loaded successfully!")
    h,w=image.shape[:2]
    #rotating the image
    #creating rotation matrix
    centre=(w//2,h//2)

    Matrix=cv2.getRotationMatrix2D(centre,75,1.0)#matrix created
    rotated_image=cv2.warpAffine(image,Matrix,(w,h))#rotating image
    cv2.imshow("Rotated Image",rotated_image)   
    cv2.imshow("Original Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

