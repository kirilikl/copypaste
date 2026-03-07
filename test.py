import pgzero
#КОНСТАНТЫ
WIDTH=600
HEIGHT=600
#ПЕРЕМЕННЫЕ
cookies = 0
#ПЕРСОНАЖИ
bg = Actor("bgBlue")
cookie = Actor("cookie", (WIDTH//2, HEIGHT//2))
#ФУНКЦИЯ ОТРИСОВКИ
def draw():
    screen.clear()
    bg.draw()
    cookie.draw()
    screen.draw.text(str(cookies), 
                center=(WIDTH//2,  50), 
                color=(255, 153, 51), 
                fontsize=50)
#ОСНОВНОЙ ИГРОВОЙ ЦИКЛ
def update(dt):
    cookie.angle += 1
#ОБРАБОТЧИК МЫШИ
def on_mouse_down(button, pos):
    global cookies
    if button == mouse.LEFT and cookie.collidepoint(pos):
        cookies += 1






