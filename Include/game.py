# Add background image and music
# region IMPORT
from pygame.font import Font
import sys
from asyncio import events
import pygame
from pygame.locals import *
import time
import random
from pathlib import Path
from rich.table import Table
from rich.console import Console
from os import system
from sys import exit
# from _tema1 import *

# endregion

# region VAR
SIZE = 40
# BACKGROUND_COLOR = (110, 110, 5)
LAYAR = (1000, 680)
PATH = Path("./res/image")
PATH_IKON = Path("./res/ikon")
PATH_MUSIC = Path("./res/music")
SKIN = {
    'Original': 'block.jpg',
    'Elit': 'block_elit.jpeg',
    'Epic': 'block_epic.jpeg',
    'Spesial': 'block_spesial.jpeg',
    'Putih': 'block_putih.jpg',
    'Gradiasi 1': 'block_gradiasi1.jpg',

    # Tema ke 1
    'Theme 1': 'ular_tema1.jpg'
}
MAKANAN = {
    'Jengkol': 'jengkol.jpg',
    'Cabe': "cabe.jpg",
    'Pete': "pete.jpg",

    'Theme 1': 'food_tema1.jpg'
}
BG_IMAGE = {
    "Hijau": "background.jpg",

    # Tema ke 1
    "Theme 1": "bg_tema1.jpg"
}
IKON = pygame.image.load(PATH_IKON/"ikon.png")
konsol = Console()
bg_game = None
get_skin = None
get_food = None
# endregion


def cls(): return system("@cls")
def stop(): return system("@pause")
def keluar(): return system("@exit")


def default():
    global fd_image, def_food, sk_image, def_skin, bg_game, TBL_BORDER, TBL_HEADER, TBL_COLUMN
    global get_food, get_skin

    # default
    TBL_BORDER = "#c19a00"
    TBL_HEADER = "#13a10d"
    TBL_COLUMN = "#fafafa"
    fd_image = PATH / MAKANAN["Jengkol"]
    sk_image = PATH / SKIN["Original"]
    bg_game = PATH / BG_IMAGE["Hijau"]
    def_food = "Jengkol"
    def_skin = "Original"
    get_food = "Jengkol"
    get_skin = "Original"


def pengaturan():
    global fd_image, sk_image, get_food, get_skin

    cls()
    tabel = Table(title="Launcher Untuk Snake Game",
                  header_style=TBL_HEADER,
                  border_style=TBL_BORDER,
                  title_justify="center")
    tabel.add_column("Pengaturan Skin, Makanan, dan Tema", style=TBL_COLUMN)
    tabel.add_row("1. Pengaturan Makanan")
    tabel.add_row("2. Pengaturan Skin")
    tabel.add_row("3. Pengaturan Tema")
    tabel.add_row("4. Kembali")
    konsol.print(tabel, justify="center")
    konsol.print("\nTekan nomor di atas untuk melanjutkan: (1,2,...,4)")
    pilih = str(input(">> "))

    if pilih == "1":
        def set_makanan():
            cls()
            global fd_image, get_food, get_skin
            fd_image = str(
                input("Masukan Makanan (Cabe, Jengkol, Pete):\n>> "))
            get_food = fd_image
            if fd_image == "jengkol" or fd_image == 'Jengkol' or fd_image == '':
                fd_image = PATH / MAKANAN["Jengkol"]
            elif fd_image == "cabe" or fd_image == "Cabe":
                fd_image = PATH / MAKANAN["Cabe"]
            elif fd_image == "pete" or fd_image == "Pete":
                fd_image = PATH / MAKANAN["Pete"]
            else:
                print(
                    f'Makanan Hanya Terdiri Dari:\n\tCabe\n\tJengkol\n\tPete!\n>> {fd_image} Tidak dikenal!')
                stop()
                pengaturan()
            if get_skin == '':
                get_skin = 'Original'
            if get_food == '':
                get_food = 'Jengkol'
            pengaturan()
        set_makanan()

    elif pilih == '2':
        def set_skin():
            cls()
            global sk_image, get_skin, get_food
            sk_image = str(input(
                "Masukan Skin Ular (Original, Elit, Epic, Spesial): (Tinggalkan Kosong Untuk Skin Original)\n>> "))
            get_skin = sk_image
            if sk_image == "elit" or sk_image == 'Elit':
                sk_image = PATH / SKIN['Elit']
            elif sk_image == "epic" or sk_image == 'Epic':
                sk_image = PATH / SKIN["Epic"]
            elif sk_image == "spesial" or sk_image == 'Spesial':
                sk_image = PATH / SKIN['Spesial']
            elif sk_image == '' or sk_image == 'original' or sk_image == 'Original':
                sk_image = PATH / SKIN["Original"]
            elif sk_image == 'putih' or sk_image == 'Putih':
                sk_image = PATH / SKIN["Putih"]
            else:
                print(f'\n>> {sk_image} Tidak dikenal!')
                stop()
                pengaturan()

            if get_skin == '':
                get_skin = 'Original'
            if get_food == '':
                get_food = 'Jengkol'
            pengaturan()
        set_skin()
    elif pilih == '3':
        cls()
        tabel = None

        def set_tema():
            global get_skin, get_food
            global bg_game, TBL_HEADER, TBL_BORDER, TBL_COLUMN, sk_image, fd_image, BG_IMAGE
            tabel = Table("Pengaturan Tema", border_style=TBL_BORDER)
            tabel.add_column('Pilih Tema')
            tabel.add_row('1. Default', style='white')
            tabel.add_row('2. Candy', style='magenta')
            tabel.add_row('3. Kembali')
            konsol.print(tabel, justify='center')
            konsol.print('Pilih Tema Dengan Memasukan Angka (1, ..., 3):')
            plh_tma = str(input('>> '))
            if plh_tma == '2':
                TBL_HEADER = "#c19a00"
                TBL_COLUMN = "#b4009f"
                TBL_BORDER = "#3a96de"
                bg_game = PATH / BG_IMAGE["Theme 1"]
                sk_image = PATH / SKIN["Theme 1"]
                fd_image = PATH / MAKANAN["Theme 1"]
                get_food, get_skin = "Tema 1", "Tema 1"
                main()
            if plh_tma == '2':
                default()
                main()

        set_tema()
    elif pilih == '4':
        if get_food == None and get_skin == None:
            get_food = def_food
            get_skin = def_skin
        get_food = get_food.capitalize()
        get_skin = get_skin.capitalize()
        main()


