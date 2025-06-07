import pygame
import random
pygame.init()

print("""
Feed your pet!
------------------------

Controls:
- Move the food left and right with the LEFT and RIGHT arrow keys.
- Press SPACEBAR or left mouse button to drop the food.

Objective:
Feed your pet as many times as you can to reach its happiness!
""")


WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pet")

LIGHT_GREEN = (144, 238, 144)
PINK = (255, 182, 193)
BROWN = (139, 69, 19)

class GameObject:
    def __init__(self, x, y):
        self._x = x
        self._y = y

# Base class
class GameObject:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_position(self):
        return self._x, self._y

    def set_position(self, x, y):
        self._x = x
        self._y = y


# Pet class
class Pet(GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self._size = size
        self._happiness = 0

    def draw(self, surface):
        pygame.draw.circle(surface, PINK, (self._x, self._y), self._size)

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def get_size(self):
        return self._size

    def increase_happiness(self):
        self._happiness += 1

    def get_happiness(self):
        return self._happiness


# Food class
class Food(GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self._size = size

    def draw(self, surface):
        pygame.draw.circle(surface, BROWN, (self._x, self._y), self._size)

    def get_size(self):
        return self._size


# Game setup
pet = Pet(WIDTH // 2, HEIGHT // 2, 30)
foods = []

clock = pygame.time.Clock()
running = True
speed = 5

# Game loop
while running:
    screen.fill(LIGHT_GREEN)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click spawns food
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            new_food = Food(mx, my, 10)
            foods.append(new_food)

    # Keyboard input → move the pet
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pet.move(-speed, 0)
    if keys[pygame.K_RIGHT]:
        pet.move(speed, 0)
    if keys[pygame.K_UP]:
        pet.move(0, -speed)
    if keys[pygame.K_DOWN]:
        pet.move(0, speed)

    # Draw pet
    pet.draw(screen)

    # Draw and check food collision
    for food in foods[:]:
        food.draw(screen)

        # Collision detection
        px, py = pet.get_position()
        fx, fy = food.get_position()
        distance = ((px - fx) ** 2 + (py - fy) ** 2) ** 0.5

        if distance < pet.get_size() + food.get_size():
            foods.remove(food)
            pet.increase_happiness()

    # Show happiness (score)
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Happiness: {pet.get_happiness()}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
