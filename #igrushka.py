import winsound
import random
import time
import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

# дисплей
disp = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('PLAY A DNA GAME')

# цвета
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
yellow = pygame.Color(255, 255, 0)
grey = pygame.Color(50, 50, 50)
green = pygame.Color(50, 200, 80)

# картино4ки
header = pygame.image.load('./images/header.png')
main = pygame.image.load('./images/main.png')
dee_enay = pygame.image.load('./images/dee enay.png')
mouse = pygame.image.load('./images/mouse.png')
m = pygame.image.load('./images/m.png')
instructions = pygame.image.load('./images/help.png')
play1 = pygame.image.load('./images/play1.png')
play2 = pygame.image.load('./images/play2.png')
ap = pygame.image.load('./images/apicture.png')
tp = pygame.image.load('./images/tpicture.png')
gp = pygame.image.load('./images/gpicture.png')
cp = pygame.image.load('./images/cpicture.png')
brickp = pygame.image.load('./images/brick.png')
aw = pygame.image.load('./images/aw.png')
tw = pygame.image.load('./images/tw.png')
cw = pygame.image.load('./images/cw.png')
gw = pygame.image.load('./images/gw.png')
end = pygame.image.load('./images/end.png')

# текстик
text100 = pygame.font.Font('freesansbold.ttf', 100)
text30 = pygame.font.Font('freesansbold.ttf', 30)
text20 = pygame.font.Font('freesansbold.ttf', 20)

# переменные_мои_любимые
loop = 'main'
mousex = 620
mousey = 190
loopcounting = 0
points = 0
mx = 5
my = 0
direction = 0
direction1 = 0
bases = ['A', 'T', 'G', 'C']


# Пересчет_координат_блин
class coordinates():
    def __init__(self, xcoordinate, ycoordinate):
        self.xcoordinate = float(xcoordinate) # пересчитывает у-координату
        self.ycoordinate = float(ycoordinate) # пересчитывает х-координату

    def convert(self): #конвертирует координаты в удобоваримый вид, конвертирует из клеточных координат в пиксельные, следит, чтобы они не вываливались за игровое поле
        convertedx = float(self.xcoordinate * 50) + 500
        convertedy = float(self.ycoordinate * 50) + 150
        if convertedx < 500:
            convertedx = 500
        elif convertedx > 900:
            convertedx = 900
        if convertedy < 150:
            convertedy = 150
        elif convertedy > 600:
            convertedy = 600
        return convertedx, convertedy # возвращает координаты для дальнейшего использования


def aplacer(): #размещает на экране аденин. Выбирает координаты одной из клеток рандомайзером. Возвращает координаты.
    x = int(random.uniform(0, 8))
    y = int(random.uniform(0, 9))
    aplace = coordinates(x, y)
    x, y = aplace.convert()
    return x, y


def tplacer(): #размещает на экране тимин (но ничего не рисует). Выбирает координаты одной из клеток рандомайзером. Возвращает координаты.
    x = int(random.uniform(0, 8))
    y = int(random.uniform(0, 9))
    tplace = coordinates(x, y)
    x, y = tplace.convert()
    return x, y


def cplacer(): #размещает на экране цитозин (но ничего не рисует). Выбирает координаты одной из клеток рандомайзером. Возвращает координаты.
    x = int(random.uniform(0, 8))
    y = int(random.uniform(0, 9))
    cplace = coordinates(x, y)
    x, y = cplace.convert()
    return x, y


def gplacer(): #размещает на экране гуанин (но ничего не рисует). Выбирает координаты одной из клеток рандомайзером. Возвращает координаты.
    x = int(random.uniform(0, 8))
    y = int(random.uniform(0, 9))
    gplace = coordinates(x, y)
    x, y = gplace.convert()
    return x, y

def brickplacer(): #размещает на экране кирпич (но ничего не рисует). Выбирает координаты одной из клеток рандомайзером. Возвращает координаты.
    x = int(random.uniform(0, 8))
    y = int(random.uniform(0, 9))
    brickplace = coordinates(x, y)
    x, y = brickplace.convert()
    return x, y

