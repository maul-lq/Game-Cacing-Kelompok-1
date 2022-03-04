# Monday, February - 28 - 2022 (28/2/22) [22:57:04,954 PM]  /  GMT+0700 || 9
# TODO: Translate semua isi dari class Pengaturan ke menu utama!
from random import randint
import pygame_widgets as pw

from pygame import *
from sys import exit
from fig import rgb, Tombol, tema1, tema0, tema2, tema3, theme_path_1

# inisialisasi pygame
init()
judul = 'Snake Game'
# frame rate
fps = time.Clock()

thp1 = theme_path_1

wLine = tema0['wl']
bg = tema0['bg']
pn1 = tema0['pn1']
warnaTeks = tema0['tk']
# tombol
wBA = tema0['btnA']
wBH = tema0['btnH']
wBP = tema0['btnP']
wBSh = tema0['btnSh']


# membuat window / layar
imgSize = 30  # Ukuran gambar (ular, makanan, dll)
celln = 23
WIN_SIZE = (imgSize*celln, imgSize*celln)
layar = display.set_mode(WIN_SIZE)

# memuat judul dan ikon
display.set_caption('Game Ular | Kelompok 1')
display.set_icon(image.load('./res/ikon/ikon.png'))


class MAKANAN:
    def __init__(self) -> None:
        self.acakPos()
        self.food = image.load('./res/image/makanan/sate.png')

    def gambar_makanan(self):
        fdRect = Rect(int(self.pos.x)*imgSize,
                      int(self.pos.y)*imgSize,
                      imgSize, imgSize)

        layar.blit(self.food, fdRect)

    def acakPos(self):
        self.x = randint(0, celln-1)
        self.y = randint(0, celln-1)
        self.pos = Vector2(self.x, self.y)

# Membuat layar /  tampilan menu utama