def about():
    cls()
    teks = """
Cara Bermain
------------

[blue][W] = Mengarah ke Atas[/blue]
[red][A] = Mengarah ke Kiri[/red]
[yellow][D] = Mengarah ke Kanan[/yellow]
[magenta][S] = Mengarah ke Bawah[/magenta]

Tujuan: Mengambil makanan agar skor bertambah.

Tentang
-------
Game ini dibuat oleh kelompok 4, game ini sangat sederhana yaitu ular mengambil
makanan. game ini  melatih ke fokusan  dalam bermain karena  jika  salah  dalam
bermain.

Dibuat oleh:
- Maulana Ibrahim           - Rafli Aulia Pranoto
- Muhammad Azis Abdillah    - Fathul Karomah Diarsah
- Muhammad Sutrino.
"""
    konsol.print(teks, style="yellow")
    stop()


def main():
    global fd_image, get_food  # Variabel Tampilan Makanan di globalkan
    global sk_image, get_skin  # Variabel Tampilan Skin di globalkan
    global pilih, TBL_BORDER, TBL_HEADER, TBL_COLUMN

    # Main Menu
    cls()
    tabel = Table(title="Launcher Untuk Snake Game",
                  header_style=TBL_HEADER,
                  border_style=TBL_BORDER,
                  title_justify="full")
    tabel.add_column("Snake Game 1.0.0", style=TBL_COLUMN)
    tabel.add_row("1. Mulai")
    tabel.add_row("2. Tentang")
    tabel.add_row("3. Pengaturan")
    tabel.add_row("4. Keluar")
    konsol.print(tabel, justify="center")
    if get_food == None and get_skin == None:
        konsol.print(
            f"[Skin]: {def_skin}, [Makanan]: {def_food}", justify='center', style="yellow")
    else:
        konsol.print(
            f"[Skin]: {get_skin}, [Makanan]: {get_food}", justify='center', style="yellow")
    konsol.print("\nTekan nomor di atas untuk melanjutkan: (1,2,...,4)")
    pilih = str(input(">> "))
    if pilih == '1':
        cls()
        konsol.print("Game Bekerja....")
        Game().run()
    elif pilih == '2':
        about()
    elif pilih == '3':
        pengaturan()
        pass
    elif pilih == '4':
        pilih = '4'
    else:
        pilih = None
        konsol.print(f'Masukan {pilih} tidak dikenal!\nCoba lagi!')
        stop()
        main()


class Makanan:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(
            fd_image).convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24)*SIZE
        self.y = random.randint(1, 16)*SIZE


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(sk_image).convert()
        self.direction = 'down'

        self.length = 5
        self.x = [40, 40, 40, 40, 40]
        self.y = [40, 40, 40, 40, 40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game: Kelompok 1")
        pygame.display.set_icon(IKON)

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode(LAYAR)
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.makanan = Makanan(self.surface)
        self.makanan.draw()

    def play_background_music(self):
        pygame.mixer.music.load(PATH_MUSIC / 'bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound(PATH_MUSIC / "crash.mp3")
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound(PATH_MUSIC / "ding.mp3")

        pygame.mixer.Sound.play(sound)
        # pygame.mixer.music.stop()

    def reset(self):
        self.snake = Snake(self.surface)
        self.makanan = Makanan(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        global bg_game
        bg = pygame.image.load(bg_game)
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.makanan.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating makanan scenario
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.makanan.x, self.makanan.y):
                self.play_sound("ding")
                self.snake.increase_length()
                self.makanan.move()

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise "Collision Occurred"

        # snake colliding with the boundries of the window
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 680):
            self.play_sound('crash')
            raise "Hit the boundry error"
        if not (0 <= self.snake.x[0] <= 1000-SIZE and 0 <= self.snake.y[0] <= 680-SIZE):
            self.play_sound('crash')
            raise "Hit the boundry error"

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(
            f"Skor: {self.snake.length-4}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self):
        self.bg = pygame.image.load(bg_game)
        self.surface.blit(self.bg, (0, 0))
        font = pygame.font.SysFont('arial', 25)
        line1 = font.render(
            f"Game over! Skor Anda {(self.snake.length-4)}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 240))
        line2 = font.render(
            "Untuk Memulai Ulang Tekan [ENTER].", True, (255, 255, 255))
        line3 = font.render(
            "Untuk Kembali ke Menu Tekan [Escape]!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 280))
        self.surface.blit(line3, (200, 280+25))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN or event.key == K_SPACE:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT or event.key == K_a:
                            self.snake.move_left()

                        elif event.key == K_RIGHT or event.key == K_d:
                            self.snake.move_right()

                        elif event.key == K_UP or event.key == K_w:
                            self.snake.move_up()

                        elif event.key == K_DOWN or event.key == K_s:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)


if __name__ == '__main__':
    # stop()
    cls()
    default()
    while True:
        main()
        if pilih == '4':
            break
