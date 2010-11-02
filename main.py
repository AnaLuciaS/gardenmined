import pygame, sys, os, random
from pygame.locals import *
pygame.init()

# Codigo copiado do jogo Pybomb v1.0 e modificado de acordo com a nossa necessidade =D

def multiimageload(images):
    list = []
    for image in images:
        list.append(pygame.image.load(image))
    return list

MEDIUM = pygame.font.Font("resources\Samson.ttf", 24)

img_marker = pygame.image.load("resources\img_marker.png")
img_flag = pygame.image.load("resources\img_flor2.png")
img_bombsleft = MEDIUM.render("Bombs left: ", True, (255, 255, 255))
img_spaces = multiimageload(["resources\img_empty.png", "resources\img_1.png", "resources\img_2.png", "resources\img_3.png", "resources\img_4.png", "resources\img_5.png", "resources\img_6.png", "resources\img_7.png", "resources\img_8.png", "resources\img_bomba4.png"])

class Game(object):
    def __init__(self, m, n, bombs):
        self.bombsnumber = bombs
        self.bombsleft = bombs
        self.img_bombsleft = MEDIUM.render(str(self.bombsleft), True, (255, 255, 255))
        self.m = m
        self.n = n
        self.todiscover = m * n - bombs
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
        for bomb in range(self.bombsnumber):
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
        self.startgame(10, 10, 5, "PyBomb - Very Easy")
        self.mouseleft = "up"
        self.mouseright = "up"
        self.mode = 1
        self.clock = pygame.time.Clock()
        self.loop()
    def startgame(self, m, n, bombs, caption):
        self.mode = 1
        self.game = Game(m, n, bombs)
        self.width = m * 32 + 120 
        self.height = n * 32 + 32 
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
        self.screen = pygame.display.get_surface()
    def win(self):
        self.mode = 2
        for a in range(self.game.m):
            for b in range(self.game.n):
                if self.game.seenboard[a][b] == 0:
                    if self.game.board[a][b] == -1:
                        self.game.seenboard[a][b] = -1
    def lose(self):
        self.mode = 3
        for a in range(self.game.m):
            for b in range(self.game.n):
                if self.game.seenboard[a][b] == 0:
                    if self.game.board[a][b] == -1:
                        self.game.seenboard[a][b] = 1
    def loop(self):
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
            if event.type == QUIT or (event.type == KEYDOWN and event.key ==27):
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
                if (self.mouse_x in range(0, self.game.m * 32)): 
                     if (self.mouse_y in range(32, 32 + self.game.n * 32)): 
                        if self.game.started == False:
                            if self.game.seenboard[self.mouse_x // 32][(self.mouse_y - 32) // 32] == 0: 
                                self.game.start(self.mouse_x // 32, (self.mouse_y - 32) // 32) 
                        if self.game.discover(self.mouse_x // 32, (self.mouse_y - 32) // 32) == "Bomb": 
                            self.lose()
                        if self.game.todiscover == 0:
                            self.win()
        if self.mouseright == "pressed":
            if self.mode == 1:
                if (self.mouse_x in range(0, self.game.m * 32)):
                    if (self.mouse_y in range(32, 32 + self.game.n * 32)):
                        self.game.flag(self.mouse_x // 32, (self.mouse_y - 32) // 32)
    def draw(self):
        screen = self.screen
        
        if self.mouse_x in range(self.width - 120, self.width):
                if self.mouse_y in range(12, 36):
                    pygame.draw.rect(screen, (0, 0, 0), (self.width - 119, 12, 118, 24), 1)
                if self.mouse_y in range(44, 68):
                    pygame.draw.rect(screen, (0, 0, 0), (self.width - 119, 44, 118, 24), 1)
                if self.mouse_y in range(76, 100):
                    pygame.draw.rect(screen, (0, 0, 0), (self.width - 119, 76, 118, 24), 1)
                if self.mouse_y in range(108, 132):
                    pygame.draw.rect(screen, (0, 0, 0), (self.width - 119, 108, 118, 24), 1)
                if self.mouse_y in range(140, 164):
                    pygame.draw.rect(screen, (0, 0, 0), (self.width - 119, 140, 118, 24), 1)
                if self.mouse_y in range(172, 196):
                    pygame.draw.rect(screen, (0, 0, 0), (self.width - 119, 172, 118, 24), 1)
        
        pygame.draw.rect(screen, (255, 255, 255), (0, 32, self.width - 121, self.height - 32))
        for a in range(self.game.m):
            for b in range(self.game.n):
                if self.game.seenboard[a][b] == 1:
                    screen.blit(img_spaces[self.game.board[a][b]], (a * 32, 32 + b * 32))
                elif self.game.seenboard[a][b] == -1:
                    screen.blit(img_flag, (a * 32, 32 + b * 32))
        for a in range(self.game.m):
            pygame.draw.line(screen, (0, 0, 0), (a * 32, 32), (a * 32, 32 + self.game.n * 32))
        for b in range(self.game.n):
            pygame.draw.line(screen, (0, 0, 0), (0, 32 + b * 32), (self.game.m * 32, 32 + b * 32))
        if self.mouse_x in range(0, self.game.m * 32):
            if self.mouse_y in range(32, 32 + self.game.n * 32):
                screen.blit(img_marker, ((self.mouse_x // 32) * 32 - 4, (self.mouse_y // 32) * 32 - 4))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, self.width, self.height), 1)
        pygame.display.flip()

Main()
