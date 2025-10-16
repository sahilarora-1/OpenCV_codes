import cv2

# Ask for image path
path = input("Enter the path of the image you want to convert to grayscale: ")

# Read the image
image = cv2.imread(path)

# Check if image is loaded properly
if image is None:
    print("❌ Image not found! Please check the path.")
    exit()

print("✅ Image found successfully!")

# Ask user whether to save or show
res = input("Do you want to save or show the image? (s = save, w = show): ").lower()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if res == 's':
    name = input("Enter the name to save the grayscale image (with extension, e.g., gray.jpg): ")
    success = cv2.imwrite(name, gray)
    if success:
        print("💾 File saved successfully as", name)
    else:
        print("⚠️ Error: File could not be saved. Please retry.")
elif res == 'w':
    cv2.imshow('Grayscale Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("🖼️ Image displayed successfully.")
else:
    print("⚠️ Invalid choice. Please enter 's' or 'w'.")
