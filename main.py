import pygame

from asteroid import Asteroid
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)

    asteroid = Asteroid(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3, 10)

    asteroid.velocity = pygame.Vector2(0, 10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for item in drawable_group:
            item.draw(screen)
        updatable_group.update(dt)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
