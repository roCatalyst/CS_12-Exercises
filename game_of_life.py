import pyxel

SCREEN_WIDTH, SCREEN_HEIGHT = 100, 100

class Cell():
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.alive = False

    def set_state(self, state: bool):
        self.alive = state

class Game():
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Conway's Game of Life", fps=60)

        self.instructions_h = 20

        #initialize grid
        self.cell_w, self.cell_h = 2, 2
        self.Grid: list[list[Cell]] = [[Cell(i, j, self.cell_w, self.cell_h) for j in range(self.instructions_h, SCREEN_HEIGHT, self.cell_w)] for i in range(0, SCREEN_WIDTH, self.cell_h)]
        self.pause = True

        pyxel.mouse(visible=True)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_P):
            self.pause = not self.pause

        if pyxel.btnp(pyxel.KEY_C):
            for row in self.Grid:
                for cell in row:
                    cell.set_state(False)

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            for row in self.Grid:
                for cell in row:
                    if (cell.x <= pyxel.mouse_x < cell.x+cell.w) and (cell.y <= pyxel.mouse_y < cell.y+cell.h):
                        cell.set_state(not cell.alive)

        if (not self.pause) and (pyxel.frame_count%30==0):
            grid_h = len(self.Grid)
            grid_w = len(self.Grid[0])

            n_state = [[self.Grid[i][j].alive for j in range(grid_w)] for i in range(grid_h)]
            for i in range(grid_h):
                for j in range(grid_w):
                    cnt = 0
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if (di,dj) == (0,0): continue
                            if (self.Grid[(i+di)%grid_h][(j+dj)%grid_w].alive == True):
                                cnt += 1

                    if (self.Grid[i][j].alive):
                        if (2<=cnt<=3):
                            n_state[i][j] = True
                        else:
                            n_state[i][j] = False
                    elif (not self.Grid[i][j].alive) and (cnt == 3):
                        n_state[i][j] = True


            for i in range(grid_h):
                for j in range(grid_w):
                    #print(f"({i},{j}) is now {n_state[i][j]}")
                    self.Grid[i][j].set_state(n_state[i][j])

    def draw(self):
        pyxel.cls(0)
        for row in self.Grid:
            for cell in row:
                if cell.alive:
                    pyxel.rect(cell.x, cell.y, cell.w, cell.h, pyxel.COLOR_WHITE)

        pyxel.rect(0,0,SCREEN_WIDTH,self.instructions_h,pyxel.COLOR_GREEN)
        pyxel.text(1,0,"P: pause/play", pyxel.COLOR_WHITE)
        pyxel.text(1,7, "Left Click: Change State", pyxel.COLOR_WHITE)
        pyxel.text(1,14, "Q: Quit    C: Clear", pyxel.COLOR_WHITE)

        if self.pause:
            pyxel.text(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, "PAUSED", pyxel.COLOR_RED)

Game()