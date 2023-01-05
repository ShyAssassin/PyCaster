import sys
import contextlib
# just to get rid of welcome message
with contextlib.redirect_stdout(None):
    import pygame as pg
from .console import Console
from .settings import Settings


class PyCaster:
    def __init__(self):
        pg.init()
        self.console: Console = Console(self)
        self.settings: Settings = Settings()
        self.clock: pg.time.Clock = pg.time.Clock()
        self.display: pg.display = pg.display.set_mode(self.settings.resolution)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.settings.running = False

    def update(self):
        pass

    def draw(self):
        self.display.fill("black")

    def run(self):
        self.settings.running = True
        while self.settings.running:
            self.check_events()
            self.update()
            self.draw()
        pg.quit()
        sys.exit()
