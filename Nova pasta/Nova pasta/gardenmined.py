import pygame, sys, os, random
from pygame.locals import *
pygame.init()

# Codigo copiado do jogo Pybomb v1.0 e modificado de acordo com a nossa necessidade =D

def multiimageload(images):
    list = []
    for image in images:
        list.append(pygame.image.load(image))
    return list

MEDIUM = pygame.font.Font("resources" + os.sep + "CHICK___.ttf", 24)

#Carregando imagens

#img_marker = pygame.image.load("resources" + os.sep + "img_marker.png")
img_flag = pygame.image.load("resources" + os.sep + "img_flor1.png")
img_bombsleft = MEDIUM.render("bomba left: ", True, (255, 255, 255))
img_spaces = multiimageload(["resources" + os.sep + "img_1.png", "resources" + os.sep + "img_2.png", "resources" + os.sep + "img_3.png", "resources" + os.sep + "img_4.png", "resources" + os.sep + "img_5.png", "resources" + os.sep + "img_6.png", "resources" + os.sep + "img_7.png", "resources" + os.sep + "img_8.png", "resources" + os.sep + "img_bomba1.png"])
som_bomba = pygame.mixer.Sound("resources" + os.sep + "explode.wav")
img_fundoo = pygame.image.load("resources" + os.sep + "a.png")
#img_fundo2 = pygame.image.load("resources" + os.sep + "img_fundooo.png")
som_on = pygame.image.load("resources" + os.sep + "Som.png")
#som_off = pygame.image.load("resources" + os.sep + "som_off.png")
#img_bombsleft = MEDIUM.render("Bombs left: ", True, (255, 255, 255))
#img_youwin = MEDIUM.render("Parabens Voce Venceu!", True, (0, 255, 0))
#img_youlose = MEDIUM.render("Nao foi dessa vez =(", False, (255, 0, 0))
voltar_menu = pygame.image.load("resources" + os.sep + "seta_voltar.png")
bordas = pygame.image.load("resources" + os.sep + "bordas.png")
nome = pygame.image.load("resources" + os.sep + "nome.png")


class Game(object):
    def __init__(self, m, n, bomba):
        self.numero_bombas = bomba
        self.bombsleft = bomba
        self.img_bombsleft = MEDIUM.render(str(self.bombsleft), True, (255, 255, 255))
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

# Montagem dos quadradinhos

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
    def __init__(self):
        self.startgame(15, 15, 30, "PyBomb - Easy")
        self.mouseleft = "up"
        self.mouseright = "up"
        self.mode = 1
        self.clock = pygame.time.Clock()
        self.loop()
    def startgame(self, m, n, bomba, legenda):
        self.mode = 1
        self.game = Game(m, n, bomba)
        self.width= m * 33 + 220
        self.height = n * 33 + 90 
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
    def perder(self):
        self.mode = 3
        for a in range(self.game.m):
            for b in range(self.game.n):
                if self.game.seenboard[a][b] == 0:
                    if self.game.board[a][b] == -1:
                        self.game.seenboard[a][b] = 1
                    
    def loop(self):
        self.screen.blit(nome, (100,500))
        self.screen.blit(voltar_menu, (0, 350))
        self.screen.blit(som_on, (0, 150))
        self.screen.blit(bordas, (550, 50))
        #self.screen.blit(img_fundoo, (0,0))
        
        while True:
            self.clock.tick(30)
            self.input(pygame.event.get())
            self.action()
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
                        if self.game.todiscover == 0:
                            self.ganhar()
        if self.mouseright == "pressed":
            if self.mode == 1:
                if (self.mouse_x in range(0, 64 + self.game.m * 64)):
                    if (self.mouse_y in range(0, 32 + self.game.n * 32)):
                        self.game.flag((self.mouse_x - 64) // 32, (self.mouse_y - 32) // 32)
        
                                
    def draw(self):
        screen = self.screen          
                    
        #if self.mode == 2:
            #screen.blit(img_youwin, (4, 4))
        #elif self.mode == 3:
            #screen.blit(img_youlose, (4, 4))
        
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

    
