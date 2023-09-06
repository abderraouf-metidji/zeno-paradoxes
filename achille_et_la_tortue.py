import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)
text_color = BLACK



class Runner:
    def __init__(self, name, speed, image_path):
        self.name = name
        self.speed = speed
        self.position = 0
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (self.position, HEIGHT // 2)

    def move_forward(self):
        self.position += self.speed
        self.rect.center = (self.position, HEIGHT // 2)

    def print_position(self):
        print(f"{self.name} is at {self.position} meters.")


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Achille & The Turtle")

achille = Runner("Achille", 20, "images/achille.png")
turtle = Runner("Turtle", 2, "images/turtle.png")

clock = pygame.time.Clock()

turtle.position = 250

race = 10000

while achille.position < race:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    achille.move_forward()
    turtle.move_forward()

    screen.fill(WHITE)

    screen.blit(achille.image, achille.rect)
    screen.blit(turtle.image, turtle.rect)

    achille.print_position()
    turtle.print_position()

    achille_text = font.render(f"{achille.name}: {achille.position} meters", True, text_color)
    turtle_text = font.render(f"{turtle.name}: {turtle.position} meters", True, text_color)

    screen.blit(achille_text, (10, 10))
    screen.blit(turtle_text, (10, 50))

    pygame.display.flip()

    clock.tick(1)

    if achille.position >= turtle.position:
        print("Achille overtook the Turtlel.")
        break

print("Race finished!")

pygame.quit()
sys.exit()