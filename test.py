import pgzero

WIDTH = 800
HEIGHT = 200
FPS = 30

dino = Actor("dino1")
cactus = Actor("cactus")

dino.pos = (dino.width, 160)
cactus.pos = (WIDTH - cactus.width, 170)

state = "pause"
jumping = True
jump_speed = 13

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    dino.draw()
    cactus.draw()

def on_key_down(key):
    global state, jumping, jump_speed
    if key == keys.SPACE and state != 'running':
        state = "running"
        dino.pos = (dino.width, 160)
        jumping = False
        jump_speed = 0
        dino.image = "dino1"
        cactus.pos = (WIDTH - cactus.width, 170)

    elif key == keys.SPACE and not jumping:
        jump_speed = 13
        jumping = True

def update(dt):
    global jumping, state, jump_speed

    if state == 'running':
        cactus.x -= 10
        if cactus.x < 0:
            cactus.x = WIDTH

        if dino.colliderect(cactus) and abs(cactus.center[0] - dino.center[0]) < 30:
            state = 'pause'
            dino.pos = (WIDTH // 2, HEIGHT // 2)
            dino.image = "restart" 

        if jumping:
            dino.y -= jump_speed
            jump_speed -= 1
            if jump_speed < -13:
                dino.y = 160
                jump_speed = 0
                jumping = False
    
