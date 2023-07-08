import pygame
import sys

pygame.init()

# Colours
colour_background = (255, 255, 255)

# Game Setup
FPS = 60  # because higher refresh rates aren't real
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

gameWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cubes that look round? Idk man")


class Coord:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z


class Line:
    def __init__(self, start: Coord, end: Coord):
        self.start = start
        self.end = end

        self.length = (
            (end.x - start.x) ** 2 +
            (end.y - start.y) ** 2 +
            (end.z - start.z) ** 2
        ) ** 0.5


def main():
    looping = True

    while looping:

        # Input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Processing
        # This section will be built out later

        # Render elements of the game
        # bottom up

        gameWindow.fill(colour_background)

        # force window update
        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    main()
