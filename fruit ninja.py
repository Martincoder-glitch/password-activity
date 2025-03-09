import pgzrun
import random
HEIGHT=500
WIDTH=500
goku=Actor("goku")
goku.x=200
goku.y=100
images=["apple","banana","mango","pineapple","watermelon","bomb"]
fruits=[]
score=0
game=True
def draw():
    
    screen.blit("background",(0,0))
    screen.draw.text("score:"+str(score),color="black",topleft=(10,10)) 
    goku.draw()
    for fruit in fruits:
        fruit.draw()
    if game == False:
        screen.fill("red")
        screen.draw.text("gameover",topleft=(10,10),color="blue")
def on_mouse_move(pos):
    if goku.collidepoint(pos):
        goku.pos=pos
        
def make_fruit():
    fruitimg=random.choice(images)
    fruit=Actor(fruitimg)
    fruit.x=random.randint(50,WIDTH-50)
    fruit.y=random.randint(50,HEIGHT-50)
    fruits.append(fruit)
def update():
    global score,game,fruits
    for fruit in fruits: 
        fruit.y +=random.randint(1,5)
        if goku.colliderect(fruit):
            if fruit.image =="bomb":
                game=False
            else:
                fruits.remove(fruit)
                score +=1  
                fruits=[]  
def on_mouse_down(pos):
    global game
    if game==True:
        animate(goku,pos=pos,angle=goku.angle_to(pos)-90,duration=1)
clock.schedule_interval(make_fruit,1)






pgzrun.go()