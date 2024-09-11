import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
BIRD_WIDTH, BIRD_HEIGHT = 34, 24
PIPE_WIDTH, PIPE_HEIGHT = 80, 500
PIPE_GAP = 150
GRAVITY = 0.5
JUMP_STRENGTH = -10
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_image.fill(YELLOW)
pipe_image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
pipe_image.fill(GREEN)

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def draw(self):
        win.blit(bird_image, (self.x, self.y))


class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(100, HEIGHT - PIPE_GAP - 100)
        self.top = self.height
        self.bottom = HEIGHT - (self.height + PIPE_GAP)

    def update(self):
        self.x -= 5

    def draw(self):
        win.blit(pipe_image, (self.x, 0, PIPE_WIDTH, self.top))
        win.blit(pipe_image, (self.x, HEIGHT - self.bottom, PIPE_WIDTH, self.bottom))

def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        bird.update()
        for pipe in pipes:
            pipe.update()
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                pipes.append(Pipe())
                score += 1

        # Check for collisions
        for pipe in pipes:
            if (bird.x + BIRD_WIDTH > pipe.x and bird.x < pipe.x + PIPE_WIDTH and
                (bird.y < pipe.top or bird.y + BIRD_HEIGHT > HEIGHT - pipe.bottom)):
                running = False

        # Draw everything
        win.fill(BLUE)
        for pipe in pipes:
            pipe.draw()
        bird.draw()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()