class GAME:
    def __init__(self) -> None:
        # region Menu Utama
        # inisialisasi menu utama
        self.aktif = True
        self.title_font = font.Font(None, 70)
        self.btn_font1 = font.Font(None, 40)
        self.wline = 1

        # membuat background
        self.bg1 = Surface(WIN_SIZE)
        self.bg1_rect = self.bg1.get_rect(topleft=(0, 0))
        self.bg1.fill(bg)

        # membuat judul
        self.judul = self.title_font.render(
            judul, True, warnaTeks)
        self.judul_rect = self.judul.get_rect(center=(WIN_SIZE[0]/2, 75))

        # membuat panel untuk meletakan / memberi posisi tombol
        self.panel_11 = Surface((380, 480))
        self.panel_11Rect = self.panel_11.get_rect(midtop=(self.judul_rect.midbottom[0],
                                                           self.judul_rect.midbottom[1]+100))
        self.panel_11.fill(pn1)

        # region Tombol
        # TODO: Membuat Tombol berfungsi
        # membuat tombol play
        self.btn_playRect = Rect((self.panel_11Rect.topleft[0]+10,
                                  self.panel_11Rect.topleft[1]+10),
                                 (self.panel_11Rect.width, 100))
        self.btn_play = Tombol(self.bg1,
                               self.btn_playRect.x,
                               self.btn_playRect.y,
                               self.btn_playRect.width-20,
                               self.btn_playRect.height,
                               self.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks="Play",
                               sudutRad=3,
                               onClick=self.fbtn_play)

        # membuat tombol pengaturan
        self.btn_pengRect = Rect((self.panel_11Rect.topleft[0]+10,
                                  self.btn_playRect.midbottom[1]+20),
                                 (self.panel_11Rect.width, 100))
        self.btn_peng = Tombol(self.bg1,
                               self.btn_pengRect.x,
                               self.btn_pengRect.y,
                               self.btn_pengRect.width-20,
                               self.btn_pengRect.height,
                               self.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks="Pengaturan",
                               sudutRad=3,
                               onClick=self.btn_pengaturan)

        # membuat tombol keluar
        self.btn_keluarRect = Rect((self.panel_11Rect.topleft[0]+10,
                                    self.btn_pengRect.midbottom[1]+20),
                                   (self.panel_11Rect.width, 100))

        self.btn_keluar = Tombol(self.bg1,
                                 self.btn_keluarRect.x,
                                 self.btn_keluarRect.y,
                                 self.btn_pengRect.width-20,
                                 self.btn_pengRect.height,
                                 self.btn_font1,
                                 warnaTeks=warnaTeks,
                                 warnaAktif=wBA,
                                 warnaDitekan=wBP,
                                 warnaHover=wBH,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 teks='Keluar',
                                 sudutRad=3,
                                 onClick=lambda: exit())
        # endregion

        # endregion

        # region Pengaturan
        # membuat background
        self.bg = Surface(WIN_SIZE)
        self.bg_rect = self.bg.get_rect(topleft=(0, 0))
        self.bg.fill(bg)

        # top panel
        self.panel_1 = Surface((WIN_SIZE[0], 100))
        self.panel_1Rect = self.panel_1.get_rect(topleft=(0, 0))
        self.panel_1.fill(pn1)

        # inisialisasi
        self.paktif = True
        self.font_h1 = font.Font(None, 50)
        self.font_h2 = font.Font(None, 35)
        self.btn_font = font.Font(None, 25)

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
                                  warnaAktif=wBA,
                                  warnaHover=wBH,
                                  warnaDitekan=wBP,
                                  warnaTeks=warnaTeks,
                                  shadowDistance=2,
                                  shadowColour=wBSh,
                                  sudutRad=3,
                                  onClick=self.klikKembali)

        # membuat tombol tema bawaan
        self.btn_defaultRect = Rect((self.btn_kembaliRect.topright[0]+20,
                                     self.btn_kembaliRect.topright[1]),
                                    self.btnSize)
        self.btn_defaultT = Tombol(self.bg,
                                   self.btn_defaultRect.x,
                                   self.btn_defaultRect.y,
                                   self.btn_defaultRect.width,
                                   self.btn_defaultRect.height,
                                   self.btn_font, 20,
                                   'Default Theme',
                                   warnaAktif=wBA,
                                   warnaHover=wBH,
                                   warnaDitekan=wBP,
                                   warnaTeks=warnaTeks,
                                   shadowDistance=2,
                                   shadowColour=wBSh,
                                   sudutRad=3,
                                   onClick=self.setDefTheme)

        # region Tombol Theme
        self.btnSize = (180, 100)
        # Tema ke 1
        self.btn_theme1Rect = Rect((self.panel_1Rect.bottomleft[0]+20,
                                    self.panel_1Rect.bottomleft[1]+25,),
                                   self.btnSize)
        self.btn_theme1 = Tombol(self.bg,
                                 self.btn_theme1Rect.x,
                                 self.btn_theme1Rect.y,
                                 self.btn_theme1Rect.width,
                                 self.btn_theme1Rect.height,
                                 self.btn_font, 50,
                                 'Theme 1',
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=self.setTheme1)

        # Tema ke 2
        self.btn_theme2Rect = Rect((self.btn_theme1Rect.bottomleft[0],
                                    self.btn_theme1Rect.bottomleft[1]+50),
                                   self.btnSize)
        self.btn_theme2 = Tombol(self.bg,
                                 self.btn_theme2Rect.x,
                                 self.btn_theme2Rect.y,
                                 self.btn_theme2Rect.width,
                                 self.btn_theme2Rect.height,
                                 self.btn_font, 50,
                                 "Theme 2",
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=self.setTheme2)
        # Tema ke 3
        self.btn_theme3Rect = Rect((self.btn_theme2Rect.bottomleft[0],
                                    self.btn_theme2Rect.bottomleft[1]+50,),
                                   self.btnSize)
        self.btn_theme3 = Tombol(self.bg,
                                 self.btn_theme3Rect.x,
                                 self.btn_theme3Rect.y,
                                 self.btn_theme3Rect.width,
                                 self.btn_theme3Rect.height,
                                 self.btn_font, 50,
                                 'Theme 3',
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=self.setTheme3)

        # endregion
        # endregion

        # membuat tulisan
        self.teks1 = self.font_h2.render(
            f'Theme: Default', True, warnaTeks)
        self.teks1_rect = self.teks1.get_rect(bottomleft=(self.btn_kembaliRect.topleft[0],
                                                          self.btn_kembaliRect.topleft[1]-20))
        # endregion

        # region Play
        # inisialisasi si ular dan makanannya
        self.makanan = MAKANAN()
        self.plAktif = True

        # membuat background
        self.pbg = Surface(WIN_SIZE)
        self.pbg_rect = self.pbg.get_rect(topleft=(0, 0))
        self.pbg.fill(bg)

        # rumput
        self.warnaRumput = rgb(175, 199, 72)
        # endregion

        self.btn_defaultT.disable()
        self.btn_defaultT.hide()
        self.btn_kembali.hide()
        self.btn_theme1.hide()
        self.btn_theme2.hide()
        self.btn_theme3.hide()

        # region Ular
        # inisialisasi ular
        self.badan = [Vector2(5, 10), Vector2(
            4, 10), Vector2(3, 10)]
        self.arah = Vector2(0, 0)
        self.newblok = False

        self.h_up = image.load(thp1/'kepala_up.png').convert_alpha()
        self.h_down = image.load(thp1/'kepala_down.png').convert_alpha()
        self.h_left = image.load(thp1/'kepala_left.png').convert_alpha()
        self.h_right = image.load(thp1/'kepala_right.png').convert_alpha()

        self.b_tr = image.load(thp1/'badan_tr.png').convert_alpha()
        self.b_tl = image.load(thp1/'badan_tl.png').convert_alpha()
        self.b_bl = image.load(thp1/'badan_bl.png').convert_alpha()
        self.b_br = image.load(thp1/'badan_br.png').convert_alpha()

        self.b_v = image.load(thp1/'badan_v.png').convert_alpha()
        self.b_h = image.load(thp1/'badan_h.png').convert_alpha()

        self.t_up = image.load(thp1/'ekor_up.png').convert_alpha()
        self.t_down = image.load(thp1/'ekor_down.png').convert_alpha()
        self.t_left = image.load(thp1/'ekor_left.png').convert_alpha()
        self.t_right = image.load(thp1/'ekor_right.png').convert_alpha()
        # endregion
        pass

    def btn_pengaturan(self):
        self.btn_defaultT.show()
        self.btn_kembali.show()
        self.btn_theme1.show()
        self.btn_theme2.show()
        self.btn_theme3.show()

        self.btn_keluar.hide()
        self.btn_play.hide()
        self.btn_peng.hide()

        self.pengaturan()

    def fbtn_play(self):
        self.badan = [Vector2(5, 10), Vector2(
            4, 10), Vector2(3, 10)]
        self.arah = Vector2(0, 0)
        self.play()

    def draw(self):
        layar.blit(self.bg1, self.bg1_rect)
        layar.blit(self.judul, self.judul_rect)
        # mebuat garis bawah pada judul
        draw.line(layar, wLine,
                  (self.judul_rect.midleft[0],
                   self.judul_rect.midleft[1]+40),
                  (self.judul_rect.midright[0], self.judul_rect.midright[1]+40), 3)

        # layar.blit(self.panel_1, self.panel_11Rect)

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

    # ! Membuat menu pengaturan
    def pengDraw(self):
        # gambar tampilan pengaturan
        layar.blit(self.bg, self.bg_rect)
        layar.blit(self.panel_1, self.panel_1Rect)
        layar.blit(self.teksH1, self.teksH1_rect)
        layar.blit(self.teks1, self.teks1_rect)

        if self.wline == 0:
            # garis kotak di pinggir layar
            draw.line(layar, wLine, (0, 0), (WIN_SIZE[0], 0), 2)
            draw.line(layar, wLine, (0, 0), (0, WIN_SIZE[1]), 2)
            draw.line(layar,
                      wLine,
                      (self.bg_rect.bottomleft[0],
                       self.bg_rect.bottomleft[1]-2),
                      (self.bg_rect.bottomright[0],
                       self.bg_rect.bottomright[1]-2),
                      2)
            draw.line(layar,
                      wLine,
                      (self.bg_rect.bottomright[0]-2,
                       self.bg_rect.bottomright[1]),
                      (self.bg_rect.topright[0]-2, self.bg_rect.topright[1]),
                      2)

            # Garis di antara tombol kembali dan tulisan "Theme:"
            draw.line(layar,
                      wLine,
                      (0,
                       self.teks1_rect.midbottom[1]+10),
                      (WIN_SIZE[0],
                       self.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      wLine,
                      (0, self.panel_1Rect.midbottom[1]),
                      (WIN_SIZE[0], self.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      wLine,
                      (self.btn_defaultRect.midtop[0]+30,
                       self.btn_defaultRect.topright[1]-10),
                      (self.btn_defaultRect.midtop[0]+30, self.panel_1Rect.midbottom[1]), 3)

        if self.wline == 1:
            # garis kotak di pinggir layar
            draw.line(layar, tema1['wl'], (0, 0), (WIN_SIZE[0], 0), 2)
            draw.line(layar, tema1['wl'], (0, 0), (0, WIN_SIZE[1]), 2)
            draw.line(layar,
                      tema1['wl'],
                      (self.bg_rect.bottomleft[0],
                       self.bg_rect.bottomleft[1]-2),
                      (self.bg_rect.bottomright[0],
                       self.bg_rect.bottomright[1]-2),
                      2)
            draw.line(layar,
                      tema1['wl'],
                      (self.bg_rect.bottomright[0]-2,
                       self.bg_rect.bottomright[1]),
                      (self.bg_rect.topright[0]-2, self.bg_rect.topright[1]),
                      2)

            # Garis di antara tombol kembali dan tulisan "Theme:"
            draw.line(layar,
                      tema1['wl'],
                      (0,
                       self.teks1_rect.midbottom[1]+10),
                      (WIN_SIZE[0],
                       self.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      tema1['wl'],
                      (0, self.panel_1Rect.midbottom[1]),
                      (WIN_SIZE[0], self.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema1['wl'],
                      (self.btn_defaultRect.midtop[0]+30,
                       self.btn_defaultRect.topright[1]-10),
                      (self.btn_defaultRect.midtop[0]+30, self.panel_1Rect.midbottom[1]), 3)

        if self.wline == 2:
            # garis kotak di pinggir layar
            draw.line(layar, tema2['wl'], (0, 0), (WIN_SIZE[0], 0), 2)
            draw.line(layar, tema2['wl'], (0, 0), (0, WIN_SIZE[1]), 2)
            draw.line(layar,
                      tema2['wl'],
                      (self.bg_rect.bottomleft[0],
                       self.bg_rect.bottomleft[1]-2),
                      (self.bg_rect.bottomright[0],
                       self.bg_rect.bottomright[1]-2),
                      2)
            draw.line(layar,
                      tema2['wl'],
                      (self.bg_rect.bottomright[0]-2,
                       self.bg_rect.bottomright[1]),
                      (self.bg_rect.topright[0]-2, self.bg_rect.topright[1]),
                      2)

            # Garis di antara tombol kembali dan tulisan "Theme:"
            draw.line(layar,
                      tema2['wl'],
                      (0,
                       self.teks1_rect.midbottom[1]+10),
                      (WIN_SIZE[0],
                       self.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      tema2['wl'],
                      (0, self.panel_1Rect.midbottom[1]),
                      (WIN_SIZE[0], self.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema2['wl'],
                      (self.btn_defaultRect.midtop[0]+30,
                       self.btn_defaultRect.topright[1]-10),
                      (self.btn_defaultRect.midtop[0]+30, self.panel_1Rect.midbottom[1]), 3)
        pass

    def pengaturan(self):
        while self.paktif:
            ki = event.get()
            for ki in ki:
                if ki.type == QUIT:
                    quit()
                    exit()

            self.pengDraw()

            pw.update(ki)
            display.update()
            fps.tick(60)

    def klikKembali(self):
        self.btn_kembali.hide()
        self.btn_defaultT.hide()
        self.btn_theme1.hide()
        self.btn_theme2.hide()
        self.btn_theme3.hide()

        self.btn_keluar.show()
        self.btn_play.show()
        self.btn_peng.show()
        self.run()

    def setDefTheme(self):
        global warnaTeks
        self.wline = 0
        self.bg.fill(tema0['bg'])
        self.panel_1.fill(tema0['pn1'])
        warnaTeks = tema0['tk']

        # region Pengaturan
        self.teks1 = self.font_h2.render('Theme: Default', True, warnaTeks)
        self.teksH1 = self.font_h1.render(
            'Pengaturan | Theme Game Ular', True, warnaTeks)
        self.btn_kembali.inactiveColour = tema0['btnA']
        self.btn_kembali.hoverColour = tema0['btnH']
        self.btn_kembali.pressedColour = tema0['btnP']
        self.btn_kembali.textColour = warnaTeks
        self.btn_defaultT.inactiveColour = tema0['btnA']
        self.btn_defaultT.hoverColour = tema0['btnH']
        self.btn_defaultT.pressedColour = tema0['btnP']
        self.btn_defaultT.textColour = warnaTeks
        self.btn_theme1.inactiveColour = tema0['btnA']
        self.btn_theme1.hoverColour = tema0['btnH']
        self.btn_theme1.pressedColour = tema0['btnP']
        self.btn_theme1.textColour = warnaTeks
        self.btn_theme2.inactiveColour = tema0['btnA']
        self.btn_theme2.hoverColour = tema0['btnH']
        self.btn_theme2.pressedColour = tema0['btnP']
        self.btn_theme2.textColour = warnaTeks
        self.btn_theme3.inactiveColour = tema0['btnA']
        self.btn_theme3.hoverColour = tema0['btnH']
        self.btn_theme3.pressedColour = tema0['btnP']
        self.btn_theme3.textColour = warnaTeks
        # endregion

        # region Menu Utama
        self.bg1.fill(tema0['bg'])
        self.btn_play.inactiveColour = tema0['btnA']
        self.btn_play.hoverColour = tema0['btnH']
        self.btn_play.pressedColour = tema0['btnP']
        self.btn_play.textColour = warnaTeks
        self.btn_keluar.inactiveColour = tema0['btnA']
        self.btn_keluar.hoverColour = tema0['btnH']
        self.btn_keluar.pressedColour = tema0['btnP']
        self.btn_keluar.textColour = warnaTeks
        self.btn_peng.inactiveColour = tema0['btnA']
        self.btn_peng.hoverColour = tema0['btnH']
        self.btn_peng.pressedColour = tema0['btnP']
        self.btn_peng.textColour = warnaTeks
        self.btn_keluar.inactiveColour = tema0['btnA']
        self.btn_keluar.hoverColour = tema0['btnH']
        self.btn_keluar.pressedColour = tema0['btnP']
        self.btn_keluar.textColour = warnaTeks
        self.judul = self.title_font.render(
            judul, True, warnaTeks)
        # endregion

        # region Ular
        self.h_up = image.load(thp1/'kepala_up.png').convert_alpha()
        self.h_down = image.load(thp1/'kepala_down.png').convert_alpha()
        self.h_left = image.load(thp1/'kepala_left.png').convert_alpha()
        self.h_right = image.load(thp1/'kepala_right.png').convert_alpha()

        self.b_tr = image.load(thp1/'badan_tr.png').convert_alpha()
        self.b_tl = image.load(thp1/'badan_tl.png').convert_alpha()
        self.b_bl = image.load(thp1/'badan_bl.png').convert_alpha()
        self.b_br = image.load(thp1/'badan_br.png').convert_alpha()

        self.b_v = image.load(thp1/'badan_v.png').convert_alpha()
        self.b_h = image.load(thp1/'badan_h.png').convert_alpha()

        self.t_up = image.load(thp1/'ekor_up.png').convert_alpha()
        self.t_down = image.load(thp1/'ekor_down.png').convert_alpha()
        self.t_left = image.load(thp1/'ekor_left.png').convert_alpha()
        self.t_right = image.load(thp1/'ekor_right.png').convert_alpha()
        # endregion

        # region END
        self.btn_defaultT.disable()
        self.btn_theme1.enable()
        self.btn_theme2.enable()
        self.btn_theme3.enable()
        # region
        pass

    def setTheme1(self):
        global warnaTeks
        self.wline = 1
        self.bg.fill(tema1['bg'])
        self.panel_1.fill(tema1['pn1'])
        warnaTeks = tema1['tk']

        self.teks1 = self.font_h2.render('Theme: Red Brick', True, warnaTeks)
        self.teksH1 = self.font_h1.render(
            'Pengaturan | Theme Game Ular', True, warnaTeks)
        self.btn_kembali.inactiveColour = tema1['btnA']
        self.btn_kembali.hoverColour = tema1['btnH']
        self.btn_kembali.pressedColour = tema1['btnP']
        self.btn_kembali.textColour = warnaTeks
        self.btn_defaultT.inactiveColour = tema1['btnA']
        self.btn_defaultT.hoverColour = tema1['btnH']
        self.btn_defaultT.pressedColour = tema1['btnP']
        self.btn_defaultT.textColour = warnaTeks
        self.btn_theme1.inactiveColour = tema1['btnA']
        self.btn_theme1.hoverColour = tema1['btnH']
        self.btn_theme1.pressedColour = tema1['btnP']
        self.btn_theme1.textColour = warnaTeks
        self.btn_theme2.inactiveColour = tema1['btnA']
        self.btn_theme2.hoverColour = tema1['btnH']
        self.btn_theme2.pressedColour = tema1['btnP']
        self.btn_theme2.textColour = warnaTeks
        self.btn_theme3.inactiveColour = tema1['btnA']
        self.btn_theme3.hoverColour = tema1['btnH']
        self.btn_theme3.pressedColour = tema1['btnP']
        self.btn_theme3.textColour = warnaTeks

        self.bg1.fill(tema1['bg'])
        self.btn_play.inactiveColour = tema1['btnA']
        self.btn_play.hoverColour = tema1['btnH']
        self.btn_play.pressedColour = tema1['btnP']
        self.btn_play.textColour = warnaTeks
        self.btn_keluar.inactiveColour = tema1['btnA']
        self.btn_keluar.hoverColour = tema1['btnH']
        self.btn_keluar.pressedColour = tema1['btnP']
        self.btn_keluar.textColour = warnaTeks
        self.btn_peng.inactiveColour = tema1['btnA']
        self.btn_peng.hoverColour = tema1['btnH']
        self.btn_peng.pressedColour = tema1['btnP']
        self.btn_peng.textColour = warnaTeks
        self.btn_keluar.inactiveColour = tema1['btnA']
        self.btn_keluar.hoverColour = tema1['btnH']
        self.btn_keluar.pressedColour = tema1['btnP']
        self.btn_keluar.textColour = warnaTeks
        self.judul = self.title_font.render(
            judul, True, warnaTeks)

        self.btn_defaultT.enable()
        self.btn_theme1.disable()
        self.btn_theme2.enable()
        self.btn_theme3.enable()
        pass

    def setTheme2(self):
        global warnaTeks
        self.bg.fill(tema2['bg'])
        self.panel_1.fill(tema2['pn1'])
        warnaTeks = tema2['tk']
        self.wline = 2

        self.teks1 = self.font_h2.render('Theme: Snowy Time', True, warnaTeks)
        self.teksH1 = self.font_h1.render(
            'Pengaturan | Theme Game Ular', True, warnaTeks)
        self.btn_kembali.inactiveColour = tema2['btnA']
        self.btn_kembali.hoverColour = tema2['btnH']
        self.btn_kembali.pressedColour = tema2['btnP']
        self.btn_kembali.textColour = warnaTeks
        self.btn_defaultT.inactiveColour = tema2['btnA']
        self.btn_defaultT.hoverColour = tema2['btnH']
        self.btn_defaultT.pressedColour = tema2['btnP']
        self.btn_defaultT.textColour = warnaTeks
        self.btn_theme1.inactiveColour = tema2['btnA']
        self.btn_theme1.hoverColour = tema2['btnH']
        self.btn_theme1.pressedColour = tema2['btnP']
        self.btn_theme1.textColour = warnaTeks
        self.btn_theme2.inactiveColour = tema2['btnA']
        self.btn_theme2.hoverColour = tema2['btnH']
        self.btn_theme2.pressedColour = tema2['btnP']
        self.btn_theme2.textColour = warnaTeks
        self.btn_theme3.inactiveColour = tema2['btnA']
        self.btn_theme3.hoverColour = tema2['btnH']
        self.btn_theme3.pressedColour = tema2['btnP']
        self.btn_theme3.textColour = warnaTeks

        self.bg1.fill(tema2['bg'])
        self.btn_play.inactiveColour = tema2['btnA']
        self.btn_play.hoverColour = tema2['btnH']
        self.btn_play.pressedColour = tema2['btnP']
        self.btn_play.textColour = warnaTeks
        self.btn_keluar.inactiveColour = tema2['btnA']
        self.btn_keluar.hoverColour = tema2['btnH']
        self.btn_keluar.pressedColour = tema2['btnP']
        self.btn_keluar.textColour = warnaTeks
        self.btn_peng.inactiveColour = tema2['btnA']
        self.btn_peng.hoverColour = tema2['btnH']
        self.btn_peng.pressedColour = tema2['btnP']
        self.btn_peng.textColour = warnaTeks
        self.btn_keluar.inactiveColour = tema2['btnA']
        self.btn_keluar.hoverColour = tema2['btnH']
        self.btn_keluar.pressedColour = tema2['btnP']
        self.btn_keluar.textColour = warnaTeks
        self.judul_rect = self.judul_rect
        self.judul = self.title_font.render(
            judul, True, warnaTeks)

        self.btn_defaultT.enable()
        self.btn_theme1.enable()
        self.btn_theme2.disable()
        self.btn_theme3.enable()
        pass

    def setTheme3(self):
        global warnaTeks
        self.bg.fill(tema3['bg'])
        self.panel_1.fill(tema3['pn1'])
        warnaTeks = tema3['tk']

        self.teks1 = self.font_h2.render('Theme: Pastel', True, warnaTeks)
        self.teksH1 = self.font_h1.render(
            'Pengaturan | Theme Game Ular', True, warnaTeks)
        self.btn_kembali.inactiveColour = tema3['btnA']
        self.btn_kembali.hoverColour = tema3['btnH']
        self.btn_kembali.pressedColour = tema3['btnP']
        self.btn_kembali.textColour = warnaTeks
        self.btn_defaultT.inactiveColour = tema3['btnA']
        self.btn_defaultT.hoverColour = tema3['btnH']
        self.btn_defaultT.pressedColour = tema3['btnP']
        self.btn_defaultT.textColour = warnaTeks
        self.btn_theme1.inactiveColour = tema3['btnA']
        self.btn_theme1.hoverColour = tema3['btnH']
        self.btn_theme1.pressedColour = tema3['btnP']
        self.btn_theme1.textColour = warnaTeks
        self.btn_theme2.inactiveColour = tema3['btnA']
        self.btn_theme2.hoverColour = tema3['btnH']
        self.btn_theme2.pressedColour = tema3['btnP']
        self.btn_theme2.textColour = warnaTeks
        self.btn_theme3.inactiveColour = tema3['btnA']
        self.btn_theme3.hoverColour = tema3['btnH']
        self.btn_theme3.pressedColour = tema3['btnP']
        self.btn_theme3.textColour = warnaTeks

        self.bg1.fill(tema3['bg'])
        self.btn_play.inactiveColour = tema3['btnA']
        self.btn_play.hoverColour = tema3['btnH']
        self.btn_play.pressedColour = tema3['btnP']
        self.btn_play.textColour = warnaTeks
        self.btn_keluar.inactiveColour = tema3['btnA']
        self.btn_keluar.hoverColour = tema3['btnH']
        self.btn_keluar.pressedColour = tema3['btnP']
        self.btn_keluar.textColour = warnaTeks
        self.btn_peng.inactiveColour = tema3['btnA']
        self.btn_peng.hoverColour = tema3['btnH']
        self.btn_peng.pressedColour = tema3['btnP']
        self.btn_peng.textColour = warnaTeks
        self.btn_keluar.inactiveColour = tema3['btnA']
        self.btn_keluar.hoverColour = tema3['btnH']
        self.btn_keluar.pressedColour = tema3['btnP']
        self.btn_keluar.textColour = warnaTeks
        self.judul_rect = self.judul_rect
        self.judul = self.title_font.render(
            judul, True, warnaTeks)

        self.btn_defaultT.enable()
        self.btn_theme1.enable()
        self.btn_theme2.enable()
        self.btn_theme3.disable()

        pass

    def drawElem(self):
        layar.blit(self.pbg, self.pbg_rect)
        self.rumput()

        self.makanan.gambar_makanan()
        self.gambar_ular()

    def update(self):
        self.gerakSiular()
        self.cek_tabrakan()
        self.cek_gagal()

    def cek_tabrakan(self):
        if self.makanan.pos == self.badan[0]:
            self.makanan.acakPos()
            self.tambah_blok()
            print(self.newblok)
            pass

        for blok in self.badan[1:]:
            if blok == self.makanan.pos:
                self.makanan.acakPos()

    def cek_gagal(self):
        if not 0 <= self.badan[0].x < celln or not 0 <= self.badan[0].y < celln:
            self.gameOver()

        for blok in self.badan[1:]:
            if blok == self.badan[0]:
                self.gameOver()

        pass

    def gameOver(self):
        self.reset()

    def play(self):
        UPDATE_LAYAR = USEREVENT
        time.set_timer(UPDATE_LAYAR, 150)
        while self.plAktif:
            for ki in event.get():
                if ki.type == QUIT:
                    quit()
                    exit()
                if ki.type == UPDATE_LAYAR:
                    self.update()
                if ki.type == KEYDOWN:
                    if ki.key == K_ESCAPE:
                        self.run()

                    # Kontrol si ular
                    if ki.key == K_UP:
                        if self.arah.y != 1:
                            self.arah = Vector2(0, -1)

                    if ki.key == K_RIGHT:
                        if self.arah.x != -1:
                            self.arah = Vector2(1, 0)

                    if ki.key == K_DOWN:
                        if self.arah.y != -1:
                            self.arah = Vector2(0, 1)

                    if ki.key == K_LEFT:
                        if self.arah.x != 1:
                            self.arah = Vector2(-1, 0)

                pass

            self.drawElem()
            display.update()
            fps.tick(60)

    def rumput(self):
        for i in range(celln):
            if i % 2 == 0:
                for j in range(celln):
                    if j % 2 == 0:
                        rumputRect = Rect(j*imgSize, i*imgSize,
                                          imgSize, imgSize)
                        draw.rect(layar, self.warnaRumput, rumputRect)
            else:
                for j in range(celln):
                    if j % 2 != 0:
                        rumputRect = Rect(j*imgSize, i*imgSize,
                                          imgSize, imgSize)
                        draw.rect(layar, self.warnaRumput, rumputRect)
                pass
        pass

    # region Ular
    def gambar_ular(self):
        self.update_hg()
        self.update_eg()

        for i, blok in enumerate(self.badan):
            x_pos = int(blok.x)*imgSize
            y_pos = int(blok.y)*imgSize
            ular_rect = Rect(x_pos, y_pos,
                             imgSize, imgSize)

            if i == 0:
                layar.blit(self.kepala, ular_rect)
            elif i == len(self.badan)-1:
                layar.blit(self.ekor, ular_rect)
            else:
                blok_sebelum = self.badan[i+1]-blok
                blok_selanjutnya = self.badan[i-1]-blok

                if blok_sebelum.x == blok_selanjutnya.x:
                    layar.blit(self.b_v, ular_rect)
                elif blok_sebelum.y == blok_selanjutnya.y:
                    layar.blit(self.b_h, ular_rect)
                else:
                    if blok_sebelum.x == -1 and blok_selanjutnya.y == -1 \
                            or blok_sebelum.y == -1 and blok_selanjutnya.x == -1:
                        layar.blit(self.b_tl, ular_rect)
                    if blok_sebelum.x == -1 and blok_selanjutnya.y == 1 \
                            or blok_sebelum.y == 1 and blok_selanjutnya.x == -1:
                        layar.blit(self.b_bl, ular_rect)
                    if blok_sebelum.x == 1 and blok_selanjutnya.y == -1 \
                            or blok_sebelum.y == -1 and blok_selanjutnya.x == 1:
                        layar.blit(self.b_tr, ular_rect)
                    if blok_sebelum.x == 1 and blok_selanjutnya.y == 1 \
                            or blok_sebelum.y == 1 and blok_selanjutnya.x == 1:
                        layar.blit(self.b_br, ular_rect)

        pass

    def update_hg(self):
        # baagian kepla
        rKepala = self.badan[1]-self.badan[0]
        if rKepala == Vector2(1, 0):
            self.kepala = self.h_left
        elif rKepala == Vector2(-1, 0):
            self.kepala = self.h_right
        elif rKepala == Vector2(0, 1):
            self.kepala = self.h_down
        elif rKepala == Vector2(0, -1):
            self.kepala = self.h_up

    def update_eg(self):
        # baagian kepla
        rEkor = self.badan[-2]-self.badan[-1]
        if rEkor == Vector2(1, 0):
            self.ekor = self.t_left
        elif rEkor == Vector2(-1, 0):
            self.ekor = self.t_right
        elif rEkor == Vector2(0, 1):
            self.ekor = self.t_down
        elif rEkor == Vector2(0, -1):
            self.ekor = self.t_up

    def gerakSiular(self):
        if self.newblok == True:
            # copy badan
            badanC = self.badan[:]
            badanC.insert(0, badanC[0]+self.arah)
            self.badan = badanC[:]
            self.newblok = False
        else:
            badanC = self.badan[:-1]
            badanC.insert(0, badanC[0]+self.arah)
            self.badan = badanC[:]

    def tambah_blok(self):
        self.newblok = True

    def reset(self):
        self.badan = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.arah = Vector2(0, 0)
    # endregion


if __name__ == "__main__":
    m = GAME()
    m.run()
