import pgzrun
WIDTH=800
HEIGHT=600
rocket=Actor("rocket")
rocket.x=450
rocket.y=450
bullets=[]
aliens=[]
score=0
for x in range(5):
    for y in range (5):
        alien=Actor("alien")
        alien.x=100+50*x
        alien.y=100+50*y
        aliens.append(alien)
        

def draw():
    screen.clear()
    screen.blit("gmgfhag",(0,0))
    screen.draw.text("Score :"+str(score),(20,20),color="orange")
    rocket.draw()
    for bullet in bullets:
        bullet.draw()
    for alien in aliens:
        alien.draw()
def update():
    global score
    if (keyboard.left):
        rocket.x -=5
    if (keyboard.right):
        rocket.x +=5
    for bullet in bullets:
        bullet.y-=5
    for alien in aliens:
        alien.y+=0.135
        for bullet in bullets:
            if alien.colliderect(bullet):
                score=score+1
                aliens.remove(alien)
                bullets.remove(bullet)
def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("bullet")
        bullet.x=rocket.x
        bullet.y=rocket.y -10
        bullets.append(bullet)
        








pgzrun.go()