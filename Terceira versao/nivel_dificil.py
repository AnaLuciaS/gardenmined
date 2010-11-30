# -*- coding: utf-8 -*-

import pygame, sys, os, random
from pygame.locals import *
pygame.init()

import time



def multiimageload(images):
    list = []
    for image in images:
        list.append(pygame.image.load(image))
    return list

MEDIUM = pygame.font.Font("resources" + os.sep + "CHICK___.ttf", 24)
som_tocando = True


#Carregando imagens

img_flag = pygame.image.load("resources" + os.sep + "img_flor1.png")
img_spaces = multiimageload(["resources" + os.sep + "img_1.png", "resources" + os.sep + "img_2.png", "resources" + os.sep + "img_3.png", "resources" + os.sep + "img_4.png", "resources" + os.sep + "img_5.png", "resources" + os.sep + "img_6.png", "resources" + os.sep + "img_7.png", "resources" + os.sep + "img_8.png", "resources" + os.sep + "img_bomba1.png"])
img_fundoo = pygame.image.load("resources" + os.sep + "a.png")
som_on = pygame.image.load("resources" + os.sep + "Som.png")
som_off = pygame.image.load("resources" + os.sep + "Sem_som.png")
img_voce_venceu = pygame.image.load("resources" + os.sep + "ganhar.png")
img_voce_perdeu = pygame.image.load("resources" + os.sep + "perder.png")
voltar_menu = pygame.image.load("resources" + os.sep + "seta_voltar.png")
bordas = pygame.image.load("resources" + os.sep + "bordas.png")
nome = pygame.image.load("resources" + os.sep + "nome.png")

#carregando sons

som_bomba = pygame.mixer.Sound("resources" + os.sep + "explode.wav")

# Corpo do jogo

class Game(object):
    def __init__(self, m, n, bomba):
        self.numero_bombas = bomba
        self.bombsleft = bomba
        self.m = m
        self.n = n
        self.todiscover = m * n - bomba
        self.board = []
        for b in range(self.n):
            self.board.append([])
        for b in range(self.n):
            for a in range(self.m):
                self.board[b].append(0)
        self.seenboard = []
        for b in range(self.n):
            self.seenboard.append([])
        for b in range(self.n):
            for a in range(self.m):
                self.seenboard[b].append(0)
        self.started = False




    def start(self, x, y):
        self.started = True
        for bomb in range(self.numero_bombas):
            free = False
            while not free:
                a = random.randint(0, self.m - 1)
                b = random.randint(0, self.n - 1)
                free = True
                if (self.board[a][b] == -1) or ((a == x) and (b == y)):
                    free = False
            self.board[a][b] = -1
            if a > 0:
                if self.board[a-1][b] != - 1:
                    self.board[a-1][b] += 1
                if b > 0:
                    if self.board[a-1][b-1] != - 1:
                        self.board[a-1][b-1] += 1
                if b < self.n - 1:
                    if self.board[a-1][b+1] != - 1:
                        self.board[a-1][b+1] += 1
            if a < self.m - 1:
                if self.board[a+1][b] != - 1:
                    self.board[a+1][b] += 1
                if b > 0:
                    if self.board[a+1][b-1] != - 1:
                        self.board[a+1][b-1] += 1
                if b < self.n - 1:
                    if self.board[a+1][b+1] != - 1:
                        self.board[a+1][b+1] += 1
            if b > 0:
                if self.board[a][b-1] != - 1:
                    self.board[a][b-1] += 1
            if b < self.n - 1:
                if self.board[a][b+1] != - 1:
                    self.board[a][b+1] += 1
    def discover(self, x, y):
        if self.seenboard[x][y] == 0:
            self.seenboard[x][y] = 1
            if self.board[x][y] != -1:
                self.todiscover -= 1
            else:
                return "Bomb"
            if self.board[x][y] == 0:
                if x > 0:
                    self.discover(x-1, y)
                    if y > 0:
                        self.discover(x-1, y-1)
                    if y < self.n - 1:
                        self.discover(x-1, y+1)
                if x < self.m - 1:
                    self.discover(x+1, y)
                    if y > 0:
                        self.discover(x+1, y-1)
                    if y < self.n - 1:
                        self.discover(x+1, y+1)
                if y > 0:
                    self.discover(x, y-1)
                if y < self.n - 1:
                    self.discover(x, y+1)

    def flag(self, x, y):
        if self.seenboard[x][y] == 0:
            self.seenboard[x][y] = -1
            self.bombsleft -= 1
            self.img_bombsleft = MEDIUM.render(str(self.bombsleft), True, (255, 255, 255))
        elif self.seenboard[x][y] == -1:
            self.seenboard[x][y] = 0
            self.bombsleft += 1
            self.img_bombsleft = MEDIUM.render(str(self.bombsleft), True, (255, 255, 255))



