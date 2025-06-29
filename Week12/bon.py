import pygame
import sys

def zeichne_bon(screen, font, produkte):
    screen.fill((255, 255, 255))
    y = 20
    gesamt = 0

    title = font.render("BON", True, (0, 0, 0))
    screen.blit(title, (100, y))
    y += 40

    for name, preis in produkte:
        text = font.render(f"{name:15} {preis:.2f} €", True, (0, 0, 0))
        screen.blit(text, (20, y))
        y += 30
        gesamt += preis

    y += 10
    pygame.draw.line(screen, (0, 0, 0), (20, y), (250, y), 2)
    y += 10
    total_text = font.render(f"Gesamt: {gesamt:.2f} €", True, (0, 0, 0))
    screen.blit(total_text, (20, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 400))
    pygame.display.set_caption("Bon Generator")
    font = pygame.font.SysFont(None, 28)

    produkte = [
        ("Apfel", 0.99),
        ("Brot", 2.50),
        ("Milch", 1.20)
    ]

    zeichne_bon(screen, font, produkte)
    pygame.display.flip()

    # Warten bis Fenster geschlossen wird
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
