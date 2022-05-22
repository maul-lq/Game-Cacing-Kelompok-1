# /-------------/
# / Game Cacing /
# / Kelompok 1  /
# /-------------/

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
display.set_icon(image.load('./res/ikon/ikon.png', 'Ikon')
                 )  # Ikon buat gamenya
# endregion


class Makanan:
    def __init__(makanan) -> None:
        makanan.acakPos()
        makanan.index_makanan = 0
        makanan.fr_makanan = [image.load(mkn/'pete_f0.png').convert_alpha(),
                           image.load(mkn/'pete_f1.png').convert_alpha(),
                           image.load(mkn/'pete_f2.png').convert_alpha(),
                           image.load(mkn/'pete_f2.png').convert_alpha(),
                           image.load(mkn/'pete_f1.png').convert_alpha(),
                           image.load(mkn/'pete_f0.png').convert_alpha()]
        makanan.fr_makanan0 = [image.load(mkn/'pete_f0.png').convert_alpha(),
                            image.load(mkn/'pete_f1.png').convert_alpha(),
                            image.load(mkn/'pete_f2.png').convert_alpha(),
                            image.load(mkn/'pete_f2.png').convert_alpha(),
                            image.load(mkn/'pete_f1.png').convert_alpha(),
                            image.load(mkn/'pete_f0.png').convert_alpha()]
        makanan.fr_makanan1 = [image.load(mkn/'jengkol_f0.png').convert_alpha(),
                            image.load(mkn/'jengkol_f1.png').convert_alpha(),
                            image.load(mkn/'jengkol_f2.png').convert_alpha(),
                            image.load(mkn/'jengkol_f2.png').convert_alpha(),
                            image.load(mkn/'jengkol_f1.png').convert_alpha(),
                            image.load(mkn/'jengkol_f0.png').convert_alpha()]
        makanan.fr_makanan2 = [image.load(mkn/'nasgor_f0.png').convert_alpha(),
                            image.load(mkn/'nasgor_f1.png').convert_alpha(),
                            image.load(mkn/'nasgor_f2.png').convert_alpha(),
                            image.load(mkn/'nasgor_f2.png').convert_alpha(),
                            image.load(mkn/'nasgor_f1.png').convert_alpha(),
                            image.load(mkn/'nasgor_f0.png').convert_alpha()]
        makanan.fr_makanan3 = [image.load(mkn/'sate_f0.png').convert_alpha(),
                            image.load(mkn/'sate_f1.png').convert_alpha(),
                            image.load(mkn/'sate_f2.png').convert_alpha(),
                            image.load(mkn/'sate_f2.png').convert_alpha(),
                            image.load(mkn/'sate_f1.png').convert_alpha(),
                            image.load(mkn/'sate_f0.png').convert_alpha()]
        makanan.makanan = image.load(mkn/'pete.png').convert_alpha()

        makanan.display_makananAktif = 0
        pass

    def acakPos(makanan):
        makanan.fd_xPos = randint(1, celln-2)
        makanan.fd_yPos = randint(3, celln-2)
        makanan.fd_pos = Vector2(makanan.fd_xPos, makanan.fd_yPos)

        pass

    def gambar_makanan(makanan, display=False):
        if not display:
            fdrect = Rect(int(makanan.fd_pos.x)*imgSize,
                          int(makanan.fd_pos.y)*imgSize,
                          imgSize, imgSize)

            layar.blit(makanan.fr_makanan[int(makanan.index_makanan)], fdrect)
        else:
            if makanan.display_makananAktif == 0:
                layar.blits([(makanan.fr_makanan0[int(makanan.index_makanan)], Rect((17*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan1[2], Rect(
                                 (18*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan2[2], Rect(
                                 (19*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan3[2], Rect((20*imgSize, 17*imgSize), (imgSize, imgSize)))])
            if makanan.display_makananAktif == 1:
                layar.blits([(makanan.fr_makanan0[2], Rect((17*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan1[2], Rect(
                                 (18*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan2[int(makanan.index_makanan)], Rect(
                                 (19*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan3[2], Rect((20*imgSize, 17*imgSize), (imgSize, imgSize)))])
            if makanan.display_makananAktif == 2:
                layar.blits([(makanan.fr_makanan0[2], Rect((17*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan1[2], Rect(
                                 (18*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan2[2], Rect(
                                 (19*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan3[int(makanan.index_makanan)], Rect((20*imgSize, 17*imgSize), (imgSize, imgSize)))])
            if makanan.display_makananAktif == 3:
                layar.blits([(makanan.fr_makanan0[2], Rect((17*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan1[int(makanan.index_makanan)], Rect(
                                 (18*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan2[2], Rect(
                                 (19*imgSize, 17*imgSize), (imgSize, imgSize))),
                             (makanan.fr_makanan3[2], Rect((20*imgSize, 17*imgSize), (imgSize, imgSize)))])
        pass


class Cacing(Makanan):
    def __init__(cacing) -> None:
        super().__init__()
        cacing.badan = [Vector2(5, 12), Vector2(
            4, 12), Vector2(3, 12), Vector2(2, 12)]
        cacing.arah = Vector2(0, 0)
        cacing.newblok = False

        cacing.h_up = image.load(thp1/'kepala_up.png').convert_alpha()
        cacing.h_down = image.load(thp1/'kepala_down.png').convert_alpha()
        cacing.h_left = image.load(thp1/'kepala_left.png').convert_alpha()
        cacing.h_right = image.load(thp1/'kepala_right.png').convert_alpha()

        cacing.b_tr = image.load(thp1/'badan_tr.png').convert_alpha()
        cacing.b_tl = image.load(thp1/'badan_tl.png').convert_alpha()
        cacing.b_bl = image.load(thp1/'badan_bl.png').convert_alpha()
        cacing.b_br = image.load(thp1/'badan_br.png').convert_alpha()

        cacing.b_v = image.load(thp1/'badan_v.png').convert_alpha()
        cacing.b_h = image.load(thp1/'badan_h.png').convert_alpha()

        cacing.t_up = image.load(thp1/'ekor_up.png').convert_alpha()
        cacing.t_down = image.load(thp1/'ekor_down.png').convert_alpha()
        cacing.t_left = image.load(thp1/'ekor_left.png').convert_alpha()
        cacing.t_right = image.load(thp1/'ekor_right.png').convert_alpha()

        pass

    def gambar_ular(cacing):
        cacing.update_hg()
        cacing.update_eg()

        for index, blok in enumerate(cacing.badan):
            x_pos = int(blok.x)*imgSize
            y_pos = int(blok.y)*imgSize
            ular_rect = Rect(x_pos, y_pos,
                             imgSize, imgSize)

            if index == 0:  # index ke 0 jadi kepalanya
                layar.blit(cacing.kepala, ular_rect)
            # index terakhir dari list badan jadi ekornya
            elif index == len(cacing.badan)-1:
                layar.blit(cacing.ekor, ular_rect)
            else:
                blok_sebelum = cacing.badan[index+1]-blok
                blok_selanjutnya = cacing.badan[index-1]-blok

                if blok_sebelum.x == blok_selanjutnya.x:
                    layar.blit(cacing.b_v, ular_rect)
                elif blok_sebelum.y == blok_selanjutnya.y:
                    layar.blit(cacing.b_h, ular_rect)
                else:
                    if blok_sebelum.x == -1 and blok_selanjutnya.y == -1 \
                            or blok_sebelum.y == -1 and blok_selanjutnya.x == -1:
                        # badan belok ke kiri dari atas.
                        layar.blit(cacing.b_tl, ular_rect)
                    if blok_sebelum.x == 1 and blok_selanjutnya.y == -1 \
                            or blok_sebelum.y == -1 and blok_selanjutnya.x == 1:
                        # badan belok ke kanan dari atas.
                        layar.blit(cacing.b_tr, ular_rect)
                    if blok_sebelum.x == -1 and blok_selanjutnya.y == 1 \
                            or blok_sebelum.y == 1 and blok_selanjutnya.x == -1:
                        # badan belok ke kiri dari bawah.
                        layar.blit(cacing.b_bl, ular_rect)
                    if blok_sebelum.x == 1 and blok_selanjutnya.y == 1 \
                            or blok_sebelum.y == 1 and blok_selanjutnya.x == 1:
                        # badan belok ke kanan dari bawah
                        layar.blit(cacing.b_br, ular_rect)

        pass

    def update_hg(cacing):
        # baagian kepla
        rKepala = cacing.badan[1]-cacing.badan[0]
        if rKepala == Vector2(1, 0):
            cacing.kepala = cacing.h_left
        elif rKepala == Vector2(-1, 0):
            cacing.kepala = cacing.h_right
        elif rKepala == Vector2(0, 1):
            cacing.kepala = cacing.h_down
        elif rKepala == Vector2(0, -1):
            cacing.kepala = cacing.h_up

    def update_eg(cacing):
        # baagian kepla
        rEkor = cacing.badan[-2]-cacing.badan[-1]
        if rEkor == Vector2(1, 0):
            cacing.ekor = cacing.t_left
        elif rEkor == Vector2(-1, 0):
            cacing.ekor = cacing.t_right
        elif rEkor == Vector2(0, 1):
            cacing.ekor = cacing.t_down
        elif rEkor == Vector2(0, -1):
            cacing.ekor = cacing.t_up

    def gerakSiular(cacing):
        if cacing.newblok == True:
            # copy badan
            badanC = cacing.badan[:]
            badanC.insert(0, badanC[0]+cacing.arah)
            cacing.badan = badanC[:]
            cacing.newblok = False
        else:
            if cacing.arah != Vector2(0, 0):
                badanC = cacing.badan[:-1]
                badanC.insert(0, badanC[0]+cacing.arah)
                cacing.badan = badanC[:]

    def tambah_blok(cacing):
        cacing.newblok = True

    def reset(cacing):
        cacing.badan = [Vector2(5, 12), Vector2(
            4, 12), Vector2(3, 12), Vector2(2, 12)]
        cacing.arah = Vector2(0, 0)
        cacing.fd_pos = Vector2(8, 12)

    def len(cacing):
        return len(cacing.badan)


class GAME(Cacing):
    def __init__(game) -> None:
        super().__init__()
        # region Menu Utama
        # inisialisasi menu utama
        game.aktif = True
        game.title_font = font.Font(
            LOKASI_FONT_UNTUK_TULISAN / 'StudioGrotesk-Regular.ttf', 70)
        game.btn_font1 = font.Font(None, 40)
        game.wline = 0

        game.makanan_ke1 = game.fr_makanan0
        game.makanan_ke2 = game.fr_makanan0
        game.makanan_ke3 = game.fr_makanan0

        game.def_fdPos1 = Vector2(20, 13)
        game.def_fdPos2 = Vector2(11, 20)
        game.def_fdPos3 = Vector2(2, 13)
        game.fd_pos1 = game.def_fdPos1
        game.fd_pos2 = game.def_fdPos2
        game.fd_pos3 = game.def_fdPos3

        # membuat background
        game.bg1 = Surface(UKURAN_WINDOWS)
        game.bg1_rect = game.bg1.get_rect(topleft=(0, 0))
        game.bg1.fill(bg)

        # membuat judul
        game.judul = game.title_font.render(
            judul, True, warnaTeks)
        game.judul_rect = game.judul.get_rect(center=(UKURAN_WINDOWS[0]/2, 75))

        # membuat panel untuk meletakan / memberi posisi tombol
        game.panel_11 = Surface((380, 480))
        game.panel_11Rect = game.panel_11.get_rect(midtop=(game.judul_rect.midbottom[0],
                                                           game.judul_rect.midbottom[1]+100))
        game.panel_11.fill(pn1)

        # region Tombol
        # TODO: Membuat Tombol berfungsi
        # membuat tombol play
        game.btn_playRect = Rect((game.panel_11Rect.topleft[0]+10,
                                  game.panel_11Rect.topleft[1]+10),
                                 (game.panel_11Rect.width, 100))
        game.btn_play = Tombol(layar,
                               game.btn_playRect.x,
                               game.btn_playRect.y,
                               game.btn_playRect.width-20,
                               game.btn_playRect.height,
                               game.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks=nama_tombol_main,
                               sudutRad=3,
                               onRelease=game.fbtn_play)

        # membuat tombol pengaturan
        game.btn_pengRect = Rect((game.panel_11Rect.topleft[0]+10,
                                  game.btn_playRect.midbottom[1]+20),
                                 (game.panel_11Rect.width, 100))
        game.btn_peng = Tombol(layar,
                               game.btn_pengRect.x,
                               game.btn_pengRect.y,
                               game.btn_pengRect.width-20,
                               game.btn_pengRect.height,
                               game.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks=nama_tombol_pengaturan,
                               sudutRad=3,
                               onRelease=game.btn_pengaturan)

        # membuat tombol keluar
        game.btn_keluarRect = Rect((game.panel_11Rect.topleft[0]+10,
                                    game.btn_pengRect.midbottom[1]+20),
                                   (game.panel_11Rect.width, 100))

        game.btn_keluar = Tombol(layar,
                                 game.btn_keluarRect.x,
                                 game.btn_keluarRect.y,
                                 game.btn_pengRect.width-20,
                                 game.btn_pengRect.height,
                                 game.btn_font1,
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
        game.bg = Surface(UKURAN_WINDOWS)
        game.bg_rect = game.bg.get_rect(topleft=(0, 0))
        game.bg.fill(bg)

        # top panel
        game.panel_1 = Surface((UKURAN_WINDOWS[0], 100))
        game.panel_1Rect = game.panel_1.get_rect(topleft=(0, 0))
        game.panel_1.fill(pn1)

        # inisialisasi
        game.paktif = True
        game.font_h1 = font.Font(
            LOKASI_FONT_UNTUK_TULISAN/'StudioGrotesk-Regular.ttf', 33)
        game.font_h2 = font.Font(
            LOKASI_FONT_UNTUK_TULISAN/'StudioGrotesk-Regular.ttf', 25)
        game.btn_font = font.Font(None, 25)

        # Tampilan Gambar Gamenya pada setiap tema
        game.tampilan_tema_default = image.load(
            LOKASI_GAMBAR_DAN_LAIN2 / 'ptd.png').convert()
        game.tampilan_tema_1 = image.load(
            LOKASI_GAMBAR_DAN_LAIN2 / 'pt1.png').convert()
        game.tampilan_tema_2 = image.load(
            LOKASI_GAMBAR_DAN_LAIN2 / 'pt2.png').convert()
        game.tampilan_tema_3 = image.load(
            LOKASI_GAMBAR_DAN_LAIN2 / 'pt3.png').convert()

        game.tt_rect = game.tampilan_tema_default.get_rect(
            midtop=(game.panel_1Rect.midbottom[0]+(game.panel_1Rect.midbottom[0]//2)-23,
                    game.panel_1Rect.midbottom[1]+30))

        # membuat tulisan Pengaturan
        game.teksH1 = game.font_h1.render(
            teks_di_pengaturan_h1, True, warnaTeks)
        game.teksH1_rect = game.teksH1.get_rect(midleft=(game.panel_1Rect.midleft[0]+20,
                                                         game.panel_1Rect.midleft[1]))
        game.teksh2 = game.font_h2.render(
            teks_di_pengaturan_h2, True, warnaTeks)
        game.teksh2_rect = game.teksh2.get_rect(topleft=(12*30+35, 0))
        game.teksh2_rect.y = 540-game.teksh2_rect.height-33

        # region Tombol
        # membuat tombol kembali
        game.btnSize = (150, 75)
        game.btn_kembaliRect = Rect((game.bg_rect.bottomleft[0]+20,
                                     (game.bg_rect.bottomleft[1]-game.btnSize[1])-20),
                                    game.btnSize)
        game.btn_kembali = Tombol(game.bg,
                                  game.btn_kembaliRect.x,
                                  game.btn_kembaliRect.y,
                                  game.btn_kembaliRect.width,
                                  game.btn_kembaliRect.height,
                                  game.btn_font,
                                  20,
                                  nama_tombol_kembali,
                                  warnaAktif=wBA,
                                  warnaHover=wBH,
                                  warnaDitekan=wBP,
                                  warnaTeks=warnaTeks,
                                  shadowDistance=2,
                                  shadowColour=wBSh,
                                  sudutRad=3,
                                  onRelease=game.klikKembali)

        # membuat tombol tema bawaan
        game.btn_defaultRect = Rect((game.btn_kembaliRect.topright[0]+20,
                                     game.btn_kembaliRect.topright[1]),
                                    game.btnSize)
        game.btn_defaultT = Tombol(game.bg,
                                   game.btn_defaultRect.x,
                                   game.btn_defaultRect.y,
                                   game.btn_defaultRect.width,
                                   game.btn_defaultRect.height,
                                   game.btn_font, 20,
                                   nama_tombol_default,
                                   warnaAktif=wBA,
                                   warnaHover=wBH,
                                   warnaDitekan=wBP,
                                   warnaTeks=warnaTeks,
                                   shadowDistance=2,
                                   shadowColour=wBSh,
                                   sudutRad=3,
                                   onClick=game.setDefTheme)

        game.btn_soundRect = Rect((game.btn_defaultRect.topright[0]+20,
                                   game.btn_defaultRect.topright[1]),
                                  game.btnSize)

        game.btn_sound = Tombol(game.bg,
                                game.btn_soundRect.x,
                                game.btn_soundRect.y,
                                game.btn_soundRect.width,
                                game.btn_soundRect.height,
                                game.btn_font, 20,
                                nama_tombol_suara_ON,
                                warnaAktif=wBA,
                                warnaHover=wBH,
                                warnaDitekan=wBP,
                                warnaTeks=warnaTeks,
                                shadowDistance=2,
                                shadowColour=wBSh,
                                sudutRad=3,
                                onRelease=game.klik_SoundbtnON)

        # region Tombol Theme
        game.btnSize = (180, 100)
        # Tema ke 1
        game.btn_theme1Rect = Rect((game.panel_1Rect.bottomleft[0]+20,
                                    game.panel_1Rect.bottomleft[1]+25,),
                                   game.btnSize)
        game.btn_theme1 = Tombol(game.bg,
                                 game.btn_theme1Rect.x,
                                 game.btn_theme1Rect.y,
                                 game.btn_theme1Rect.width,
                                 game.btn_theme1Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_1,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme1)

        # Tema ke 2
        game.btn_theme2Rect = Rect((game.btn_theme1Rect.bottomleft[0],
                                    game.btn_theme1Rect.bottomleft[1]+50),
                                   game.btnSize)
        game.btn_theme2 = Tombol(game.bg,
                                 game.btn_theme2Rect.x,
                                 game.btn_theme2Rect.y,
                                 game.btn_theme2Rect.width,
                                 game.btn_theme2Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_2,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme2)
        # Tema ke 3
        game.btn_theme3Rect = Rect((game.btn_theme2Rect.bottomleft[0],
                                    game.btn_theme2Rect.bottomleft[1]+50,),
                                   game.btnSize)
        game.btn_theme3 = Tombol(game.bg,
                                 game.btn_theme3Rect.x,
                                 game.btn_theme3Rect.y,
                                 game.btn_theme3Rect.width,
                                 game.btn_theme3Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_3,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme3)

        # endregion
        # endregion

        # # membuat tulisan
        # ! TIDAK DIGUNAKAN....
        game.teks1 = game.font_h2.render(
            f'Theme: Default', True, warnaTeks)
        game.teks1_rect = game.teks1.get_rect(bottomleft=(game.btn_kembaliRect.topleft[0],
                                                          game.btn_kembaliRect.topleft[1]-20))
        # endregion

        # region Play
        # membuat si ular, suara, makanannya, dll.
        game.plAktif = True
        game.reset()
        game.go_nskor = 0
        game.go_high_skor = 0
        game.nths = 0
        game.isreset = False
        game.apakahGameOver = False
        game.btn_soundState = 'ON'

        # suara
        game.suara_makan = mixer.Sound(LOKASI_SUARA / "suara_makan.mp3")
        game.suara_nabrak = mixer.Sound(LOKASI_SUARA / "suara_nabrak.mp3")
        game.suara_latar_belakang = mixer.Sound(LOKASI_SUARA / "bgm.mp3")
        game.suara_latar_belakang.set_volume(0.58)
        game.suara_makan.set_volume(0.7)
        game.suara_nabrak.set_volume(0.7)

        # membuat background
        game.pbg = Surface(UKURAN_WINDOWS)
        game.pbg_rect = game.pbg.get_rect(topleft=(0, 0))
        game.pbg.fill(bg)

        # region Border
        # mwmbuat panel skor
        game.pskor = Surface((UKURAN_WINDOWS[0], imgSize*2))
        game.pskor_rect = game.pskor.get_rect(topleft=(0, 0))
        game.pskor.fill(skp)

        game.border3 = Surface((imgSize*(celln), imgSize))
        game.border3_rect = game.border3.get_rect(
            topleft=game.pskor_rect.bottomleft)
        game.border3.fill(brd)

        game.border0 = Surface((imgSize, imgSize*(celln-2)))
        game.border0_rect = game.border0.get_rect(
            topleft=game.border3_rect.bottomleft)
        game.border0.fill(brd)

        game.border1 = Surface((imgSize*(celln-1), imgSize))
        game.border1_rect = game.border1.get_rect(
            bottomleft=(game.border0_rect.bottomright[0],
                        UKURAN_WINDOWS[1]))
        game.border1.fill(brd)

        game.border2 = Surface((imgSize, imgSize*(celln-1)))
        game.border2_rect = game.border2.get_rect(
            topright=game.border3_rect.topright)
        game.border2.fill(brd)

        game.boardRect = Rect(game.border0_rect.topright,
                              (imgSize*21, imgSize*19))
        # endregion

        # rumput
        game.warnaRumput = tema0['rm']

        # region Tampilan Game Over
        game.plgAktif = True
        game.pngmRect = Rect((0, 0), (350, 400))
        game.pngmRect.center = game.boardRect.center

        # piala
        game.piala = image.load('./res/image/misc/piala.png').convert_alpha()

        # region Tombol
        game.btnHomeRect = Rect((game.pngmRect.midleft[0]+10,
                                 (game.pngmRect.bottomleft[1]-int(game.btnSize[1]/2))-30),
                                (int(game.btnSize[0]/2)+40, int(game.btnSize[1]/2)+20))
        game.btnHome = Tombol(layar,
                              game.btnHomeRect.x,
                              game.btnHomeRect.y,
                              game.btnHomeRect.width,
                              game.btnHomeRect.height,
                              game.btn_font1, 20,
                              nama_tombol_kembali_ke_menu_utama,
                              warnaTeks,
                              wBA, wBH, wBP, 20, 2,
                              onRelease=game.klikHome)

        game.btnResetRect = Rect((game.pngmRect.midright[0]-10-(int(game.btnSize[0]/2)+40),
                                  (game.pngmRect.bottomright[1]-int(game.btnSize[1]/2))-30),
                                 (int(game.btnSize[0]/2)+40, int(game.btnSize[1]/2)+20))
        game.btnReset = Tombol(layar,
                               game.btnResetRect.x,
                               game.btnResetRect.y,
                               game.btnResetRect.width,
                               game.btnResetRect.height,
                               game.btn_font1, 20,
                               nama_tombol_ulang_game,
                               warnaTeks,
                               wBA, wBH, wBP, 20, 2,
                               onRelease=game.klikReset)
        # endregion

        # endregion
        # endregion

        # region Enable & Disable Tombol
        # PENTING!
        # Jika ada tombol baru disembunyikan!
        # game.btn_defaultT.disable()
        game.btn_defaultT.hide()
        game.btn_kembali.hide()
        game.btn_theme1.hide()
        game.btn_theme2.hide()
        game.btn_theme3.hide()
        # game.btnHome.disable()
        game.btnHome.hide()
        # game.btnReset.disable()
        game.btnReset.hide()
        # game.btn_sound.disable()
        game.btn_sound.hide()
        # endregion

        pass

    # ! Membuat menu Utama
    # region Menu Utama

    # gambar makanan pada menu utama!
    def gambar_makanan_MU(game):
        """Gambar makanan pada menu utama."""
        if game.wline == 0:
            game.makanan_ke1 = game.fr_makanan0
            game.makanan_ke2 = game.fr_makanan0
            game.makanan_ke3 = game.fr_makanan0
        elif game.wline == 1:
            game.makanan_ke1 = game.fr_makanan1
            game.makanan_ke2 = game.fr_makanan1
            game.makanan_ke3 = game.fr_makanan1
        elif game.wline == 2:
            game.makanan_ke1 = game.fr_makanan2
            game.makanan_ke2 = game.fr_makanan2
            game.makanan_ke3 = game.fr_makanan2
        elif game.wline == 3:
            game.makanan_ke1 = game.fr_makanan3
            game.makanan_ke2 = game.fr_makanan3
            game.makanan_ke3 = game.fr_makanan3

        # posisi ke tiga makanan pada menu utama!
        fdrect1 = Rect(
            (game.fd_pos1.x*imgSize, game.fd_pos1.y*imgSize), (imgSize, imgSize))
        fdrect2 = Rect(
            (game.fd_pos2.x*imgSize, game.fd_pos2.y*imgSize), (imgSize, imgSize))
        fdrect3 = Rect(
            (game.fd_pos3.x*imgSize, game.fd_pos3.y*imgSize), (imgSize, imgSize))

        layar.blit(game.makanan_ke1[int(game.index_makanan)], fdrect1)
        layar.blit(game.makanan_ke2[int(game.index_makanan)], fdrect2)
        layar.blit(game.makanan_ke3[int(game.index_makanan)], fdrect3)

        pass

    def gambar(game):
        """Gambar si ular dan makanannya"""
        game.gambar_makanan_MU()
        game.gambar_ular()
        pass

    def draw(game):
        layar.blit(game.bg1, game.bg1_rect)
        game.rumput()

        game.gambar()

        layar.blit(game.judul, game.judul_rect)
        # mebuat garis bawah pada judul

        if game.wline == 0:
            draw.line(layar, wLine,
                      (game.judul_rect.midleft[0],
                       game.judul_rect.midleft[1]+40),
                      (game.judul_rect.midright[0], game.judul_rect.midright[1]+40), 3)
        elif game.wline == 1:
            draw.line(layar, tema1['wl'],
                      (game.judul_rect.midleft[0],
                       game.judul_rect.midleft[1]+40),
                      (game.judul_rect.midright[0], game.judul_rect.midright[1]+40), 3)
        elif game.wline == 2:
            draw.line(layar, tema2['wl'],
                      (game.judul_rect.midleft[0],
                       game.judul_rect.midleft[1]+40),
                      (game.judul_rect.midright[0], game.judul_rect.midright[1]+40), 3)
        elif game.wline == 3:
            draw.line(layar, tema3['wl'],
                      (game.judul_rect.midleft[0],
                       game.judul_rect.midleft[1]+40),
                      (game.judul_rect.midright[0], game.judul_rect.midright[1]+40), 3)

        # layar.blit(game.panel_1, game.panel_11Rect)

        pass

    def run(game):
        game.badan = [Vector2(13, 5), Vector2(12, 5), Vector2(
            11, 5), Vector2(10, 5), Vector2(9, 5)]
        UPDATE_CACING = USEREVENT+1
        pygame.time.set_timer(UPDATE_CACING, KECEPATAN_ULAR_BERGERAK)
        bisagerak = False
        game.arah = Vector2(0, 0)
        game.fd_pos1 = game.def_fdPos1
        game.fd_pos2 = game.def_fdPos2
        game.fd_pos3 = game.def_fdPos3
        while game.aktif:
            ki = event.get()
            if len(game.badan) == 66 and bisagerak == False:
                game.arah = Vector2(0, 0)
                bisagerak = True

            if game.index_makanan >= len(game.makanan_ke1):
                game.index_makanan = 0

            for ki in ki:
                if ki.type == QUIT:
                    quit()
                    exit()
                if ki.type == UPDATE_CACING:
                    game.update(untukMenuUtama=True)

                if ki.type == KEYDOWN and len(game.badan) >= 66 and bisagerak == True:
                    if ki.key == K_w or ki.key == K_UP:
                        if game.arah.y != 1:
                            game.arah = Vector2(0, -1)

                    if ki.key == K_d or ki.key == K_RIGHT:
                        if game.arah.x != -1:
                            game.arah = Vector2(1, 0)

                    if ki.key == K_s or ki.key == K_DOWN:
                        if game.arah.y != -1:
                            game.arah = Vector2(0, 1)

                    if ki.key == K_a or ki.key == K_LEFT:
                        if game.arah.x != 1:
                            game.arah = Vector2(-1, 0)
            if len(game.badan) < 66:
                if game.badan[0] == game.fd_pos1:
                    game.fd_pos1 = Vector2(-1, -1)
                else:
                    if game.badan[-1] == game.def_fdPos1:
                        game.fd_pos1 = game.def_fdPos1

                if game.badan[0] == game.fd_pos2:
                    game.fd_pos2 = Vector2(-1, -1)
                else:
                    if game.badan[-1] == game.def_fdPos2:
                        game.fd_pos2 = game.def_fdPos2

                if game.badan[0] == game.fd_pos3:
                    game.fd_pos3 = Vector2(-1, -1)
                else:
                    if game.badan[-1] == game.def_fdPos3:
                        game.fd_pos3 = game.def_fdPos3

            else:
                game.fd_pos1, game.fd_pos2, game.fd_pos3 = Vector2(
                    -1, -1), Vector2(-1, -1), Vector2(-1, -1)

            if len(game.badan) < 66:
                if game.arah == Vector2(0, 0):
                    game.arah = Vector2(1, 0)

                # ular bergerak berputar se arah jarum jam
                # jika kepala ular koordinatnya di 20,5
                if game.badan[0].distance_to(Vector2(20, 5)) == 0.0:
                    game.arah = Vector2(0, 1)
                # jika kepala ular koordinatnya di 20,20
                if game.badan[0].distance_to(Vector2(20, 20)) == 0.0:
                    game.arah = Vector2(-1, 0)
                # jika kepala ular koordinatnya di 2,20
                if game.badan[0].distance_to(Vector2(2, 20)) == 0.0:
                    game.arah = Vector2(0, -1)
                # jika kepala ular koordinatnya di 2,5
                if game.badan[0].distance_to(Vector2(2, 5)) == 0.0:
                    game.arah = Vector2(1, 0)

            game.draw()

            pw.update(ki)
            display.update()
            fps.tick(FPS)
            game.index_makanan += KONST_ANI*10

        pass
    # endregion

    # ! Membuat menu pengaturan
    # region Pengaturan
    def pengDraw(game):
        # gambar tampilan pengaturan
        layar.blit(game.bg, game.bg_rect)
        layar.blit(game.panel_1, game.panel_1Rect)
        layar.blit(game.teksH1, game.teksH1_rect)
        layar.blit(game.teksh2, game.teksh2_rect)
        # layar.blit(game.teks1, game.teks1_rect)

        # region Garis dan Tampilan Map
        # hanya ganti warna si garis-garis
        if game.wline == 0:
            # Tampilan Map
            layar.blit(game.tampilan_tema_default, game.tt_rect)

            # garis kotak di pinggir layar
            draw.line(layar, wLine, (0, 0), (UKURAN_WINDOWS[0], 0), 2)
            draw.line(layar, wLine, (0, 0), (0, UKURAN_WINDOWS[1]), 2)
            draw.line(layar,
                      wLine,
                      (game.bg_rect.bottomleft[0],
                       game.bg_rect.bottomleft[1]-2),
                      (game.bg_rect.bottomright[0],
                       game.bg_rect.bottomright[1]-2),
                      2)
            draw.line(layar,
                      wLine,
                      (game.bg_rect.bottomright[0]-2,
                       game.bg_rect.bottomright[1]),
                      (game.bg_rect.topright[0]-2, game.bg_rect.topright[1]),
                      2)

            # Garis di antara tombol kembali dan tulisan "Theme:"
            draw.line(layar,
                      wLine,
                      (0,
                       game.teks1_rect.midbottom[1]+10),
                      (UKURAN_WINDOWS[0],
                       game.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      wLine,
                      (0, game.panel_1Rect.midbottom[1]),
                      (UKURAN_WINDOWS[0], game.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      wLine,
                      (game.btn_defaultRect.midtop[0]+30,
                       game.btn_defaultRect.topright[1]-10),
                      (game.btn_defaultRect.midtop[0]+30, game.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      wLine,
                      (game.btn_defaultRect.midtop[0] +
                       30, game.teksh2_rect.y-30),
                      (UKURAN_WINDOWS[0]-1, game.teksh2_rect.y-30), 3)

        if game.wline == 1:
            # Tampilan Map
            layar.blit(game.tampilan_tema_1, game.tt_rect)

            # garis kotak di pinggir layar
            draw.line(layar, tema1['wl'], (0, 0), (UKURAN_WINDOWS[0], 0), 2)
            draw.line(layar, tema1['wl'], (0, 0), (0, UKURAN_WINDOWS[1]), 2)
            draw.line(layar,
                      tema1['wl'],
                      (game.bg_rect.bottomleft[0],
                       game.bg_rect.bottomleft[1]-2),
                      (game.bg_rect.bottomright[0],
                       game.bg_rect.bottomright[1]-2),
                      2)
            draw.line(layar,
                      tema1['wl'],
                      (game.bg_rect.bottomright[0]-2,
                       game.bg_rect.bottomright[1]),
                      (game.bg_rect.topright[0]-2, game.bg_rect.topright[1]),
                      2)

            # Garis di antara tombol kembali dan tulisan "Theme:"
            draw.line(layar,
                      tema1['wl'],
                      (0,
                       game.teks1_rect.midbottom[1]+10),
                      (UKURAN_WINDOWS[0],
                       game.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      tema1['wl'],
                      (0, game.panel_1Rect.midbottom[1]),
                      (UKURAN_WINDOWS[0], game.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema1['wl'],
                      (game.btn_defaultRect.midtop[0]+30,
                       game.btn_defaultRect.topright[1]-10),
                      (game.btn_defaultRect.midtop[0]+30, game.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema1['wl'],
                      (game.btn_defaultRect.midtop[0] +
                       30, game.teksh2_rect.y-30),
                      (UKURAN_WINDOWS[0]-1, game.teksh2_rect.y-30), 3)

        if game.wline == 2:
            # Tampilan Map
            layar.blit(game.tampilan_tema_2, game.tt_rect)

            # garis kotak di pinggir layar
            draw.line(layar, tema2['wl'], (0, 0), (UKURAN_WINDOWS[0], 0), 2)
            draw.line(layar, tema2['wl'], (0, 0), (0, UKURAN_WINDOWS[1]), 2)
            draw.line(layar,
                      tema2['wl'],
                      (game.bg_rect.bottomleft[0],
                       game.bg_rect.bottomleft[1]-2),
                      (game.bg_rect.bottomright[0],
                       game.bg_rect.bottomright[1]-2),
                      2)
            draw.line(layar,
                      tema2['wl'],
                      (game.bg_rect.bottomright[0]-2,
                       game.bg_rect.bottomright[1]),
                      (game.bg_rect.topright[0]-2, game.bg_rect.topright[1]),
                      2)

            # Garis di antara tombol kembali dan tulisan "Theme:"
            draw.line(layar,
                      tema2['wl'],
                      (0,
                       game.teks1_rect.midbottom[1]+10),
                      (UKURAN_WINDOWS[0],
                       game.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      tema2['wl'],
                      (0, game.panel_1Rect.midbottom[1]),
                      (UKURAN_WINDOWS[0], game.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema2['wl'],
                      (game.btn_defaultRect.midtop[0]+30,
                       game.btn_defaultRect.topright[1]-10),
                      (game.btn_defaultRect.midtop[0]+30, game.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema2['wl'],
                      (game.btn_defaultRect.midtop[0] +
                       30, game.teksh2_rect.y-30),
                      (UKURAN_WINDOWS[0]-1, game.teksh2_rect.y-30), 3)

        if game.wline == 3:
            # Tampilan Map
            layar.blit(game.tampilan_tema_3, game.tt_rect)

            # garis kotak di pinggir layar
            draw.line(layar, tema3['wl'], (0, 0), (UKURAN_WINDOWS[0], 0), 2)
            draw.line(layar, tema3['wl'], (0, 0), (0, UKURAN_WINDOWS[1]), 2)
            draw.line(layar,
                      tema3['wl'],
                      (game.bg_rect.bottomleft[0],
                       game.bg_rect.bottomleft[1]-2),
                      (game.bg_rect.bottomright[0],
                       game.bg_rect.bottomright[1]-2),
                      2)
            draw.line(layar,
                      tema3['wl'],
                      (game.bg_rect.bottomright[0]-2,
                       game.bg_rect.bottomright[1]),
                      (game.bg_rect.topright[0]-2, game.bg_rect.topright[1]),
                      2)

            # Garis di antara tombol kembali dan tulisan "Theme:"
            draw.line(layar,
                      tema3['wl'],
                      (0,
                       game.teks1_rect.midbottom[1]+10),
                      (UKURAN_WINDOWS[0],
                       game.teks1_rect.midbottom[1]+10), 3)

            draw.line(layar,
                      tema3['wl'],
                      (0, game.panel_1Rect.midbottom[1]),
                      (UKURAN_WINDOWS[0], game.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema3['wl'],
                      (game.btn_defaultRect.midtop[0]+30,
                       game.btn_defaultRect.topright[1]-10),
                      (game.btn_defaultRect.midtop[0]+30, game.panel_1Rect.midbottom[1]), 3)

            draw.line(layar,
                      tema3['wl'],
                      (game.btn_defaultRect.midtop[0] +
                       30, game.teksh2_rect.y-30),
                      (UKURAN_WINDOWS[0]-1, game.teksh2_rect.y-30), 3)
        # endregion

        game.gambar_makanan(display=True)
        game.gambar_ular()
        pass

    def pengaturan(game):
        game.badan = [Vector2(15, 17), Vector2(
            14, 17), Vector2(13, 17), Vector2(12, 17)]
        tunggu = True
        while game.paktif:
            ki = event.get()
            for ki in ki:
                if ki.type == QUIT:
                    quit()
                    exit()

            if game.index_makanan >= len(game.fr_makanan):
                game.index_makanan = 0

            if tunggu:
                tm.sleep(TMFB)
                tunggu = False
            game.pengDraw()

            pw.update(ki)
            display.update()
            fps.tick(FPS)
            game.index_makanan += KONST_ANI*10

    # endregion

    # ! membuat Game Cacingnya
    # region Game
    def drawElem(game):
        layar.blit(game.pbg, game.pbg_rect)
        game.rumput()

        game.gambar_makanan()
        game.gambar_ular()

        layar.blits([(game.pskor, game.pskor_rect),
                     (game.border0, game.border0_rect),
                     (game.border1, game.border1_rect),
                     (game.border2, game.border2_rect),
                     (game.border3, game.border3_rect)])

        game.skor()

    def update(game, untukMenuUtama=False):
        if not untukMenuUtama:
            game.gerakSiular()
            game.cek_tabrakan()
            game.cek_gagal()
        else:
            game.gerakSiular()
            game.cek_tabrakan(untukMenuUtama=True)

    def cek_tabrakan(game, untukMenuUtama=False):
        """Cek si cacing jika nabrak makanan."""
        if not untukMenuUtama:
            if game.fd_pos.distance_to(game.badan[0]) == 0.0:
                game.acakPos()
                if not game.apakahGameOver:
                    game.tambah_blok()
                    game.go_nskor += 1
                game.suara_makan.play()
            for blok in game.badan[1:]:
                if blok == game.fd_pos:
                    game.acakPos()
        else:
            if game.badan[0].x == -1:
                game.badan[0].x = celln
            if game.badan[0].x == celln+1:
                game.badan[0].x = 0
            if game.badan[0].y == -1:
                game.badan[0].y = celln
            if game.badan[0].y == celln+1:
                game.badan[0].y = 0
            pass

            if game.fd_pos1.distance_to(game.badan[0]) == 0.0:
                game.tambah_blok()
                # game.suara_makan.play()
            if game.fd_pos2.distance_to(game.badan[0]) == 0.0:
                game.tambah_blok()

            if game.fd_pos2.distance_to(game.badan[0]) == 0.0:
                game.tambah_blok()
            pass

    def cek_gagal(game):
        """Cek si cacing jika nabrak tembok atau badannya sendiri."""
        if not 1 <= game.badan[0].x < celln-1 or not 3 <= game.badan[0].y < celln-1:
            game.apakahGameOver = True
            game.suara_latar_belakang.stop()
            game.suara_nabrak.play()
            game.gameOver()
            pass
        else:
            game.apakahGameOver = False

        for blok in game.badan[1:]:
            if blok == game.badan[0] and game.arah != Vector2(0, 0):
                game.apakahGameOver = True
                game.suara_latar_belakang.stop()
                game.suara_nabrak.play()
                game.gameOver()
        pass

    def drawGameOver(game):
        if game.nths == 0:
            draw.rect(layar, tema0['pn1'], game.pngmRect, 0, 4)
        elif game.nths == 1:
            draw.rect(layar, tema1['pn1'], game.pngmRect, 0, 4)
        elif game.nths == 2:
            draw.rect(layar, tema2['pn1'], game.pngmRect, 0, 4)
        elif game.nths == 3:
            draw.rect(layar, tema3['pn1'], game.pngmRect, 0, 4)
        # membuat tulisan game over
        if game.wline == 0:
            game.tkgmover = game.font_h1.render('Game Over', True, tema0['tk'])
        if game.wline == 1:
            game.tkgmover = game.font_h1.render('Game Over', True, tema1['tk'])
        if game.wline == 2:
            game.tkgmover = game.font_h1.render('Game Over', True, tema2['tk'])
        if game.wline == 3:
            game.tkgmover = game.font_h1.render('Game Over', True, tema3['tk'])
        game.tkgmoverRect = game.tkgmover.get_rect(midtop=(game.pngmRect.midtop[0],
                                                           game.pngmRect.midtop[1]+10))

        # game.pngmRect.center = game.boardRect.center

        # region Skor dan HighSkor
        game.display_makanan2x = transform.smoothscale(
            game.makanan, (game.pskor_rect.height-25, game.pskor_rect.height-25))
        game.display_makanan2xRect = game.display_makanan2x.get_rect(
            midleft=(game.pngmRect.midleft[0]+40, int(game.boardRect.midleft[1]-(game.boardRect.midleft[1]*(1/4)))))

        if game.wline == 0:
            game.teks_skor = game.font_h1.render(
                f'{game.nskor}', True, tema0['tk'])
        if game.wline == 1:
            game.teks_skor = game.font_h1.render(
                f'{game.nskor}', True, tema1['tk'])
        if game.wline == 2:
            game.teks_skor = game.font_h1.render(
                f'{game.nskor}', True, tema2['tk'])
        if game.wline == 3:
            game.teks_skor = game.font_h1.render(
                f'{game.nskor}', True, tema3['tk'])

        game.teks_skorRect = game.teks_skor.get_rect(
            midleft=game.display_makanan2xRect.midright)
        game.teks_skorRect.x += 5
        game.teks_skorRect.y += 2

        # membuat high skor
        if game.go_nskor >= game.go_high_skor:
            game.go_high_skor = game.go_nskor
        if game.wline == 0:
            teks_hskor = game.font_h1.render(
                f'{game.go_high_skor}', True, tema0['tk'])
        if game.wline == 1:
            teks_hskor = game.font_h1.render(
                f'{game.go_high_skor}', True, tema1['tk'])
        if game.wline == 2:
            teks_hskor = game.font_h1.render(
                f'{game.go_high_skor}', True, tema2['tk'])
        if game.wline == 3:
            teks_hskor = game.font_h1.render(
                f'{game.go_high_skor}', True, tema3['tk'])
        teks_hskorRect = teks_hskor.get_rect(
            midleft=(game.pngmRect.midright[0]-80, game.teks_skorRect.midright[1]))

        pialaRect = game.piala.get_rect(
            midright=(teks_hskorRect.midleft[0]-5, teks_hskorRect.midleft[1]))

        # endregion

        layar.blits([(game.tkgmover, game.tkgmoverRect), (game.display_makanan2x, game.display_makanan2xRect),
                     (game.teks_skor, game.teks_skorRect), (teks_hskor, teks_hskorRect), (game.piala, pialaRect)])
        pass

    def gameOver(game):
        # region 'Disable' & 'Enable' Tombol
        game.btnHome.enable()
        game.btnHome.show()
        game.btnReset.enable()
        game.btnReset.show()
        game.btn_play.disable()
        game.btn_keluar.disable()
        game.btn_peng.disable()
        game.btn_play.hide()
        game.btn_keluar.hide()
        game.btn_peng.hide()
        # endregion
        while game.plgAktif:
            ki = event.get()
            for ki in ki:
                if ki.type == QUIT:
                    quit()
                    exit()
                if ki.type == KEYDOWN:
                    if ki.key == K_RETURN:
                        game.klikReset()
                if ki.type == KEYDOWN:
                    if ki.key == K_SPACE:
                        game.klikHome()

            game.drawGameOver()
            pw.update(ki)
            display.update()
            fps.tick(FPS)

    def play(game):
        UPDATE_CACING = USEREVENT
        pygame.time.set_timer(UPDATE_CACING, KECEPATAN_ULAR_BERGERAK)
        tunggu = True
        while game.plAktif:
            for ki in event.get():
                if ki.type == QUIT:
                    quit()
                    exit()
                if ki.type == UPDATE_CACING:
                    game.update()

                if ki.type == KEYDOWN:
                    # Kontrol si ular
                    if ki.key == K_w or ki.key == K_UP:
                        if game.arah.y != 1:
                            game.arah = Vector2(0, -1)

                    if ki.key == K_d or ki.key == K_RIGHT:
                        if game.arah.x != -1:
                            game.arah = Vector2(1, 0)

                    if ki.key == K_s or ki.key == K_DOWN:
                        if game.arah.y != -1:
                            game.arah = Vector2(0, 1)

                    if ki.key == K_a or ki.key == K_LEFT:
                        if game.arah.x != 1 and game.arah != Vector2(0,0):
                            game.arah = Vector2(-1, 0)

                pass

            if game.index_makanan >= 5:
                game.index_makanan = 0

            if tunggu:
                tm.sleep(TMFB)
                tunggu = False

            game.drawElem()
            display.update()
            game.index_makanan += (KONST_ANI*10)
            fps.tick(FPS)

    def skor(game):
        # membuat tulisan skor
        game.display_makanan2x = transform.smoothscale(
            game.makanan, (game.pskor_rect.height-25, game.pskor_rect.height-25))
        game.display_makanan2xRect = game.display_makanan2x.get_rect(
            midleft=(game.border0_rect.topright[0]+125, game.pskor_rect.midleft[1]))

        game.nskor = 0
        game.nskor+= game.go_nskor

        if game.wline == 0:
            game.teks_skor = game.font_h1.render(
                f'{game.nskor}', True, tema0['tk'])
        if game.wline == 1:
            game.teks_skor = game.font_h1.render(
                f'{game.nskor}', True, tema1['tk'])
        if game.wline == 2:
            game.teks_skor = game.font_h1.render(
                f'{game.nskor}', True, tema2['tk'])
        if game.wline == 3:
            game.teks_skor = game.font_h1.render(
                f'{game.nskor}', True, tema3['tk'])

        game.teks_skorRect = game.teks_skor.get_rect(
            midleft=game.display_makanan2xRect.midright)
        game.teks_skorRect.x += 5
        game.teks_skorRect.y += 2

        # membuat piala jika player mengulang game
        dis_piala2x = transform.smoothscale(
            game.piala, (game.pskor_rect.height-25, game.pskor_rect.height-25))
        dis_piala2xRect = dis_piala2x.get_rect(
            midleft=(game.border0_rect.topright[0]+(125*3), game.pskor_rect.midleft[1]))

        layar.blits([(game.teks_skor, game.teks_skorRect),
                    (game.display_makanan2x, game.display_makanan2xRect)])

        if game.go_high_skor != 0:
            if game.nskor >= game.go_high_skor:
                game.go_high_skor = game.nskor

            if game.wline == 0:
                teks_hskor = game.font_h1.render(
                    f'{game.go_high_skor}', True, tema0['tk'])
            if game.wline == 1:
                teks_hskor = game.font_h1.render(
                    f'{game.go_high_skor}', True, tema1['tk'])
            if game.wline == 2:
                teks_hskor = game.font_h1.render(
                    f'{game.go_high_skor}', True, tema2['tk'])
            if game.wline == 3:
                teks_hskor = game.font_h1.render(
                    f'{game.go_high_skor}', True, tema3['tk'])
            teks_hskorRect = teks_hskor.get_rect(
                midleft=(dis_piala2xRect.midright[0]+5, dis_piala2xRect.midright[1]+1))

            layar.blit(dis_piala2x, dis_piala2xRect)
            layar.blit(teks_hskor, teks_hskorRect)

        pass

    def rumput(game):
        # Gambar Rumput / Kotak2
        for i in range(celln):
            if i % 2 == 0:
                for j in range(celln):
                    if j % 2 == 0:
                        rumputRect = Rect(j*imgSize, i*imgSize,
                                          imgSize, imgSize)
                        draw.rect(layar, game.warnaRumput, rumputRect)
            else:
                for j in range(celln):
                    if j % 2 != 0:
                        rumputRect = Rect(j*imgSize, i*imgSize,
                                          imgSize, imgSize)
                        draw.rect(layar, game.warnaRumput, rumputRect)
                pass
        pass

    # endregion

    # region Fungsi Tombol2 Jika Di Klik
    def klikHome(game):
        game.btnHome.disable()
        game.btnHome.hide()
        game.btnReset.disable()
        game.btnReset.hide()
        game.btn_play.enable()
        game.btn_keluar.enable()
        game.btn_peng.enable()
        game.btn_play.show()
        game.btn_keluar.show()
        game.btn_peng.show()
        game.run()

    def klikReset(game):
        game.btnHome.disable()
        game.btnHome.hide()
        game.btnReset.disable()
        game.btnReset.hide()
        game.go_nskor = 0
        game.reset()
        game.suara_latar_belakang.play()
        game.play()

    def btn_pengaturan(game):
        game.btn_defaultT.show()
        game.btn_kembali.show()
        game.btn_theme1.show()
        game.btn_theme2.show()
        game.btn_theme3.show()

        game.btn_keluar.hide()
        game.btn_play.hide()
        game.btn_peng.hide()

        game.btn_sound.show()

        game.pengaturan()

    def klikKembali(game):
        game.btn_kembali.hide()
        game.btn_defaultT.hide()
        game.btn_theme1.hide()
        game.btn_theme2.hide()
        game.btn_theme3.hide()

        game.btn_keluar.show()
        game.btn_play.show()
        game.btn_peng.show()

        game.btn_sound.disable()
        game.btn_sound.hide()

        # taro cacing & makanan ke posisi awalnya
        game.badan = [Vector2(13, 5), Vector2(12, 5), Vector2(
            11, 5), Vector2(10, 5), Vector2(9, 5)]
        game.arah = Vector2(0, 0)
        game.fd_pos1 = game.def_fdPos1
        game.fd_pos2 = game.def_fdPos2
        game.fd_pos3 = game.def_fdPos3
        game.run()

    def klik_SoundbtnON(game):
        game.suara_latar_belakang.set_volume(0.58)
        game.suara_makan.set_volume(0.7)
        game.suara_nabrak.set_volume(0.7)
        game.btn_soundState = 'ON'

        if game.wline == 0:
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_ON,
                                    warnaAktif=wBA,
                                    warnaHover=wBH,
                                    warnaDitekan=wBP,
                                    warnaTeks=warnaTeks,
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnOFF)
            game.btn_sound.hoverColour = tema0['btnH']
            game.btn_sound.pressedColour = tema0['btnP']
            game.btn_sound.inactiveColour = tema0['btnA']
            game.btn_sound.textColour = rgb(233, 255, 191)
        if game.wline == 1:
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_ON,
                                    warnaAktif=tema1['btnA'],
                                    warnaHover=tema1['btnH'],
                                    warnaDitekan=tema1['btnP'],
                                    warnaTeks=tema1['tk'],
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnOFF)
            game.btn_sound.hoverColour = tema1['btnH']
            game.btn_sound.pressedColour = tema1['btnP']
            game.btn_sound.inactiveColour = tema1['btnA']
            game.btn_sound.textColour = tema1['tk']
        if game.wline == 2:
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_ON,
                                    warnaAktif=tema2['btnA'],
                                    warnaHover=tema2['btnH'],
                                    warnaDitekan=tema2['btnP'],
                                    warnaTeks=tema2['tk'],
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnOFF)
            game.btn_sound.hoverColour = tema2['btnH']
            game.btn_sound.pressedColour = tema2['btnP']
            game.btn_sound.inactiveColour = tema2['btnA']
            game.btn_sound.textColour = tema2['tk']
        if game.wline == 3:
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_ON,
                                    warnaAktif=tema3['btnA'],
                                    warnaHover=tema3['btnH'],
                                    warnaDitekan=tema3['btnP'],
                                    warnaTeks=tema3['tk'],
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnOFF)
            game.btn_sound.hoverColour = tema3['btnH']
            game.btn_sound.pressedColour = tema3['btnP']
            game.btn_sound.inactiveColour = tema3['btnA']
            game.btn_sound.textColour = tema3['tk']
        pass

    def klik_SoundbtnOFF(game):
        game.suara_latar_belakang.set_volume(0.0)
        game.suara_makan.set_volume(0.0)
        game.suara_nabrak.set_volume(0.0)
        game.btn_soundState = 'OFF'

        if game.wline == 0:
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_OFF,
                                    warnaAktif=wBA,
                                    warnaHover=wBH,
                                    warnaDitekan=wBP,
                                    warnaTeks=warnaTeks,
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnON)
            game.btn_sound.hoverColour = tema0['btnH']
            game.btn_sound.pressedColour = tema0['btnP']
            game.btn_sound.inactiveColour = tema0['btnA']
            game.btn_sound.textColour = rgb(233, 255, 191)
        if game.wline == 1:
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_OFF,
                                    warnaAktif=tema1['btnA'],
                                    warnaHover=tema1['btnH'],
                                    warnaDitekan=tema1['btnP'],
                                    warnaTeks=tema1['tk'],
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnON)
            game.btn_sound.hoverColour = tema1['btnH']
            game.btn_sound.pressedColour = tema1['btnP']
            game.btn_sound.inactiveColour = tema1['btnA']
            game.btn_sound.textColour = tema1['tk']
        if game.wline == 2:
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_OFF,
                                    warnaAktif=tema2['btnA'],
                                    warnaHover=tema2['btnH'],
                                    warnaDitekan=tema2['btnP'],
                                    warnaTeks=tema2['tk'],
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnON)
            game.btn_sound.hoverColour = tema2['btnH']
            game.btn_sound.pressedColour = tema2['btnP']
            game.btn_sound.inactiveColour = tema2['btnA']
            game.btn_sound.textColour = tema2['tk']
        if game.wline == 3:
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_OFF,
                                    warnaAktif=tema3['btnA'],
                                    warnaHover=tema3['btnH'],
                                    warnaDitekan=tema3['btnP'],
                                    warnaTeks=tema3['tk'],
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnON)
            game.btn_sound.hoverColour = tema3['btnH']
            game.btn_sound.pressedColour = tema3['btnP']
            game.btn_sound.inactiveColour = tema3['btnA']
            game.btn_sound.textColour = tema3['tk']
        pass

    def fbtn_play(game):
        game.reset()
        game.go_nskor = 0
        game.suara_latar_belakang.play(-1)
        game.play()

    def setDefTheme(game):
        global warnaTeks
        game.wline = 0
        game.bg.fill(tema0['bg'])
        game.panel_1.fill(tema0['pn1'])
        warnaTeks = tema0['tk']
        game.display_makananAktif = 0

        # region pengaturan
        game.btn_kembali = Tombol(game.bg,
                                  game.btn_kembaliRect.x,
                                  game.btn_kembaliRect.y,
                                  game.btn_kembaliRect.width,
                                  game.btn_kembaliRect.height,
                                  game.btn_font,
                                  20,
                                  nama_tombol_kembali,
                                  warnaAktif=wBA,
                                  warnaHover=wBH,
                                  warnaDitekan=wBP,
                                  warnaTeks=warnaTeks,
                                  shadowDistance=2,
                                  shadowColour=wBSh,
                                  sudutRad=3,
                                  onRelease=game.klikKembali)

        # membuat tombol tema bawaan
        game.btn_defaultT = Tombol(game.bg,
                                   game.btn_defaultRect.x,
                                   game.btn_defaultRect.y,
                                   game.btn_defaultRect.width,
                                   game.btn_defaultRect.height,
                                   game.btn_font, 20,
                                   nama_tombol_default,
                                   warnaAktif=wBA,
                                   warnaHover=wBH,
                                   warnaDitekan=wBP,
                                   warnaTeks=warnaTeks,
                                   shadowDistance=2,
                                   shadowColour=wBSh,
                                   sudutRad=3,
                                   onClick=game.setDefTheme)

        if game.btn_soundState == 'ON':
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_ON,
                                    warnaAktif=wBA,
                                    warnaHover=wBH,
                                    warnaDitekan=wBP,
                                    warnaTeks=warnaTeks,
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnON)
        if game.btn_soundState == 'OFF':
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_OFF,
                                    warnaAktif=wBA,
                                    warnaHover=wBH,
                                    warnaDitekan=wBP,
                                    warnaTeks=warnaTeks,
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnOFF)

        game.btn_theme1 = Tombol(game.bg,
                                 game.btn_theme1Rect.x,
                                 game.btn_theme1Rect.y,
                                 game.btn_theme1Rect.width,
                                 game.btn_theme1Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_1,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme1)

        # Tema ke 2
        game.btn_theme2 = Tombol(game.bg,
                                 game.btn_theme2Rect.x,
                                 game.btn_theme2Rect.y,
                                 game.btn_theme2Rect.width,
                                 game.btn_theme2Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_2,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme2)
        # Tema ke 3
        game.btn_theme3 = Tombol(game.bg,
                                 game.btn_theme3Rect.x,
                                 game.btn_theme3Rect.y,
                                 game.btn_theme3Rect.width,
                                 game.btn_theme3Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_3,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme3)

        game.teks1 = game.font_h2.render('Theme: Default', True, warnaTeks)
        game.teksH1 = game.font_h1.render(
            teks_di_pengaturan_h1, True, warnaTeks)

        game.teksh2 = game.font_h2.render(
            teks_di_pengaturan_h2, True, tema0['tk'])
        game.teksh2_rect = game.teksh2.get_rect(topleft=(12*30+35, 0))
        game.teksh2_rect.y = 540-game.teksh2_rect.height-33
        # endregion

        # region Menu Utama
        game.btn_play = Tombol(layar,
                               game.btn_playRect.x,
                               game.btn_playRect.y,
                               game.btn_playRect.width-20,
                               game.btn_playRect.height,
                               game.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks=nama_tombol_main,
                               sudutRad=3,
                               onRelease=game.fbtn_play)

        # membuat tombol pengaturan
        game.btn_peng = Tombol(layar,
                               game.btn_pengRect.x,
                               game.btn_pengRect.y,
                               game.btn_pengRect.width-20,
                               game.btn_pengRect.height,
                               game.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks=nama_tombol_pengaturan,
                               sudutRad=3,
                               onRelease=game.btn_pengaturan)

        # membuat tombol keluar

        game.btn_keluar = Tombol(layar,
                                 game.btn_keluarRect.x,
                                 game.btn_keluarRect.y,
                                 game.btn_pengRect.width-20,
                                 game.btn_pengRect.height,
                                 game.btn_font1,
                                 warnaTeks=warnaTeks,
                                 warnaAktif=wBA,
                                 warnaDitekan=wBP,
                                 warnaHover=wBH,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 teks=nama_tombol_keluar,
                                 sudutRad=3,
                                 onRelease=lambda: exit())

        game.bg1.fill(tema0['bg'])
        game.judul = game.title_font.render(
            judul, True, warnaTeks)
        # endregion

        # region Ular
        game.h_up = image.load(thp1/'kepala_up.png').convert_alpha()
        game.h_down = image.load(thp1/'kepala_down.png').convert_alpha()
        game.h_left = image.load(thp1/'kepala_left.png').convert_alpha()
        game.h_right = image.load(thp1/'kepala_right.png').convert_alpha()

        game.b_tr = image.load(thp1/'badan_tr.png').convert_alpha()
        game.b_tl = image.load(thp1/'badan_tl.png').convert_alpha()
        game.b_bl = image.load(thp1/'badan_bl.png').convert_alpha()
        game.b_br = image.load(thp1/'badan_br.png').convert_alpha()

        game.b_v = image.load(thp1/'badan_v.png').convert_alpha()
        game.b_h = image.load(thp1/'badan_h.png').convert_alpha()

        game.t_up = image.load(thp1/'ekor_up.png').convert_alpha()
        game.t_down = image.load(thp1/'ekor_down.png').convert_alpha()
        game.t_left = image.load(thp1/'ekor_left.png').convert_alpha()
        game.t_right = image.load(thp1/'ekor_right.png').convert_alpha()
        # endregion

        # region Play
        game.nths = 0
        game.warnaRumput = tema0['rm']
        game.pbg.fill(tema0['bg'])
        game.pskor.fill(tema0['skp'])
        game.border0.fill(tema0['brd'])
        game.border1.fill(tema0['brd'])
        game.border2.fill(tema0['brd'])
        game.border3.fill(tema0['brd'])

        game.btnHome = Tombol(layar,
                              game.btnHomeRect.x,
                              game.btnHomeRect.y,
                              game.btnHomeRect.width,
                              game.btnHomeRect.height,
                              game.btn_font1, 20,
                              nama_tombol_kembali_ke_menu_utama,
                              warnaTeks,
                              wBA, wBH, wBP, 20, 2,
                              onRelease=game.klikHome)

        game.btnReset = Tombol(layar,
                               game.btnResetRect.x,
                               game.btnResetRect.y,
                               game.btnResetRect.width,
                               game.btnResetRect.height,
                               game.btn_font1, 20,
                               nama_tombol_ulang_game,
                               warnaTeks,
                               wBA, wBH, wBP, 20, 2,
                               onRelease=game.klikReset)
        # endregion

        # makanan
        game.fr_makanan = [image.load(mkn/'pete_f0.png').convert_alpha(),
                           image.load(mkn/'pete_f1.png').convert_alpha(),
                           image.load(mkn/'pete_f2.png').convert_alpha(),
                           image.load(mkn/'pete_f2.png').convert_alpha(),
                           image.load(mkn/'pete_f1.png').convert_alpha(),
                           image.load(mkn/'pete_f0.png').convert_alpha()]
        game.makanan = image.load(mkn/'pete.png').convert_alpha()

        # region END
        game.btn_keluar.hide()
        game.btn_play.hide()
        game.btn_peng.hide()
        game.btnHome.hide()
        game.btnReset.hide()
        # endregion
        pass

    def setTheme1(game):
        game.wline = 1
        game.bg.fill(tema1['bg'])
        game.panel_1.fill(tema1['pn1'])
        warnaTeks = tema1['tk']
        wBA = tema1['btnA']
        wBH = tema1['btnH']
        wBP = tema1['btnP']
        game.display_makananAktif = 1

        game.btn_keluar.hide()
        game.btn_play.hide()
        game.btn_peng.hide()

        game.btn_sound.show()
        game.btn_sound.enable()

        # region pengaturan
        game.btn_kembali = Tombol(game.bg,
                                  game.btn_kembaliRect.x,
                                  game.btn_kembaliRect.y,
                                  game.btn_kembaliRect.width,
                                  game.btn_kembaliRect.height,
                                  game.btn_font,
                                  20,
                                  nama_tombol_kembali,
                                  warnaAktif=wBA,
                                  warnaHover=wBH,
                                  warnaDitekan=wBP,
                                  warnaTeks=warnaTeks,
                                  shadowDistance=2,
                                  shadowColour=wBSh,
                                  sudutRad=3,
                                  onRelease=game.klikKembali)

        # membuat tombol tema bawaan
        game.btn_defaultT = Tombol(game.bg,
                                   game.btn_defaultRect.x,
                                   game.btn_defaultRect.y,
                                   game.btn_defaultRect.width,
                                   game.btn_defaultRect.height,
                                   game.btn_font, 20,
                                   nama_tombol_default,
                                   warnaAktif=wBA,
                                   warnaHover=wBH,
                                   warnaDitekan=wBP,
                                   warnaTeks=warnaTeks,
                                   shadowDistance=2,
                                   shadowColour=wBSh,
                                   sudutRad=3,
                                   onClick=game.setDefTheme)

        if game.btn_soundState == 'ON':
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_ON,
                                    warnaAktif=wBA,
                                    warnaHover=wBH,
                                    warnaDitekan=wBP,
                                    warnaTeks=warnaTeks,
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnON)
        if game.btn_soundState == 'OFF':
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_OFF,
                                    warnaAktif=wBA,
                                    warnaHover=wBH,
                                    warnaDitekan=wBP,
                                    warnaTeks=warnaTeks,
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnOFF)

        # region Tombol Theme
        game.btn_theme1 = Tombol(game.bg,
                                 game.btn_theme1Rect.x,
                                 game.btn_theme1Rect.y,
                                 game.btn_theme1Rect.width,
                                 game.btn_theme1Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_1,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme1)

        # Tema ke 2
        game.btn_theme2 = Tombol(game.bg,
                                 game.btn_theme2Rect.x,
                                 game.btn_theme2Rect.y,
                                 game.btn_theme2Rect.width,
                                 game.btn_theme2Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_2,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme2)
        # Tema ke 3
        game.btn_theme3 = Tombol(game.bg,
                                 game.btn_theme3Rect.x,
                                 game.btn_theme3Rect.y,
                                 game.btn_theme3Rect.width,
                                 game.btn_theme3Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_3,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme3)

        # game.teks1 = game.font_h2.render('Theme: ', True, warnaTeks)
        game.teksH1 = game.font_h1.render(
            teks_di_pengaturan_h1, True, tema1['tk'])

        game.teksh2 = game.font_h2.render(
            teks_di_pengaturan_h2, True, tema1['tk'])
        game.teksh2_rect = game.teksh2.get_rect(topleft=(12*30+35, 0))
        game.teksh2_rect.y = 540-game.teksh2_rect.height-33
        # endregion
        # endregion

        # region menu utama
        game.btn_play = Tombol(layar,
                               game.btn_playRect.x,
                               game.btn_playRect.y,
                               game.btn_playRect.width-20,
                               game.btn_playRect.height,
                               game.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks=nama_tombol_main,
                               sudutRad=3,
                               onRelease=game.fbtn_play)

        # membuat tombol pengaturan
        game.btn_peng = Tombol(layar,
                               game.btn_pengRect.x,
                               game.btn_pengRect.y,
                               game.btn_pengRect.width-20,
                               game.btn_pengRect.height,
                               game.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks=nama_tombol_pengaturan,
                               sudutRad=3,
                               onRelease=game.btn_pengaturan)

        # membuat tombol keluar

        game.btn_keluar = Tombol(layar,
                                 game.btn_keluarRect.x,
                                 game.btn_keluarRect.y,
                                 game.btn_pengRect.width-20,
                                 game.btn_pengRect.height,
                                 game.btn_font1,
                                 warnaTeks=warnaTeks,
                                 warnaAktif=wBA,
                                 warnaDitekan=wBP,
                                 warnaHover=wBH,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 teks=nama_tombol_keluar,
                                 sudutRad=3,
                                 onRelease=lambda: exit())

        game.bg1.fill(tema1['bg'])
        game.judul = game.title_font.render(
            judul, True, tema1['tk'])
        # endregion

        # region Ular
        game.h_up = image.load(thp2/'kepala_up.png').convert_alpha()
        game.h_down = image.load(thp2/'kepala_down.png').convert_alpha()
        game.h_left = image.load(thp2/'kepala_left.png').convert_alpha()
        game.h_right = image.load(thp2/'kepala_right.png').convert_alpha()

        game.b_tr = image.load(thp2/'badan_tr.png').convert_alpha()
        game.b_tl = image.load(thp2/'badan_tl.png').convert_alpha()
        game.b_bl = image.load(thp2/'badan_bl.png').convert_alpha()
        game.b_br = image.load(thp2/'badan_br.png').convert_alpha()

        game.b_v = image.load(thp2/'badan_v.png').convert_alpha()
        game.b_h = image.load(thp2/'badan_h.png').convert_alpha()

        game.t_up = image.load(thp2/'ekor_up.png').convert_alpha()
        game.t_down = image.load(thp2/'ekor_down.png').convert_alpha()
        game.t_left = image.load(thp2/'ekor_left.png').convert_alpha()
        game.t_right = image.load(thp2/'ekor_right.png').convert_alpha()
        # endregion

        # region Play
        game.nths = 1
        game.warnaRumput = tema1['rm']
        game.pbg.fill(tema1['bg'])
        game.pskor.fill(tema1['skp'])
        game.border0.fill(tema1['brd'])
        game.border1.fill(tema1['brd'])
        game.border2.fill(tema1['brd'])
        game.border3.fill(tema1['brd'])

        game.btnHome = Tombol(layar,
                              game.btnHomeRect.x,
                              game.btnHomeRect.y,
                              game.btnHomeRect.width,
                              game.btnHomeRect.height,
                              game.btn_font1, 20,
                              nama_tombol_kembali_ke_menu_utama,
                              warnaTeks,
                              wBA, wBH, wBP, 20, 2,
                              onRelease=game.klikHome)

        game.btnReset = Tombol(layar,
                               game.btnResetRect.x,
                               game.btnResetRect.y,
                               game.btnResetRect.width,
                               game.btnResetRect.height,
                               game.btn_font1, 20,
                               nama_tombol_ulang_game,
                               warnaTeks,
                               wBA, wBH, wBP, 20, 2,
                               onRelease=game.klikReset)
        # endregion

        game.fr_makanan = [image.load(mkn/'nasgor_f0.png').convert_alpha(),
                           image.load(mkn/'nasgor_f1.png').convert_alpha(),
                           image.load(mkn/'nasgor_f2.png').convert_alpha(),
                           image.load(mkn/'nasgor_f2.png').convert_alpha(),
                           image.load(mkn/'nasgor_f1.png').convert_alpha(),
                           image.load(mkn/'nasgor_f0.png').convert_alpha()]

        game.makanan = image.load(mkn/'nasgor.png').convert_alpha()

        game.btn_keluar.hide()
        game.btn_play.hide()
        game.btn_peng.hide()
        game.btnHome.hide()
        game.btnReset.hide()
        pass

    def setTheme2(game):
        game.bg.fill(tema2['bg'])
        game.panel_1.fill(tema2['pn1'])
        warnaTeks = tema2['tk']
        wBA = tema2['btnA']
        wBH = tema2['btnH']
        wBP = tema2['btnP']
        game.wline = 2
        game.display_makananAktif = 2

        # region pengaturan
        game.btn_kembali = Tombol(game.bg,
                                  game.btn_kembaliRect.x,
                                  game.btn_kembaliRect.y,
                                  game.btn_kembaliRect.width,
                                  game.btn_kembaliRect.height,
                                  game.btn_font,
                                  20,
                                  nama_tombol_kembali,
                                  warnaAktif=wBA,
                                  warnaHover=wBH,
                                  warnaDitekan=wBP,
                                  warnaTeks=warnaTeks,
                                  shadowDistance=2,
                                  shadowColour=wBSh,
                                  sudutRad=3,
                                  onRelease=game.klikKembali)

        # membuat tombol tema bawaan
        game.btn_defaultT = Tombol(game.bg,
                                   game.btn_defaultRect.x,
                                   game.btn_defaultRect.y,
                                   game.btn_defaultRect.width,
                                   game.btn_defaultRect.height,
                                   game.btn_font, 20,
                                   nama_tombol_default,
                                   warnaAktif=wBA,
                                   warnaHover=wBH,
                                   warnaDitekan=wBP,
                                   warnaTeks=warnaTeks,
                                   shadowDistance=2,
                                   shadowColour=wBSh,
                                   sudutRad=3,
                                   onClick=game.setDefTheme)

        if game.btn_soundState == 'ON':
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_ON,
                                    warnaAktif=wBA,
                                    warnaHover=wBH,
                                    warnaDitekan=wBP,
                                    warnaTeks=warnaTeks,
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnON)
        if game.btn_soundState == 'OFF':
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_OFF,
                                    warnaAktif=wBA,
                                    warnaHover=wBH,
                                    warnaDitekan=wBP,
                                    warnaTeks=warnaTeks,
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnOFF)

        game.btn_theme1 = Tombol(game.bg,
                                 game.btn_theme1Rect.x,
                                 game.btn_theme1Rect.y,
                                 game.btn_theme1Rect.width,
                                 game.btn_theme1Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_1,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme1)

        # Tema ke 2
        game.btn_theme2Rect = Rect((game.btn_theme1Rect.bottomleft[0],
                                    game.btn_theme1Rect.bottomleft[1]+50),
                                   game.btnSize)
        game.btn_theme2 = Tombol(game.bg,
                                 game.btn_theme2Rect.x,
                                 game.btn_theme2Rect.y,
                                 game.btn_theme2Rect.width,
                                 game.btn_theme2Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_2,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme2)
        # Tema ke 3
        game.btn_theme3Rect = Rect((game.btn_theme2Rect.bottomleft[0],
                                    game.btn_theme2Rect.bottomleft[1]+50,),
                                   game.btnSize)
        game.btn_theme3 = Tombol(game.bg,
                                 game.btn_theme3Rect.x,
                                 game.btn_theme3Rect.y,
                                 game.btn_theme3Rect.width,
                                 game.btn_theme3Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_3,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme3)

        game.teksH1 = game.font_h1.render(
            teks_di_pengaturan_h1, True, warnaTeks)

        game.teksh2 = game.font_h2.render(
            teks_di_pengaturan_h2, True, tema2['tk'])
        game.teksh2_rect = game.teksh2.get_rect(topleft=(12*30+35, 0))
        game.teksh2_rect.y = 540-game.teksh2_rect.height-33
        # endregion

        # region menu utama
        game.btn_play = Tombol(layar,
                               game.btn_playRect.x,
                               game.btn_playRect.y,
                               game.btn_playRect.width-20,
                               game.btn_playRect.height,
                               game.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks=nama_tombol_main,
                               sudutRad=3,
                               onRelease=game.fbtn_play)

        # membuat tombol pengaturan
        game.btn_peng = Tombol(layar,
                               game.btn_pengRect.x,
                               game.btn_pengRect.y,
                               game.btn_pengRect.width-20,
                               game.btn_pengRect.height,
                               game.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks=nama_tombol_pengaturan,
                               sudutRad=3,
                               onRelease=game.btn_pengaturan)

        # membuat tombol keluar

        game.btn_keluar = Tombol(layar,
                                 game.btn_keluarRect.x,
                                 game.btn_keluarRect.y,
                                 game.btn_pengRect.width-20,
                                 game.btn_pengRect.height,
                                 game.btn_font1,
                                 warnaTeks=warnaTeks,
                                 warnaAktif=wBA,
                                 warnaDitekan=wBP,
                                 warnaHover=wBH,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 teks=nama_tombol_keluar,
                                 sudutRad=3,
                                 onRelease=lambda: exit())

        game.bg1.fill(tema2['bg'])
        game.judul = game.title_font.render(
            judul, True, warnaTeks)
        # endregion

        # region Ular
        game.h_up = image.load(thp3/'kepala_up.png').convert_alpha()
        game.h_down = image.load(thp3/'kepala_down.png').convert_alpha()
        game.h_left = image.load(thp3/'kepala_left.png').convert_alpha()
        game.h_right = image.load(thp3/'kepala_right.png').convert_alpha()

        game.b_tr = image.load(thp3/'badan_tr.png').convert_alpha()
        game.b_tl = image.load(thp3/'badan_tl.png').convert_alpha()
        game.b_bl = image.load(thp3/'badan_bl.png').convert_alpha()
        game.b_br = image.load(thp3/'badan_br.png').convert_alpha()

        game.b_v = image.load(thp3/'badan_v.png').convert_alpha()
        game.b_h = image.load(thp3/'badan_h.png').convert_alpha()

        game.t_up = image.load(thp3/'ekor_up.png').convert_alpha()
        game.t_down = image.load(thp3/'ekor_down.png').convert_alpha()
        game.t_left = image.load(thp3/'ekor_left.png').convert_alpha()
        game.t_right = image.load(thp3/'ekor_right.png').convert_alpha()
        # endregion

        # region Play
        game.nths = 2
        game.warnaRumput = tema2['rm']
        game.pbg.fill(tema2['bg'])
        game.pskor.fill(tema2['skp'])
        game.border0.fill(tema2['brd'])
        game.border1.fill(tema2['brd'])
        game.border2.fill(tema2['brd'])
        game.border3.fill(tema2['brd'])

        game.btnHome = Tombol(layar,
                              game.btnHomeRect.x,
                              game.btnHomeRect.y,
                              game.btnHomeRect.width,
                              game.btnHomeRect.height,
                              game.btn_font1, 20,
                              nama_tombol_kembali_ke_menu_utama,
                              warnaTeks,
                              wBA, wBH, wBP, 20, 2,
                              onRelease=game.klikHome)

        game.btnReset = Tombol(layar,
                               game.btnResetRect.x,
                               game.btnResetRect.y,
                               game.btnResetRect.width,
                               game.btnResetRect.height,
                               game.btn_font1, 20,
                               nama_tombol_ulang_game,
                               warnaTeks,
                               wBA, wBH, wBP, 20, 2,
                               onRelease=game.klikReset)
        # endregion

        game.fr_makanan = [image.load(mkn/'sate_f0.png').convert_alpha(),
                           image.load(mkn/'sate_f1.png').convert_alpha(),
                           image.load(mkn/'sate_f2.png').convert_alpha(),
                           image.load(mkn/'sate_f2.png').convert_alpha(),
                           image.load(mkn/'sate_f1.png').convert_alpha(),
                           image.load(mkn/'sate_f0.png').convert_alpha()]

        game.makanan = image.load(mkn/'sate.png').convert_alpha()

        game.btn_keluar.hide()
        game.btn_play.hide()
        game.btn_peng.hide()
        game.btnHome.hide()
        game.btnReset.hide()
        pass

    def setTheme3(game):
        game.bg.fill(tema3['bg'])
        game.panel_1.fill(tema3['pn1'])
        warnaTeks = tema3['tk']
        wBA = tema3['btnA']
        wBH = tema3['btnH']
        wBP = tema3['btnP']
        game.wline = 3
        game.display_makananAktif = 3

        # region pengaturan
        # membuat tombol kembali
        game.btn_kembali = Tombol(game.bg,
                                  game.btn_kembaliRect.x,
                                  game.btn_kembaliRect.y,
                                  game.btn_kembaliRect.width,
                                  game.btn_kembaliRect.height,
                                  game.btn_font,
                                  20,
                                  nama_tombol_kembali,
                                  warnaAktif=wBA,
                                  warnaHover=wBH,
                                  warnaDitekan=wBP,
                                  warnaTeks=warnaTeks,
                                  shadowDistance=2,
                                  shadowColour=wBSh,
                                  sudutRad=3,
                                  onRelease=game.klikKembali)

        # membuat tombol tema bawaan
        game.btn_defaultT = Tombol(game.bg,
                                   game.btn_defaultRect.x,
                                   game.btn_defaultRect.y,
                                   game.btn_defaultRect.width,
                                   game.btn_defaultRect.height,
                                   game.btn_font, 20,
                                   nama_tombol_default,
                                   warnaAktif=wBA,
                                   warnaHover=wBH,
                                   warnaDitekan=wBP,
                                   warnaTeks=warnaTeks,
                                   shadowDistance=2,
                                   shadowColour=wBSh,
                                   sudutRad=3,
                                   onClick=game.setDefTheme)

        if game.btn_soundState == 'ON':
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_ON,
                                    warnaAktif=wBA,
                                    warnaHover=wBH,
                                    warnaDitekan=wBP,
                                    warnaTeks=warnaTeks,
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnON)
        if game.btn_soundState == 'OFF':
            game.btn_sound = Tombol(game.bg,
                                    game.btn_soundRect.x,
                                    game.btn_soundRect.y,
                                    game.btn_soundRect.width,
                                    game.btn_soundRect.height,
                                    game.btn_font, 20,
                                    nama_tombol_suara_OFF,
                                    warnaAktif=wBA,
                                    warnaHover=wBH,
                                    warnaDitekan=wBP,
                                    warnaTeks=warnaTeks,
                                    shadowDistance=2,
                                    shadowColour=wBSh,
                                    sudutRad=3,
                                    onRelease=game.klik_SoundbtnOFF)

        game.btn_theme1 = Tombol(game.bg,
                                 game.btn_theme1Rect.x,
                                 game.btn_theme1Rect.y,
                                 game.btn_theme1Rect.width,
                                 game.btn_theme1Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_1,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme1)

        # Tema ke 2
        game.btn_theme2 = Tombol(game.bg,
                                 game.btn_theme2Rect.x,
                                 game.btn_theme2Rect.y,
                                 game.btn_theme2Rect.width,
                                 game.btn_theme2Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_2,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme2)
        # Tema ke 3
        game.btn_theme3 = Tombol(game.bg,
                                 game.btn_theme3Rect.x,
                                 game.btn_theme3Rect.y,
                                 game.btn_theme3Rect.width,
                                 game.btn_theme3Rect.height,
                                 game.btn_font, 50,
                                 nama_tema_ke_3,
                                 warnaAktif=wBA,
                                 warnaHover=wBH,
                                 warnaDitekan=wBP,
                                 warnaTeks=warnaTeks,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 sudutRad=3,
                                 onClick=game.setTheme3)

        # game.teks1 = game.font_h2.render('Theme: Pastel', True, warnaTeks)
        game.teksH1 = game.font_h1.render(
            teks_di_pengaturan_h1, True, warnaTeks)
        # endregion

        # region menu utama
        game.btn_play = Tombol(layar,
                               game.btn_playRect.x,
                               game.btn_playRect.y,
                               game.btn_playRect.width-20,
                               game.btn_playRect.height,
                               game.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks=nama_tombol_main,
                               sudutRad=3,
                               onRelease=game.fbtn_play)

        # membuat tombol pengaturan
        game.btn_peng = Tombol(layar,
                               game.btn_pengRect.x,
                               game.btn_pengRect.y,
                               game.btn_pengRect.width-20,
                               game.btn_pengRect.height,
                               game.btn_font1,
                               warnaTeks=warnaTeks,
                               warnaAktif=wBA,
                               warnaDitekan=wBP,
                               warnaHover=wBH,
                               shadowDistance=2,
                               shadowColour=wBSh,
                               teks=nama_tombol_pengaturan,
                               sudutRad=3,
                               onRelease=game.btn_pengaturan)

        # membuat tombol keluar

        game.btn_keluar = Tombol(layar,
                                 game.btn_keluarRect.x,
                                 game.btn_keluarRect.y,
                                 game.btn_pengRect.width-20,
                                 game.btn_pengRect.height,
                                 game.btn_font1,
                                 warnaTeks=warnaTeks,
                                 warnaAktif=wBA,
                                 warnaDitekan=wBP,
                                 warnaHover=wBH,
                                 shadowDistance=2,
                                 shadowColour=wBSh,
                                 teks=nama_tombol_keluar,
                                 sudutRad=3,
                                 onRelease=lambda: exit())

        game.bg1.fill(tema3['bg'])
        game.judul = game.title_font.render(
            judul, True, warnaTeks)

        game.teksh2 = game.font_h2.render(
            teks_di_pengaturan_h2, True, tema3['tk'])
        game.teksh2_rect = game.teksh2.get_rect(topleft=(12*30+35, 0))
        game.teksh2_rect.y = 540-game.teksh2_rect.height-33
        # endregion

        # region Ular
        game.h_up = image.load(thp4/'kepala_up.png').convert_alpha()
        game.h_down = image.load(thp4/'kepala_down.png').convert_alpha()
        game.h_left = image.load(thp4/'kepala_left.png').convert_alpha()
        game.h_right = image.load(thp4/'kepala_right.png').convert_alpha()

        game.b_tr = image.load(thp4/'badan_tr.png').convert_alpha()
        game.b_tl = image.load(thp4/'badan_tl.png').convert_alpha()
        game.b_bl = image.load(thp4/'badan_bl.png').convert_alpha()
        game.b_br = image.load(thp4/'badan_br.png').convert_alpha()

        game.b_v = image.load(thp4/'badan_v.png').convert_alpha()
        game.b_h = image.load(thp4/'badan_h.png').convert_alpha()

        game.t_up = image.load(thp4/'ekor_up.png').convert_alpha()
        game.t_down = image.load(thp4/'ekor_down.png').convert_alpha()
        game.t_left = image.load(thp4/'ekor_left.png').convert_alpha()
        game.t_right = image.load(thp4/'ekor_right.png').convert_alpha()
        # endregion

        # region Play
        game.nths = 3
        game.warnaRumput = tema3['rm']
        game.pbg.fill(tema3['bg'])
        game.pskor.fill(tema3['skp'])
        game.border0.fill(tema3['brd'])
        game.border1.fill(tema3['brd'])
        game.border2.fill(tema3['brd'])
        game.border3.fill(tema3['brd'])

        game.btnHome = Tombol(layar,
                              game.btnHomeRect.x,
                              game.btnHomeRect.y,
                              game.btnHomeRect.width,
                              game.btnHomeRect.height,
                              game.btn_font1, 20,
                              nama_tombol_kembali_ke_menu_utama,
                              warnaTeks,
                              wBA, wBH, wBP, 20, 2,
                              onRelease=game.klikHome)

        game.btnReset = Tombol(layar,
                               game.btnResetRect.x,
                               game.btnResetRect.y,
                               game.btnResetRect.width,
                               game.btnResetRect.height,
                               game.btn_font1, 20,
                               nama_tombol_ulang_game,
                               warnaTeks,
                               wBA, wBH, wBP, 20, 2,
                               onRelease=game.klikReset)
        # endregion

        game.fr_makanan = [image.load(mkn/'jengkol_f0.png').convert_alpha(),
                           image.load(mkn/'jengkol_f1.png').convert_alpha(),
                           image.load(mkn/'jengkol_f2.png').convert_alpha(),
                           image.load(mkn/'jengkol_f2.png').convert_alpha(),
                           image.load(mkn/'jengkol_f1.png').convert_alpha(),
                           image.load(mkn/'jengkol_f0.png').convert_alpha()]

        game.makanan = image.load(mkn/'jengkol.png').convert_alpha()

        game.btn_keluar.hide()
        game.btn_play.hide()
        game.btn_peng.hide()
        game.btnHome.hide()
        game.btnReset.hide()

        pass

    # endregion


if __name__ == "__main__":
    m = GAME()
    looping = False

    def loading_frame():
        global waktu
        tampilan_loading = ProgressBar(layar, 0, 0,
                                       UKURAN_WINDOWS[0]-200, 75, lambda: 1 - (tm.time() - waktu_mulai) / 10)
        tampilan_loading.incompletedColour = rgb(53, 53, 53)
        tampilan_loading.setX(100)
        tampilan_loading.setY(
            int(UKURAN_WINDOWS[1]/2)-(tampilan_loading.getHeight()/2)+10)

        waktu = 1 - (tm.time() - waktu_mulai) / 10

        string_teks = 'Memuat'
        fr_teks = [m.font_h1.render(string_teks[0:2], True, tema0['btnA']),
                   m.font_h1.render(string_teks[2:4], True, tema1['btnA']),
                   m.font_h1.render(string_teks[4:6], True, tema2['btnA']),
                   m.font_h1.render(string_teks, True, tema3['btnA']),
                   m.font_h1.render(string_teks, True, rgb(150, 150, 150))]

        teks_koordinat = (
            UKURAN_WINDOWS[0]/2, int((UKURAN_WINDOWS[1]/2)-(tampilan_loading.getHeight()/2)-20))
        teks_rect = fr_teks[4].get_rect(center=teks_koordinat)

        # region frame - teks rect
        # kasih posisi tiap teks di dalam framenya
        f_teks_rect0 = fr_teks[0].get_rect(
            topleft=teks_rect.topleft)  # untuk posisi tuliasn "Lo"
        f_teks_rect1 = fr_teks[1].get_rect(
            midleft=f_teks_rect0.midright)  # untuk posisi tuliasn "ad"
        f_teks_rect2 = fr_teks[2].get_rect(
            midleft=f_teks_rect1.midright)  # untuk posisi tuliasn "in"
        # untuk posisi tuliasn "Loading"
        f_teks_rect3 = fr_teks[3].get_rect(midleft=f_teks_rect0.midleft)
        # endregion

        frame_teks_rect = [f_teks_rect0,
                           f_teks_rect1, f_teks_rect2, f_teks_rect3]
        fr_teks_dot = [m.font_h1.render('.', True, rgb(150, 150, 150)),
                       m.font_h1.render('..', True, rgb(150, 150, 150)),
                       m.font_h1.render('...', True, rgb(150, 150, 150)),
                       m.font_h1.render('....', True, rgb(150, 150, 150))]

        teks_dot_rect = fr_teks_dot[0].get_rect(midleft=teks_rect.midright)

        # region Variabel Index dari frame teks, teks_rect, dll.
        frame_index_teks = 0
        frame_index_teks_rect = 0
        frame_index_teks_dot = 0
        frame_index_loading_icColour = 0
        # endregion

        m.btn_play.hide()
        m.btn_peng.hide()
        m.btn_keluar.hide()
        m.btn_play.disable()
        m.btn_peng.disable()
        m.btn_keluar.disable()

        # loading
        while (tampilan_loading.percent != 0 and frame_index_loading_icColour != 4) or looping:
            ki = event.get()
            for ki in ki:
                if ki.type == QUIT:
                    quit()
                    exit()

            if frame_index_teks_rect >= len(frame_teks_rect):
                frame_index_teks_rect = 0
            if frame_index_teks >= len(fr_teks)-1:
                frame_index_teks = 0
            if frame_index_teks_dot >= len(fr_teks_dot):
                frame_index_teks_dot = 0
            if frame_index_loading_icColour >= len(frame_warna_loading):
                frame_index_loading_icColour = 0

            fr_teks_rect = frame_teks_rect[int(frame_index_teks_rect)]
            teks = fr_teks[int(frame_index_teks)]
            teks_dot = fr_teks_dot[int(frame_index_teks_dot)]
            tampilan_loading.completedColour = frame_warna_loading[int(
                frame_index_loading_icColour)]

            layar.fill(rgb(12, 12, 12))
            # layar.blits([(teks_dot, teks_dot_rect),
            #             (fr_teks[4], teks_rect), (teks, fr_teks_rect)])
            layar.blits([(teks_dot, teks_dot_rect), (fr_teks[4], teks_rect)])
            pw.update(ki)
            display.update()

            frame_index_teks_rect += KONST_ANI
            frame_index_teks += KONST_ANI
            frame_index_teks_dot += KONST_ANI
            frame_index_loading_icColour += KONST_ANI

        tampilan_loading.disable()
        tampilan_loading.hide()

        return 0

    loading_frame()
    m.btn_play.show()
    m.btn_peng.show()
    m.btn_keluar.show()
    m.btn_play.enable()
    m.btn_peng.enable()
    m.btn_keluar.enable()
    m.run()
