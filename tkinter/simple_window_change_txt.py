import tkinter as tk

def changeText():
  text.set("Welcome to WayToLearnX!")  


gui = tk.Tk()
gui.geometry('300x100')  

text = tk.StringVar()
text.set("Hello World!")

label = tk.Label(gui, textvariable=text)
label.pack(pady=20)

button = tk.Button(gui, text="Changer le text", command=changeText)
button.pack()

gui.mainloop()