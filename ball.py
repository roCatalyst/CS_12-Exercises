import pyxel
from dataclasses import dataclass

SCREEN_WIDTH, SCREEN_HEIGHT = 100, 150
BALL_RADIUS = 10.0
GRASS_HEIGHT = 10
TEXT_DIFF = 7

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
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, "Keepie Uppie", fps=60)

        pyxel.mouse(visible=True)
        self.state = self.init_state()
        self.jump_height = -3
        self.high_score = 0

        pyxel.run(self.update, self.draw)

    def init_state(self) -> State:
        b = Ball(SCREEN_WIDTH//2, SCREEN_HEIGHT-BALL_RADIUS-2, BALL_RADIUS, 0, 0, 0.1)

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
            if (pyxel.mouse_x - ball.x)**2 + (pyxel.mouse_y - ball.y)**2 <= ball.radius**2:
                self.state.score += 1
                ball.vy = self.jump_height
                ball.vx += (ball.x - pyxel.mouse_x)*0.1

        if self.state.start:
            if (ball.top_y >= SCREEN_HEIGHT):
                ball.vy, ball.vx = 0, 0
                self.state.is_game_over = True
                self.high_score = max(self.high_score, self.state.score)

            if (ball.left_x <= 0 or ball.right_x >= SCREEN_WIDTH):
                ball.vx *= -1

            ball.x += ball.vx
            ball.y += ball.vy

            if not self.state.is_game_over:
                ball.vy += ball.ay

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.state.is_game_over:
            if pyxel.btnp(key=pyxel.KEY_SPACE):
                self.state = self.init_state()

        if not self.state.is_game_over:
            self.update_ball()
    
    def draw(self):
        #draw background
        pyxel.cls(pyxel.COLOR_LIGHT_BLUE)
        pyxel.rect(0,SCREEN_HEIGHT-GRASS_HEIGHT, SCREEN_WIDTH, GRASS_HEIGHT, pyxel.COLOR_LIME)

        if not self.state.start:
            pyxel.text(1, 1, "Let's play Keepie Uppie!", pyxel.COLOR_BLACK)  
            pyxel.text(1, 1 + TEXT_DIFF, "Keep the ball in the air!", pyxel.COLOR_BLACK)  
            pyxel.text(1, 1 + 2*TEXT_DIFF, "To start, left click", pyxel.COLOR_BLACK)   
            pyxel.text(1, 1 + 3*TEXT_DIFF, "the ball", pyxel.COLOR_BLACK)   
        
        if not self.state.is_game_over:
            #draw ball
            ball = self.state.ball
            pyxel.circ(ball.x, ball.y, ball.radius, pyxel.COLOR_WHITE)

            if self.state.start:
                #draw score
                score = self.state.score
                pyxel.text(SCREEN_WIDTH//2, 1, str(score), pyxel.COLOR_BLACK)
        else:
            pyxel.text(1, 1, f"Score: {self.state.score}", pyxel.COLOR_BLACK)
            pyxel.text(1, 1 + TEXT_DIFF, f"Best: {self.high_score}", pyxel.COLOR_BLACK)
            pyxel.text(1, 1 + 2*TEXT_DIFF, f"play again? [SPACE]", pyxel.COLOR_BLACK)
            pyxel.text(1, 1 + 3*TEXT_DIFF, f"Quit? [Q]", pyxel.COLOR_BLACK)
        

if __name__ == "__main__":
    Game()