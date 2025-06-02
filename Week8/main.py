import pygame
import random
import sys

WIDTH = 800
HEIGHT = 600

class Unicorn:
    def __init__(self):
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.rect = pygame.Rect(random.randint(0, WIDTH-50), random.randint(0, HEIGHT-50), 50, 50)
        self.speed_x = random.randint(1, 5)
        self.speed_y = random.randint(1, 5)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speed_x *= -1
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Einhorn-Animation 🦄")
clock = pygame.time.Clock()

unicorns = [Unicorn() for _ in range(5)]

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for unicorn in unicorns:
        unicorn.move()
        unicorn.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

