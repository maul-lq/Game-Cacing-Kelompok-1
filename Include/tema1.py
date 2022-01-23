from typing import Iterable
import pygame
import sys
from pygame.font import Font
from pygame.locals import *
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Game Base", "Game Dasar")
layar = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 20)
draw = pygame.draw
mouse = pygame.mouse
red = 255
green = 255
blue = 255


def draw_text(text: str = ..., fontStyle: Font = ..., color: tuple = (red, green, blue), permukaan: pygame.Surface = ..., x_pos: float = int, y_pos: float = int):
    textObj = fontStyle.render(text, True, color)
    textRect = textObj.get_rect()
    textRect.topleft = (x_pos, y_pos)
    permukaan.blit(textObj, textRect)


kelik = False


def main_menu():
    while True:

        layar.fill((0, 0, 0))
        draw_text("Menu Utama", font, (225, 225, 225), layar, 20, 20)

        mouseX, mouseY = pygame.mouse.get_pos()

        tombol_1 = pygame.Rect(50, 100, 200, 50)
        tombol_2 = pygame.Rect(50, 100, 200, 50)

        if tombol_1.collidepoint((mouseX, mouseY)):
            if kelik:
                game()
        if tombol_2.collidepoint((mouseX, mouseY)):
            if kelik:
                opsi()

        draw.rect(layar, (225, 0, 0), tombol_1)
        draw.rect(layar, (225, 0, 0), tombol_2)

        kelik = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                pass
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == True:
                    kelik = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        layar.fill((0, 0, 0))
        draw_text("Game", font, (225, 225, 225), layar, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)


def opsi():
    running = True
    while running:
        layar.fill((0, 0, 0))
        draw_text("Opsimenu", font, (225, 225, 225), layar, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
