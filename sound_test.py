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
        pyxel.load("MEGALOVANIA.pyxres")
        self.play_button = Button(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 10, 10)
        pyxel.run(self.update, self.draw)
      

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