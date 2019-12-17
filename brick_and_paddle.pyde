posX = 100

def setup():
      size(640,640)
      background(79, 90, 247)

def paddle():
    circ()
    rectang()
              
def circ(): 
    fill(247, 101, 79) 
    circle(-1, 618,15)
    circle(101,618, 15)

def rectang():
    fill(143, 137, 136)
    rect(0,610,100,15)
    
    
def draw():
    global posX
    paddle()
    posX = mouseX
    if mouseX<10:
        posX = 10
    elif mouseX > 530:
        posX = 530
    if keyPressed:
        if keyCode == RIGHT:
           posX = posX + 5
        elif keyCode == LEFT:
           posX = posX - 5
            
    pushMatrix()
    translate(posX,0)
    background(79, 90, 247)
    paddle()
    popMatrix()
#noLoop    
        

     
    

    
    
      
