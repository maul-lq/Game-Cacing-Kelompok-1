# Wednesday, February - 9 - 2022 (9/2/22) [12:35:48,265 PM]  /  GMT+0700 || 6
from random import randint
from pygame import *
from pygame_gui import *
from pygame.locals import *
from pathlib import Path


# region Variabel
DEFAULT_FPS = 60
WIN_RES = (640, 640)  # Window Resolution  (1000x680)
BTN_SIZE = (200, 70)  # (400x100)
GAME_PANEL_SIZE = (500, 500)  # (500x500)
GAMESTAT_PANEL_SIZE = (520, 80)  # (520x80)
SK_SIZE = 20
FD_SIZE = 20

JUDUL = 'Game Kelompok 1: Ular Scam!'
PATH_BG = Path('./res/image/bg')
PATH_SK = Path('./res/image/sk')
PATH_FD = Path('./res/image/fd')
THEME = {
    #! Default
    # background
    'bg': Color('#16c60c'),
    'bg1': Color('#005706'),
    # judul
    'jd': Color('#ff0000'),
    # teks
    'tx': Color('#fafafa'),

    # region Red
    'rbg': Color('#c65d5d'),
    'rbg1': Color('#c50f1e'),
    'rjd': Color('#ffff00'),
    'rtx': Color('#ffca00'),
    # endregion

    # region Pink
    'pbg': Color('#FC8BC0'),
    'pbg1': Color('#e85e9f'),
    'pjd': Color('#25C0C0'),
    'ptx': Color('#F3BC50')
}
THEME_IMG = {
    # !Default
    'bg_preview': 'bg_preview.png',
    'bg_def': 'bg_th_def.png',
    'bg_wall_def': 'bg_th_wall_def.png',
    'sk_def': 'sk_th_def.png',
    'fd_def': 'jengkol.png',

    # ?Red
    'bg_preview1': 'bg_preview1.png',
    'bg_red': 'bg_th_1.png',

    # ?Pink
    'bg_preview2': 'bg_preview2.png',
    'bg_pink': 'bg_th_2.png'
}

display.set_caption(JUDUL)
layar = display.set_mode((WIN_RES))


def draw_btn(UIManager: UIManager, teks: str = 'Tombol', luas: tuple = (20, 20), xy_pos: tuple = (0, 0), terlihat: int = 1):
    """
    Fungsi Membuat Tombol Menggunakan Pygame & Pygame_gui.

    Args:
        UIManager (layar): Sebuah argumen yang membutuhkan ``UIManager`` sebagai layar.
        teks (str, optional): Sebuah argumen teks yang di butuhkan untuk meulis pada tombol / menamainya. Defaults to 'Tombol'.
        luas (Tuple, optional): Luas sebuah tombol tersebut berupa tuple (Lebar, Tinggi). Defaults to (float, float).
        xy_pos (Tuple, optional): Sebuah argumen (x_pos, y_pos) untuk menempatkan posisi tombol pada layar / ``UIManager``. Defaults to (float, float).
        terlihat (int, optional): Sebuah argumen untuk menampilkan / menyembunyikan tombol. Defaults to 1.
        anchor (tuple, optional): Sebuah argumen untuk memberikan posisi tombol yang tepat, ('anchor', xy_pos). Defaults to None

    Returns:
        UIButton: Sebuah tombol yang bisa ditekan.
    """
    return elements.UIButton(Rect((xy_pos), (luas)), teks, UIManager, visible=terlihat)


def draw_teks(teks: str = ..., fontStyle: tuple = (str, int, bool, bool), color: tuple = ..., permukaan: Surface = ..., x_pos: float = 0, y_pos: float = 0):
    init()
    teksObj = font.SysFont(
        fontStyle[0], fontStyle[1], fontStyle[2], fontStyle[3]).render(teks, True, color)
    teksRect = teksObj.get_rect()
    teksRect.topleft = (x_pos, y_pos)
    return permukaan.blit(teksObj, teksRect)