class Main(object):
    def __init__(self, bomba):
        self.startgame(15, 15, bomba, "Garden Mined - Dificil")
        self.mouseleft = "up"
        self.mouseright = "up"
        self.mode = 1
        self.clock = pygame.time.Clock()
        self.loop()
    def startgame(self, m, n, bomba, legenda):
        self.mode = 1
        self.game = Game(m, n, bomba)
        self.width= 800
        self.height = 600
        self.ganhardow = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(legenda)
        self.screen = screen = pygame.display.set_mode((self.width,self.height))

    def ganhar(self):
        self.mode = 2
        for a in range(self.game.m):
            for b in range(self.game.n):
                if self.game.seenboard[a][b] == 0:
                    if self.game.board[a][b] == -1:
                        self.game.seenboard[a][b] = -1
        self.draw()
        pygame.display.update(self.screen.blit(img_voce_venceu, (150, 150)))
        
    def perder(self):
        self.mode = 3
        for a in range(self.game.m):
            for b in range(self.game.n):
                if self.game.seenboard[a][b] == 0:
                    if self.game.board[a][b] == -1:
                        self.game.seenboard[a][b] = 1
        self.draw()
        pygame.display.update(self.screen.blit(img_voce_perdeu, (150, 150)))

        
    def loop(self):
        self.screen.blit(nome, (100,500))
        self.screen.blit(voltar_menu, (0, 350))
        self.screen.blit(bordas, (550, 50))
        self.screen.blit(som_on, (0, 150))
        self.paused = False
                
        while True:
            self.clock.tick(30)
            self.input(pygame.event.get())
            valor = self.action()
            
            
            pygame.display.update()
                    
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()
            
            
            cliquePos = (0, 350)
            cliqueSize = (50, 50)
            
            if cliquePos[0] <= mouse_pos[0] <= cliquePos[0] + cliqueSize[0]\
                and cliquePos[1] <= mouse_pos[1] <= cliquePos[1] + cliqueSize[1]:
                if mouse_press[0] :
                    return


            cliqueSon = (0, 150)
            sonSize = (50, 50)
            
            if cliqueSon[0] <= mouse_pos[0] <= cliqueSon[0] + sonSize[0]\
                and cliqueSon[1] <= mouse_pos[1] <= cliqueSon[1] + sonSize[1]:
                    if mouse_press[0] :
                        if self.paused:
                            self.paused = False
                            pygame.mixer.music.play(-1)
                            self.screen.blit(som_on, (0, 150))
                            
                        else:
                            self.paused = True
                            pygame.mixer.music.stop()
                            self.screen.blit(som_off, (0, 150))
                  
                     
            if  valor == True:
                time.sleep(1)
                while True:
                    
                    pygame.display.update()
                    
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()
                            
                    mouse_press = pygame.mouse.get_pressed()
                    
                    if mouse_press[0]:
                        return
                    
            self.draw()
    def input(self, events):
        if self.mouseleft == "released":
            self.mouseleft = "up"
        if self.mouseright == "released":
            self.mouseright = "up"
        if self.mouseleft == "pressed":
            self.mouseleft = "down"
        if self.mouseright == "pressed":
            self.mouseright = "down"
        
        for event in events:
            if event.type == QUIT or (event.type == KEYDOWN and event.key == 27):
                pygame.time.delay(100)
                sys.exit(0)
            (self.mouse_x, self.mouse_y) = pygame.mouse.get_pos()


            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouseleft = "pressed"
                elif event.button == 3:
                    self.mouseright = "pressed"
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouseleft = "released"
                elif event.button == 3:
                    self.mouseright = "released"

 

    def action(self):
        sair = False
        if self.mouseleft == "pressed":
            if self.mode == 1:
                if (self.mouse_x in range(64, 64 + self.game.m * 32)): 
                     if (self.mouse_y in range(32, 32 + self.game.n * 32)): 
                        if self.game.started == False:
                            if self.game.seenboard[(self.mouse_x -64) // 32][(self.mouse_y - 32) // 32] == 0: 
                                self.game.start((self.mouse_x - 64) // 32, (self.mouse_y - 32) // 32) 
                        if self.game.discover((self.mouse_x - 64 )// 32, (self.mouse_y - 32) // 32) == "Bomb":
                            som_bomba.play()
                            self.perder()
                            sair = True
                        if self.game.todiscover == 0:
                            self.ganhar()
                            sair = True
        if self.mouseright == "pressed":
            if self.mode == 1:
                if (self.mouse_x in range(0, 64 + self.game.m * 64)):
                    if (self.mouse_y in range(0, 32 + self.game.n * 32)):
                        self.game.flag((self.mouse_x - 64) // 32, (self.mouse_y - 32) // 32)

                        
        return sair




    def draw(self):
        screen = self.screen
                  
        for a in range(self.game.m):
            for b in range(self.game.n):
                    
                if self.game.seenboard[a][b] == 1:          
                   pygame.display.update(screen.blit(img_spaces[self.game.board[a][b]], (a * 32 + 64 , b * 32 + 32)))
                elif self.game.seenboard[a][b] == -1:
                    pygame.display.update(screen.blit(img_flag, (a * 32 + 64 , b * 32 + 32)))
                else:
                    planoFundo = pygame.image.load("resources" + os.sep + "a.png").convert()
                    pygame.display.update(screen.blit(planoFundo,(a * 32 + 64, 32 + b * 32)))




        pygame.display.flip()

    
