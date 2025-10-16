# 🧠 OpenCV Image Processor

A simple Python project demonstrating basic image processing using OpenCV.
This collection of scripts helps beginners understand how to manipulate images — including converting to grayscale, resizing, rotating, and flipping.

# 📦 Overview

Each script in this project performs a specific image operation.
The main goal is to help you learn essential OpenCV functions step by step.

# 🖤 1. gray_convertor.py

A program to:

Load an image from disk

Convert it to grayscale using cv2.cvtColor()

Display and optionally save the converted image

Main Function Used:

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 📐 2. shape_attribute.py

Used to fetch image properties such as:

Height

Width

Number of color channels

Main Concept:

h, w, c = image.shape
print("Height:", h, "Width:", w, "Channels:", c)

# 📏 3. resize.py

Used to resize the image to custom dimensions provided by the user.

Main Function Used:

resized = cv2.resize(image, (width, height))


Features:

Prompts user for new dimensions

Displays and optionally saves resized image

# 🔄 4. rotation.py

Used to rotate an image around its center by a given angle.

Main Functions Used:

R = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, R, (w, h))


Features:

Allows rotation by any angle (e.g., 45°, 90°, etc.)

Can scale the image (zoom in/out) using the scale parameter

# 🔃 5. flipped.py

Used to flip images in different directions.

Main Function Used:

cv2.flip(image, flipCode)


Flip Codes:

Flip Code	Direction
0	Vertical
1	Horizontal
-1	Both (Vertical + Horizontal)

Features:

Displays all flipped versions

Allows user to save the output images

# 6. shapes_assignment.py


This Python script allows you to interactively draw shapes and add custom text to any image using the OpenCV library.
It’s part of my OpenCV learning journey, focusing on image manipulation and user-driven graphic overlays.

🎯 Features

🖊️ Draw lines, rectangles, and circles with custom coordinates.

✍️ Add text anywhere on the image with adjustable font, color, and size.

🎨 Choose color dynamically — red, green, or blue (with fallback to white).

💾 Option to save the modified image with a custom filename.

🧠 Simple command-line interface for user input.



# ⚙️ Requirements

Make sure you have:

pip install opencv-python


Place your image file in the same folder (e.g., car.jpg or resized_car.jpg) before running the scripts.

🧠 Learning Outcomes

By completing this project, you’ll learn:

How to load and display images using OpenCV

How to access image dimensions and channels

How to perform common transformations (flip, rotate, resize)

How to draw different shapes on images(line, rectangle, circle, text)

How to save processed images

👨‍💻 Author

Sahil Arora
Learning OpenCV for computer vision and image processing.
Repository created for hands-on practice and demonstration.

💬 Feedback

Feel free to open an issue or suggest improvements!
Your feedback helps make this repo better. 🙌