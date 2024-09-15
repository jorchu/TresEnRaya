import pygame as py
import random as rn
import sys

import numpy

py.init()

inMenu = True
runing = False
endMenssage = False
ia = False
local = False

mapa = [
       [2,2,2],
       [2,2,2],
       [2,2,2]
       ]
mapa = numpy.array(mapa)

tableroSize = 300, 300
size = 300,340


space =  tableroSize[0] // len(mapa), tableroSize[1] // len(mapa[0])
screen = py.display.set_mode(size)
font = py.font.SysFont('Arial', 30)


propBPlay = (tableroSize[0]//2-75, 10, 150, 80, (0,0,0))
propBLocal = (propBPlay[0], propBPlay[1]+100, 150, 80, (0,0,0))
propBExit = (propBPlay[0], propBLocal[1]+100, 150, 80, (0,0,0))

propBReanude = (propBPlay[0], 10, 160, 80, (0,0,0))
propBMainMenu = (tableroSize[0]//2-85, propBReanude[1]+100, 190, 80, (0,0,0))

mensWinProp = (40, tableroSize[1]//2-60, 240, 70, (0,0,0))
mensEmpateProp = (80, tableroSize[1]//2-60, 150, 70, (0,0,0))

replayProp = (80, mensWinProp[1]+100, 150, 70, (0,0,0))

player1Prop = (5, tableroSize[1]+10, (70, 70, 255), 'PLAYER_1', 125, tableroSize[1]+10)
player2Prop = (170, tableroSize[1]+10, (255, 70, 70), 'PLAYER_2', 145, tableroSize[1]+10)

############

player_ia = 0#rnl.Red(structure = [9, 5, 5, 5, 9], ultCapa=1, confName="tresRay.bin")
#player_ia.coste = lambda empty, empate: empty + 2*empate
#player_ia.deriCoste = lambda empty, empate: empty

def replay():
    global endMenssage, runing, mapa
    
    mapa = [
        [2,2,2],
        [2,2,2],
        [2,2,2]
        ]
    mapa = numpy.array(mapa)
    table.ficha = 0

    runing = True
    endMenssage = False
    play()

def menssageWin(menss):
    global endMenssage, inMenu

    while endMenssage:
        pos = py.mouse.get_pos()

        if menss == 'EMPATE':
            mensEmpate.draw(pos, menss, 1)
        else:
            mensWin.draw(pos, menss, 1)
        buttReplay.draw(pos, 'REPLAY')

        for e in py.event.get():
            if e.type == py.QUIT:
                sys.exit()
            if e.type == py.MOUSEBUTTONDOWN:
                buttReplay.click(pos, replay)

            if e.type == py.KEYDOWN:
                if e.key == py.K_ESCAPE:
                    inMenu = True
                    endMenssage = False
                    mainMenu() 


        py.display.update()


class player:
    def __init__(self, prop):
        self.xName = prop[0]
        self.yName = prop [1]
        self.color = prop[2]
        self.name = prop[3]
        self.xMark = prop[4]
        self.yMark = prop[5]
        self.sizeFont = 22
        self.mark = 0

    def drawName(self):
        playerFont = py.font.SysFont('Arial', self.sizeFont)
        text = playerFont.render(self.name, 1, self.color)
        screen.blit(text, (self.xName, self.yName))

    def drawMark(self):
        markFont = py.font.SysFont('Arial', self.sizeFont)
        text = markFont.render(str(self.mark),1 , self.color)
        screen.blit(text,(self.xMark, self.yMark))



class tablero:
    def __init__(self):
        self.long = 90
        self.ficha = 0

    def tableroDraw(self):
        for i in range(1, 3):
            py.draw.line(screen, (0,0,0), (space[0]*i, 0), (space[0]*i, tableroSize[1]))
            py.draw.line(screen, (0,0,0), (0, space[1]*i), (tableroSize[0], space[1]*i))

    def drawX(self, f, c):
        py.draw.line(screen, (255,50,50), (f*space[0]+5, c*space[1]+5), (f*space[0]+5+self.long, c*space[1]+5+self.long), 4)
        py.draw.line(screen, (255,50,50), (f*space[0] + 5 + self.long, c*space[1]+5), (f*space[0]+5, c*space[1]+5+self.long),4)
    
    def drawO(self, f, c):
        py.draw.circle(screen, (50,50,255), (space[0]*f+space[0]//2, space[1]*c+space[1]//2), 45)
        py.draw.circle(screen, (255,255,255), (space[0]*f+space[0]//2, space[1]*c+space[1]//2), 40)

    def tap(self, pos):
        place = int(pos[0] // space[0]), int(pos[1] // space[1])
        mapa[place[1]][place[0]] = self.ficha #Posiblemente haya que cambiarlo
        if self.ficha == 0:
            self.ficha = 1
        else:
            self.ficha = 0
    
    def empity(self, pos):
        place = int(pos[0] // space[0]), int(pos[1] // space[1])
        print(space, pos, place)
        empity = True

        if mapa[place[1]][place[0]] != 2:
            empity = False
        return empity
    
    def win(self):
        global runing, endMenssage
        if mapa[0][0] == mapa[1][1] and mapa[1][1] == mapa [2][2]:
            if mapa[0][0] == 1:
                runing = False
                endMenssage = True
                player2.mark += 1
                menssageWin('PLAYER_2 WIN')
            elif mapa[0][0] == 0:
                runing = False
                endMenssage = True
                player1.mark += 1
                menssageWin('PLAYER_1 WIN')

        if mapa[0][2] == mapa[1][1] and mapa[1][1] == mapa [2][0]:
            if mapa[0][2] == 1:
                runing = False
                endMenssage = True
                player2.mark += 1
                menssageWin('PLAYER_2 WIN')

            elif mapa[0][2] == 0:
                runing = False
                endMenssage = True
                player1.mark += 1
                menssageWin('PLAYER_1 WIN')

        for i in range(len(mapa)):
            if (mapa[i] == 3).all():
                runing = False
                endMenssage = True
                player2.mark += 1
                menssageWin('PLAYER_2 WIN')
                
            elif mapa[i].sum() == 0:
                print(mapa)
                runing = False
                endMenssage = True
                player1.mark += 1
                menssageWin('PLAYER_1 WIN')
                

            if mapa[0][i] == 1 and mapa[1][i] == 1 and mapa[2][i] == 1: # <--- Revisar
                runing = False
                endMenssage = True
                player2.mark += 1
                menssageWin('PLAYER_2 WIN')
            if mapa[0][i] == 0 and mapa[1][i] == 0 and mapa[2][i] == 0: # <--- Revisar
                runing = False
                endMenssage = True
                player1.mark += 1
                menssageWin('PLAYER_1 WIN')
            
        if not 2 in mapa[0] and not 2 in mapa[1] and not 2 in mapa[2]:
            runing = False
            endMenssage = True
            menssageWin('EMPATE')

def playLocal():
    global inMenu, runing, local
    local = True
    inMenu = False
    runing = True
    replay()

class button:
    def __init__(self, propieties):
        self.width = propieties[2] 
        self.height = propieties[3]
        self.x = propieties[0]
        self.y = propieties[1]
        self.color = propieties[4]
        self.size = (self.x, self.y, self.width, self.height)
        
    def draw(self, pos, text, do =0):
        if not(pos[0] in range(self.x, self.x + self.width) and pos[1] in range(self.y, self.y +self. height)):
            py.draw.rect(screen, self.color, self.size)
            text_button = font.render(text, 0, (255,255,255))
            screen.blit(text_button, (self.x+10, self.y+30))
        elif do:
            py.draw.rect(screen, self.color, self.size)
            text_button = font.render(text, 0, (255,255,255))
            screen.blit(text_button, (self.x+10, self.y+30))
        else:
            py.draw.rect(screen, (50,50,50), self.size)
            text_button = font.render(text, 0, (255,255,255))
            screen.blit(text_button, (self.x+10, self.y+30))

    def click(self, pos, func=''):
        if pos[0] in range(self.x, self.x + self.width) and pos[1] in range(self.y, self.y +self. height):
            if func:
                func()


buttPlay = button(propBPlay)
buttLocal = button(propBLocal)
buttExit = button(propBExit)
buttReanude = button(propBReanude)
buttMainMenu = button(propBMainMenu)
buttReplay = button(replayProp)

mensWin = button(mensWinProp)
mensEmpate = button(mensEmpateProp)

player1 = player(player1Prop)
player2 = player(player2Prop)

table = tablero()

def playIA():
    global runing, inMenu, ia
    ia = True
    runing = True
    inMenu = False
    replay()

def mainMenu(gameMenu=False):
    global inMenu, ia, local
    local = False
    ia = False

    screen.fill((255,255,255))
    py.display.set_caption('TRES EN RAYA')
    while inMenu:
        pos = py.mouse.get_pos()
        if gameMenu:
            buttReanude.draw(pos, "REANUDE")
            buttMainMenu.draw(pos, "MAIN MENU")
            buttExit.draw(pos, "EXIT")

        else:
            player1.mark = 0
            player2.mark = 0
            buttPlay.draw(pos, "PLAY")
            buttLocal.draw(pos, "LOCAL")
            buttExit.draw(pos, "EXIT")

        for e in py.event.get():
            if e.type == py.QUIT:
                sys.exit()
            if e.type == py.MOUSEBUTTONDOWN:
                if gameMenu:
                    buttPlay.click(pos, playLocal)
                    buttLocal.click(pos, mainMenu)
                    buttExit.click(pos, sys.exit)
                else:
                    buttPlay.click(pos, playIA)
                    buttLocal.click(pos, playLocal)
                    buttExit.click(pos, sys.exit)

            if e.type == py.KEYDOWN:
                if e.type == py.K_ESCAPE:
                    inMenu = False
                    sys.exit()

        py.display.update()



def play():
    global runing, inMenu, ia, local

    while runing: #Empieza con False
        screen.fill((255,255,255))

        posPlayer = py.mouse.get_pos()
        posIA = rn.randint(0, 300), rn.randint(0, 300)

        table.tableroDraw()
        player1.drawName()
        player2.drawName()
        player1.drawMark()
        player2.drawMark()

        if table.ficha == 0:
            player2.color = (255, 70, 70)
            player1.color = (0,0,255)
        else:
            player1.color = (70, 70, 255)
            player2.color = (255, 0, 0)

        for e in py.event.get():
            if e.type == py.QUIT:
                sys.exit()
            ##MODO

            if e.type == py.MOUSEBUTTONDOWN:
                if posPlayer[1] <= tableroSize[1] and local:
                    if table.empity(posPlayer):
                        table.tap(posPlayer)
                elif posPlayer[1] <= tableroSize[1] and table.ficha == 0:
                    if table.empity(posPlayer):
                        table.tap(posPlayer)
 
            if e.type == py.KEYDOWN:
                if e.key == py.K_ESCAPE:
                    inMenu = True
                    runing = False
                    mainMenu(1)

        if ia and table.ficha == 1:
            
            player_ia.propagar(mapa.reshape(9))
            #print(9)
            output = 0
            for l, neu in enumerate(player_ia.red[-1]):
                output = l if neu.a > output else neu.a
                print(l, neu.a)
            print(output)
            pos = [(output//3)*100, (output %3) *100]
            print(pos)
            if table.empity(pos):
                table.tap(pos)
            else:
                player_ia.entrenar(inputs = mapa.reshape(9), ciclos= 1000, ln = 0.005, parametrosDC= [5, 0], dcoste = 1)

        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if mapa[i][j] == 0:
                    table.drawO(j, i)
                elif mapa[i][j] == 1:
                    table.drawX(j, i)
        table.win()

        py.display.update()



mainMenu()
