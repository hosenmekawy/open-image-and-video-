import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np
import tensorflow as tf

# Define the GUI


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Classification")

        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.select_button = tk.Button(
            master, text="Select Image", command=self.select_image)
        self.select_button.pack()

        self.predict_button = tk.Button(
            master, text="Predict", command=self.predict)
        self.predict_button.pack()

    # Function to select an image file
    def select_image(self):
        self.image_path = filedialog.askopenfilename()
        self.image = Image.open(self.image_path)
        self.image = self.image.resize((224, 224))
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(150, 150, image=self.photo)

    # Function to predict the image class
    def predict(self):
        # Load the pre-trained model
        model = tf.keras.applications.MobileNetV2(weights='imagenet')

        # Preprocess the image
        img_array = np.array(self.image)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(
            img_array)
        img_array = np.expand_dims(img_array, axis=0)

        # Make the prediction
        prediction = model.predict(img_array)

        # Display the predicted class
        class_name = tf.keras.applications.mobilenet_v2.decode_predictions(prediction)[
            0][0][1]
        messagebox.showinfo(
            "Prediction", f"The image is classified as: {class_name}")


# Create the GUI window
root = tk.Tk()
gui = GUI(root)
root.mainloop()
