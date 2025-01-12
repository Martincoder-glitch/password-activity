import pgzrun
import random
from random import randint
WIDTH=500
HEIGHT=500
TITLE="dragon ball game"
goku=Actor("goku") 
goku.x = 200
goku.y=100
hit=Actor("hit")
hit.x = 250
hit.y = 300
score=0
gameover=False


def draw(): 
    screen.clear()
    screen.blit("dragon",(0,0))
    hit.draw()
    goku.draw()
    screen.draw.text("score:"+str(score),color="black",topleft=(10,10)) 
    if gameover == True:
        screen.fill("red")  
        screen.draw.text("gameover"+str(score),color="black",topleft=(10,10))
def place_Hit():
    hit.x=randint(70,(WIDTH-70))
    hit.y=randint(70,(HEIGHT-70))

def update():
    global score
    if keyboard.up:
        goku.y -=10
    if keyboard.down:
        goku.y +=10
    if keyboard.left:
        goku.x -=10
    if keyboard.right:
        goku.x +=10        
    if goku.colliderect(hit):
        place_Hit()
        score +=1
def timeup():
    global gameover
    gameover=True
clock.schedule(timeup,120.0)


pgzrun.go()
