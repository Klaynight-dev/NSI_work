from tkinter import *
import tkinter.messagebox as tkMessageBox
import time


class StopWatch(Frame):  
                                                         
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0        
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()               
        self.MakeWidget()      

    def MakeWidget(self):                         
        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 50), fg="white", bg="blue")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=2, padx=2)                      
    
    def Updater(self): 
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)
    
    def SetTime(self, nextElap):
        minutes = int(nextElap/60)
        seconds = int(nextElap - minutes*60.0)
        miliSeconds = int((nextElap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))
        
    def Start(self):                                                     
        if not self.onRunning:            
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1        
    
    def Stop(self):                                    
        if self.onRunning:
            self.after_cancel(self.timer)            
            self.nextTime = time.time() - self.startTime    
            self.SetTime(self.nextTime)
            self.onRunning = 0

    def Exit(self):
        result = tkMessageBox.askquestion('Information Système', 'Es-tu sûre de vouloir quitter le programme ?', icon='warning')
        if result == 'yes':
            root.destroy()
            exit()
    
    def Reset(self):                                  
        self.startTime = time.time()         
        self.nextTime = 0.0    
        self.SetTime(self.nextTime)
        
def Main():
    global root
    
    root = Tk()
    root.title("Chronomètre")
    width = 600
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Top = Frame(root, width=600)
    Top.pack(side=TOP)
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
    Bottom = Frame(root, width=600)
    Bottom.pack(side=BOTTOM)
    Start =  Button(Bottom, text='Lancer', command=stopWatch.Start, width=10, height=2)
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='Arreter', command=stopWatch.Stop, width=10, height=2)
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='Réinitialiser', command=stopWatch.Reset, width=10, height=2)
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text='Quitter', command=stopWatch.Exit, width=10, height=2)
    Exit.pack(side=LEFT)
    Title = Label(Top, text="CHRONOMETRE", font=("arial", 20), fg="white", bg="grey")
    Title.pack(fill=X)
    root.config(bg="grey")
    root.mainloop() 
    
if __name__ == '__main__':
    Main()
