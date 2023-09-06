import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)
text_color = BLACK

class Throw:
    def __init__(self, name, position, image_path):
        self.name = name
        self.position = position
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect = (position, HEIGHT // 2)

    def rock_position(self):
        rock.position += ((tree.position - rock.position) *0.5)
        self.rect = (self.position, HEIGHT // 2)

    def print_position(self):
        print(f"The rock is at {self.position} meters.")

#Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dichotomie")

clock = pygame.time.Clock()

tree = Throw("Tree", 100, "images/tree.png")
rock = Throw("Rock", 0, "images/rock.png")

while rock.position < tree.position:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rock.rock_position()

    screen.fill(WHITE)

    screen.blit(tree.image, tree.rect)
    screen.blit(rock.image, rock.rect)

    rock.print_position()

    rock_text = font.render(f"{rock.name}: {rock.position} meters", True, text_color)
    
    screen.blit(rock_text, (10, 10))

    pygame.display.flip()

    clock.tick(1)

print("The rock hit the tree!")

pygame.quit()
sys.exit()