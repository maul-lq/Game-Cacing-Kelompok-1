from pygame_widgets.button import Button
from pathlib import Path
import pygame_widgets
import pygame


def rgb(r: int, g: int, b: int, a: int = 255):
    return pygame.Color(r, g, b, a)


# Theme Colour, Skin, etc.
# bg=backgroun, pn1=Panel 1,
# tk=Teks, btn[A,H,P,Sh]=Tombol[aktif,pointerdiarahkan,ditekan,bayangan]
theme_path_1 = Path('./res/image/ular/tema0')
theme_path_2 = Path('./res/image/ular/tema1')
theme_path_3 = Path('./res/image/ular/tema2')
theme_path_4 = Path('./res/image/ular/tema3')

makanan = Path('./res/image/makanan/')

# region Theme Colour
# ulet buah
tema0 = {
    'bg': rgb(180, 204, 73),
    'pn1': rgb(122, 153, 104),
    'tk': rgb(233, 255, 191),
    'btnA': rgb(153, 174, 45),
    'btnH': rgb(166, 189, 50),
    'btnP': rgb(109, 123, 35),
    'btnSh': rgb(25, 21, 45),
    'wl': rgb(233, 255, 191),
    'skp': rgb(122, 153, 104),
    'brd': rgb(122, 160, 100),
    'rm': rgb(175, 199, 72)
}
# cacing tanah
tema1 = {
    'bg': rgb(255, 170, 94),
    'pn1': rgb(208, 129, 89),
    'tk': rgb(13, 43, 69),
    'btnA': rgb(187, 86, 58),
    'btnH': rgb(201, 102, 74),
    'btnP': rgb(134, 64, 45),
    'btnSh': rgb(13, 43, 69),
    'wl': rgb(255, 236, 214),
    'skp': rgb(246, 160, 85),
    'brd': rgb(244, 150, 67),
    'rm': rgb(255, 165, 87)
}
#
tema2 = {
    'bg': rgb(255, 255, 255),
    'pn1': rgb(139, 202, 221),
    'tk': rgb(44, 74, 120),
    'btnA': rgb(167, 188, 201),
    'btnH': rgb(214, 225, 233),
    'btnP': rgb(115, 141, 157),
    'btnSh': rgb(32, 40, 78),
    'wl': rgb(115, 141, 157),
    'skp': rgb(110, 188, 212),
    'brd': rgb(130, 196, 217),
    'rm': rgb(250, 250, 250)
}
tema3 = {
    'bg': rgb(150, 206, 180),
    'pn1': rgb(255, 238, 173),
    'tk': rgb(217, 83, 79),
    'btnA': rgb(255, 173, 96),
    'btnH': rgb(254, 187, 123),
    'btnP': rgb(255, 150, 51),
    'btnSh': rgb(49, 94, 73),
    'skp': rgb(255, 233, 143),
    'brd': rgb(255, 225, 107),
    'rm': rgb(157, 210, 185)
}
# endregion

# region Default Var
wLine = tema0['wl']
bg = tema0['bg']
pn1 = tema0['pn1']
warnaTeks = tema0['tk']
skp = tema0['skp']
brd = tema0['brd']

# tombol
wBA = tema0['btnA']
wBH = tema0['btnH']
wBP = tema0['btnP']
wBSh = tema0['btnSh']
# endregion


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
           onClick=lambda: print(True, 0),
           onRelease=lambda: print(True, 1)):

    return Button(win, x_pos, y_pos, lebar, tinggi, text=teks, fontSize=fontSize, margin=margin,
                  inactiveColour=warnaAktif, hoverColour=warnaHover, pressedColour=warnaDitekan,
                  radius=sudutRad, onClick=onClick, textColour=warnaTeks, shadowDistance=shadowDistance,
                  shadowColour=shadowColour, font=font, onRelease=onRelease)


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
