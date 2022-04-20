# Terakhir Di Edit: Monday, February - 28 - 2022 (28/2/22) [22:57:04,954 PM]  /  GMT+0700 || 9
import time as tm
from random import randint
from sys import exit

import pygame_widgets as pw
from pygame import *

from fig import *

waktu_mulai = tm.time()


# region
# inisialisasi pygame
init()
thp1 = LOKASI_ULAR_TEMA_KE_1
thp2 = LOKASI_ULAR_TEMA_KE_2
thp3 = LOKASI_ULAR_TEMA_KE_3
thp4 = LOKASI_ULAR_TEMA_KE_4
mkn = LOKASI_MAKANAN

# membuat window / layar
imgSize = UKURAN_GAMBAR  # Ukuran gambar (ular, makanan, dll)
celln = BANYAK_KOTAK
layar = display.set_mode(UKURAN_WINDOWS)

# memuat judul dan ikon
display.set_caption(JUDUL_PADA_WINDOWS)
display.set_icon(image.load('./res/ikon/ikon.png'))  # Ikon buat gamenya
# endregion


class GAME:
    def __init__(self):
        # region Menu Utama
        # inisialisasi menu utama
        self.aktif = True
        self.title_font = font.Font(
            LOKASI_FONT_UNTUK_TULISAN / 'StudioGrotesk-Regular.ttf', 70)
        self.btn_font1 = font.Font(None, 40)
        self.wline = 0

        # membuat background
        self.bg1 = Surface(UKURAN_WINDOWS)
        self.bg1_rect = self.bg1.get_rect(topleft=(0, 0))
        self.bg1.fill(bg)

        # membuat judul
        self.judul = self.title_font.render(
            judul, True, warnaTeks)
        self.judul_rect = self.judul.get_rect(center=(UKURAN_WINDOWS[0]/2, 75))

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
                               teks=nama_tombol_main,
                               sudutRad=3,
                               onRelease=self.fbtn_play)

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
                               teks=nama_tombol_pengaturan,
                               sudutRad=3,
                               onRelease=self.btn_pengaturan)

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
                                 teks=nama_tombol_keluar,
                                 sudutRad=3,
                                 onRelease=lambda: exit())
        # endregion

        # endregion

        # region Pengaturan
        # membuat background
        self.bg = Surface(UKURAN_WINDOWS)
        self.bg_rect = self.bg.get_rect(topleft=(0, 0))
        self.bg.fill(bg)

        # top panel
        self.panel_1 = Surface((UKURAN_WINDOWS[0], 100))
        self.panel_1Rect = self.panel_1.get_rect(topleft=(0, 0))
        self.panel_1.fill(pn1)

        # inisialisasi
        self.paktif = True
        self.font_h1 = font.Font(
            LOKASI_FONT_UNTUK_TULISAN/'StudioGrotesk-Regular.ttf', 33)
        self.font_h2 = font.Font(
            LOKASI_FONT_UNTUK_TULISAN/'StudioGrotesk-Regular.ttf', 28)
        self.btn_font = font.Font(None, 25)

        # Tampilan Gambar Gamenya pada setiap tema
        self.tampilan_tema_default = image.load(
            LOKASI_GAMBAR_DAN_LAIN2 / 'ptd.png').convert()
        self.tampilan_tema_1 = image.load(
            LOKASI_GAMBAR_DAN_LAIN2 / 'pt1.png').convert()
        self.tampilan_tema_2 = image.load(
            LOKASI_GAMBAR_DAN_LAIN2 / 'pt2.png').convert()
        self.tampilan_tema_3 = image.load(
            LOKASI_GAMBAR_DAN_LAIN2 / 'pt3.png').convert()

        self.tt_rect = self.tampilan_tema_default.get_rect(
            midtop=(self.panel_1Rect.midbottom[0]+(self.panel_1Rect.midbottom[0]//2)-23,
                    self.panel_1Rect.midbottom[1]+10))

        # membuat tulisan Pengaturan
        self.teksH1 = self.font_h1.render(
            teks_di_pengaturan_h1, True, warnaTeks)
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
                                  nama_tombol_kembali,
                                  warnaAktif=wBA,
                                  warnaHover=wBH,
                                  warnaDitekan=wBP,
                                  warnaTeks=warnaTeks,
                                  shadowDistance=2,
                                  shadowColour=wBSh,
                                  sudutRad=3,
                                  onRelease=self.klikKembali)

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
                                   nama_tombol_default,
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
                                 nama_tema_ke_1,
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
                                 nama_tema_ke_2,
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
                                 nama_tema_ke_3,
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

        # # membuat tulisan
        self.teks1 = self.font_h2.render(
            f'Theme: Default', True, warnaTeks)
        self.teks1_rect = self.teks1.get_rect(bottomleft=(self.btn_kembaliRect.topleft[0],
                                                          self.btn_kembaliRect.topleft[1]-20))
        # endregion

        # region Play
        # inisialisasi si ular dan makanannya
        self.plAktif = True
        self.reset()
        self.go_nskor = 0
        self.go_high_skor = 0
        self.nths = 0
        self.isreset = False

        # suara
        self.suara_makan = mixer.Sound(LOKASI_SUARA / "suara_makan.mp3")
        self.suara_nabrak = mixer.Sound(LOKASI_SUARA / "suara_nabrak.mp3")
        self.suara_latar_belakang = mixer.Sound(LOKASI_SUARA / "bgm.mp3")
        self.suara_latar_belakang.set_volume(0.58)
        self.suara_makan.set_volume(0.7)
        self.suara_nabrak.set_volume(0.7)

        # membuat background
        self.pbg = Surface(UKURAN_WINDOWS)
        self.pbg_rect = self.pbg.get_rect(topleft=(0, 0))
        self.pbg.fill(bg)

        # region Border
        # mwmbuat panel skor
        self.pskor = Surface((UKURAN_WINDOWS[0], imgSize*2))
        self.pskor_rect = self.pskor.get_rect(topleft=(0, 0))
        self.pskor.fill(skp)

        self.border3 = Surface((imgSize*(celln), imgSize))
        self.border3_rect = self.border3.get_rect(
            topleft=self.pskor_rect.bottomleft)
        self.border3.fill(brd)

        self.border0 = Surface((imgSize, imgSize*(celln-2)))
        self.border0_rect = self.border0.get_rect(
            topleft=self.border3_rect.bottomleft)
        self.border0.fill(brd)

        self.border1 = Surface((imgSize*(celln-1), imgSize))
        self.border1_rect = self.border1.get_rect(
            bottomleft=(self.border0_rect.bottomright[0],
                        UKURAN_WINDOWS[1]))
        self.border1.fill(brd)

        self.border2 = Surface((imgSize, imgSize*(celln-1)))
        self.border2_rect = self.border2.get_rect(
            topright=self.border3_rect.topright)
        self.border2.fill(brd)

        self.boardRect = Rect(self.border0_rect.topright,
                              (imgSize*21, imgSize*19))
        # endregion

        # rumput
        self.warnaRumput = tema0['rm']

        # region Tampilan Game Over
        self.plgAktif = True
        self.pngmRect = Rect((0, 0), (350, 400))
        self.pngmRect.center = self.boardRect.center

        # piala
        self.piala = image.load('./res/image/misc/piala.png').convert_alpha()

        # region Tombol
        self.btnHomeRect = Rect((self.pngmRect.midleft[0]+10,
                                 (self.pngmRect.bottomleft[1]-int(self.btnSize[1]/2))-30),
                                (int(self.btnSize[0]/2)+40, int(self.btnSize[1]/2)+20))
        self.btnHome = Tombol(layar,
                              self.btnHomeRect.x,
                              self.btnHomeRect.y,
                              self.btnHomeRect.width,
                              self.btnHomeRect.height,
                              self.btn_font1, 20,
                              nama_tombol_kembali_ke_menu_utama,
                              warnaTeks,
                              wBA, wBH, wBP, 20, 2,
                              onRelease=self.klikHome)

        self.btnResetRect = Rect((self.pngmRect.midright[0]-10-(int(self.btnSize[0]/2)+40),
                                  (self.pngmRect.bottomright[1]-int(self.btnSize[1]/2))-30),
                                 (int(self.btnSize[0]/2)+40, int(self.btnSize[1]/2)+20))
        self.btnReset = Tombol(layar,
                               self.btnResetRect.x,
                               self.btnResetRect.y,
                               self.btnResetRect.width,
                               self.btnResetRect.height,
                               self.btn_font1, 20,
                               nama_tombol_ulang_game,
                               warnaTeks,
                               wBA, wBH, wBP, 20, 2,
                               onRelease=self.klikReset)
        # endregion

        # endregion
        # endregion

        # region Enable & Disable Tombol
        self.btn_defaultT.disable()
        self.btn_defaultT.hide()
        self.btn_kembali.hide()
        self.btn_theme1.hide()
        self.btn_theme2.hide()
        self.btn_theme3.hide()
        self.btnHome.disable()
        self.btnHome.hide()
        self.btnReset.disable()
        self.btnReset.hide()
        # endregion

        # region Ular
        # inisialisasi ular
        self.badan = [Vector2(5, 12), Vector2(
            4, 12), Vector2(3, 12), Vector2(2, 12)]
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

        # region Makanan
        self.acakPos()
        self.index_makanan = 0
        self.fr_makanan = [image.load(mkn/'pete_f0.png').convert_alpha(),
                           image.load(mkn/'pete_f1.png').convert_alpha(),
                           image.load(mkn/'pete_f2.png').convert_alpha(),
                           image.load(mkn/'pete_f2.png').convert_alpha(),
                           image.load(mkn/'pete_f1.png').convert_alpha(),
                           image.load(mkn/'pete_f0.png').convert_alpha()]
        self.makanan = image.load(mkn/'pete.png').convert_alpha()
        # endregion
        pass

    # ! Membuat menu Utama
    # region Menu Utama
    def draw(self):
        layar.blit(self.bg1, self.bg1_rect)
        layar.blit(self.judul, self.judul_rect)
        # mebuat garis bawah pada judul

        if self.wline == 0:
            draw.line(layar, wLine,
                      (self.judul_rect.midleft[0],
                       self.judul_rect.midleft[1]+40),
                      (self.judul_rect.midright[0], self.judul_rect.midright[1]+40), 3)
        elif self.wline == 1:
            draw.line(layar, tema1['wl'],
                      (self.judul_rect.midleft[0],
                       self.judul_rect.midleft[1]+40),
                      (self.judul_rect.midright[0], self.judul_rect.midright[1]+40), 3)
        elif self.wline == 2:
            draw.line(layar, tema2['wl'],
                      (self.judul_rect.midleft[0],
                       self.judul_rect.midleft[1]+40),
                      (self.judul_rect.midright[0], self.judul_rect.midright[1]+40), 3)
        elif self.wline == 3:
            draw.line(layar, tema3['wl'],
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
            fps.tick(FPS)

        pass
    # endregion

    # ! Membuat menu pengaturan
    # region Pengaturan
    def pengDraw(self):
        # gambar tampilan pengaturan
        layar.blit(self.bg, self.bg_rect)
        layar.blit(self.panel_1, self.panel_1Rect)
        layar.blit(self.teksH1, self.teksH1_rect)
        # layar.blit(self.teks1, self.teks1_rect)

        # region Garis dan Tampilan Map
        # hanya ganti warna si garis-garis
        if self.wline == 0:
            # Tampilan Map
            layar.blit(self.tampilan_tema_default, self.tt_rect)

            # garis kotak di pinggir layar
            draw.line(layar, wLine, (0, 0), (UKURAN_WINDOWS[0], 0), 2)
            draw.line(layar, wLine, (0, 0), (0, UKURAN_WINDOWS[1]), 2)
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
                      (UKURAN_WINDOWS[0],
                       self.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      wLine,
                      (0, self.panel_1Rect.midbottom[1]),
                      (UKURAN_WINDOWS[0], self.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      wLine,
                      (self.btn_defaultRect.midtop[0]+30,
                       self.btn_defaultRect.topright[1]-10),
                      (self.btn_defaultRect.midtop[0]+30, self.panel_1Rect.midbottom[1]), 3)

        if self.wline == 1:
            # Tampilan Map
            layar.blit(self.tampilan_tema_1, self.tt_rect)

            # garis kotak di pinggir layar
            draw.line(layar, tema1['wl'], (0, 0), (UKURAN_WINDOWS[0], 0), 2)
            draw.line(layar, tema1['wl'], (0, 0), (0, UKURAN_WINDOWS[1]), 2)
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
                      (UKURAN_WINDOWS[0],
                       self.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      tema1['wl'],
                      (0, self.panel_1Rect.midbottom[1]),
                      (UKURAN_WINDOWS[0], self.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema1['wl'],
                      (self.btn_defaultRect.midtop[0]+30,
                       self.btn_defaultRect.topright[1]-10),
                      (self.btn_defaultRect.midtop[0]+30, self.panel_1Rect.midbottom[1]), 3)

        if self.wline == 2:
            # Tampilan Map
            layar.blit(self.tampilan_tema_2, self.tt_rect)

            # garis kotak di pinggir layar
            draw.line(layar, tema2['wl'], (0, 0), (UKURAN_WINDOWS[0], 0), 2)
            draw.line(layar, tema2['wl'], (0, 0), (0, UKURAN_WINDOWS[1]), 2)
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
                      (UKURAN_WINDOWS[0],
                       self.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      tema2['wl'],
                      (0, self.panel_1Rect.midbottom[1]),
                      (UKURAN_WINDOWS[0], self.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema2['wl'],
                      (self.btn_defaultRect.midtop[0]+30,
                       self.btn_defaultRect.topright[1]-10),
                      (self.btn_defaultRect.midtop[0]+30, self.panel_1Rect.midbottom[1]), 3)

        if self.wline == 3:
            # Tampilan Map
            layar.blit(self.tampilan_tema_3, self.tt_rect)

            # garis kotak di pinggir layar
            draw.line(layar, tema3['wl'], (0, 0), (UKURAN_WINDOWS[0], 0), 2)
            draw.line(layar, tema3['wl'], (0, 0), (0, UKURAN_WINDOWS[1]), 2)
            draw.line(layar,
                      tema3['wl'],
                      (self.bg_rect.bottomleft[0],
                       self.bg_rect.bottomleft[1]-2),
                      (self.bg_rect.bottomright[0],
                       self.bg_rect.bottomright[1]-2),
                      2)
            draw.line(layar,
                      tema3['wl'],
                      (self.bg_rect.bottomright[0]-2,
                       self.bg_rect.bottomright[1]),
                      (self.bg_rect.topright[0]-2, self.bg_rect.topright[1]),
                      2)

            # Garis di antara tombol kembali dan tulisan "Theme:"
            draw.line(layar,
                      tema3['wl'],
                      (0,
                       self.teks1_rect.midbottom[1]+10),
                      (UKURAN_WINDOWS[0],
                       self.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      tema3['wl'],
                      (0, self.panel_1Rect.midbottom[1]),
                      (UKURAN_WINDOWS[0], self.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema3['wl'],
                      (self.btn_defaultRect.midtop[0]+30,
                       self.btn_defaultRect.topright[1]-10),
                      (self.btn_defaultRect.midtop[0]+30, self.panel_1Rect.midbottom[1]), 3)
        # endregion
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
            fps.tick(FPS)

    # endregion

    # ! membuat Game Ularnya
    # region Game

    def drawElem(self):
        layar.blit(self.pbg, self.pbg_rect)
        self.rumput()

        self.gambar_makanan()
        self.gambar_ular()

        layar.blits([(self.pskor, self.pskor_rect),
                     (self.border0, self.border0_rect),
                     (self.border1, self.border1_rect),
                     (self.border2, self.border2_rect),
                     (self.border3, self.border3_rect)])

        self.skor()

    def update(self):
        self.gerakSiular()
        self.cek_tabrakan()
        self.cek_gagal()

    def cek_tabrakan(self):
        if self.fd_pos.distance_to(self.badan[0]) == 0.0:
            self.acakPos()
            self.tambah_blok()
            self.go_nskor += 1
            # print(self.newblok)
            self.suara_makan.play()
            pass

        for blok in self.badan[1:]:
            if blok == self.fd_pos:
                self.acakPos()

    def cek_gagal(self):
        if not 1 <= self.badan[0].x < celln-1 or not 3 <= self.badan[0].y < celln-1:
            self.suara_latar_belakang.stop()
            self.suara_nabrak.play()
            self.gameOver()

        for blok in self.badan[1:]:
            if blok == self.badan[0] and self.arah != Vector2(0, 0):
                self.suara_latar_belakang.stop()
                self.suara_nabrak.play()
                self.gameOver()

        pass

    def drawGameOver(self):
        if self.nths == 0:
            draw.rect(layar, tema0['pn1'], self.pngmRect, 0, 4)
        elif self.nths == 1:
            draw.rect(layar, tema1['pn1'], self.pngmRect, 0, 4)
        elif self.nths == 2:
            draw.rect(layar, tema2['pn1'], self.pngmRect, 0, 4)
        elif self.nths == 3:
            draw.rect(layar, tema3['pn1'], self.pngmRect, 0, 4)
        # membuat tulisan game over
        self.tkgmover = self.font_h1.render('Game Over', True, warnaTeks)
        self.tkgmoverRect = self.tkgmover.get_rect(midtop=(self.pngmRect.midtop[0],
                                                           self.pngmRect.midtop[1]+10))

        self.pngmRect.center = self.boardRect.center

        # region Skor dan HighSkor
        self.display_makanan2x = transform.smoothscale(
            self.makanan, (self.pskor_rect.height-25, self.pskor_rect.height-25))
        self.display_makanan2xRect = self.display_makanan2x.get_rect(
            midleft=(self.pngmRect.midleft[0]+40, int(self.boardRect.midleft[1]-(self.boardRect.midleft[1]*(1/4)))))

        self.teks_skor = self.font_h1.render(f'{self.nskor}', True, warnaTeks)
        self.teks_skorRect = self.teks_skor.get_rect(
            midleft=self.display_makanan2xRect.midright)
        self.teks_skorRect.x += 5
        self.teks_skorRect.y += 2

        # membuat high skor
        if self.go_nskor >= self.go_high_skor:
            self.go_high_skor = self.go_nskor
        teks_hskor = self.font_h1.render(
            f'{self.go_high_skor}', True, warnaTeks)
        teks_hskorRect = teks_hskor.get_rect(
            midleft=(self.pngmRect.midright[0]-80, self.teks_skorRect.midright[1]))

        pialaRect = self.piala.get_rect(
            midright=(teks_hskorRect.midleft[0]-5, teks_hskorRect.midleft[1]))

        # endregion

        layar.blits([(self.tkgmover, self.tkgmoverRect), (self.display_makanan2x, self.display_makanan2xRect),
                     (self.teks_skor, self.teks_skorRect), (teks_hskor, teks_hskorRect), (self.piala, pialaRect)])
        pass

    def gameOver(self):
        # region Disable & Enable Tombol
        self.btnHome.enable()
        self.btnHome.show()
        self.btnReset.enable()
        self.btnReset.show()
        self.btn_play.disable()
        self.btn_keluar.disable()
        self.btn_peng.disable()
        self.btn_play.hide()
        self.btn_keluar.hide()
        self.btn_peng.hide()
        # endregion

        while self.plgAktif:
            ki = event.get()
            for ki in ki:
                if ki.type == QUIT:
                    quit()
                    exit()
                if ki.type == KEYDOWN:
                    if ki.key == K_RETURN:
                        self.klikReset()
                if ki.type == KEYDOWN:
                    if ki.key == K_SPACE:
                        self.klikHome()
            self.drawGameOver()
            pw.update(ki)
            display.update()
            fps.tick(FPS)

    def play(self):
        UPDATE_LAYAR = USEREVENT
        pygame.time.set_timer(UPDATE_LAYAR, KECEPATAN_ULAR_BERGERAK)
        ditekan = False
        while self.plAktif:
            for ki in event.get():
                if ki.type == QUIT:
                    quit()
                    exit()
                if ki.type == UPDATE_LAYAR:
                    self.update()
                    ditekan = True

                if ki.type == KEYDOWN:

                    # Kontrol si ular
                    if ki.key == K_w or ki.key == K_UP:
                        if self.arah.y != 1 and ditekan == True:
                            self.arah = Vector2(0, -1)
                            ditekan = False

                    if ki.key == K_d or ki.key == K_RIGHT:
                        if self.arah.x != -1 and ditekan == True:
                            self.arah = Vector2(1, 0)
                            ditekan = False

                    if ki.key == K_s or ki.key == K_DOWN:
                        if self.arah.y != -1 and ditekan == True:
                            self.arah = Vector2(0, 1)
                            ditekan = False

                    if ki.key == K_a or ki.key == K_LEFT:
                        if self.arah.x != 1 and ditekan == True:
                            self.arah = Vector2(-1, 0)
                            ditekan = False

                pass

            if self.index_makanan >= 5:
                self.index_makanan = 0

            self.drawElem()
            display.update()
            fps.tick(FPS)
            self.index_makanan += 0.1

    def skor(self):
        # membuat tulisan skor
        self.display_makanan2x = transform.smoothscale(
            self.makanan, (self.pskor_rect.height-25, self.pskor_rect.height-25))
        self.display_makanan2xRect = self.display_makanan2x.get_rect(
            midleft=(self.border0_rect.topright[0]+125, self.pskor_rect.midleft[1]))

        self.nskor = int(len(self.badan)-5)
        self.nskor += 1
        self.teks_skor = self.font_h1.render(f'{self.nskor}', True, warnaTeks)
        self.teks_skorRect = self.teks_skor.get_rect(
            midleft=self.display_makanan2xRect.midright)
        self.teks_skorRect.x += 5
        self.teks_skorRect.y += 2

        # membuat piala jika player mengulang game
        dis_piala2x = transform.smoothscale(
            self.piala, (self.pskor_rect.height-25, self.pskor_rect.height-25))
        dis_piala2xRect = dis_piala2x.get_rect(
            midleft=(self.border0_rect.topright[0]+(125*3), self.pskor_rect.midleft[1]))

        layar.blits([(self.teks_skor, self.teks_skorRect),
                    (self.display_makanan2x, self.display_makanan2xRect)])

        if self.go_high_skor != 0:
            if self.nskor >= self.go_high_skor:
                self.go_high_skor = self.nskor

            teks_hskor = self.font_h1.render(
                f'{self.go_high_skor}', True, warnaTeks)
            teks_hskorRect = teks_hskor.get_rect(
                midleft=(dis_piala2xRect.midright[0]+5, dis_piala2xRect.midright[1]+1))

            layar.blit(dis_piala2x, dis_piala2xRect)
            layar.blit(teks_hskor, teks_hskorRect)

        pass

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

    # endregion

    # region Ular
    def gambar_ular(self):
        self.update_hg()
        self.update_eg()

        for i, blok in enumerate(self.badan):
            x_pos = int(blok.x)*imgSize
            y_pos = int(blok.y)*imgSize
            ular_rect = Rect(x_pos, y_pos,
                             imgSize, imgSize)

            if i == 0:  # index ke 0 jadi kepalanya
                layar.blit(self.kepala, ular_rect)
            elif i == len(self.badan)-1:  # index terakhir dari list badan jadi ekornya
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
            if self.arah != Vector2(0, 0):
                badanC = self.badan[:-1]
                badanC.insert(0, badanC[0]+self.arah)
                self.badan = badanC[:]

    def tambah_blok(self):
        self.newblok = True

    def reset(self):
        self.badan = [Vector2(5, 12), Vector2(
            4, 12), Vector2(3, 12), Vector2(2, 12)]
        self.arah = Vector2(0, 0)
        self.fd_pos = Vector2(8, 12)
    # endregion

    # region Makanan
    def acakPos(self):
        self.fd_xPos = randint(1, celln-2)
        self.fd_yPos = randint(3, celln-2)
        self.fd_pos = Vector2(self.fd_xPos, self.fd_yPos)

        pass

    def gambar_makanan(self):
        fdrect = Rect(int(self.fd_pos.x)*imgSize,
                      int(self.fd_pos.y)*imgSize,
                      imgSize, imgSize)

        layar.blit(self.fr_makanan[int(self.index_makanan)], fdrect)
        pass

    # endregion

    # region Fungsi Tombol
    def klikHome(self):
        self.btnHome.disable()
        self.btnHome.hide()
        self.btnReset.disable()
        self.btnReset.hide()
        self.btn_play.enable()
        self.btn_keluar.enable()
        self.btn_peng.enable()
        self.btn_play.show()
        self.btn_keluar.show()
        self.btn_peng.show()
        self.run()

    def klikReset(self):
        self.btnHome.disable()
        self.btnHome.hide()
        self.btnReset.disable()
        self.btnReset.hide()
        self.reset()
        self.go_nskor = 0
        self.suara_latar_belakang.play()
        self.play()

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

    def fbtn_play(self):
        # self.badan = [Vector2(5, 12), Vector2(
        #     4, 12), Vector2(3, 12), Vector2(2, 12)]
        # self.arah = Vector2(0, 0)
        # self.fd_pos = Vector2(8, 12)
        self.reset()
        self.go_nskor = 0
        self.suara_latar_belakang.play(-1)
        self.play()

    def setDefTheme(self):
        global warnaTeks
        self.wline = 0
        self.bg.fill(tema0['bg'])
        self.panel_1.fill(tema0['pn1'])
        warnaTeks = tema0['tk']

        # region Pengaturan
        # self.teks1 = self.font_h2.render('Theme: Default', True, warnaTeks)
        self.teksH1 = self.font_h1.render(
            teks_di_pengaturan_h1, True, warnaTeks)
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

        # region Play
        self.nths = 0
        self.warnaRumput = tema0['rm']
        self.pbg.fill(tema0['bg'])
        self.pskor.fill(tema0['skp'])
        self.border0.fill(tema0['brd'])
        self.border1.fill(tema0['brd'])
        self.border2.fill(tema0['brd'])
        self.border3.fill(tema0['brd'])
        self.btnReset.inactiveColour = tema0['btnA']
        self.btnReset.hoverColour = tema0['btnH']
        self.btnReset.pressedColour = tema0['btnP']
        self.btnHome.inactiveColour = tema0['btnA']
        self.btnHome.hoverColour = tema0['btnH']
        self.btnHome.pressedColour = tema0['btnP']
        # endregion

        # makanan
        self.fr_makanan = [image.load(mkn/'pete_f0.png').convert_alpha(),
                           image.load(mkn/'pete_f1.png').convert_alpha(),
                           image.load(mkn/'pete_f2.png').convert_alpha(),
                           image.load(mkn/'pete_f2.png').convert_alpha(),
                           image.load(mkn/'pete_f1.png').convert_alpha(),
                           image.load(mkn/'pete_f0.png').convert_alpha()]
        self.makanan = image.load(mkn/'pete.png').convert_alpha()

        # region END
        self.btn_defaultT.disable()
        self.btn_theme1.enable()
        self.btn_theme2.enable()
        self.btn_theme3.enable()
        # endregion
        pass

    def setTheme1(self):
        global warnaTeks
        self.wline = 1
        self.bg.fill(tema1['bg'])
        self.panel_1.fill(tema1['pn1'])
        warnaTeks = tema1['tk']

        # region pengaturan
        # self.teks1 = self.font_h2.render('Theme: ', True, warnaTeks)
        self.teksH1 = self.font_h1.render(
            teks_di_pengaturan_h1, True, warnaTeks)
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
        # endregion

        # region menu utama
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
        # endregion

        # region Ular
        self.h_up = image.load(thp2/'kepala_up.png').convert_alpha()
        self.h_down = image.load(thp2/'kepala_down.png').convert_alpha()
        self.h_left = image.load(thp2/'kepala_left.png').convert_alpha()
        self.h_right = image.load(thp2/'kepala_right.png').convert_alpha()

        self.b_tr = image.load(thp2/'badan_tr.png').convert_alpha()
        self.b_tl = image.load(thp2/'badan_tl.png').convert_alpha()
        self.b_bl = image.load(thp2/'badan_bl.png').convert_alpha()
        self.b_br = image.load(thp2/'badan_br.png').convert_alpha()

        self.b_v = image.load(thp2/'badan_v.png').convert_alpha()
        self.b_h = image.load(thp2/'badan_h.png').convert_alpha()

        self.t_up = image.load(thp2/'ekor_up.png').convert_alpha()
        self.t_down = image.load(thp2/'ekor_down.png').convert_alpha()
        self.t_left = image.load(thp2/'ekor_left.png').convert_alpha()
        self.t_right = image.load(thp2/'ekor_right.png').convert_alpha()
        # endregion

        # region Play
        self.nths = 1
        self.warnaRumput = tema1['rm']
        self.pbg.fill(tema1['bg'])
        self.pskor.fill(tema1['skp'])
        self.border0.fill(tema1['brd'])
        self.border1.fill(tema1['brd'])
        self.border2.fill(tema1['brd'])
        self.border3.fill(tema1['brd'])
        self.btnReset.inactiveColour = tema1['btnA']
        self.btnReset.hoverColour = tema1['btnH']
        self.btnReset.pressedColour = tema1['btnP']
        self.btnHome.inactiveColour = tema1['btnA']
        self.btnHome.hoverColour = tema1['btnH']
        self.btnHome.pressedColour = tema1['btnP']
        # endregion

        self.fr_makanan = [image.load(mkn/'nasgor_f0.png').convert_alpha(),
                           image.load(mkn/'nasgor_f1.png').convert_alpha(),
                           image.load(mkn/'nasgor_f2.png').convert_alpha(),
                           image.load(mkn/'nasgor_f2.png').convert_alpha(),
                           image.load(mkn/'nasgor_f1.png').convert_alpha(),
                           image.load(mkn/'nasgor_f0.png').convert_alpha()]
        
        self.makanan = image.load(mkn/'nasgor.png').convert_alpha()

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

        # region pengaturan
        # self.teks1 = self.font_h2.render('Theme: Snowy Time', True, warnaTeks)
        self.teksH1 = self.font_h1.render(
            teks_di_pengaturan_h1, True, warnaTeks)
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
        # endregion

        # region menu utama
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
        # endregion

        # region Ular
        self.h_up = image.load(thp3/'kepala_up.png').convert_alpha()
        self.h_down = image.load(thp3/'kepala_down.png').convert_alpha()
        self.h_left = image.load(thp3/'kepala_left.png').convert_alpha()
        self.h_right = image.load(thp3/'kepala_right.png').convert_alpha()

        self.b_tr = image.load(thp3/'badan_tr.png').convert_alpha()
        self.b_tl = image.load(thp3/'badan_tl.png').convert_alpha()
        self.b_bl = image.load(thp3/'badan_bl.png').convert_alpha()
        self.b_br = image.load(thp3/'badan_br.png').convert_alpha()

        self.b_v = image.load(thp3/'badan_v.png').convert_alpha()
        self.b_h = image.load(thp3/'badan_h.png').convert_alpha()

        self.t_up = image.load(thp3/'ekor_up.png').convert_alpha()
        self.t_down = image.load(thp3/'ekor_down.png').convert_alpha()
        self.t_left = image.load(thp3/'ekor_left.png').convert_alpha()
        self.t_right = image.load(thp3/'ekor_right.png').convert_alpha()
        # endregion

        # region Play
        self.nths = 2
        self.warnaRumput = tema2['rm']
        self.pbg.fill(tema2['bg'])
        self.pskor.fill(tema2['skp'])
        self.border0.fill(tema2['brd'])
        self.border1.fill(tema2['brd'])
        self.border2.fill(tema2['brd'])
        self.border3.fill(tema2['brd'])
        self.btnReset.inactiveColour = tema2['btnA']
        self.btnReset.hoverColour = tema2['btnH']
        self.btnReset.pressedColour = tema2['btnP']
        self.btnHome.inactiveColour = tema2['btnA']
        self.btnHome.hoverColour = tema2['btnH']
        self.btnHome.pressedColour = tema2['btnP']
        # endregion

        self.fr_makanan = [image.load(mkn/'sate_f0.png').convert_alpha(),
                           image.load(mkn/'sate_f1.png').convert_alpha(),
                           image.load(mkn/'sate_f2.png').convert_alpha(),
                           image.load(mkn/'sate_f2.png').convert_alpha(),
                           image.load(mkn/'sate_f1.png').convert_alpha(),
                           image.load(mkn/'sate_f0.png').convert_alpha()]
        
        self.makanan = image.load(mkn/'sate.png').convert_alpha()

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
        self.wline = 3

        # region pengaturan
        # self.teks1 = self.font_h2.render('Theme: Pastel', True, warnaTeks)
        self.teksH1 = self.font_h1.render(
            teks_di_pengaturan_h1, True, warnaTeks)
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
        # endregion

        # region menu utama
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
        # endregion

        # region Ular
        self.h_up = image.load(thp4/'kepala_up.png').convert_alpha()
        self.h_down = image.load(thp4/'kepala_down.png').convert_alpha()
        self.h_left = image.load(thp4/'kepala_left.png').convert_alpha()
        self.h_right = image.load(thp4/'kepala_right.png').convert_alpha()

        self.b_tr = image.load(thp4/'badan_tr.png').convert_alpha()
        self.b_tl = image.load(thp4/'badan_tl.png').convert_alpha()
        self.b_bl = image.load(thp4/'badan_bl.png').convert_alpha()
        self.b_br = image.load(thp4/'badan_br.png').convert_alpha()

        self.b_v = image.load(thp4/'badan_v.png').convert_alpha()
        self.b_h = image.load(thp4/'badan_h.png').convert_alpha()

        self.t_up = image.load(thp4/'ekor_up.png').convert_alpha()
        self.t_down = image.load(thp4/'ekor_down.png').convert_alpha()
        self.t_left = image.load(thp4/'ekor_left.png').convert_alpha()
        self.t_right = image.load(thp4/'ekor_right.png').convert_alpha()
        # endregion

        # region Play
        self.nths = 3
        self.warnaRumput = tema3['rm']
        self.pbg.fill(tema3['bg'])
        self.pskor.fill(tema3['skp'])
        self.border0.fill(tema3['brd'])
        self.border1.fill(tema3['brd'])
        self.border2.fill(tema3['brd'])
        self.border3.fill(tema3['brd'])
        self.btnReset.inactiveColour = tema3['btnA']
        self.btnReset.hoverColour = tema3['btnH']
        self.btnReset.pressedColour = tema3['btnP']
        self.btnHome.inactiveColour = tema3['btnA']
        self.btnHome.hoverColour = tema3['btnH']
        self.btnHome.pressedColour = tema3['btnP']
        # endregion

        self.fr_makanan = [image.load(mkn/'jengkol_f0.png').convert_alpha(),
                           image.load(mkn/'jengkol_f1.png').convert_alpha(),
                           image.load(mkn/'jengkol_f2.png').convert_alpha(),
                           image.load(mkn/'jengkol_f2.png').convert_alpha(),
                           image.load(mkn/'jengkol_f1.png').convert_alpha(),
                           image.load(mkn/'jengkol_f0.png').convert_alpha()]
        
        self.makanan = image.load(mkn/'jengkol.png').convert_alpha()

        self.btn_defaultT.enable()
        self.btn_theme1.enable()
        self.btn_theme2.enable()
        self.btn_theme3.disable()

        pass

    # endregion


if __name__ == "__main__":
    m = GAME()
    from pygame_widgets.progressbar import ProgressBar

    tampilan_loading = ProgressBar(layar, 0, 0,
                                   UKURAN_WINDOWS[0]-200, 80, lambda: 1 - (tm.time() - waktu_mulai) / 10)
    tampilan_loading.incompletedColour = rgb(54, 152, 12)
    tampilan_loading.completedColour = rgb(53, 53, 53)
    tampilan_loading.setX(100)
    tampilan_loading.setY(
        int(UKURAN_WINDOWS[1]/2)-(tampilan_loading.getHeight()/2))

    waktu = 1 - (tm.time() - waktu_mulai) / 10

    fr_teks = [m.font_h1.render('Loading.', True, rgb(199, 199, 199)),
               m.font_h1.render('Loading..', True, rgb(199, 199, 199)),
               m.font_h1.render('Loading...', True, rgb(199, 199, 199))]

    teks_rect = fr_teks[0].get_rect(center=(
        UKURAN_WINDOWS[0]/2, int((UKURAN_WINDOWS[1]/2)-(tampilan_loading.getHeight()/2)-50)))
    index_teks = 0

    m.btn_play.disable()
    m.btn_peng.disable()
    m.btn_keluar.disable()

    while tampilan_loading.percent != 0:
        ki = event.get()
        for ki in ki:
            if ki.type == QUIT:
                quit()
                exit()

        if index_teks >= len(fr_teks):
            index_teks = 0

        teks = fr_teks[int(index_teks)]

        layar.fill(rgb(12, 12, 12))
        layar.blit(teks, teks_rect)
        pw.update(ki)
        display.update()

        index_teks += 0.025

    tampilan_loading.disable()
    tampilan_loading.hide()
    m.btn_play.enable()
    m.btn_peng.enable()
    m.btn_keluar.enable()
    m.run()
