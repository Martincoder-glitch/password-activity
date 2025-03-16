import pgzrun
import random
WIDTH=500
HEIGHT=500
score=0
images=["bluebubble","greenbuble","orangebubble","pinkbubble","redbubbble","yellowbuble"]
bubbles=[]
game=True
def draw():
    global game
    screen.blit("background",(0,0))
    screen.draw.text("score:"+str(score),color="black",topleft=(10,10)) 
    if game==True:
        for bubble in bubbles:
            bubble.draw()
            animate(bubble,y=50,duration=0.4)
        if len(bubbles)>=7:
            game=False 
    if game==False:
        sounds.song.stop()
        screen.draw.text("gameover, you scored this much "+str(score),color="red",topleft=(200,250))       
def on_mouse_down(pos):
    global score
    global bubbles
    for bubble in bubbles:
        if bubble.collidepoint(pos):
            sounds.pop.play()
            if bubble.image=="bluebubble":
                score+=2
            elif bubble.image=="yellowbuble":
                score+=2
            elif bubble.image=="greenbuble":
                score+=2
            else:
                score+=1
            bubbles.remove(bubble)
def make_bubbles():
    bubbleimg=random.choice(images)
    bubble=Actor(bubbleimg)
    bubble.x=random.randint(50,WIDTH-50)
    bubble.y=random.randint(400,HEIGHT)
    bubbles.append(bubble)



def update():
    global score
    pass
clock.schedule_interval(make_bubbles,0.4)
sounds.song.play(loops=-1)
pgzrun.go()