import pgzero
#КОНСТАНТЫ
WIDTH=600
HEIGHT=600
#ПЕРЕМЕННЫЕ
cookies = 0
points_pos = []
autoclickPerSecond = 0
#ПЕРСОНАЖИ
bg = Actor("bgBlue")
cookie = Actor("cookie", (WIDTH//2, HEIGHT//2))

cursor = Actor("cursor", (50, HEIGHT//2))
cursor.value = 1
cursor.price = 10
cursor.amount = 0

grandma = Actor('grandma', (50, HEIGHT//2 + 110))
grandma.value = 5
grandma.price = 50
grandma.amount = 0

garden = Actor('garden', (50, HEIGHT//2 + 200))
garden.value = 10
garden.price = 500
garden.amount = 0

upgrades = [cursor, grandma, garden]
#СВОИ ФУНКЦИИ
def autoclickFunc():
    global cookies, upgrades
    autoclickPerSecond = 0
    for i in upgrades:
        autoclickPerSecond += i.value * i.amount
        cookies += autoclickPerSecond
#ТАЙМЕР
clock.schedule_interval(autoclickFunc, 1)
#ФУНКЦИЯ ОТРИСОВКИ
def draw():
    screen.clear()
    bg.draw()
    cookie.draw()
    screen.draw.text(str(cookies), center=(WIDTH//2,  50), color=(255, 153, 51), fontsize=50)
    screen.draw.text('+' + str(autoclickPerSecond), center=(WIDTH//2,  95), color=(0, 255, 255), fontsize=25)
    
    for i in points_pos:
        screen.draw.text("+1", center=i, color=(255 , 255, 255), fontsize=30)
    for i in upgrades:
        i.draw()
        if cookies >= i.price:
            screen.draw.text(str(i.price), center=(i.x, i.y+50), color=(100, 255, 100), fontsize=25)
        else:
            screen.draw.text(str(i.price), center=(i.x, i.y+50), color=(255, 100, 100), fontsize=25)

    
#ОСНОВНОЙ ИГРОВОЙ ЦИКЛ
def update(dt):
    cookie.angle += 1
    for i in points_pos:
        if i[1] > 0:    
            i[1] -=4
        else:
            points_pos.remove(i)
            
#ОБРАБОТЧИК МЫШИ
def on_mouse_down(button, pos):
    global cookies, autoclick
    if button == mouse.LEFT and cookie.collidepoint(pos):
       points_pos.append(pos)
       cookies += 1
    for i in upgrades:
        if button == mouse.LEFT and i.collidepoint(pos):
            if cookies >= i.price:
                i.amount += 1
                cookies -= i.price
                i.price = int(i.price * 1.5)
    
