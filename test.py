import pgzero
#КОНСТАНТЫ
WIDTH=600
HEIGHT=600
#ПЕРЕМЕННЫЕ
cookies = 0
points_pos = []
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

#СВОИ ФУНКЦИИ
def autoclickFunc():
    global cookies
    cookies += cursor.value * cursor.amount
    cookies += grandma.value * grandma.amount
    cookies += garden.value * garden.amount
 
#ТАЙМЕР
clock.schedule_interval(autoclickFunc, 1)
#ФУНКЦИЯ ОТРИСОВКИ
def draw():
    screen.clear()
    bg.draw()
    cookie.draw()
    screen.draw.text(str(cookies), center=(WIDTH//2,  50), color=(255, 153, 51), fontsize=50)
    for i in points_pos:
        screen.draw.text("+1", center=i, color=(255, 255, 255), fontsize=30)

    cursor.draw()
    screen.draw.text(str(cursor.price), center=(cursor.x, cursor.y+50), color=(255, 255, 255), fontsize=25)
    grandma.draw()
    screen.draw.text(str(grandma.price), center=(grandma.x, grandma.y+50), color=(255, 255, 255), fontsize=25)
    garden.draw()
    screen.draw.text(str(garden.price), center=(garden.x, garden.y+50), color=(255, 255, 255), fontsize=25)
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
    if button == mouse.LEFT and cursor.collidepoint(pos):
        if cookies >= cursor.price:
            cursor.amount += 1
            cookies -= cursor.price
            cursor.price = int(cursor.price * 1.5)
    if button == mouse.LEFT and grandma.collidepoint(pos):
        if cookies >= grandma.price:
            grandma.amount += 1
            cookies -= grandma.price
            grandma.price = int(grandma.price * 1.5)
    if button == mouse.LEFT and garden.collidepoint(pos):
        if cookies >= garden.price:
            garden.amount += 1
            cookies -= garden.price
            garden.price = int(garden.price * 1.5)
 
