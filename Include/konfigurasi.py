# /------------------------------/
# / Pengaturan Untuk Game Cacing /
# / @copyright 2022              /
# /------------------------------/

from pathlib import Path
from typing import Callable

import pygame
from pygame_widgets.button import Button
from pygame_widgets.widget import WidgetBase


def rgb(*args, a: int = 255):
    """Fungsi Membuat Warna

    Args:
        r (int): Warna merah maksimal 255
        g (int): Warna hijau maksimal 255
        b (int): Warna biru maksimal 255
        a (int, optional): Tingkat transparannya warna dengan maksimal nilainya 255. Defaults to 255.

    Returns:
        Color: Menghasilkan warna
    """
    if len(args) == 3:
        return pygame.Color(args[0], args[1], args[2], a)
    elif len(args) == 1:
        return pygame.Color(args[0],args[0],args[0], a)


# Konstant
KONST_ANI = 0.015 # kecepatan animasi.
TMFB = 0.6

UKURAN_GAMBAR = 30  # Ukuran gambar (ular, makanan)
BANYAK_KOTAK = 23
UKURAN_WINDOWS = (UKURAN_GAMBAR*BANYAK_KOTAK, UKURAN_GAMBAR*BANYAK_KOTAK)

# Warna tema, model cacing, dll.
# frame rate
fps = pygame.time.Clock()
FPS = 30
# bg=backgroun, pn1=Panel 1,
# tk=Teks, btn[A,H,P,Sh]=Tombol[aktif,pointerdiarahkan,ditekan,bayangan]
LOKASI_FONT_UNTUK_TULISAN = Path('./res/font')
LOKASI_CACING_TEMA_KE_1 = Path('./res/image/ular/tema0')
LOKASI_CACING_TEMA_KE_2 = Path('./res/image/ular/tema1')
LOKASI_CACING_TEMA_KE_3 = Path('./res/image/ular/tema2')
LOKASI_CACING_TEMA_KE_4 = Path('./res/image/ular/tema3')
LOKASI_SUARA = Path('./res/music')
LOKASI_GAMBAR_DAN_LAIN2 = Path('./res/image/misc')

LOKASI_MAKANAN = Path('./res/image/makanan/')

# Kecepatan Ular
KECEPATAN_CACING_BERGERAK = 160  # bergerak setiap x milisekon

# Penamaan dan Warna Tema
JUDUL_PADA_WINDOWS = 'Game Cacing | Kelompok 1'
judul = 'Game Cacing'
teks_di_pengaturan_h1 = "Pengaturan - Tema"
teks_di_pengaturan_h2 = 'Cacing dan Makanan'
nama_tombol_main = "Main"
nama_tombol_pengaturan = 'Pengaturan'
nama_tombol_keluar = 'Keluar'
nama_tombol_kembali_ke_menu_utama = 'Kembali'
nama_tombol_kembali = 'Kembali'
nama_tombol_ulang_game = 'Ulang'
nama_tombol_suara_ON = 'Suara ON'
nama_tombol_suara_OFF = 'Suara OFF'

# region Warna Tema
# cacing hutan
nama_tema_ke_0 = 'Cacing Hutan'
nama_tombol_default = nama_tema_ke_0
tema0 = {
    'bg': rgb(12, 46, 68),
    'pn1': rgb(19, 76, 76),
    'tk': rgb(249, 230, 207),
    'btnA': rgb(51, 152, 75),
    'btnH': rgb(46, 138, 67),
    'btnP': rgb(40, 113, 57),
    'btnSh': rgb(0,0,0),
    'wl': rgb(90, 197, 79),
    'skp': rgb(19, 76, 76),
    'brd': rgb(22, 85, 85),
    'rm': rgb(13, 49, 74)
}
# cacing tanah
nama_tema_ke_1 = 'Cacing Tanah'
tema1 = {
    'bg': rgb(246, 170, 30),
    'pn1': rgb(186, 55, 8),
    'tk': rgb(35, 9, 1),
    'btnA': rgb(146, 28, 12),
    'btnH': rgb(135, 27, 13),
    'btnP': rgb(120, 21, 8),
    'btnSh': rgb(0,0,0),
    'wl': rgb(99, 23, 8),
    'skp': rgb(186, 55, 8),
    'brd': rgb(194, 59, 10),
    'rm': rgb(243, 164, 18)
}
nama_tema_ke_2 = 'Cacing Kutub'
tema2 = {
    'bg': rgb(25, 132, 159),
    'pn1': rgb(75, 91, 104),
    'tk': rgb(219, 219, 220),
    'btnA': rgb(75, 91, 104),
    'btnH': rgb(67, 80, 91),
    'btnP': rgb(57, 67, 76),
    'btnSh': rgb(0,0,0),
    'wl': rgb(197, 195, 198),
    'skp': rgb(65, 76, 89),
    'brd': rgb(75, 91, 104),
    'rm': rgb(20, 127, 156)
}
nama_tema_ke_3 = 'Cacing Emas'
tema3 = {
    'bg': rgb(255, 255, 255),
    'pn1': rgb(205, 205, 205),
    'tk': rgb(20, 33, 62),
    'btnA': rgb(230, 230, 230),
    'btnH': rgb(200, 200, 200),
    'btnP': rgb(185,185,185),
    'btnSh': rgb(0,0,0),
    'wl': rgb(253, 163, 18),
    'brd': rgb(220,220,220),
    'skp': rgb(205, 205, 205),
    'rm': rgb(230, 230, 230)
}

frame_warna_loading = [tema0['btnA'], tema1['btnA'], tema2['btnA'], tema3['btnA']]
# endregion

# region Default
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
           warnaTeks: tuple = rgb(0, 0, 0),
           warnaAktif: tuple = rgb(50, 50, 50),
           warnaHover: tuple = rgb(100, 100, 100),
           warnaDitekan: tuple = rgb(25, 25, 25),
           margin: int = 20,
           sudutRad: int = 0,
           shadowDistance: int = 1,
           shadowColour: tuple = rgb(0,0,0),
           onClick=lambda: None,
           onRelease=lambda: print(True, 1)):

    return Button(win, x_pos, y_pos, lebar, tinggi, text=teks, fontSize=fontSize, margin=margin,
                  inactiveColour=warnaAktif, hoverColour=warnaHover, pressedColour=warnaDitekan,
                  radius=sudutRad, onClick=onClick, textColour=warnaTeks, shadowDistance=shadowDistance,
                  shadowColour=shadowColour, font=font, onRelease=onRelease)


class ProgressBar(WidgetBase):
    def __init__(self, win, x, y, width, height, progress: Callable[[], float], **kwargs):
        super().__init__(win, x, y, width, height)
        self.progress = progress

        self.curved = kwargs.get('curved', False)

        self.completedColour = kwargs.get('completedColour', (0, 200, 0))
        self.incompletedColour = kwargs.get(
            'incompletedColour', (100, 100, 100))

        self.percent = self.progress()

        self.radius = self._height / 2 if self.curved else 0

        self.disable()

    def listen(self, events):
        pass

    def draw(self):
        """ Display to surface """
        self.percent = min(max(self.progress(), 0), 1)

        if not self._hidden:
            pygame.draw.rect(self.win, self.incompletedColour,
                             ((self._x, self._y, self._width, self._height)), border_radius=2)
            pygame.draw.rect(self.win, self.completedColour,
                             (self._x, self._y,
                              int(self._width * (1 - self.percent)), self._height), border_radius=2)


if __name__ == "__main__":
    print(len(frame_warna_loading))
