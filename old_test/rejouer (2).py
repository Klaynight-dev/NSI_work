import tkinter as tk
from tkinter.simpledialog import Dialog

def jouer():
    def quite():
        global repetition
        if askyesno("Rejouer", "Voulez vous rejouer ?"):
            repetition=1
            root.destroy()
        else:
            repetition=0
            root.destroy()
    root = tk.Tk()
    tk.Button(root, text="Rejouer ?", command=quite).grid(padx=20, pady=20)

    root.mainloop()

class AskYesNo(Dialog):
    def __init__(self, title, message, parent=None):
        if not parent:
            parent = tk._default_root

        self.message = message
        Dialog.__init__(self, parent, title)

    def body(self, master):
        w = tk.Label(master, text=self.message, justify=tk.LEFT)
        w.grid(row=0, padx=5, sticky=tk.W)

    def buttonbox(self):
        """ajout d'une button box standard.

        Nous utilisons Oui et Non en texte
        """

        box = tk.Frame(self)

        w = tk.Button(box, text="Oui", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Non", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def apply(self):
        "If Oui was clicked"
        self.result = True

def askyesno(title, message):
    "Returns if the user clicked the Oui button."
    msg = AskYesNo(title=title, message=message)
    return msg.result is True

repetition = 2

jouer()