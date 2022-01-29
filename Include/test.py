from time import sleep

from pygame import *
from pygame.locals import *
from pygame_gui import *

init()
WIN_SIZE = (1000, 680)  # (LEBAR, TINGGI)
TITLE = "Kelompok 1: Game Ular Kotak!!"
FPS = 60

fontStyle = font.SysFont(None, 40)

# region default var
red = 255
green = 255
blue = 255
# endregion


def draw_text(text: str = ..., fontStyle: font.Font = ..., color: tuple = (red, green, blue), permukaan: Surface = ..., x_pos: float = int, y_pos: float = int):
    textObj = fontStyle.render(text, True, color)
    textRect = textObj.get_rect()
    textRect.topleft = (x_pos, y_pos)
    permukaan.blit(textObj, textRect)


class MenuUtama:
    def __init__(self):
        init()
        display.set_caption(TITLE)

        self.layar = display.set_mode(WIN_SIZE)
        self.manager = UIManager(WIN_SIZE)

        self.layar_bg = Surface(WIN_SIZE)
        self.clock = time.Clock()
        self.fps = self.clock.tick(FPS)/1000.0

        self.layar_bg.fill(Color('#5e6745'))

        # Text
        draw_text("Menu Utama: Game Ular Kotak!", fontStyle, Color(
            '#e3eec0'), permukaan=self.layar_bg, x_pos=20, y_pos=20)

        # Button
        self.btnSize = (200, 100)
        self.btn_play = elements.UIButton(
            Rect((20, 100), self.btnSize), "Main", self.manager)
        self.btn_pengaturan = elements.UIButton(
            Rect((20, 250), self.btnSize), "Pengaturan", self.manager)

    def run(self):
        self.running = True  # Game Sedang Berjalan

        while self.running:
            for peristiwa in event.get():
                if peristiwa.type == QUIT or peristiwa.type == K_F4:
                    self.running = False

                if peristiwa.type == KEYDOWN:
                    if peristiwa.key == K_RETURN:
                        Game().run()
                        pass

                if peristiwa.type == UI_BUTTON_PRESSED:
                    if peristiwa.ui_element == self.btn_play:
                        Game().run()
                    if peristiwa.ui_element == self.btn_pengaturan:
                        Pengaturan().run()

                self.manager.process_events(peristiwa)

            self.manager.update(self.fps)
            self.layar.blit(self.layar_bg, (0, 0))
            self.manager.draw_ui(self.layar)

            display.update()


class Pengaturan:
    def __init__(self) -> None:
        init()

    def run(self):
        self.running = True
        while self.running:
            pass


class Game:
    def __init__(self):
        init()
        display.set_caption(TITLE)

        self.layar = display.set_mode(WIN_SIZE)

    def Layar(self):
        self.layar.fill((250, 250, 250))

    def run(self):
        self.running = True  # Game Sedang Berjalan

        while self.running:
            self.Layar()
            for peristiwa in event.get():
                if peristiwa.type == QUIT or peristiwa.type == K_F4:
                    self.running = False
                    quit()

                if peristiwa.type == KEYDOWN:
                    if peristiwa.key == K_RETURN:
                        MenuUtama().run()

            display.update()
            time.Clock().tick(FPS)


if __name__ == '__main__':
    MenuUtama().run()
    # import pygame
    # import pygame_gui

    # pygame.init()

    # pygame.display.set_caption('Quick Start')
    # window_surface = pygame.display.set_mode((800, 600))

    # background = pygame.Surface((800, 600))
    # background.fill(pygame.Color('#000000'))

    # manager = pygame_gui.UIManager((800, 600))

    # hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
    #                                             text='Say Hello',
    #                                             manager=manager)

    # clock = pygame.time.Clock()
    # is_running = True

    # while is_running:
    #     time_delta = clock.tick(60)/1000.0
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             is_running = False

    #         if event.type == pygame_gui.UI_BUTTON_PRESSED:
    #             if event.ui_element == hello_button:
    #                 print('Hello World!')

    #         manager.process_events(event)

    #     manager.update(time_delta)

    #     window_surface.blit(background, (0, 0))
    #     manager.draw_ui(window_surface)

    #     pygame.display.update()