# луп
# основная функция игры. Заставляет игру, собственно, работать
while True:
    for event in pygame.event.get():
        if loop == 'main':
            amatx = [] #Кортеж с аденинами
            tmatx = [] #Кортеж с тиминами
            cmatx = [] #Кортеж с цитозинами
            gmatx = [] #Кортеж с гуанинами
            brickmatx = [] #Кортеж с кирпичами
            points = 0 #Очки
            loop2 = 0 #Вспомогательная переменная
	    #Рисуем всякое:
            pygame.draw.rect(disp, black, (0, 0, 1000, 700))
            disp.blit(header, (0, 0))
            disp.blit(main, (0, 150))
            disp.blit(mouse, (mousex, mousey))
        # Выбор_в_главном_меню. В зависимости от нажатых кнопок можно выйти из игры, передвинуть мышь для выбора и сделать выбор.
	#mousey - y-координата мыши
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    winsound.Beep(500, 100)
                    if mousey == 390 or mousey == 290:
                        mousey = mousey - 100
                    else:
                        mousey = mousey

                elif event.key == K_DOWN:
                    winsound.Beep(500, 100)
                    if mousey == 190 or mousey == 290:
                        mousey = mousey + 100
                    else:
                        mousey = mousey
	#Собственно переход к другим экранам:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if mousey == 190:
                        winsound.Beep(1000, 100)
                        loop = 'play'
                    elif mousey == 290:
                        winsound.Beep(1000, 100)
                        loop = 'help'
                    elif mousey == 390:
                        winsound.Beep(1000, 100)
                        pygame.quit()
                        sys.exit()

        if loop == 'play': #Экран игры. Сама игра, всё, что на ней происходит
            if loopcounting == 0:
		#Задаём стартовые параметры:
                starttime = time.time()
                endtime = starttime + 30
                target = bases[int(random.uniform(0, 4))]
	#всё ещё задаём стартовые параметры:
            loopcounting = loopcounting + 1
            now = time.time()
            mouseposition = coordinates(mx, my).convert()
            timer = text30.render('Time: ' + str(int(endtime - now)) + ' sec', True, white)
            pointtext = text30.render('Score: ' + str(points) + ' pts', True, white)
            pygame.draw.rect(disp, black, (0, 0, 1000, 700))
            disp.blit(header, (0, 0))

            while len(amatx) < 5: #Генерим аденины, 5шт
                a = aplacer()
                if a not in amatx:
                    if a not in tmatx:
                        if a not in cmatx:
                            if a not in gmatx:
                                if a not in brickmatx:
                                    amatx.append(a)

            while len(tmatx) < 5: #Генерим тимины, 5шт
                t = tplacer()
                if t not in amatx:
                    if t not in tmatx:
                        if t not in cmatx:
                            if t not in gmatx:
                                if t not in brickmatx:
                                    tmatx.append(t)

            while len(cmatx) < 5: #Генерим цитозины, 5шт
                c = cplacer()
                if c not in amatx:
                    if c not in tmatx:
                        if c not in cmatx:
                            if c not in gmatx:
                                if c not in brickmatx:
                                    cmatx.append(c)

            while len(gmatx) < 5: #Генерим гуанины, 5шт
                g = gplacer()
                if g not in amatx:
                    if g not in tmatx:
                        if g not in cmatx:
                            if g not in gmatx:
                                if g not in brickmatx:
                                    gmatx.append(g)

            while len(brickmatx) < 5: #Генерим кирпичи, 5шт
                b = brickplacer()
                if b not in amatx:
                    if b not in tmatx:
                        if b not in cmatx:
                            if b not in gmatx:
                                if b not in brickmatx:
                                    brickmatx.append(b)

            if loopcounting % 2 == 0:
                disp.blit(play1, (0, 150))
            else:
                disp.blit(play2, (0, 150))

	#"пишет" задание
            if target == 'A':
                disp.blit(aw, (290, 190))
            elif target == 'T':
                disp.blit(tw, (290, 190))
            elif target == 'C':
                disp.blit(cw, (290, 190))
            elif target == 'G':
                disp.blit(gw, (290, 190))

            pygame.draw.rect(disp, grey, (490, 140, 480, 520))
            pygame.draw.rect(disp, black, (500, 150, 460, 500))

	#Рисует ранее сгенеренные основания и кирпичи:
            for aplace in amatx:
                disp.blit(ap, aplace)

            for tplace in tmatx:
                disp.blit(tp, tplace)

            for cplace in cmatx:
                disp.blit(cp, cplace)

            for gplace in gmatx:
                disp.blit(gp, gplace)

            for brickplace in brickmatx:
                disp.blit(brickp, brickplace)

