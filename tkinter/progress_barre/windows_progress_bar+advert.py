from tkinter import *
from tkinter.ttk import *
from random import *
from tkinter.messagebox import showinfo
import ctypes
import tkinter as tk
import tkinter as Label

root = tk.Tk()

root.geometry('350x135')

def Mbox(title, text, style):
  return ctypes.windll.user32.MessageBoxW(0, text, title, style)

progress = Progressbar(root, orient = HORIZONTAL,
              length = 300, mode = 'determinate')

def bar():
    import time
    timed=0    
    while timed<=100:
        progress['value'] = progress['value']+ randint(1,15)
        root.update_idletasks()
        timed=progress['value']
        timetravel=randint(1,5)
        timetravel=timetravel/10
        time.sleep(timetravel)
    progress['value'] = 100
    root.destroy()

    Mbox('Chargement Reussi', 'Votre programme à bien été chargé et executé', 1)

progress.pack(pady = 10)
  
Button(root, text = 'Start', command = bar).pack(pady = 10)
  
mainloop()