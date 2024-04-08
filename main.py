#!/usr/bin/env python3
import asyncio
from math import cos, sin, degrees

import pygame
import pygame_menu


class GameState:
    def __init__(self):
        self.position = (100.0, 100.0, 0.0)

    def update(self):
        keys = pygame.key.get_pressed()
        forward = 1
        angle = 0.1
        if keys[pygame.K_LEFT]:
            self.position = (self.position[0], self.position[1], self.position[2] + angle)
        if keys[pygame.K_RIGHT]:
            self.position = (self.position[0], self.position[1], self.position[2] - angle)
        if keys[pygame.K_UP]:
            self.position = (
                self.position[0] + forward * cos(self.position[2]), self.position[1] + forward * sin(self.position[2]),
                self.position[2])
        if keys[pygame.K_DOWN]:
            self.position = (
                self.position[0] - forward * cos(self.position[2]), self.position[1] - forward * sin(self.position[2]),
                self.position[2])


class Window:
    def __init__(self):
        # Create the window, saving it to a variable.
        self.window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        pygame.display.set_caption("Example resizable window")
        self.font = pygame.font.SysFont(None, 24)

        self.car_image = pygame.image.load("car.png").convert_alpha()
        self.car_image = pygame.transform.scale(self.car_image, (100, 200))

        self.menu = pygame_menu.Menu('Racer', 300, self.window.get_height())

        self.menu.add.text_input('Name :', default='John Doe')
        self.menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)])
        self.menu.add.button('Play')
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def update(self, events):
        self.menu.update(events)

    def draw(self, game_state, clock):
        self.window.fill((255, 255, 255))

        # Draw a red rectangle that resizes with the window.
        pygame.draw.rect(self.window, (200, 0, 0), (self.window.get_width() / 3,
                                                    self.window.get_height() / 3, self.window.get_width() / 3,
                                                    self.window.get_height() / 3))

        # Draw a car
        car_surface = pygame.Surface([100, 200], pygame.SRCALPHA)
        car_surface.fill((0, 0, 0))
        car_surface.blit(self.car_image, (0, 0))
        text = self.font.render('player1}', True, pygame.Color('yellow'))
        car_surface.blit(text, (20, 20))

        car_rotated = pygame.transform.rotate(car_surface, degrees(game_state.position[2]) - 90)
        car_rect = car_rotated.get_rect(
            center=(game_state.position[0], self.window.get_height() - game_state.position[1]))
        self.window.blit(car_rotated, (car_rect.x, car_rect.y))

        # Draw the UI
        text = self.font.render(f'fps: {clock.get_fps():.0f}', True, pygame.Color('blue'))
        self.window.blit(text, (20, 20))

        text = self.font.render(
            f'pos: {game_state.position[0]:.1f} {game_state.position[1]:.1f} {game_state.position[2]:.1f}', True,
            pygame.Color('blue'))
        self.window.blit(text, (20, 40))

        self.menu.draw(self.window)


class App:
    def __init__(self):
        self.window = Window()
        self.game_state = GameState()
        self.clock = pygame.time.Clock()

    async def mainloop(self):
        run = True
        while run:
            events = pygame.event.get()

            self.window.update(events)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.game_state.update()

            self.clock.tick(60)
            self.window.draw(self.game_state, self.clock)
            pygame.display.update()
            await asyncio.sleep(0)  # Very important, and keep it 0


def main():
    pygame.init()
    app = App()
    asyncio.run(app.mainloop())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pygame.quit()
