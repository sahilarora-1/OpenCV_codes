import cv2

# Read image from user-specified path
path = input("Enter image path: ")
image = cv2.imread(path)

if image is None:
    print("Error: Image not found. Check the file path.")
    exit()
else:
    print("Image loaded successfully!")

res = input("Do you want to resize the image? (y/n): ").lower() #it will covert imput to lowercase

if res == 'y':
    x = int(input("Enter width of the resized image: "))
    y = int(input("Enter height of the resized image: "))
    dimensions = (x, y)
    resized = cv2.resize(image, dimensions)
    cv2.imshow("Resized Image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Displayed the resized image. Now exiting...")
else:
    print("Image not resized.")
    see = input("Do you want to see the actual image? (y/n): ").lower()
    if see == 'y':
        cv2.imshow("Original Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Exiting...")
