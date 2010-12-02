# -*- coding: utf-8 -*-

# Parte do Codigo inicial(funcoes) do menu copiada.

import random
import os
import pygame
from pygame.locals import *
import sys
import time
import Jogo

class Opcao:

    def __init__(self, fonte, titulo, x, y, paridad, funcao_asignada):
        self.imagen_normal = fonte.render(titulo, 1, (238, 18, 137))
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


    def ativar(self):
        self.funcao_asignada()

class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load("Imagens_menu" + os.sep + "cursor1.png").convert_alpha()
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
    #Representa um menu com opcoes para um jogo
    
    def __init__(self, opcoes):

        pygame.mixer.music.load("Sons" + os.sep + "Musica_menu.wav")
        pygame.mixer.music.play(-1)
        self.opcoes = []
        fonte = pygame.font.Font("Imagens_menu" + os.sep + "billo.ttf", 35)
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
        #Altera o valor de 'self.selecionado' com as direcoes.

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
        pygame.mixer.music.load("Sons" + os.sep + "Musica_jogo.wav")
        pygame.mixer.music.play(-1)
        #Niveis diferenciados atraves da quantidade de minas, e
        # de quadrados a serem descobertos
        Jogo.Main(13, 13, 10)
        

    def medio():
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Sons" + os.sep + "Musica_jogo.wav")
        pygame.mixer.music.play(-1)
        Jogo.Main(15, 15, 25)
       

    def dificil():
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Sons" + os.sep + "Musica_jogo.wav")
        pygame.mixer.music.play(-1)
        Jogo.Main(17, 17, 40)
        

            
    class Opcao:

        def __init__(self, fonte, titulo, x, y, paridad, funcao_asignada):
            self.imagen_normal = fonte.render(titulo, 1, (255, 192, 203))
            self.image = self.imagen_normal
            self.rect = self.image.get_rect()
            self.rect.x = 500 * paridad
            self.rect.y = y
            self.funcao_asignada = funcao_asignada
            self.x = float(self.rect.x)

        def atualizar(self):
            destino_x = 200 
            self.x += (destino_x - self.x) / 30.0
            self.rect.x = int(self.x)

        def imprimir(self, screen):
            screen.blit(self.image, self.rect)


        def ativar(self):
            self.funcao_asignada()
#Menu Princial    
    class Menu:
        
        
        def __init__(self, opciones):
           
            self.opcoes = []
            fonte = pygame.font.Font("Imagens_menu" + os.sep + "ch.ttf", 50)
            x = 210 
            y = 260
            paridad = 1

            self.cursor = Cursor(x - 69, y -3 , 100)

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
                         
#Menu dos niveis                            
    if __name__ == '__main__':
        
        sair = False
        opcao = [
            ("Apenas Flores", facil),
            ("Alguns Espinhos", medio),
            ("Nem Tudo Sao Flores", dificil),
            ]

        pygame.font.init()

        pygame.display.set_caption ("Garden Mined - Niveis")
        screen = pygame.display.set_mode ((800, 600))
        fundo = pygame.image.load("Imagens_menu" +os.sep+ "niveis.png").convert()
        sair_tela = pygame.image.load("Imagens_jogo" + os.sep + "seta_voltar.png")
        
        menu = Menu(opcao)
        
        while not sair:
            for e in pygame.event.get():
                if e.type == QUIT:
                    sair = True

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()
            
            
            sairPos = (10, 500)
            sairSize = (50, 50)
            
            if sairPos[0] <= mouse_pos[0] <= sairPos[0] + sairSize[0]\
                and sairPos[1] <= mouse_pos[1] <= sairPos[1] + sairSize[1]:
                if mouse_press[0] :
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("Sons" + os.sep + "Musica_menu.wav")
                    pygame.mixer.music.play(-1)
                    
                    return
                
            screen.blit(fundo, (0, 0))
            screen.blit(sair_tela, (10, 500))
            menu.atualizar()
            menu.imprimir(screen)
        

            pygame.display.flip()
            pygame.time.delay(0)

    
