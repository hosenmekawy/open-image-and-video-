# this task made fully by hussen mekawy
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.choose_file_button = tk.Button(self)
        self.choose_file_button["text"] = "Choose file"
        self.choose_file_button["command"] = self.choose_file
        self.choose_file_button.pack()

        self.train_button = tk.Button(self)
        self.train_button["text"] = "Train model"
        self.train_button["command"] = self.train_model
        self.train_button.pack()

        self.classify_button = tk.Button(self)
        self.classify_button["text"] = "Classify data"
        self.classify_button["command"] = self.classify_data
        self.classify_button.pack()

    def choose_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        messagebox.showinfo("File chosen", f"File chosen: {self.file_path}")

    def train_model(self):
        if not hasattr(self, 'file_path'):
            messagebox.showerror("Error", "No file chosen!")
            return

        self.data = pd.read_csv(self.file_path)
        self.X = self.data.iloc[:, :-1]
        self.y = self.data.iloc[:, -1]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3)

        self.classifier = DecisionTreeClassifier()
        self.classifier.fit(self.X_train, self.y_train)

        messagebox.showinfo("Model trained", "Model trained successfully!")

    def classify_data(self):
        if not hasattr(self, 'classifier'):
            messagebox.showerror("Error", "No model trained!")
            return

        self.data_to_classify = pd.read_csv(self.file_path)
        self.predictions = self.classifier.predict(self.data_to_classify.iloc[:, :-1])

        messagebox.showinfo("Data classified", f"Predictions: {self.predictions}")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
