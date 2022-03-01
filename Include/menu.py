# Monday, February - 28 - 2022 (28/2/22) [22:57:04,954 PM]  /  GMT+0700 || 9
# TODO: Membuat tampilan Pengaturan
import pygame_widgets as pw

from pygame import *
from pygame_widgets.dropdown import Dropdown
from sys import exit
from fig import rgb, Tombol

# inisialisasi pygame
init()
# frame rate
fps = time.Clock()
warnaTeks = rgb(225, 225, 225)

tema1 = {
    'bg': rgb(255, 170, 94),
    'pn1': rgb(208, 129, 89),
    'tk': 'rgb(13, 43, 69)'
}

# membuat window / layar
imgSize = 30  # Ukuran gambar (ular, makanan, dll)
cellSize = 23
WIN_SIZE = (imgSize*cellSize, imgSize*cellSize)
layar = display.set_mode(WIN_SIZE)

# memuat judul dan ikon
display.set_caption('Game Ular Redux | Kelompok 1')
display.set_icon(image.load('./res/ikon/ikon.png'))


# Membuat layar /  tampilan menu utama
class MENU_UTAMA:
    def __init__(self) -> None:
        # inisialisasi menu utama
        self.aktif = True
        self.title_font = font.Font(None, 70)
        self.btn_font = font.Font(None, 40)

        # membuat background
        self.bg = Surface(WIN_SIZE)
        self.bg_rect = self.bg.get_rect(topleft=(0, 0))
        self.bg.fill(rgb(81, 82, 98))

        # membuat judul
        self.judul = self.title_font.render(
            'Ular Game Redux', True, rgb(84, 51, 68))
        self.judul_rect = self.judul.get_rect(center=(WIN_SIZE[0]/2, 75))

        # membuat panel untuk meletakan / memberi posisi tombol
        self.panel_1 = Surface((380, 480))
        self.panel_1Rect = self.panel_1.get_rect(midtop=(self.judul_rect.midbottom[0],
                                                         self.judul_rect.midbottom[1]+100))
        self.panel_1.fill(rgb(48, 93, 66))

        # region Tombol
        # TODO: Membuat Tombol berfungsi
        # membuat tombol play
        self.btn_playRect = Rect((self.panel_1Rect.topleft[0]+10,
                                  self.panel_1Rect.topleft[1]+10),
                                 (self.panel_1Rect.width, 100))
        self.btn_play = Tombol(self.bg,
                               self.btn_playRect.x,
                               self.btn_playRect.y,
                               self.btn_playRect.width-20,
                               self.btn_playRect.height,
                               self.btn_font,
                               teks="Play",
                               sudutRad=3,
                               onClick=lambda: print(True))

        # membuat tombol pengaturan
        self.btn_pengRect = Rect((self.panel_1Rect.topleft[0]+10,
                                  self.btn_playRect.midbottom[1]+20),
                                 (self.panel_1Rect.width, 100))
        self.btn_peng = Tombol(self.bg,
                               self.btn_pengRect.x,
                               self.btn_pengRect.y,
                               self.btn_pengRect.width-20,
                               self.btn_pengRect.height,
                               self.btn_font,
                               teks="Pengaturan",
                               sudutRad=3,
                               onClick=self.btn_pengaturan)

        # membuat tombol keluar
        self.btn_keluarRect = Rect((self.panel_1Rect.topleft[0]+10,
                                    self.btn_pengRect.midbottom[1]+20),
                                   (self.panel_1Rect.width, 100))

        self.btn_keluar = Tombol(self.bg,
                                 self.btn_keluarRect.x,
                                 self.btn_keluarRect.y,
                                 self.btn_pengRect.width-20,
                                 self.btn_pengRect.height,
                                 self.btn_font,
                                 teks='Keluar',
                                 sudutRad=3,
                                 onClick=lambda: exit())
        # endregion

        pass

    def btn_pengaturan(self):
        return MENU_PENGATURAN().run()

    def draw(self):
        layar.blit(self.bg, self.bg_rect)
        layar.blit(self.judul, self.judul_rect)
        # mebuat garis bawah pada judul
        draw.line(layar, rgb(238, 255, 204),
                  (self.judul_rect.midleft[0], self.judul_rect.midleft[1]+40),
                  (self.judul_rect.midright[0], self.judul_rect.midright[1]+40), 3)

        # layar.blit(self.panel_1, self.panel_1Rect)

        pass

    def run(self):
        while self.aktif:
            ki = event.get()
            for ki in ki:
                if ki.type == QUIT:
                    quit()
                    exit()

            self.draw()

            pw.update(ki)
            display.update()
            fps.tick(60)

        pass


