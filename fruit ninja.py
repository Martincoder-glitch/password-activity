import pgzrun
import random
HEIGHT=500
WIDTH=500
goku=Actor("goku")
goku.x=200
goku.y=100
images=["apple","banana","mango","pineapple","watermelon"]
fruits=[]
def draw():
    
    screen.blit("background",(0,0))
    goku.draw()
    for fruit in fruits:
        fruit.draw()
def on_mouse_move(pos):
    if goku.collidepoint(pos):
        goku.pos=pos
        
def make_fruit():
    fruitimg=random.choice(images)
    fruit=Actor(fruitimg)
    fruit.x=random.randint(50,WIDTH-50)
    fruit.y=random.randint(50,HEIGHT-50)
    fruits.append(fruit)
    
clock.schedule_interval(make_fruit,15)






pgzrun.go()