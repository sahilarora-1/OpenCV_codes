import cv2
import os

# Ask for source
ask = int(input("Enter 1 to record from camera or 2 to read from file: "))

if ask == 1:
    cap = cv2.VideoCapture(0)
elif ask == 2:
    path = input("Enter the path of the video file: ")
    cap = cv2.VideoCapture(path)
else:
    print("❌ Invalid input. Exiting.")
    exit()

# Check if video/camera opened successfully
if not cap.isOpened():
    print("❌ Unable to open camera or video file.")
    exit()

# Ask whether to save
res = int(input("Enter 1 to save video or 2 to just view: "))

video = None

if res == 1:
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 30  # default

    filename = input("Enter name with extension (.avi or .mp4): ")
    extension = os.path.splitext(filename)[1].lower()

    # Select codec
    if extension == '.avi':
        codec = cv2.VideoWriter_fourcc(*'XVID')
    elif extension == '.mp4':
        codec = cv2.VideoWriter_fourcc(*'mp4v')
    else:
        print("⚠️ Unsupported format. Use .avi or .mp4 only.")
        cap.release()
        exit()

    video = cv2.VideoWriter(filename, codec, fps, (width, height))
    print(f"🎬 Recording started... Saving as {filename}")
elif res == 2:
    print("👀 Viewing only — no saving.")
else:
    print("⚠️ Invalid input. Exiting.")
    cap.release()
    exit()

# --- Main loop (recording or viewing) ---
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Video source ended or not found.")
        break

    # Save if enabled
    if video is not None:
        video.write(frame)

    # Show video
    cv2.imshow('Video (Press q to quit)', frame)

    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Quitting...")
        break

# --- Cleanup ---
cap.release()
if video is not None:
    video.release()
cv2.destroyAllWindows()
print("✅ All resources released. Exiting...")