def ajuda():
    sair = False
    pygame.font.init()
    pygame.display.set_caption ("Garden Mined - Instruçoes")
    screen = pygame.display.set_mode ((800, 600))
    fundo = pygame.image.load("Imagens_menu" + os.sep + "instrucao.png").convert()
    sair_tela = pygame.image.load("Imagens_jogo" + os.sep + "seta_voltar.png")
    
    while not sair:
            for e in pygame.event.get():

                mouse_pos = pygame.mouse.get_pos()
                mouse_press = pygame.mouse.get_pressed()
            
                sairPos = (10, 500)
                sairSize = (50, 50)
            
                if sairPos[0] <= mouse_pos[0] <= sairPos[0] + sairSize[0]\
                    and sairPos[1] <= mouse_pos[1] <= sairPos[1] + sairSize[1]:
                    if mouse_press[0] :
                        sair = True
                
            screen.blit(fundo, (0, 0))
            screen.blit(sair_tela, (10, 500))
            pygame.display.flip()
            pygame.time.delay(10)

def creditos():
    sair = False    
    pygame.font.init()
    pygame.display.set_caption ("Garden Mined - Creditos")
    screen = pygame.display.set_mode ((800, 600))
    fundo = pygame.image.load("Imagens_menu" + os.sep + "creditos.png").convert()
    sair_tela = pygame.image.load("Imagens_jogo" + os.sep + "seta_voltar.png")
    
    while not sair:
        for e in pygame.event.get():
        

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()
            
            sairPos = (10, 500)
            sairSize = (50, 50)
            
            if sairPos[0] <= mouse_pos[0] <= sairPos[0] + sairSize[0]\
                and sairPos[1] <= mouse_pos[1] <= sairPos[1] + sairSize[1]:
                if mouse_press[0] :
                    sair = True
                
        screen.blit(fundo, (0, 0))
        screen.blit(sair_tela, (10, 500))
            
        pygame.display.flip()
        pygame.time.delay(10)

def sair_do_jogo():
    sair = False
    pressionou = False
    pygame.font.init()
    fundo = pygame.image.load("Imagens_menu" + os.sep + "sair.png").convert()
    sair_tela = pygame.image.load("Imagens_jogo" + os.sep + "seta_voltar.png")
    pygame.time.delay(10)
    
    while not sair:
        tecla = pygame.key.get_pressed()
        for e in pygame.event.get():
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()

            cliqueSair = (200, 200)
            sairSize = (200, 200)
            
            if cliqueSair[0] <= mouse_pos[0] <= cliqueSair[0] + sairSize[0]\
                and cliqueSair[1] <= mouse_pos[1] <= cliqueSair[1] + sairSize[1]:
                    if mouse_press[0] :
                        sys.exit(0)
                        
                        

            sairPos = (10, 500)
            sairSize = (50, 50)
            
            if sairPos[0] <= mouse_pos[0] <= sairPos[0] + sairSize[0]\
                and sairPos[1] <= mouse_pos[1] <= sairPos[1] + sairSize[1]:
                if mouse_press[0] :
                    sair = True
                
        screen.blit(fundo, (200, 200))
        screen.blit(sair_tela, (10, 500))
        pygame.display.flip()
        pygame.time.delay(10)

#Menu principal
if __name__ == '__main__':  
        
    sair = False
    opcao = [
        ("Jogar", escolher_niveis),
        ("Ajuda", ajuda),
        ("Creditos", creditos),
        ("Sair do Jogo", sair_do_jogo)
        ]

    
    pygame.mixer.music.load("Sons" + os.sep + "Musica_menu.wav")
    pygame.mixer.music.play(-1)
    pygame.display.set_caption ("Garden Mined")
    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    fundo = pygame.image.load("Imagens_menu" + os.sep + "fundo_menu.png").convert()
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
