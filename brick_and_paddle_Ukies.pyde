width=540
height=640
key_mode = 0  
posX = 100
import random
def setup():
    size(width, height)
    background(0)
   

def rectangle_gray():
    fill(129,135,128)
    rect(0,20,width,height)
def rectangle_bleu():
    fill(50,10,227)
    rect(10,30,width-20,height)
def rectangles_red():
    fill(219,29,29)
    x=10
    y=30
    for j in range(10):        
            rect(x,y,(width-20)/10,30)
            x=x+(width-20)/10
            noLoop    
    translate(0,y)
    noLoop
def ball():
    fill(219,29,29)
    circle (70,600,20)
    fill(255,255,255)
    circle(68,597,6)

#def snow():
  #  for i in range(100):
   #     rect(random.randint(10,width-10),random.randint(240,height-10),5,5)
    #    fill(255,255,227)

def circ():
    fill(219,29,29)
    circle(9, 618,15)
    circle(126,618, 15)
def rectang():
    fill(141, 137, 136)
    rect(10,610
         ,115,15)            
def paddle():
    circ()
    rectang()
def draw():
     global posX
     global key_mode    
     rectangle_gray()
     rectangle_bleu()
     y=30
     fill(255,255,227)
     rect(random.randint(10,width-10),random.randint(240,height-10),3,3)
    # if frameCount%7 == 0:
       # snow()
     pushMatrix()
     for i in range(7):
        y=(y*i)              
        rectangles_red()
     popMatrix()

     if keyPressed:
        key_mode = 1
     if mousePressed:
        key_mode = 0
     if key_mode:
        if keyPressed:
            if keyCode == RIGHT:
                posX = posX + 5
                if posX > 395:
                    posX = 395
            elif keyCode == LEFT:
                posX = posX - 5
                if posX<10:
                    posX = 10
     else:
        posX = mouseX
        if mouseX<12:
            posX = 12
        elif mouseX > 395:
            posX = 395
     if keyPressed:
        if keyCode == RIGHT:
           posX = posX + 5
        elif keyCode == LEFT:
           posX = posX - 5
     pushMatrix()
     translate(posX,0)
     paddle()
     ball()
     popMatrix()    