class UI:
    def __init__(self, theme: str = 'default'):
        init()
        display.set_caption(JUDUL)
        self.fps = time.Clock().tick(DEFAULT_FPS)
        self.layar = display.set_mode(WIN_RES)
        self.setTheme = theme
        self.theme = self.setTheme
        self.loadInterface(self.setTheme)
        self.id = [
            # Default 0-3
            'bg',
            'bg1',
            'jd',
            'tx',
        ]
        if self.setTheme == 'default':
            self.theme = 'default'
        elif self.setTheme == 'red':
            self.theme = 'red'
        elif self.setTheme == 'pink':
            self.theme = 'pink'
        # Membuat var map img
        self.bg_map = image.load(PATH_BG / THEME_IMG['bg_def'])
        self.bg_wall = image.load(PATH_BG / THEME_IMG['bg_wall_def'])
        self.bg_map_preview = image.load(PATH_BG / THEME_IMG['bg_preview'])
        self.sk_img = image.load(PATH_SK / THEME_IMG['sk_def'])
        self.fd_img = image.load(PATH_FD / THEME_IMG['fd_def'])

        self.ularX = (((GAME_PANEL_SIZE[0]/2) % 20)*SK_SIZE)-40
        self.ularY = (((GAME_PANEL_SIZE[1]/2) % 20)*SK_SIZE)+20
        self.ular_Xpos = 0
        self.ular_Ypos = 0

        self.loop_opt = True
        self.loop_home = True
        pass

    def loadInterface(self, theme: str):
        self.theme = theme
        if self.theme == 'default':
            self.id = [
                # Default 0-4
                'bg',
                'bg1',
                'jd',
                'tx'
            ]
            self.bg_map_preview = image.load(PATH_BG / THEME_IMG['bg_preview'])
            self.bg_map = image.load(PATH_BG / THEME_IMG['bg_def'])
            self.bg_wall = image.load(PATH_BG / THEME_IMG['bg_wall_def'])
            self.fd_img = image.load(PATH_FD / THEME_IMG['fd_def'])
        elif self.theme == 'red':
            self.id = [
                # Red 0-3
                'rbg',
                'rbg1',
                'rjd',
                'rtx'
            ]
            self.bg_map_preview = image.load(
                PATH_BG / THEME_IMG['bg_preview1'])
            self.bg_map = image.load(PATH_BG / THEME_IMG['bg_red'])
        elif self.theme == 'pink':
            self.id = [
                # Pink 0-4
                'pbg',
                'pbg1',
                'pjd',
                'ptx',
            ]
            self.bg_map_preview = image.load(
                PATH_BG / THEME_IMG['bg_preview2'])
            self.bg_map = image.load(PATH_BG / THEME_IMG['bg_pink'])
        # region Menu Utama
        self.layar_utama = Surface(WIN_RES)
        self.manager_utama = UIManager(WIN_RES)
        self.layar_utama.fill(THEME[self.id[0]])
        self.lyr_um = Surface(
            (BTN_SIZE[0]+40, (WIN_RES[1]/2)+20))
        self.lyr_um.fill(THEME[self.id[1]])

        # Teks
        draw_teks("SNAKE", ('Arial', 100, True, False),
                  THEME[self.id[2]], self.layar_utama, WIN_RES[0]/2-(287/2), 20)
        # print(judul().width)

        # Tombol
        self.btn_play = draw_btn(self.manager_utama, 'START', BTN_SIZE, ((
            WIN_RES[0]-BTN_SIZE[0])/2, (WIN_RES[1]/2)-(BTN_SIZE[1]+10)))
        self.btn_option = draw_btn(
            self.manager_utama, 'OPTION', BTN_SIZE, ((WIN_RES[0]-BTN_SIZE[0])/2, (WIN_RES[1]/2)))
        self.btn_keluar = draw_btn(
            self.manager_utama, 'EXIT', BTN_SIZE, ((WIN_RES[0]-BTN_SIZE[0])/2, (WIN_RES[1]/2)+(BTN_SIZE[1]+10)))
        # endregion

        # region Menu Pengaturan
        self.manager_opt = UIManager(WIN_RES)
        self.layar_option = Surface(WIN_RES)
        self.layar_option.fill(THEME[self.id[0]])

        self.lyr_on = Surface((WIN_RES[0]-20, WIN_RES[1]-145))
        self.lyr_on.fill(THEME[self.id[1]])
        self.lyr_onXYpos = self.lyr_on.get_size()

        self.lyr_pwv = Surface((350, 350))
        self.lyr_pwvXYpos = self.lyr_pwv.get_size()

        # Teks
        self.h1 = draw_teks('OPTIONS', ('Arial', 100, True, False),
                            THEME[self.id[2]], self.layar_option, WIN_RES[0]/2-(370/2), 20)
        # print(self.h1.bottomright)
        self.h2 = draw_teks('Theme', ('Arial', 50, True, False),
                            THEME[self.id[3]], self.lyr_on, 10, 10)
        self.h2_2 = draw_teks('Preview Theme', ('Arial', 50, True, False),
                              THEME[self.id[3]], self.lyr_on, (self.lyr_onXYpos[0]-50)-self.lyr_pwvXYpos[0], 10)

        # print(h1().width)

        # region Tombol

        # region Theme
        # ? Default
        self.btn_theme = draw_btn(
            self.manager_opt, 'Default', (BTN_SIZE[0]/2, BTN_SIZE[1]/2), (20+(BTN_SIZE[0]-200) + 20, (WIN_RES[1]-(BTN_SIZE[1]/2))-20))

        # ? Red
        self.btn_theme1 = draw_btn(
            self.manager_opt, 'Red', (BTN_SIZE[0]/2, BTN_SIZE[1]/2), (20, (200)+5))

        # ? Pink
        self.btn_theme2 = draw_btn(
            self.manager_opt, 'Pink', (BTN_SIZE[0]/2, BTN_SIZE[1]/2), (20+(BTN_SIZE[0]/2)+20, (200)+5))
        # endregion

        self.btn_kembali = draw_btn(
            self.manager_opt, 'Kembali', (BTN_SIZE[0]-200, BTN_SIZE[1]/2), (20, (WIN_RES[1]-(BTN_SIZE[1]/2))-20))
        # endregion
        # endregion

        # region Game
        self.layar_game = Surface(WIN_RES)
        self.manager_game = UIManager(WIN_RES)
        self.layar_game.fill(Color(THEME[self.id[0]]))

        self.tembok = Surface((GAME_PANEL_SIZE[0]+20, GAME_PANEL_SIZE[1]+20))
        self.tembok.blit(self.bg_wall, (0, 0))
        self.layar_gamePlay = Surface(GAME_PANEL_SIZE)
        self.layar_gamePlay.fill(Color(THEME[self.id[1]]))
        self.layar_gamePlay.blit(self.bg_map, (0, 0))
        self.layar_gameStat = Surface(GAMESTAT_PANEL_SIZE)
        self.layar_gameStat.fill(Color(THEME[self.id[1]]))
        # endregion

    def home(self):
        self.loadInterface(self.setTheme)
        while self.loop_home:

            for pristw in event.get():
                if pristw.type == QUIT:
                    exit()
                if pristw.type == KEYDOWN:
                    if pristw.key == K_ESCAPE:
                        self.option()

                if pristw.type == UI_BUTTON_PRESSED:
                    if pristw.ui_element == self.btn_option:
                        self.option()
                    elif pristw.ui_element == self.btn_keluar:
                        exit()
                    elif pristw.ui_element == self.btn_play:
                        pass

                self.manager_utama.process_events(pristw)

            self.manager_utama.update(self.fps)
            self.layar.blit(self.layar_utama, (0, 0))
            self.layar_utama.blit(self.lyr_um, ((
                (WIN_RES[0]-BTN_SIZE[0])/2)-20, (WIN_RES[1]/2)-(BTN_SIZE[1]+10)-20))
            self.manager_utama.draw_ui(self.layar_utama)
            time.Clock().tick(DEFAULT_FPS)
            display.update()

    def option(self):
        self.loadInterface(self.setTheme)
        while self.loop_opt:

            for pristw in event.get():
                if pristw.type == QUIT:
                    exit()

                if pristw.type == KEYDOWN:
                    if pristw.key == K_ESCAPE:
                        self.home()
                if pristw.type == UI_BUTTON_PRESSED:
                    if pristw.ui_element == self.btn_kembali:
                        self.home()
                    if pristw.ui_element == self.btn_theme:
                        self.setTheme = self.loadInterface('default')
                    if pristw.ui_element == self.btn_theme1:
                        self.setTheme = self.loadInterface('red')
                    if pristw.ui_element == self.btn_theme2:
                        self.setTheme = self.loadInterface('pink')

                self.manager_opt.process_events(pristw)

            self.manager_opt.update(self.fps)
            self.layar.blit(self.layar_option, (0, 0))
            self.layar_option.blit(
                self.lyr_on, (10, 135))
            self.lyr_on.blit(
                self.lyr_pwv, ((self.lyr_onXYpos[0]-50)-self.lyr_pwvXYpos[0], ((self.lyr_onXYpos[1]*(1/4))-(self.lyr_pwvXYpos[1]*(1/4))+(self.h2_2.height+10))))
            self.lyr_pwv.blit(self.bg_map_preview, (0, 0))
            self.manager_opt.draw_ui(self.layar_option)
            time.Clock().tick(DEFAULT_FPS)
            display.update()

    def Ular(self, x_pos: float, y_pos: float):
        self.layar_gamePlay.blit(self.sk_img, (x_pos, y_pos))

    def Game(self):
        self.loadInterface(self.setTheme)
        while self.loop_game:
            for pristw in event.get():
                if pristw.type == QUIT:
                    exit()

                if pristw.type == KEYDOWN:
                    if pristw.key == K_ESCAPE:
                        self.home()

                self.manager_game.process_events(pristw)

            # Memperbarui posisi ular
            self.ularX += self.ular_Xpos
            self.ularY += self.ular_Ypos

            self.manager_game.update(self.fps)
            self.layar.blit(self.layar_game, (0, 0))
            self.layar_game.blit(
                self.tembok, (((WIN_RES[0]/2)-(GAME_PANEL_SIZE[0]/2))-10, ((WIN_RES[1]-GAME_PANEL_SIZE[1])/2)-10))
            self.layar_game.blit(self.layar_gamePlay,
                                 ((WIN_RES[0]/2)-(GAME_PANEL_SIZE[0]/2), (WIN_RES[1]-GAME_PANEL_SIZE[1])/2))
            self.layar_game.blit(self.layar_gameStat, ((
                (WIN_RES[0]/2)-(GAME_PANEL_SIZE[0]/2))-10, 0))
            self.manager_game.draw_ui(self.layar_game)
            self.Ular(self.ularX, self.ularY)
            time.Clock().tick(DEFAULT_FPS)
            display.update()


if __name__ == '__main__':
    UI().home()
