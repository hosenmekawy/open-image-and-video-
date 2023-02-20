import cv2
import tkinter as tk
from tkinter import filedialog

def open_image():
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def open_video():
    file_path = filedialog.askopenfilename()
    cap = cv2.VideoCapture(file_path)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

# Create a Tkinter window
window = tk.Tk()
window.title("OpenCV Image/Video Viewer")
window.geometry("400x200")

# Create buttons for image and video
img_btn = tk.Button(window, text="Open Image", command=open_image)
img_btn.pack(pady=10)

vid_btn = tk.Button(window, text="Open Video", command=open_video)
vid_btn.pack(pady=10)

# Run the window
window.mainloop()
