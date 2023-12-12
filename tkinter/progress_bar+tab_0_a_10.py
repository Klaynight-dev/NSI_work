from tkinter import ttk
import tkinter ,time
 
class MaFenetre():
    def __init__(self):
        """ fenêtre principale"""
        self.root= tkinter.Tk()
        self.root.geometry("1200x900")
        self.root.title("fenetre principale")
        self.text1=tkinter.Text(self.root,width=33)
        self.text1.pack()
        self.ouvrirProgressBar()
        for t in range(10):
                self.text1.insert(tkinter.INSERT,t)
                self.text1.insert(tkinter.INSERT,"\t")
                time.sleep(0.1)
 
    def ouvrirProgressBar(self):
        """ fenetre secondaire (ProgressBarr)"""        
        self.f2=tkinter.Toplevel()
        self.f2.title("fenetre ProgressBar")
        self.f2.focus()
        # progressBar :
        self.pbar = ttk.Progressbar(self.f2, length=300)
        self.pbar.pack()
        self.pbar.start()
 
if __name__=='__main__':     
    fen=MaFenetre()    
    fen.root.mainloop()
