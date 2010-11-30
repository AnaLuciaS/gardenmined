# -*- coding: utf-8 -*-

import random
import os
import pygame
from pygame.locals import *
import sys
import nivel_dificil

import time

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
        self.x += (destino_x - self.x) / 30.0
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
        self.image = pygame.image.load("Menu" + os.sep + "cursor1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.selecionar(0)

    def atualizar(self): 
        self.y += (self.to_y - self.y) / 1.0
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
        x = 100 
        y = 150 
        paridad = 1

        self.cursor = Cursor(x - 69, y -3 , 60)

        for titulo, funcao in opcao:
            self.opcoes.append(Opcao(fonte, titulo, x, y, paridad, funcao))
            y += 60
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
               
                self.opcoes[self.selecionado].ativar()

        
        if self.selecionado < 0:
            self.selecionado = 0
        elif self.selecionado > self.total - 1:
            self.selecionado = self.total - 1
        
        self.cursor.selecionar(self.selecionado)

        
        self.mantem_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.atualizar()
     
        for o in self.opcoes:
            o.atualizar()
 
    def imprimir(self, screen):
        

        self.cursor.imprimir(screen)

        for opcao in self.opcoes:
            opcao.imprimir(screen)
            
def escolher_niveis():

    def facil():
        pygame.mixer.music.stop()
        #carrega a musica do jogo
        pygame.mixer.music.load("Menu/musica/musica_jogo.wav")
        pygame.mixer.music.play(-1)
        nivel_dificil.Main(10)
        

    def medio():
        pygame.mixer.music.stop()
        
        pygame.mixer.music.load("Menu/musica/musica_jogo.wav")
        pygame.mixer.music.play(-1)
        nivel_dificil.Main(20)
        print ' medio '

    def dificil():
        pygame.mixer.music.stop()
        
        pygame.mixer.music.load("Menu/musica/musica_jogo.wav")
        pygame.mixer.music.play(-1)
        nivel_dificil.Main(45)
        print " dificil "

            
    class Opcao:

        def __init__(self, fonte, titulo, x, y, paridad, funcao_asignada):
            self.imagen_normal = fonte.render(titulo, 1, (30, 144, 255))
            self.imagen_destacada = fonte.render(titulo, 1, (255, 255, 255))
            self.image = self.imagen_normal
            self.rect = self.image.get_rect()
            self.rect.x = 500 * paridad
            self.rect.y = y
            self.funcao_asignada = funcao_asignada
            self.x = float(self.rect.x)

        def atualizar(self):
            destino_x = 300 
            self.x += (destino_x - self.x) / 30.0
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



    class Menu:
        
        
        def __init__(self, opciones):
            self.opcoes = []
            fonte = pygame.font.Font("Menu" + os.sep + "amadeus.ttf", 70)
            x = 310 
            y = 200 
            paridad = 1

            self.cursor = Cursor(x - 69, y -3 , 110)

            for titulo, funcao in opcao:
                self.opcoes.append(Opcao(fonte, titulo, x, y, paridad, funcao))
                y += 100
                if paridad == 1:
                    paridad = -1
                else:
                    paridad = 1

            self.selecionado = 0
            self.total = len(self.opcoes)
            self.mantem_pulsado = False

        def atualizar(self):
            

            k = pygame.key.get_pressed()

            if not self.mantem_pulsado:
                if k[K_UP]:
                    self.selecionado -= 1
                elif k[K_DOWN]:
                    self.selecionado += 1
                elif k[K_RETURN]:
                    
                    self.opcoes[self.selecionado].ativar()

            if self.selecionado < 0:
                self.selecionado = 0
            elif self.selecionado > self.total - 1:
                self.selecionado = self.total - 1
            
            self.cursor.selecionar(self.selecionado)

            
            self.mantem_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

            self.cursor.atualizar()
         
            for o in self.opcoes:
                o.atualizar()

        def imprimir(self, screen):
           
            

            self.cursor.imprimir(screen)

            for opcao in self.opcoes:
                opcao.imprimir(screen)


                            
                            
    if __name__ == '__main__':
        
        sair = False
        opcao = [
            ("Facil", facil),
            ("Medio", medio),
            ("Dificil", dificil),
            ]

        pygame.font.init()

        pygame.display.set_caption ("Garden Mined - Niveis")
        screen = pygame.display.set_mode ((800, 600))
        fundo = pygame.image.load("menu" +os.sep+ "niveis.png").convert()
        menu = Menu(opcao)
        
        while not sair:

            tecla = pygame.key.get_pressed()

            for e in pygame.event.get():
                if e.type == QUIT:
                    sair = True

                if tecla[pygame.K_ESCAPE]:
                    sair = True



            screen.blit(fundo, (0, 0))
            menu.atualizar()
            menu.imprimir(screen)
        

            pygame.display.flip()
            pygame.time.delay(0)

    

def instrucoes():
    sair = False
    pygame.font.init()
    pygame.display.set_caption ("Garden Mined - Instruçoes")
    screen = pygame.display.set_mode ((800, 600))
    fundo = pygame.image.load("Menu" + os.sep + "instrucao.png").convert()
    
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
    pygame.display.set_caption ("Garden Mined - Creditos")
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
    pygame.time.delay(20)

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
        ("Jogar", escolher_niveis),
        ("Instrucoes", instrucoes),
        ("Creditos", creditos),
        ("Sair do Jogo", sair_do_jogo)
        ]

    pygame.display.set_caption ("Garden Mined")
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
