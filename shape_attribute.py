import cv2
#loading image
image=cv2.imread('car.jpg')
#checking image loaded or not
if image is None:
    print("❌ Image not found! Please check the path.")
else:
    #if image is loaded successfully
    print("✅ Image found successfully!")
    #getting shape of image
    h,w,c=image.shape
    print(f"Height:{h},Width:{w},Channels:{c}")