# membuat layar / tampilan menu pengaturan
class MENU_PENGATURAN:
    def __init__(self) -> None:
        # inisialisasi
        self.aktif = True
        self.font_h1 = font.Font(None, 50)
        self.font_h2 = font.Font(None, 35)
        self.btn_font = font.Font(None, 25)

        # membuat background
        self.bg = Surface(WIN_SIZE)
        self.bg_rect = self.bg.get_rect(topleft=(0, 0))
        self.bg.fill((0, 0, 0))

        # top panel
        self.panel_1 = Surface((WIN_SIZE[0], 100))
        self.panel_1Rect = self.panel_1.get_rect(topleft=(0, 0))
        self.panel_1.fill(rgb(208, 129, 89))

        # membuat tulisan Pengaturan
        self.teksH1 = self.font_h1.render(
            'Pengaturan | Theme Game Ular', True, warnaTeks)
        self.teksH1_rect = self.teksH1.get_rect(midleft=(self.panel_1Rect.midleft[0]+20,
                                                         self.panel_1Rect.midleft[1]))

        # region Tombol
        # membuat tombol kembali
        self.btnSize = (150, 75)
        self.btn_kembaliRect = Rect((self.bg_rect.bottomleft[0]+20,
                                     (self.bg_rect.bottomleft[1]-self.btnSize[1])-20),
                                    self.btnSize)
        self.btn_kembali = Tombol(self.bg,
                                  self.btn_kembaliRect.x,
                                  self.btn_kembaliRect.y,
                                  self.btn_kembaliRect.width,
                                  self.btn_kembaliRect.height,
                                  self.btn_font,
                                  20,
                                  'Kembali',
                                  sudutRad=3,
                                  onClick=self.klikKembali)

        # region Tombol Theme
        self.btnSize = (140, 80)
        # Tema ke 1
        self.btn_theme1Rect = Rect((self.panel_1Rect.bottomleft[0]+20,
                                    self.panel_1Rect.bottomleft[1]+20,),
                                   self.btnSize)
        self.btn_theme1 = Tombol(self.bg,
                                 self.btn_theme1Rect.x,
                                 self.btn_theme1Rect.y,
                                 self.btn_theme1Rect.width,
                                 self.btn_theme1Rect.height,
                                 self.btn_font, 20,
                                 'Theme 1',
                                 sudutRad=3,
                                 onClick=self.setTheme1)

        # Tema ke 2
        self.btn_theme2Rect = Rect((self.btn_theme1Rect.bottomleft[0],
                                    self.btn_theme1Rect.bottomleft[1]+20),
                                   self.btnSize)
        self.btn_theme2 = Tombol(self.bg,
                                 self.btn_theme2Rect.x,
                                 self.btn_theme2Rect.y,
                                 self.btn_theme2Rect.width,
                                 self.btn_theme2Rect.height,
                                 self.btn_font, 20,
                                 "Theme 2",
                                 sudutRad=3)
        # Tema ke 3
        self.btn_theme3Rect = Rect((self.btn_theme2Rect.bottomleft[0],
                                    self.btn_theme2Rect.bottomleft[1]+20,),
                                   self.btnSize)
        self.btn_theme3 = Tombol(self.bg,
                                 self.btn_theme3Rect.x,
                                 self.btn_theme3Rect.y,
                                 self.btn_theme3Rect.width,
                                 self.btn_theme3Rect.height,
                                 self.btn_font, 20,
                                 'Theme 3',
                                 sudutRad=3)

        # Tema ke 4
        self.btn_theme4Rect = Rect((self.btn_theme3Rect.bottomleft[0],
                                    self.btn_theme3Rect.bottomleft[1]+20),
                                   self.btnSize)
        self.btn_theme4 = Tombol(self.bg,
                                 self.btn_theme4Rect.x,
                                 self.btn_theme4Rect.y,
                                 self.btn_theme4Rect.width,
                                 self.btn_theme4Rect.height,
                                 self.btn_font, 20,
                                 "Theme 4",
                                 sudutRad=3)
        # endregion
        # endregion

        # membuat tulisan
        self.teks1 = self.font_h2.render(
            f'Theme: {tkTheme}', True, warnaTeks)
        self.teks1_rect = self.teks1.get_rect(bottomleft=(self.btn_kembaliRect.topleft[0],
                                                          self.btn_kembaliRect.topleft[1]-20))

        pass

    def klikKembali(self):
        return MENU_UTAMA().run()

    def setTheme1(self):
        global warnaTeks
        self.bg.fill(tema1['bg'])
        self.panel_1.fill(tema1['pn1'])
        warnaTeks = tema1['tk']
        pass

    def draw(self):
        layar.blit(self.bg, self.bg_rect)
        layar.blit(self.panel_1, self.panel_1Rect)
        layar.blit(self.teksH1, self.teksH1_rect)
        layar.blit(self.teks1, self.teks1_rect)

    def run(self):
        while self.aktif:
            ki = event.get()
            for ki in ki:
                if ki.type == QUIT:
                    quit()
                    exit()

            self.draw()

            pw.update(ki)
            display.update()
            fps.tick(60)


if __name__ == "__main__":
    tkTheme = 'Default'
    m = MENU_UTAMA()
    m.run()
