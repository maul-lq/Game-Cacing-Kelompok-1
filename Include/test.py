from time import sleep
from typing import Tuple

from pygame import *
from pygame.locals import *
from pygame_gui import *

init()
WIN_SIZE = (1000, 680)  # (LEBAR, TINGGI)
TITLE = "Kelompok 1: Game Ular Kotak!!"
FPS = 60
BUTTON_SIZE = (200, 100)

fontStyle = font.SysFont(None, 40)

# region default var
red = 255
green = 255
blue = 255
lebar = int
tinggi = int
x_pos = int
y_pos = int
layar = UIManager
# endregion


def draw_teks(teks: str = ..., fontStyle: font.Font = ..., color: tuple = (red, green, blue), permukaan: Surface = ..., x_pos: float = 0, y_pos: float = 0):
    teksObj = fontStyle.render(teks, True, color)
    teksRect = teksObj.get_rect()
    teksRect.topleft = (x_pos, y_pos)
    return permukaan.blit(teksObj, teksRect)


def draw_btn(UIManager: layar, teks: str = 'Tombol', luas: Tuple = (20, 20), xy_pos: Tuple = (0, 0), terlihat: int = 1, anchor: dict = None):
    """
    Fungsi Membuat Tombol Menggunakan Pygame & Pygame_gui.

    Args:
        UIManager (layar): Sebuah argumen yang membutuhkan ``UIManager`` sebagai layar.
        teks (str, optional): Sebuah argumen teks yang di butuhkan untuk meulis pada tombol / menamainya. Defaults to 'Tombol'.
        luas (Tuple, optional): Luas sebuah tombol tersebut berupa tuple (Lebar, Tinggi). Defaults to (float, float).
        xy_pos (Tuple, optional): Sebuah argumen (x_pos, y_pos) untuk menempatkan posisi tombol pada layar / ``UIManager``. Defaults to (float, float).
        terlihat (int, optional): Sebuah argumen untuk menampilkan / menyembunyikan tombol. Defaults to 1.
        anchor (Dict, optional): Sebuah argumen untuk memberikan posisi tombol yang tepat. Defaults to None

    Returns:
        UIButton: Sebuah tombol yang bisa ditekan.
    """
    return elements.UIButton(Rect(xy_pos, luas), teks, UIManager, visible=terlihat, anchors=anchor)


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
        draw_teks("Menu Utama: Game Ular Kotak!", fontStyle, Color(
            '#e3eec0'), permukaan=self.layar_bg, x_pos=20, y_pos=20)

        # Button
        BUTTON_SIZE
        self.btn_play = draw_btn(self.manager, 'Main', BUTTON_SIZE, (20, 100))
        self.btn_pengaturan = draw_btn(
            self.manager, "Pengaturan", BUTTON_SIZE, (20, 250))
        self.btn_keluar = draw_btn(
            self.manager, "Keluar", BUTTON_SIZE, (20, 400))

    def run(self):
        self.running = True  # Game Sedang Berjalan

        while self.running:
            for peristiwa in event.get():
                if peristiwa.type == QUIT or peristiwa.type == K_F4:
                    exit()

                if peristiwa.type == KEYDOWN:
                    if peristiwa.key == K_END:
                        self.manager.set_visual_debug_mode(False)
                    if peristiwa.key == K_HOME:
                        self.manager.set_visual_debug_mode(True)

                        pass

                if peristiwa.type == UI_BUTTON_PRESSED:
                    if peristiwa.ui_element == self.btn_play:
                        Game().run()
                    if peristiwa.ui_element == self.btn_pengaturan:
                        Pengaturan().run()
                    if peristiwa.ui_element == self.btn_keluar:
                        exit()

                self.manager.process_events(peristiwa)

            self.manager.update(self.fps)
            self.layar.blit(self.layar_bg, (0, 0))
            self.manager.draw_ui(self.layar)

            self.clock.tick(FPS)
            display.update()


class Pengaturan:
    def __init__(self) -> None:
        init()

        self.layar = display.set_mode(WIN_SIZE)
        self.manager = UIManager(WIN_SIZE)

        self.bg_layar = Surface(WIN_SIZE)
        self.bg_layar.fill(Color('#efefef'))

        self.btn_kembali = draw_btn(
            self.manager, 'Kembali', BUTTON_SIZE, (20, WIN_SIZE[1]-120))

    def run(self):
        self.running = True
        while self.running:
            for prstw in event.get():
                if prstw.type == QUIT:
                    exit()

                if prstw.type == KEYDOWN:
                    if prstw.key == K_ESCAPE:
                        self.running = False

                if prstw.type == UI_BUTTON_PRESSED:
                    if prstw.ui_element == self.btn_kembali:
                        self.running = False

                self.manager.process_events(prstw)

            self.manager.update(MenuUtama().fps)
            self.layar.blit(self.bg_layar, (0, 0))
            self.manager.draw_ui(self.layar)

            display.update()

class Makanan:
    def __init__(self, layar: Surface) -> None:
        pass
    
class Ular:
    def __init__(self, layar: Surface) -> None:
        pass


class Game:
    def __init__(self):
        init()
        display.set_caption(TITLE)

        self.layar = display.set_mode(WIN_SIZE)
        self.makanan = Makanan(self.layar)
        self.ular = Ular(self.layar)
        
        self.manager = UIManager(WIN_SIZE)
        self.bg_layar = Surface(WIN_SIZE)
        self.bg_layar.fill(Color('#dadada'))

        self.btn_kembali = draw_btn(
            self.manager, 'Kembali', (BUTTON_SIZE), (20, WIN_SIZE[1]-120))

    def run(self):
        self.running = True  # Game Sedang Berjalan

        while self.running:
            for peristiwa in event.get():
                if peristiwa.type == QUIT or peristiwa.type == K_F4:
                    exit()

                if peristiwa.type == KEYDOWN:
                    if peristiwa.key == K_ESCAPE:
                        self.running = False

                if peristiwa.type == UI_BUTTON_PRESSED:
                    if peristiwa.ui_element == self.btn_kembali:
                        self.running = False

                self.manager.process_events(peristiwa)

            self.manager.update(MenuUtama().fps)
            self.layar.blit(self.bg_layar, (0, 0))
            self.manager.draw_ui(self.layar)
            display.update()
            time.Clock().tick(FPS)


if __name__ == '__main__':
    MenuUtama().run()
