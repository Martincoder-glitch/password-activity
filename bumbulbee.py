import pgzrun
import random
from random import randint
WIDTH=500
HEIGHT=500
TITLE="bumblebee game"
one=Actor("one") 
one.x = 200
one.y=100
flower=Actor("flower")
flower.x = 250
flower.y = 300
score=0
gameover=False


def draw(): 
    screen.clear()
    screen.blit("background",(0,0))
    flower.draw()
    one.draw()
    screen.draw.text("score:"+str(score),color="black",topleft=(10,10)) 
    if gameover == True:
        screen.fill("red")  
        screen.draw.text("gameover"+str(score),color="black",topleft=(10,10))
def place_flower():
    flower.x=randint(70,(WIDTH-70))
    flower.y=randint(70,(HEIGHT-70))

def update():
    global score
    if keyboard.up:
        one.y -=10
    if keyboard.down:
        one.y +=10
    if keyboard.left:
        one.x -=10
    if keyboard.right:
        one.x +=10        
    if one.colliderect(flower):
        place_flower()
        score +=1
def timeup():
    global gameover
    gameover=True
clock.schedule(timeup,60.0)


pgzrun.go()
