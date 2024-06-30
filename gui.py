import tkinter as tk
import pyttsx3

def create_gui():
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.geometry("300x200")

    label = tk.Label(root, text="FRIDAY is active", font=("Helvetica", 16))
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
