import pgzero
import random

WIDTH = 288    
HEIGHT = 512   
FPS = 30      

bg = Actor("bg2")      
bird = Actor("bird1")
pipe_top = Actor("top")
pipe_bottom = Actor("bottom")
bird.x = 50            
bird.y = HEIGHT//2

velocity_y = 0
pipe_speed = 3

def reset_pipes():
    gap_y = random.randint(200, HEIGHT - 150)
    pipe_top.pos = (WIDTH + 50, gap_y - pipe_top.height // 2 - 100)  
    pipe_bottom.pos = (WIDTH + 50, gap_y + pipe_top.height // 2)  
reset_pipes()

def on_key_down(key):
    global velocity_y
    if key == keys.SPACE:
        velocity_y -= 8

def update(dt):
    global velocity_y, pipe_top, pipe_bottom, pipe_speed
    if pipe_speed > 0:
        bird.y += velocity_y
        velocity_y += 0.8
        pipe_top.x -= pipe_speed
        pipe_bottom.x -= pipe_speed

        if pipe_top.x <= -50:
            reset_pipes()
        if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom) or bird.y < 0 or bird.y > HEIGHT:
            pipe_speed = 0

def draw():        
    screen.clear() 
    bg.draw()      
    bird.draw()
    pipe_top.draw()
    pipe_bottom.draw()

