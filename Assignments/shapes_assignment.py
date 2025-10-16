import cv2

path = input("Enter the path of the image: ")
image = cv2.imread(path)

if image is not None:
    print('Image loaded successfully ✅')

    res = int(input('''What do you want to do with the image?
          1. Draw Line
          2. Draw Rectangle
          3. Draw Circle
          4. Add Text
        Enter here: '''))

    # Function to get color
    def get_color():
        color = input('Enter the color you want (r/g/b): ').lower()
        if color == 'r':
            return (0, 0, 255)  # Red
        elif color == 'g':
            return (0, 255, 0)  # Green
        elif color == 'b':
            return (255, 0, 0)  # Blue
        else:
            print('Invalid color, defaulting to white')
            return (255, 255, 255)

    # Draw Line
    if res == 1:
        x1 = int(input('Enter x1 (starting point): '))
        y1 = int(input('Enter y1 (starting point): '))
        x2 = int(input('Enter x2 (ending point): '))
        y2 = int(input('Enter y2 (ending point): '))
        color = get_color()
        thickness = int(input("Enter the thickness of the line: "))
        pt1, pt2 = (x1, y1), (x2, y2)
        Drawing_image = cv2.line(image, pt1, pt2, color, thickness)
        cv2.imshow('Line Drawn', Drawing_image)

    # Draw Rectangle
    elif res == 2:
        print("---- Enter Starting Coordinates (Top-Left Corner) ----")
        x1 = int(input('Enter x1: '))
        y1 = int(input('Enter y1: '))
        print("---- Enter Ending Coordinates (Bottom-Right Corner) ----")
        x2 = int(input('Enter x2: '))
        y2 = int(input('Enter y2: '))
        pt1, pt2 = (x1, y1), (x2, y2)
        color = get_color()
        thickness = int(input("Enter thickness of the rectangle border: "))
        Drawing_image = cv2.rectangle(image, pt1, pt2, color, thickness)
        cv2.imshow('Rectangle Drawn', Drawing_image)

    # Draw Circle
    elif res == 3:
        x = int(input("Enter x-coordinate of the center: "))
        y = int(input("Enter y-coordinate of the center: "))
        radius_len = int(input("Enter radius (in pixels): "))
        centre = (x, y)
        color = get_color()
        thickness = int(input("Enter thickness (-1 to fill the circle): "))
        Drawing_image = cv2.circle(image, centre, radius_len, color, thickness)
        cv2.imshow('Circle Drawn', Drawing_image)

    # Add Text
    elif res == 4:
        print('--- Adding Text ---')
        text = input("Enter the text you want to add: ")
        print("--- Enter Starting Point of the Text ---")
        x1 = int(input("Enter X coordinate: "))
        y1 = int(input("Enter Y coordinate: "))
        pt1 = (x1, y1)
        font = cv2.FONT_HERSHEY_SIMPLEX  # Clear readable font
        scale = float(input("Enter the scale of the text (e.g., 0.5, 1, 2): "))
        color = get_color()
        thickness = int(input("Enter the thickness of the text: "))
        Drawing_image = cv2.putText(image, text, pt1, font, scale, color, thickness, cv2.LINE_AA)
        cv2.imshow('Text Added', Drawing_image)

    else:
        print("⚠️ Invalid choice. Please enter a number from 1–4.")
        exit()

    # Display and wait
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save Option
    save = input("Do you want to save the image? (y/n): ").lower()
    if save == 'y':
        name = input("Enter the filename with extension (e.g., output.jpg): ")
        cv2.imwrite(name, Drawing_image)
        print(f'✅ Image saved successfully as {name}')
    else:
        print('🖼️ Image displayed but not saved.')

else:
    print('❌ Error: Unable to load image. Check the path provided.')
