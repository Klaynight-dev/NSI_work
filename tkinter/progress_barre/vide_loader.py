import tkinter as tk
from tkinter import ttk
 
class SampleApp(tk.Frame):
    def __init__(self,parent=None):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text= "Veuillez patienter")
        self.label.grid(row = 0, column =0)
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="indeterminate")
        self.progress.grid(row=1 , column=0)
        self.progress.start()
    def stop(self):
        self.destroy()
 
if __name__ == "__main__":
    root = tk.Tk()
    app = SampleApp(root)
    app.grid()
 
    bouton = tk.Button(root, text= "arrêter SampleApp", command= app.stop)
    bouton.grid()
    root.mainloop()