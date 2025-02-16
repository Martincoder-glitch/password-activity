import pgzrun
WIDTH=800
HEIGHT=600
rocket=Actor("rocket")
rocket.x=450
rocket.y=450
def draw():
    screen.clear()
    screen.blit("gmgfhag",(0,0))
    rocket.draw()
def update():
    if (keyboard.left):
        rocket.x -=5
    if (keyboard.right):
        rocket.x +=5









pgzrun.go()