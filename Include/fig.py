# Friday, April - 15 - 2022 (15/4/22) [11:42:27,306 AM]  /  GMT+0700 || 15

# /------------------------------/
# / Pengaturan Untuk Game Cacing /
# / @copyright 2022              /
# /------------------------------/

from pygame_widgets.button import Button
from pathlib import Path
import pygame
from typing import Callable
import pygame
from pygame_widgets.widget import WidgetBase


def rgb(r: int, g: int, b: int, a: int = 255):
    """Fungsi Membuat Warna

    Args:
        r (int): Warna merah
        g (int): Warna hijau
        b (int): Warna biru
        a (int, optional): Tingkat transparannya warna dengan maksimal nilainya 225. Defaults to 255.

    Returns:
        Color: Menghasilkan warna
    """
    return pygame.Color(r, g, b, a)


# Konstant
KONST_ANI = 0.015

UKURAN_GAMBAR = 30  # Ukuran gambar (ular, makanan)
BANYAK_KOTAK = 23
UKURAN_WINDOWS = (UKURAN_GAMBAR*BANYAK_KOTAK, UKURAN_GAMBAR*BANYAK_KOTAK)

# Theme Colour, Skin, etc.
# frame rate
fps = pygame.time.Clock()
FPS = 60
# bg=backgroun, pn1=Panel 1,
# tk=Teks, btn[A,H,P,Sh]=Tombol[aktif,pointerdiarahkan,ditekan,bayangan]
LOKASI_FONT_UNTUK_TULISAN = Path('./res/font')
LOKASI_ULAR_TEMA_KE_1 = Path('./res/image/ular/tema0')
LOKASI_ULAR_TEMA_KE_2 = Path('./res/image/ular/tema1')
LOKASI_ULAR_TEMA_KE_3 = Path('./res/image/ular/tema2')
LOKASI_ULAR_TEMA_KE_4 = Path('./res/image/ular/tema3')
LOKASI_SUARA = Path('./res/music')
LOKASI_GAMBAR_DAN_LAIN2 = Path('./res/image/misc')

LOKASI_MAKANAN = Path('./res/image/makanan/')

# Kecepatan Ular
KECEPATAN_ULAR_BERGERAK = 160  # milisec

# Penamaan dan Warna Tema
JUDUL_PADA_WINDOWS = 'Game Cacing | Kelompok 1'
judul = 'Game Cacing'
teks_di_pengaturan_h1 = "Pengaturan | Tema"
nama_tombol_main = "Main"
nama_tombol_pengaturan = 'Pengaturan'
nama_tombol_keluar = 'Keluar'
nama_tombol_kembali_ke_menu_utama = 'Kembali'
nama_tombol_kembali = 'Kembali'
nama_tombol_ulang_game = 'Ulang'
nama_tombol_default = 'Default'
# region Warna Tema / Warna - Warna
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
nama_tema_ke_1 = 'Cacing Tanah'
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
nama_tema_ke_2 = 'Cacing Kutub'
tema2 = {
    'bg': rgb(252, 252, 252),
    'pn1': rgb(139, 202, 221),
    'tk': rgb(44, 74, 120),
    'btnA': rgb(167, 188, 201),
    'btnH': rgb(214, 225, 233),
    'btnP': rgb(115, 141, 157),
    'btnSh': rgb(32, 40, 78),
    'wl': rgb(115, 141, 157),
    'skp': rgb(110, 188, 212),
    'brd': rgb(130, 196, 217),
    'rm': rgb(242, 242, 242)
}
nama_tema_ke_3 = 'Cacing Emas'
tema3 = {
    'bg': rgb(150, 206, 180),
    'pn1': rgb(255, 238, 173),
    'tk': rgb(217, 83, 79),
    'btnA': rgb(255, 173, 96),
    'btnH': rgb(254, 187, 123),
    'btnP': rgb(255, 150, 51),
    'btnSh': rgb(49, 94, 73),
    'wl': rgb(205, 65, 84),
    'skp': rgb(255, 233, 143),
    'brd': rgb(255, 225, 107),
    'rm': rgb(157, 210, 185)
}

frame_warna_loading = [tema0['btnA'],
                       tema1['btnA'], tema2['btnA'], tema3['btnA']]
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
           warnaTeks: tuple = (0, 0, 0),
           warnaAktif: tuple = (50, 50, 50),
           warnaHover: tuple = (100, 100, 100),
           warnaDitekan: tuple = (25, 25, 25),
           margin: int = 20,
           sudutRad: int = 0,
           shadowDistance: int = 0,
           shadowColour: tuple = (210, 210, 180),
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
