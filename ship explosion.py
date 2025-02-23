import pgzrun
import random
WIDTH=512
HEIGHT=544
ship=Actor("ship")
ship.x=250
ship.y=250
timer=0
enemyimages=["blueenemy","greenenemy","greyenemy","redenemy"]
enemies=[]
def draw():
    global timer
    screen.clear()
    screen.blit("map",(0,0))
    ship.draw()
    timer+=1
    if timer%80==0:
        make_enemy()
    for enemy in enemies:
        enemy.draw()
        animate(enemy,pos=ship.pos,angle=enemy.angle_to(ship.pos)-90,duration=0.5)
def on_mouse_down(pos):
    animate(ship,pos=pos,angle=ship.angle_to(pos)-90,duration=1)
def make_enemy():
    enemy=Actor("greenenemy")
    enemies.append(enemy)
    enemy.image=enemyimages[random.randint(0,3)]
    if enemy.image=="greenenemy":
        enemy.pos=(0,0)
    elif enemy.image=="blueenemy":
        enemy.pos=(512,0)
    elif enemy.image=="greyenemy":
        enemy.pos=(512,544)
    elif enemy.image=="redenemy":
        enemy.pos=(0,544)
pgzrun.go()