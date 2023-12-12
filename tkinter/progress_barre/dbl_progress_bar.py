import time
import sys

class Progressall():

    class allprogress():
        def progressbar(it, prefix="", size=60, file=sys.stdout):
            count = len(it)
            def show(j):
                x = int(size*j/count)
                file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
                file.flush()
                file.write("\r")
            show(0)
            for i, item in enumerate(it):
                yield item
                show(i+1)
                file.write("\r")
            file.flush()
        
        time_set=-2
        
        for i in progressbar(range(15), "Computing: ", 40):
            if time_set<= 1:
                time.sleep(0.3)
                time_set=time_set+1
            if time_set<=10:
                time.sleep(0.1)
                time_set=time_set+1
            if time_set<=15:
                time.sleep(0.2)
                time_set=time_set+1
        time.sleep(1)

    class ProgressBar:
        '''
        Progress bar
        '''
        def __init__ (self, valmax, maxbar, title):
            if valmax == 0:  valmax = 1
            if maxbar > 200: maxbar = 200
            self.valmax = valmax
            self.maxbar = maxbar
            self.title  = title
        
        def update(self, val):
            import sys
            # format
            if val > self.valmax: val = self.valmax
            
            # process
            perc  = round((float(val) / float(self.valmax)) * 100)
            scale = 100.0 / float(self.maxbar)
            bar   = int(perc / scale)
      
            # render 
            out = '\r %20s [%s%s] %3d %%' % (self.title, '=' * bar, ' ' * (self.maxbar - bar), perc)
            sys.stdout.write(out)



    Bar = ProgressBar(100, 60, 'Chargement :')
    time_set=-5

    for i in range(101):
            Bar.update(i)
            if time_set<= 1:
                time.sleep(0.3)
                time_set=time_set+1
            if time_set<=10:
                time.sleep(0.1)
                time_set=time_set+1
            if time_set<=15:
                time.sleep(0.2)
                time_set=time_set+1
            if time_set<=75:
                time.sleep(0.1)
                time_set=time_set+1
            if time_set<=95:
                time.sleep(0.01)
                time_set=time_set+1

