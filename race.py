import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)
text_color = BLACK

class Runner:
    def __init__(self, name, speed, position, image_path, x_position):
        self.name = name
        self.speed = speed
        self.position = position
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, HEIGHT // 2)

    def move_forward(self):
        self.position += self.speed
        self.rect.center = (self.position, HEIGHT // 2)

    def print_position(self):
        print(f"{self.name} is at {self.position} meters.")

class Race:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Achille & The Turtle")
        self.achille = Runner("Achille", 20, 0, "images/achille.png", 100)
        self.turtle = Runner("Turtle", 2, 200, "images/turtle.png", 250)
        self.clock = pygame.time.Clock()
        self.race_distance = 10000

    def run(self):
        while self.achille.position < self.race_distance:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.achille.move_forward()
            self.turtle.move_forward()

            self.screen.fill(WHITE)

            self.screen.blit(self.achille.image, self.achille.rect)
            self.screen.blit(self.turtle.image, self.turtle.rect)

            self.achille.print_position()
            self.turtle.print_position()

            achille_text = font.render(f"{self.achille.name}: {self.achille.position} meters", True, text_color)
            turtle_text = font.render(f"{self.turtle.name}: {self.turtle.position} meters", True, text_color)

            self.screen.blit(achille_text, (10, 10))
            self.screen.blit(turtle_text, (10, 50))

            pygame.display.flip()

            self.clock.tick(1)

            if self.achille.position >= self.turtle.position:
                print("Achille overtook the Turtle.")
                break

        print("Race finished!")

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    race_game = Race()
    race_game.run()
