import pgzrun
import random
from random import randint
WIDTH=500
HEIGHT=500
TITLE="bumblebee game"
bee=Actor("bee")
flower=Actor("flower")
one=Actor("one")
score=0
gameover=False


def draw(): 
    screen.clear()
    screen.blit("background",(0,0))
    flower.draw()
    one.draw()
    screen.draw.text("score:"+str(score),color="black",topleft=(10,10))

def place_flowe():
    flower.x=randint(70,(WIDTH-70))
    flower.y=randint(70,(HEIGHT-70))







pgzrun.go()
