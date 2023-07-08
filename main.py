import pygame
import sys

pygame.init()

# TODO loose plan
#  cube centred around 0, 0, 0 for simplicity
#  click and drag rotates - simple vector transformation
#  'camera' has static position at somewhere like 10, 0, 0
#  xy is flat, z is up
#  can draw based on distance from camera, or have one sided 'textures'
#  probably the former first, seems simpler


# Colours
colour_background = (255, 255, 255)

# My colour palette is rubik's cube
colour_grey = (191, 191, 191)
colour_yellow = (255, 255, 63)
colour_green = (63, 255, 63)
colour_blue = (63, 63, 255)
colour_red = (255, 63, 63)
colour_orange = (255, 191, 63)

# Game Setup
FPS = 60  # because higher refresh rates aren't real
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

gameWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cubes that look round? Idk man")


class Coord:
    def __init__(self, x: float, y: float, z: float):
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


# If you think about it, everything is a triangle
class Triangle:
    def __init__(self, a: Coord, b: Coord, c: Coord):
        self.vertices = [a, b, c]

        # 3 points sit on a plane so this is the centre of that 'plane'
        # You will also learn that I love list comprehensions
        self.centre = Coord(
            sum([c.x for c in self.vertices]) / 3,
            sum([c.y for c in self.vertices]) / 3,
            sum([c.z for c in self.vertices]) / 3
        )


def main():
    looping = True

    mouseDown = None
    mouseUp = None

    while looping:

        # Input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = pygame.mouse.get_pos()
                print(mouseDown)

            if event.type == pygame.MOUSEBUTTONUP:
                mouseUp = pygame.mouse.get_pos()
                print(mouseUp)

                # do bounds checking

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
