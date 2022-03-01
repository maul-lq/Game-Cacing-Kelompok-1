from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
import pygame_widgets
import pygame


def rgb(r: int, g: int, b: int, a: int = 255):
    return pygame.Color(r, g, b, a)


def Tombol(win: pygame.Surface,
           x_pos: int, y_pos: int,
           lebar: int, tinggi: int,
           font: pygame.font.Font,
           fontSize: int = 20,
           teks: str = "",
           warnaTeks: tuple = (0, 0, 0),
           warnaAktif: tuple = (50, 50, 50),
           warnaHover: tuple = (100, 100, 100),
           warnaDitekan: tuple = (25, 25, 25),
           margin: int = 20,
           sudutRad: int = 0,
           shadowDistance: int = 0,
           shadowColour: tuple = (210, 210, 180),
           onClick=lambda: print(True)):

    return Button(win, x_pos, y_pos, lebar, tinggi, text=teks, fontSize=fontSize, margin=margin,
                  inactiveColour=warnaAktif, hoverColour=warnaHover, pressedColour=warnaDitekan,
                  radius=sudutRad, onClick=onClick, textColour=warnaTeks, shadowDistance=shadowDistance,
                  shadowColour=shadowColour, font=font)


if __name__ == "__main__":
    import pygame_widgets
    import pygame
    import time
    from pygame_widgets.progressbar import ProgressBar

    startTime = time.time()

    pygame.init()
    win = pygame.display.set_mode((1000, 600))

    progressBar = ProgressBar(
        win, 100, 100, 500, 40, lambda: 1 - (time.time() - startTime) / 10, curved=True)

    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        win.fill((255, 255, 255))

        pygame_widgets.update(events)
        pygame.display.update()
