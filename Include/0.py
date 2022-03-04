mUtama = MENU_UTAMA()

# membuat layar / tampilan menu pengaturan


class ULAR:
    def __init__(self) -> None:
        self.badan = [Vector2(5, 10), Vector2(
            4, 10), Vector2(3, 10), Vector2(2, 10)]
        self.arah = Vector2(0, 0)
        self.newblok = False

        self.h_up = image.load('./res/image/ular/kepala_up.png')
        self.h_down = image.load('./res/image/ular/kepala_down.png')
        self.h_right = image.load('./res/image/ular/kepala_right.png')
        self.h_left = image.load('./res/image/ular/kepala_left.png')

        self.t_up = image.load('./res/image/ular/ekor_up.png')
        self.t_down = image.load('./res/image/ular/ekor_down.png')
        self.t_right = image.load('./res/image/ular/ekor_right.png')
        self.t_left = image.load('./res/image/ular/ekor_left.png')

        self.b_v = image.load('./res/image/ular/badan_v.png')
        self.b_h = image.load('./res/image/ular/badan_h.png')

        self.b_ur = image.load('./res/image/ular/badan_ur.png')
        self.b_ul = image.load('./res/image/ular/badan_ul.png')
        self.b_br = image.load('./res/image/ular/badan_br.png')
        self.b_bl = image.load('./res/image/ular/badan_bl.png')

        pass

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
                        layar.blit(self.b_ul, ular_rect)
                    if blok_sebelum.x == -1 and blok_selanjutnya.y == 1 \
                            or blok_sebelum.y == 1 and blok_selanjutnya.x == -1:
                        layar.blit(self.b_bl, ular_rect)
                    if blok_sebelum.x == 1 and blok_selanjutnya.y == -1 \
                            or blok_sebelum.y == -1 and blok_selanjutnya.x == 1:
                        layar.blit(self.b_ur, ular_rect)
                    if blok_sebelum.x == 1 and blok_selanjutnya.y == 1 \
                            or blok_sebelum.y == 1 and blok_selanjutnya.x == 1:
                        layar.blit(self.b_br, ular_rect)

    # fungsi update gambar kepalanya
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
    # fungsi update gambar buntutnya

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
        self.bg.fill(bg)

        # top panel
        self.panel_1 = Surface((WIN_SIZE[0], 100))
        self.panel_1Rect = self.panel_1.get_rect(topleft=(0, 0))
        self.panel_1.fill(pn1)

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

        pass

    def klikKembali(self):
        self.aktif = False
        mUtama.aktif = True
        mUtama.run()

    def setDefTheme(self):
        global warnaTeks
        self.bg.fill(tema0['bg'])
        self.panel_1.fill(tema0['pn1'])
        warnaTeks = tema0['tk']

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

        mUtama.bg.fill(tema0['bg'])
        mUtama.btn_play.inactiveColour = tema0['btnA']
        mUtama.btn_play.hoverColour = tema0['btnH']
        mUtama.btn_play.pressedColour = tema0['btnP']
        mUtama.btn_play.textColour = warnaTeks
        mUtama.btn_keluar.inactiveColour = tema0['btnA']
        mUtama.btn_keluar.hoverColour = tema0['btnH']
        mUtama.btn_keluar.pressedColour = tema0['btnP']
        mUtama.btn_keluar.textColour = warnaTeks
        mUtama.btn_peng.inactiveColour = tema0['btnA']
        mUtama.btn_peng.hoverColour = tema0['btnH']
        mUtama.btn_peng.pressedColour = tema0['btnP']
        mUtama.btn_peng.textColour = warnaTeks
        mUtama.btn_keluar.inactiveColour = tema0['btnA']
        mUtama.btn_keluar.hoverColour = tema0['btnH']
        mUtama.btn_keluar.pressedColour = tema0['btnP']
        mUtama.btn_keluar.textColour = warnaTeks
        mUtama.judul = mUtama.title_font.render(
            judul, True, warnaTeks)
        pass

    def setTheme1(self):
        global warnaTeks
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

        mUtama.bg.fill(tema1['bg'])
        mUtama.btn_play.inactiveColour = tema1['btnA']
        mUtama.btn_play.hoverColour = tema1['btnH']
        mUtama.btn_play.pressedColour = tema1['btnP']
        mUtama.btn_play.textColour = warnaTeks
        mUtama.btn_keluar.inactiveColour = tema1['btnA']
        mUtama.btn_keluar.hoverColour = tema1['btnH']
        mUtama.btn_keluar.pressedColour = tema1['btnP']
        mUtama.btn_keluar.textColour = warnaTeks
        mUtama.btn_peng.inactiveColour = tema1['btnA']
        mUtama.btn_peng.hoverColour = tema1['btnH']
        mUtama.btn_peng.pressedColour = tema1['btnP']
        mUtama.btn_peng.textColour = warnaTeks
        mUtama.btn_keluar.inactiveColour = tema1['btnA']
        mUtama.btn_keluar.hoverColour = tema1['btnH']
        mUtama.btn_keluar.pressedColour = tema1['btnP']
        mUtama.btn_keluar.textColour = warnaTeks
        mUtama.judul = mUtama.title_font.render(
            judul, True, warnaTeks)
        pass

    def setTheme2(self):
        global warnaTeks
        self.bg.fill(tema2['bg'])
        self.panel_1.fill(tema2['pn1'])
        warnaTeks = tema2['tk']

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

        mUtama.bg.fill(tema2['bg'])
        mUtama.btn_play.inactiveColour = tema2['btnA']
        mUtama.btn_play.hoverColour = tema2['btnH']
        mUtama.btn_play.pressedColour = tema2['btnP']
        mUtama.btn_play.textColour = warnaTeks
        mUtama.btn_keluar.inactiveColour = tema2['btnA']
        mUtama.btn_keluar.hoverColour = tema2['btnH']
        mUtama.btn_keluar.pressedColour = tema2['btnP']
        mUtama.btn_keluar.textColour = warnaTeks
        mUtama.btn_peng.inactiveColour = tema2['btnA']
        mUtama.btn_peng.hoverColour = tema2['btnH']
        mUtama.btn_peng.pressedColour = tema2['btnP']
        mUtama.btn_peng.textColour = warnaTeks
        mUtama.btn_keluar.inactiveColour = tema2['btnA']
        mUtama.btn_keluar.hoverColour = tema2['btnH']
        mUtama.btn_keluar.pressedColour = tema2['btnP']
        mUtama.btn_keluar.textColour = warnaTeks
        self.judul_rect = mUtama.judul_rect
        mUtama.judul = mUtama.title_font.render(
            judul, True, warnaTeks)

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

        mUtama.bg.fill(tema3['bg'])
        mUtama.btn_play.inactiveColour = tema3['btnA']
        mUtama.btn_play.hoverColour = tema3['btnH']
        mUtama.btn_play.pressedColour = tema3['btnP']
        mUtama.btn_play.textColour = warnaTeks
        mUtama.btn_keluar.inactiveColour = tema3['btnA']
        mUtama.btn_keluar.hoverColour = tema3['btnH']
        mUtama.btn_keluar.pressedColour = tema3['btnP']
        mUtama.btn_keluar.textColour = warnaTeks
        mUtama.btn_peng.inactiveColour = tema3['btnA']
        mUtama.btn_peng.hoverColour = tema3['btnH']
        mUtama.btn_peng.pressedColour = tema3['btnP']
        mUtama.btn_peng.textColour = warnaTeks
        mUtama.btn_keluar.inactiveColour = tema3['btnA']
        mUtama.btn_keluar.hoverColour = tema3['btnH']
        mUtama.btn_keluar.pressedColour = tema3['btnP']
        mUtama.btn_keluar.textColour = warnaTeks
        self.judul_rect = mUtama.judul_rect
        mUtama.judul = mUtama.title_font.render(
            judul, True, warnaTeks)

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
