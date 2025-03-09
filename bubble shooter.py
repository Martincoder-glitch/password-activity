import pgzrun
import random
WIDTH=500
HEIGHT=500
images=["bluebubble","greenbuble","orangebubble","pinkbubble","redbubbble","yellowbuble"]
bubbles=[]
def draw():
    screen.blit("background",(0,0))
    for bubble in bubbles:
        bubble.draw()
        animate(bubble,y=50,duration=1.5)
def make_bubbles():
    bubbleimg=random.choice(images)
    bubble=Actor(bubbleimg)
    bubble.x=random.randint(50,WIDTH-50)
    bubble.y=random.randint(400,HEIGHT)
    bubbles.append(bubble)
def update():
    pass
clock.schedule_interval(make_bubbles,1)
pgzrun.go()