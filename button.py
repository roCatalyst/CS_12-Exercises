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
        self.clicked = True

class Game:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="button test", fps=30)
        pyxel.mouse(visible=True)
        self.buttons = [
            Button(10,10,30,30),
            Button(50,10,30,30),
            Button(10,50,30,30),
            Button(50,50,30,30),
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            for btn in self.buttons:
                if (btn.x <= pyxel.mouse_x < btn.x + btn.w) and (btn.y <= pyxel.mouse_y < btn.y + btn.h):
                    btn.click()
                    

    def draw(self):
        pyxel.cls(0)

        for btn in self.buttons:
            if btn.clicked:
                pyxel.rect(btn.x, btn.y, btn.w, btn.h, pyxel.COLOR_RED)
            elif (btn.x <= pyxel.mouse_x < btn.x + btn.w) and (btn.y <= pyxel.mouse_y < btn.y + btn.h):
                pyxel.rect(btn.x, btn.y, btn.w, btn.h, pyxel.COLOR_DARK_BLUE)
            else:
                pyxel.rect(btn.x, btn.y, btn.w, btn.h, pyxel.COLOR_LIGHT_BLUE)
    

Game()