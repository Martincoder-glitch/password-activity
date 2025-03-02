import pgzrun
import random
WIDTH=512
HEIGHT=544
ship=Actor("ship")
ship.x=250
ship.y=250
timer=0
health=5
charge=0
game=True
attack=False
enemyimages=["blueenemy","greenenemy","greyenemy","redenemy"]
enemies=[]
def draw():
    global timer
    global health
    global charge
    global game
    screen.clear()
    screen.blit("map",(0,0))
    screen.draw.text("health :"+str(health),(160,520),color="red")
    screen.draw.text("charge :"+str(charge),(40,520),color="purple")
    ship.draw()
    if game==True:
        if health<1:
            game=False
            screen.draw.text("you have lost "+str(health),(250,250),color="red")
        if charge>10:
            game=False
            screen.draw.text("you have won :"+str(charge),(250,250),color="red")
        timer+=1
        if timer%80==0:
            make_enemy()
        for enemy in enemies:
            enemy.draw()
            animate(enemy,pos=ship.pos,angle=enemy.angle_to(ship.pos)-90,duration=0.5)
            if enemy.colliderect(ship):
                if attack==False:
                    health-=1
                    enemies.remove(enemy)
                else:
                    charge+=1
                    enemies.remove(enemy)
def on_mouse_down(pos):
    global attack,game
    if attack==False:
         attack=True
    if game==True:
        animate(ship,pos=pos,angle=ship.angle_to(pos)-90,duration=1,on_finished=attack_end)
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
def attack_end():
    global attack
    attack=False
pgzrun.go()