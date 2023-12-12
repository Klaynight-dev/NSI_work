import turtle
  
def drawBar(t, height, color):
    

    t.fillcolor(color)
    t.begin_fill()              
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
       
    t.end_fill()                 
  
  
xs = [48, 117, 200, 96, 134, 260, 99]
clrs = ["green", "red", "yellow", "black",
        "pink", "brown", "blue"]
  
maxheight = max(xs)
numbars = len(xs)
border = 10
   
wn = turtle.Screen()             
wn.setworldcoordinates(0 - border, 0 - border, 
                       40 * numbars + border,
                       maxheight + border)
   
tess = turtle.Turtle()           
tess.pensize(3)
   
for i in range(len(xs)):
      
    drawBar (tess, xs[i],
             clrs[i])
  
wn.exitonclick()