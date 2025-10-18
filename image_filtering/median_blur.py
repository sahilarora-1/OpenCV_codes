import cv2
image=cv2.imread(r'C:\opencv\sample_images\resized_car.jpg')
if image is not None:
    print("image found")
    res=input("do you want to apply meadian filter(yes/no)=").lower()
    if res=='yes':
        median_blur=cv2.medianBlur(image,17)#kernel should always be odd number
        cv2.imshow("Orignal Image",image)
        cv2.imshow("Median Blured Image",median_blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        #display original image
        print("Orignal Image Displayed")
        cv2.imshow("Orignal Image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("file not found retry")
