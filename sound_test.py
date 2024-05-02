import pyxel

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100

class Button:
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.clicked = False
    
    def click(self):
        self.clicked = not self.clicked

        if self.clicked:
            pyxel.playm(0, loop=True)
        else:
            pyxel.stop()

class Game:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="sound test", fps=30)
        pyxel.mouse(visible=True)
        self.init_music()
        self.play_button = Button(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 10, 10)
        pyxel.run(self.update, self.draw)

    def init_music(self):
        pyxel.sounds[0].set(
            "d2d2d3ra2rrg#2 rg2rf2rd2f2g2 c2c2d3ra2rrg#2 rg2rf2rd2f2g2",
            "s",
            "4",
            "vvvvvvvv",
            20
        )

        pyxel.sounds[1].set(
            "b1b1d3ra2rrg#2 rg2rf2rd2f2g2 a#1a#1d3ra2rrg#2 rg2rf2rd2f2g2",
            "s",
            "4",
            "vvvvvvvv",
            20
        )

        pyxel.sounds[2].set(
            "a1ra1ra1a1ra1 ra1ra1a1ra1r g1rg1rg1g1rg1 rg1rg1g1rg1r",
            "s",
            "2",
            "vvvvvvvv",
            20
        )

        pyxel.sounds[3].set(
            "d1rd1rd1d1rd1 rd1rd1d1rd1r c1rc1rc1c1rc1 rc1rc1c1rc1r",
            "s",
            "2",
            "vvvvvvvv",
            20
        )

        pyxel.sounds[4].set(
            "g1rg1rg1g1rg1 rg1rg1g1rg1r f1rf1rf1f1rg1 rg1rg1g1rg1r",
            "s",
            "2",
            "vvvvvvvv",
            20
        )

        pyxel.sounds[5].set(
            "b0rb0rb0b0rb0 rb0rb0b0rb0r a#0ra#0ra#0a#0rc1 rc1rc1c1rc1r",
            "s",
            "2",
            "vvvvvvvv",
            20
        )

        pyxel.sounds[63].set(
            "rrrrrrrr rrrrrrrr rrrrrrrr rrrrrrrr",
            "s",
            "2",
            "vvvvvvvv",
            20
        )

        pyxel.musics[0].set(
            [0, 1, 0, 1],
            [63, 63, 2, 4],
            [63, 63, 3, 5]
        )

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            b = self.play_button
            if (b.x <= pyxel.mouse_x < b.x+b.w) and (b.y <= pyxel.mouse_y < b.y+b.h):
                b.click()

    def draw(self):
        pyxel.cls(0)

        c = pyxel.COLOR_RED
        if (self.play_button.clicked):
            c = pyxel.COLOR_DARK_BLUE

        pyxel.rect(self.play_button.x, self.play_button.y, self.play_button.w, self.play_button.h, col=c)
    

Game()