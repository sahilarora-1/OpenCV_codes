import cv2
import numpy as np
image=cv2.imread(r"C:\opencv\sample_images\resized_car.jpg")
if image is not None:
    print("Imag loaded !")
    res=input("Do you want to apply Sharpening filter (yes/no)=").lower()
    if res=='yes':
        #create sharpening kernel
        sharpening_kernel = np.array([[-1,-1,-1],
                                      [-1, 9,-1],
                                      [-1,-1,-1]])
        #apply filter2D function
        sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
        #cv2.filter2D(source,ddepth,kernel)

        save=input("Do you want to save the image(yes/no)").lower()
        cv2.imshow("Orignal Image",image)
        cv2.imshow("Sharpened Image",sharpened_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if save=='yes':
            cv2.imwrite("Sharpened_Image.jpg",sharpened_image)
        else:
            print("Photo Displayed")
            exit()
    else:
        print("Orignal Image")
        cv2.imshow("Orignal Image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("image not found! ")