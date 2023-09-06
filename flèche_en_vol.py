import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 300
WHITE = (255, 255, 255)
BLACK = 0, 0, 0

font = pygame.font.Font(None, 36)
text_color = BLACK

class Archery:
    def __init__(self, name, speed, position, image_path):
        self.name = name
        self.speed = speed
        self.position = position
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (position, HEIGHT // 2)

    def arrow_position(self):
        self.position += self.speed
        self.rect.center = (self.position, HEIGHT // 2)

    def print_position(self):
        print(f"The arrow is currently at {self.position} meters.")
        

#Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying arrow")

clock = pygame.time.Clock()

target = Archery("Target", 0, 250, "images/target.png")
arrow = Archery("Arrow", 25, 0, "images/arrow.png")

while arrow.position < target.position:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    arrow.arrow_position()

    screen.fill(WHITE)

    screen.blit(target.image, target.rect)
    screen.blit(arrow.image, arrow.rect)

    arrow.print_position()

    arrow_text = font.render(f"{arrow.name}: {arrow.position} meters", True, text_color)

    screen.blit(arrow_text, (10, 10))

    pygame.display.flip()

    clock.tick(1)

print("The arrow hit the target!")

pygame.quit()
sys.exit()