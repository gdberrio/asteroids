import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def move(self, dt):
        self.position += self.velocity * dt
        print(f"position {self.position}")

    def update(self, dt):
        self.move(dt)
