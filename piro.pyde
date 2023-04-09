a=1
def setup():
    size(1000,1000)
def draw():
    frameRate(5)
    background(100)
    rotate(a)
    translate(100,-50)
    fill(random(255, 0,),random(50,255),random(50,255))
    ellipse(400,250,340,230)#голова
    push()
    fill(random(50,255),random(50,255),random(50,255))
    ellipse(400,240,70,50)
    translate(-70,-30)
    ellipse(400,240,50,50)#прав
    translate(140,-20)
    ellipse(390,240,50,50)
    global a
    if mousePressed:
        if mouseButton == RIGHT:
            a=a+1
        if mouseButton == LEFT:
            a=a-1
    
