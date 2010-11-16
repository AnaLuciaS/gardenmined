# -*- coding: utf-8 -*-
#
# autor: Renato Cesar Vieira
# web: pythonbr.superforo.net
# licencia: GPL 2

import random
import os
import pygame
from pygame.locals import *


class Opcao:

    def __init__(self, fonte, titulo, x, y, paridad, funcao_asignada):
        self.imagen_normal = fonte.render(titulo, 1, (255, 69, 0))
        self.imagen_destacada = fonte.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcao_asignada = funcao_asignada
        self.x = float(self.rect.x)

    def atualizar(self):
        destino_x = 295#105
        self.x += (destino_x - self.x) / 5.0
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
        self.y += (self.to_y - self.y) / 8.0
        self.rect.y = int(self.y)

    def selecionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    "Representa um menú com opcoes para um jogo"
    
    def __init__(self, opciones):
        self.opcoes = []
        fonte = pygame.font.Font("Menu" + os.sep + "SABRINAS.ttf", 35)
        x = 335 # Alinha a direita ou equerda
        y = 150 # Dece ou sobe as opcoes
        paridad = 1

        self.cursor = Cursor(x - 69, y + 15, 50)

        for titulo, funcao in opcao:
            self.opcoes.append(Opcao(fonte, titulo, x, y, paridad, funcao))
            y += 50
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
                # Invoca a la función asociada a la opción.
                self.opcoes[self.selecionado].ativar()

        # procura que el cursor esté entre las opciones permitidas
        if self.selecionado < 0:
            self.selecionado = 0
        elif self.selecionado > self.total - 1:
            self.selecionado = self.total - 1
        
        self.cursor.selecionar(self.selecionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantem_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.atualizar()
     
        for o in self.opcoes:
            o.atualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' o texto de cada opcao do menú."""

        self.cursor.imprimir(screen)

        for opcao in self.opcoes:
            opcao.imprimir(screen)

def comecar_novo_jogo():
    print " Mostra novo jogo."

def mostrar_opcoes():
    print " Mostra opcao."

def creditos():
    print " Mostra creditos."

def sair_do_programa():
    import sys
    print " Obrigado por utilizar este programa."
    sys.exit(0)


if __name__ == '__main__':
    
    sair = False
    opcao = [
        ("Jogar", comecar_novo_jogo),
        ("Opcoes", mostrar_opcoes),
        ("Creditos", creditos),
        ("Sair", sair_do_programa)
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
        pygame.time.delay(10)
