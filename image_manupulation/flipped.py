import cv2
image=cv2.imread('resized_car.jpg')
if image is not None:
    print('Image loaded successfully!')
    #flipping images 1=horizontal, 0=vertical and -1 = both(horizontal and vertical)
    flipped_horizontal=cv2.flip(image,1)
    flipped_vertical=cv2.flip(image,0)
    flipped_both=cv2.flip(image,-1)
    #showing images
    cv2.imshow('horizontally flipped image',flipped_horizontal)
    cv2.imshow('vertically flipped',flipped_vertical)
    cv2.imshow('vertical and horizontal flip',flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("displayed all flipped images")
    #saving images 
    res=input("do you want to save images(y/n)=").lower()
    if res=='y':
        cv2.imwrite('horizontally_flipped.jpg',flipped_horizontal)
        cv2.imwrite('vertically_flipped.jpg',flipped_vertical)
        cv2.imwrite('both_flips.jpg',flipped_both)
        print('flipped images saved! exiting...')
    else:
        print("exiting.....")
else:
    print('Error: in loading image')