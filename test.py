import pgzero

WIDTH = 800
HEIGHT = 200
FPS = 30

dino = Actor("dino1")
cactus = Actor("cactus")

dino.pos = (dino.width, 160)
cactus.pos = (WIDTH-cactus.width, 170)

state = "pause"
jumping = False
jump_speed = 0

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    dino.draw()
    cactus.draw()

def on_key_down(key):
    global state, jumping, jump_speed
    if key == keys.SPACE and state == "pause":
        state = "running"
    elif key == keys.SPACE and not jumping:
        jumping = True
        jump_speed = 13
    







