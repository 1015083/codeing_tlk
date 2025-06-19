import pygame
import random
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Basket (Player)
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 10

# Block (Falling)
block_size = 30
block_x = random.randint(0, WIDTH - block_size)
block_y = -block_size
block_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 40)
large_font = pygame.font.SysFont(None, 72)

# Clock
clock = pygame.time.Clock()
running = True
game_over = False

while running:
    clock.tick(38)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Move basket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
            basket_x += basket_speed

        # Move block
        block_y += block_speed

        # Check for catch
        basket_rect = pygame.Rect(basket_x, basket_y, basket_width, basket_height)
        block_rect = pygame.Rect(block_x, block_y, block_size, block_size)
        if basket_rect.colliderect(block_rect):
            score += 1
            block_x = random.randint(0, WIDTH - block_size)
            block_y = -block_size

        # Check for miss (Game Over)
        if block_y > HEIGHT:
            game_over = True

        # Draw
        pygame.draw.rect(screen, BLUE, basket_rect)
        pygame.draw.rect(screen, RED, block_rect)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
    else:
        # Show Game Over message
        over_text = large_font.render("GAME OVER", True, RED)
        final_score = font.render(f"Final Score: {score}", True, BLACK)
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(final_score, (WIDTH // 2 - final_score.get_width() // 2, HEIGHT // 2 + 20))

    pygame.display.flip()

pygame.quit()
sys.exit()

