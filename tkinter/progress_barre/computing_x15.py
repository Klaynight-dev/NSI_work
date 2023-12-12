import sys
import time

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

    for i in progressbar(range(15), "Computing: ", 40):
        time.sleep(0.03)
allprogress()