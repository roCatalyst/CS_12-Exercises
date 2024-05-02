import pyxel
from dataclasses import dataclass

SCREEN_WIDTH, SCREEN_HEIGHT = 100, 150

@dataclass
class Ball:
    x: float
    y: float
    radius: float
    vx: float
    vy: float
    ay: float

    @property
    def top_y(self):
        return self.y - self.radius
    
    @property
    def bot_y(self):
        return self.y + self.radius
    
    @property
    def left_x(self):
        return self.x - self.radius
    
    @property
    def right_x(self):
        return self.x + self.radius

@dataclass
class State:
    ball: Ball
    score: int
    start: bool
    is_game_over: bool

class Game:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, "Messenger Soccer", fps=60)

        pyxel.mouse(visible=True)
        self.state = self.init_state()
        self.jump_height = -2

        pyxel.run(self.update, self.draw)

    def init_state(self) -> State:
        radius: float = 10.0
        b = Ball(SCREEN_WIDTH//2, SCREEN_HEIGHT-radius-2, radius, 0, 0, 0.1)

        return State(
            ball = b,
            score = 0,
            start = False,
            is_game_over = False
        )

    def update_ball(self):
        ball = self.state.ball

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.state.start = True
            print("KICK!")
            if (pyxel.mouse_x - ball.x)**2 + (pyxel.mouse_y - ball.y)**2 <= ball.radius**2:
                ball.vy = self.jump_height
                ball.vx += (ball.x - pyxel.mouse_x)*0.1

        if self.state.start:
            #TODO: Detect ground collision
            if (ball.bot_y >= SCREEN_HEIGHT):
                ball.vy, ball.vx = 0, 0
                self.state.is_game_over = True

            #TODO: Detect wall collision
            if (ball.left_x <= 0 or ball.right_x >= SCREEN_WIDTH):
                ball.vx *= -1

            ball.x += ball.vx
            ball.y += ball.vy

            if not self.state.is_game_over:
                ball.vy += ball.ay

        print(ball)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.state.is_game_over:
            if pyxel.btnp(key=pyxel.KEY_SPACE):
                self.state = self.init_state()

        if not self.state.is_game_over:
            self.update_ball()
    
    def draw(self):
        pyxel.cls(0)

        #draw score
        score = self.state.score
        pyxel.text(SCREEN_WIDTH//2, SCREEN_HEIGHT, str(score), pyxel.COLOR_GREEN)

        #draw ball
        ball = self.state.ball
        pyxel.circ(ball.x, ball.y, ball.radius, pyxel.COLOR_WHITE)

if __name__ == "__main__":
    Game()