import random
import os
import pygame
from pygame.locals import *
import sys
from gardenmined import Main


#musica do jogo
pygame.mixer.music.load("Menu/musica/musica_menu.wav")
pygame.mixer.music.play(-1)

class Opcao:

    def __init__(self, fonte, titulo, x, y, paridad, funcao_asignada):
        self.imagen_normal = fonte.render(titulo, 1, (238, 18, 137))
        self.imagen_destacada = fonte.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcao_asignada = funcao_asignada
        self.x = float(self.rect.x)

    def atualizar(self):
        destino_x = 70
        self.x += (destino_x - self.x) / 50.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def ativar(self):
        self.funcao_asignada()

class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load("Menu" + os.sep + "cursor.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.selecionar(0)

    def atualizar(self): 
        self.y += (self.to_y - self.y) / 3.0# aumenta ou diminui a velocidade do cursor
        self.rect.y = int(self.y)

    def selecionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    "Representa um menu com opcoes para um jogo"
    
    def __init__(self, opciones):
        self.opcoes = []
        fonte = pygame.font.Font("Menu" + os.sep + "billo.ttf", 35)
        x = 335
        y = 110
        paridad = 1

        self.cursor = Cursor(x - 69, y + 15, 50)

        for titulo, funcao in opcao:
            self.opcoes.append(Opcao(fonte, titulo, x, y, paridad, funcao))
            y += 55
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.selecionado = 0
        self.total = len(self.opcoes)
        self.mantem_pulsado = False

    def atualizar(self):
        """Altera o valor de 'self.selecionado' com os direcoes."""

        k = pygame.key.get_pressed()

        if not self.mantem_pulsado:
            if k[K_UP]:
                self.selecionado -= 1
            elif k[K_DOWN]:
                self.selecionado += 1
            elif k[K_RETURN]:
                # Invoca a funcao associada a opcao.
                self.opcoes[self.selecionado].ativar()

        # verifica se o cursor esta entrelas opcoes permitidas.
        if self.selecionado < 0:
            self.selecionado = 0
        elif self.selecionado > self.total - 1:
            self.selecionado = self.total - 1
        
        self.cursor.selecionar(self.selecionado)

        # indica se o usuario mantem pulsada alguna tecla.
        self.mantem_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.atualizar()
     
        for o in self.opcoes:
            o.atualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' o texto de cada opcao do menu."""

        self.cursor.imprimir(screen)

        for opcao in self.opcoes:
            opcao.imprimir(screen)

def comecar_novo_jogo():
    pygame.mixer.music.stop()
    #carrega a musica do jogo
    pygame.mixer.music.load("Menu/musica/musica_jogo.wav")
    pygame.mixer.music.play(-1)

    Main()
    sair = False
'''    pygame.font.init()
    pygame.display.set_caption ("Garden Minde.")
    screen = pygame.display.set_mode ((800, 600))
    fundo = pygame.image.load("Menu" + os.sep + "niveis.png").convert()
    
    while not sair:
        tecla = pygame.key.get_pressed()
        for e in pygame.event.get():
            if e.type == QUIT:
                sair = True

            if tecla[pygame.K_ESCAPE]:
                sair = True

        screen.blit(fundo, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)

'''
def instrucoes():
    sair = False
    pygame.font.init()
    pygame.display.set_caption ("Garden Minde.")
    screen = pygame.display.set_mode ((800, 600))
    fundo = pygame.image.load("Menu" + os.sep + "instrucoes.png").convert()
    
    while not sair:
        tecla = pygame.key.get_pressed()
        for e in pygame.event.get():
            if e.type == QUIT:
                sair = True

            if tecla[pygame.K_ESCAPE]:
                sair = True

        screen.blit(fundo, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)

def creditos():
    sair = False    
    pygame.font.init()
    pygame.display.set_caption ("Garden Mined.")
    screen = pygame.display.set_mode ((800, 600))
    fundo = pygame.image.load("Menu" + os.sep + "creditos.png").convert()
    
    while not sair:
        tecla = pygame.key.get_pressed()
        for e in pygame.event.get():
            if e.type == QUIT:
                sair = True
            if tecla[pygame.K_ESCAPE]:
                sair = True

        screen.blit(fundo, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)

def sair_do_jogo():
    sair = False
    pressionou = False
    pygame.font.init()
    fundo = pygame.image.load("Menu" + os.sep + "sair.png").convert()
    pygame.time.delay(800)

    while not sair:
        tecla = pygame.key.get_pressed()
        for e in pygame.event.get():
            if e.type == QUIT:
                sair = True

            if tecla[pygame.K_ESCAPE]:
                sair = True

            if pressionou:
                sys.exit(0)

            if tecla[K_RETURN]:
                pressionou = True
                
        screen.blit(fundo, (200, 200))
        pygame.display.flip()
        pygame.time.delay(10)
        
if __name__ == '__main__':
    
    sair = False
    opcao = [
        ("Jogar", comecar_novo_jogo),
        ("Instrucoes", instrucoes),
        ("Creditos", creditos),
        ("Sair do Jogo", sair_do_jogo)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    fundo = pygame.image.load("Menu" + os.sep + "fundo_menu.png").convert()
    menu = Menu(opcao)

    while not sair:

        for e in pygame.event.get():
            if e.type == QUIT:
                sair = True

        screen.blit(fundo, (0, 0))
        menu.atualizar()
        menu.imprimir(screen)
        pygame.display.flip()
        pygame.time.delay(4)
