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
#СВОИ ФУНКЦИИ
def autoclickFunc():
    global cookies
    cookies += cursor.value * cursor.amount
 
#ТАЙМЕР
clock.schedule_interval(autoclickFunc, 1)
#ФУНКЦИЯ ОТРИСОВКИ
def draw():
    screen.clear()
    bg.draw()
    cookie.draw()
    cursor.draw()
    screen.draw.text(str(cursor.price), center=(cursor.x, cursor.y+50), color=(255, 255, 255), fontsize=25)
    screen.draw.text(str(cookies), center=(WIDTH//2,  50), color=(255, 153, 51), fontsize=50)
    for i in points_pos:
        screen.draw.text("+1", center=i, color=(255, 255, 255), fontsize=30)
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
 
