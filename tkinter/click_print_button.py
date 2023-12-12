import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Simple Tkinter Example")

button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

root.mainloop()