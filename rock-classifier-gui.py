import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np
import os

print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir())

model = joblib.load("model.pkl")
le = joblib.load("label_encoder.pkl")

root = tk.Tk()
root.title("Rock Classifier")
root.geometry("400x400")
root.resizable(False, False)

def classify():
    try:
        si = float(entries["SiO₂"].get())
        al = float(entries["Al₂O₃"].get())
        fe = float(entries["FeO"].get())
        mg = float(entries["MgO"].get())
        ca = float(entries["CaO"].get())


        sample = np.array([[si, al, fe, mg, ca]])
        prediction = model.predict(sample)
        rock_name = le.inverse_transform(prediction)[0]

        result_label.config(text=f"Most likely rock type: {rock_name}")
    except ValueError:
        messagebox.showerror("Incorrect data", "Please check your data for mistakes and try again")


tk.Label(root, text="Chemical content in percent:").pack(pady=10)

fields = ["SiO₂", "Al₂O₃", "FeO", "MgO", "CaO"]
entries = {}

for label in fields:
    tk.Label(root, text=f"{label}:").pack()
    entry = tk.Entry(root)
    entry.pack()
    entries[label] = entry


tk.Button(root, text="Predict Rock Type", command=classify).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
