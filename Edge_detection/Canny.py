import cv2
image=cv2.imread(r'C:\opencv\sample_images\resized_car.jpg')

if image is not None:
    print("Image Found ✔")
    res=input("Do you want to Find Canny Edges (yes/no)=").lower()
    if res=='yes':
        print('..If image would be Gray it would better for edge detection..')
        edges=cv2.Canny(image,150,250)
        ask=input("do you want to save the image(yes/no)").lower()
        if ask=='yes':
            cv2.imwrite('Canny_edge.jpg',edges)
            print("Image saved as Canny_edge.jpg")
            cv2.imshow('Orignal image', image)
            cv2.imshow('Edges detected',edges)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            exit()
        else:
            cv2.imshow('Orignal image', image)
            cv2.imshow('Edges detected',edges)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            exit()
    else:
        print("showing orignal image")
        cv2.imshow("Orignal Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("Image Not Found ! check Path ❌")