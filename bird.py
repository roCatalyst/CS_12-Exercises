#copied from sir 1cho, just added music

import random
from dataclasses import dataclass

import pyxel


@dataclass
class Bird:
    x: float
    y: float
    radius: float
    dy: float
    ay: float

    @property
    def top(self):
        return self.y - self.radius

    @property
    def bottom(self):
        return self.y + self.radius


@dataclass
class Pipe:
    x: float
    y: float
    width: int
    height: int
    dx: float

    @property
    def right(self):
        return self.x + self.width

    def update_position(self):
        self.x -= self.dx


@dataclass
class PipePair:
    top_pipe: Pipe
    bottom_pipe: Pipe
    has_been_passed: bool

    def should_be_deleted(self):
        return self.top_pipe.right <= 0 and self.bottom_pipe.right <= 0

    @classmethod
    def make_pair_random(cls, x: int, min_height: int, pipe_width: int, hole_height: int, dx: float, screen_height: int):
        hole_y = random.randint(
            min_height, screen_height - min_height - hole_height)

        return cls.make_pair(x, pipe_width, hole_y, hole_height, dx, screen_height)

    @classmethod
    def make_pair(cls, x: int, pipe_width: int, hole_y: int, hole_height: int, dx: float, screen_height: int):
        top = Pipe(
            x=x,
            y=0,
            width=pipe_width,
            height=hole_y,
            dx=dx,
        )

        bottom_height = screen_height - (hole_y + hole_height)

        bottom = Pipe(
            x=x,
            y=screen_height - bottom_height,
            width=pipe_width,
            height=bottom_height,
            dx=dx,
        )

        return PipePair(
            top_pipe=top,
            bottom_pipe=bottom,
            has_been_passed=False,
        )


@dataclass
class State:
    bird: Bird
    pipe_pairs: list[PipePair]
    score: int
    tick: int
    is_game_over: bool


class App:
    def __init__(self):
        self.fps = 60
        self.bird_radius = 5
        self.jump_height = -2
        self.pipe_width = 15
        self.pipe_opening = 20
        self.pipe_speed = 1
        self.pipe_min_height = 3
        self.pipe_hole_height = 35
        self.screen_width = 100
        self.screen_height = 100
        self.pipe_creation_interval = 1.5

        self.state = self.init_state()

        pyxel.init(self.screen_width, self.screen_height, fps=self.fps)

        pyxel.load("MEGALOVANIA.pyxres")
        pyxel.playm(0, loop=True)

        pyxel.run(self.update, self.draw)

    def init_state(self) -> State:
        bird = Bird(
            x=self.screen_width // 2,
            y=self.screen_height // 2,
            radius=self.bird_radius,
            dy=0,
            ay=0.1,
        )

        return State(
            pipe_pairs=[],
            bird=bird,
            score=0,
            tick=0,
            is_game_over=False,
        )

    def make_random_pipe_pair(self):
        pair = PipePair.make_pair_random(self.screen_width, self.pipe_min_height,
                                         self.pipe_width, self.pipe_hole_height, self.pipe_speed, self.screen_height)

        self.state.pipe_pairs.append(pair)

    def get_pipes(self):
        return [pipe for pair in self.state.pipe_pairs for pipe in [pair.top_pipe, pair.bottom_pipe]]

    def remove_pipe_pair(self, pair: PipePair):
        if pair in self.state.pipe_pairs:
            self.state.pipe_pairs.remove(pair)

    def is_in_collision(self, bird: Bird, pipe: Pipe):
        circ_dist_x = abs(bird.x - (pipe.x + pipe.width / 2))
        circ_dist_y = abs(bird.y - (pipe.y + pipe.height / 2))

        if circ_dist_x > (pipe.width / 2 + bird.radius):
            return False

        if circ_dist_y > (pipe.height / 2 + bird.radius):
            return False

        if circ_dist_x <= (pipe.width / 2):
            return True

        if circ_dist_y <= (pipe.height / 2):
            return True

        corner_dist_sq = (circ_dist_x - pipe.width / 2)**2 + \
            (circ_dist_y - pipe.height / 2)**2

        return corner_dist_sq <= (bird.radius**2)

    def update_game_over(self):
        if self.state.bird.top <= 0 or self.state.bird.bottom >= self.screen_height:
            self.state.is_game_over = True
            return

        for pipe in self.get_pipes():
            if self.is_in_collision(self.state.bird, pipe):
                self.state.is_game_over = True

    def update_pipes(self):
        frame_interval = self.pipe_creation_interval * self.fps

        if self.state.tick % frame_interval == 0:
            self.make_random_pipe_pair()

        pairs_to_delete: list[PipePair] = []

        for pair in self.state.pipe_pairs:
            pair.top_pipe.update_position()
            pair.bottom_pipe.x -= pair.bottom_pipe.dx

            if pair.should_be_deleted():
                pairs_to_delete.append(pair)

        for pair in pairs_to_delete:
            self.remove_pipe_pair(pair)


    def update_bird(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.state.bird.dy = self.jump_height

        self.state.bird.dy += self.state.bird.ay
        self.state.bird.y += self.state.bird.dy

    def update_score(self):
        for pair in self.state.pipe_pairs:
            if not pair.has_been_passed and self.state.bird.x > (pair.top_pipe.x + pair.top_pipe.width / 2):
                pair.has_been_passed = True
                self.state.score += 1

    def update_tick(self):
        self.state.tick += 1

    def update(self):
        if self.state.is_game_over:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = self.init_state()

        if not self.state.is_game_over:
            self.update_pipes()
            self.update_bird()
            self.update_game_over()
            self.update_score()
            self.update_tick()

        print(self.state)

    def draw_pipes(self):
        for pipe in self.get_pipes():
            color = 3 if self.is_in_collision(self.state.bird, pipe) else 2
            pyxel.rect(pipe.x, pipe.y, pipe.width, pipe.height, color)

    def draw_bird(self):
        pyxel.circ(int(self.state.bird.x),
                   int(self.state.bird.y), self.state.bird.radius, 1)

    def draw_score(self):
        pyxel.text(self.screen_width / 2, 5, str(self.state.score), 4)

    def draw_game_over(self):
        pyxel.text(self.screen_width / 2 - 17,
                   self.screen_height / 2 - 2, 'Game over', 4)

    def clear_screen(self):
        pyxel.cls(0)

    def draw(self):
        self.clear_screen()
        self.draw_bird()
        self.draw_pipes()
        self.draw_score()

        if self.state.is_game_over:
            self.draw_game_over()


App()