#Отрисовывает мышь, таймер, счёт
            disp.blit(m, mouseposition)
            disp.blit(timer, (20, 180))
            disp.blit(pointtext, (20, 230))
#Двигает мышь. Следит. чтобы мышь ходила строго по клеткам и никуда не сбегала
#mx и my - х- и у-координаты мыши соответственно (в клетках)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    winsound.Beep(800, 100)
                    my = my - 1
                elif event.key == K_DOWN:
                    winsound.Beep(800, 100)
                    my = my + 1
                if my < 0:
                    my = 0
                elif my > 9:
                    my = 9
                if event.key == K_LEFT:
                    direction1 = 0
                    winsound.Beep(500, 100)
                    mx = mx - 1
                elif event.key == K_RIGHT:
                    direction1 = 1
                    winsound.Beep(500, 100)
                    mx = mx + 1
                if mx < 0:
                    mx = 0
                elif mx > 8:
                    mx = 8
                if direction1 != direction:
                    m = pygame.transform.flip(m, True, False)
                    direction = direction1

	#Проверяем, кушает ли мышка нуклеотиды. И убивается ли об кирпич... Если мышка съела нуклеотид, засчитываются очки, задаётся новая цель.
            for aplace in amatx:
                if mouseposition == aplace:
                    if target == 'T':
                        winsound.Beep(1000, 30)
                        winsound.Beep(1500, 30)
                        points = points + 1
                    else:
                        winsound.Beep(1500, 200)
                        points = points - 1

                    amatx.remove(aplace)
                    target = bases[int(random.uniform(0, 4))]

            for tplace in tmatx:
                if mouseposition == tplace:
                    if target == 'A':
                        winsound.Beep(1000, 30)
                        winsound.Beep(1500, 30)
                        points = points + 1
                    else:
                        winsound.Beep(1500, 200)
                        points = points - 1

                    tmatx.remove(tplace)
                    target = bases[int(random.uniform(0, 4))]

            for cplace in cmatx:
                if mouseposition == cplace:
                    if target == 'G':
                        winsound.Beep(1000, 30)
                        winsound.Beep(1500, 30)
                        points = points + 1
                    else:
                        winsound.Beep(1500, 200)
                        points = points - 1

                    cmatx.remove(cplace)
                    target = bases[int(random.uniform(0, 4))]

            for gplace in gmatx:
                if mouseposition == gplace:
                    if target == 'C':
                        winsound.Beep(1000, 30)
                        winsound.Beep(1500, 30)
                        points = points + 1
                    else:
                        winsound.Beep(1500, 200)
                        points = points - 1

                    gmatx.remove(gplace)
                    target = bases[int(random.uniform(0, 4))]

            for brickplace in brickmatx:
                if mouseposition == brickplace:
                    loop = 'score'
                    loopcounting = 0


	#Рисует новое задание
            if target == 'A':
                disp.blit(aw, (290, 190))
            elif target == 'T':
                disp.blit(tw, (290, 190))
            elif target == 'C':
                disp.blit(cw, (290, 190))
            elif target == 'G':
                disp.blit(gw, (290, 190))

            if now > endtime: #Проверка оставшегося времени
                loop = 'score'
                loopcounting = 0

        if loop == 'help': #Отрисовка и функционирование экрана с правилами
            pygame.draw.rect(disp, black, (0, 0, 1000, 700))
            disp.blit(header, (0, 0))
            disp.blit(instructions, (0, 150))

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    winsound.Beep(1000, 100)
                    loop = 'main'

        elif loop == 'score': #Конец игры. Всё убивается, перерисовывается и т.д. Потом переходит на стартовый экран.
            pygame.draw.rect(disp, black, (0, 0, 1000, 700))
            disp.blit(header, (0, 0))
            disp.blit(end, (0, 150))
            totalpoints = text100.render(str(points), True, white)
            disp.blit(totalpoints, (550, 420))
            if loop2 == 0:
                winsound.Beep(800, 300)
                winsound.Beep(800, 200)
                winsound.Beep(1000, 800)
                loop2 = loop2 + 1
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    winsound.Beep(1000, 100)
                    loop = 'main'
                    points = 0
                    loop2 = 0

    pygame.display.update()