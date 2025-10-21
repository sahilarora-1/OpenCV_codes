import cv2
image=cv2.imread(r'C:\opencv\sample_images\resized_car.jpg')
if image is not None:
    print("Image Loaded !")
    res=input("Do you to apply Gaussian Blur (yes/no)=").lower()
    if res=='yes':
        #cv2.GaussianBlur(source, (kernel_x, kernel_Y),sigma(if 0 it automatically detects it)
        blur=cv2.GaussianBlur(image,(11,11),0)#kernel should always be odd number

        save=input("Do you want to save the image(yes/no)").lower()
        cv2.imshow("Orignal Image",image)
        cv2.imshow("Gaussian Blured Image",blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        if save=='yes':
            cv2.imwrite("Gaussian_Blured_Image.jpg",blur)
        else:
            print("Photo Displayed")
            exit()
    else:
        cv2.imshow('Orignal Image',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("Image not found check source Path")