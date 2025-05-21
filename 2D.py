import pygame
import random
import sys

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Car Racing (Drawn Cars)")

# Colors
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Lanes (optional)
lanes = [100, 170, 240, 310]  # Lane X positions

# Car size
car_width = 40
car_height = 80

# Player
player_x = lanes[1]
player_y = 500
player_rect = pygame.Rect(player_x, player_y, car_width, car_height)
player_speed = 5

# Enemy
enemy_x = random.choice(lanes)
enemy_y = -100
enemy_rect = pygame.Rect(enemy_x, enemy_y, car_width, car_height)
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Draw a car shape
def draw_car(rect, color):
    # Car body
    pygame.draw.rect(screen, color, rect)

    # Windows (light gray)
    window_rect = pygame.Rect(rect.x + 8, rect.y + 10, 24, 20)
    pygame.draw.rect(screen, (200, 200, 255), window_rect)

    # Wheels (black)
    pygame.draw.rect(screen, BLACK, (rect.x, rect.y + 10, 6, 20))  # left front
    pygame.draw.rect(screen, BLACK, (rect.x + rect.width - 6, rect.y + 10, 6, 20))  # right front
    pygame.draw.rect(screen, BLACK, (rect.x, rect.y + rect.height - 30, 6, 20))  # left back
    pygame.draw.rect(screen, BLACK, (rect.x + rect.width - 6, rect.y + rect.height - 30, 6, 20))  # right back

# Game loop
running = True
while running:
    screen.fill(GRAY)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.x > lanes[0]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.x < lanes[-1]:
        player_rect.x += player_speed

    # Move enemy
    enemy_rect.y += enemy_speed
    if enemy_rect.y > HEIGHT:
        enemy_rect.y = -100
        enemy_rect.x = random.choice(lanes)
        score += 1
        if score % 5 == 0:
            enemy_speed += 1

    # Collision
    if player_rect.colliderect(enemy_rect):
        draw_text("GAME OVER", 50, WHITE, 100, HEIGHT // 2 - 30)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    # Draw lane lines
    for i in range(6):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, i * 120 + (score % 120), 10, 60))

    # Draw cars
    draw_car(player_rect, BLUE)
    draw_car(enemy_rect, RED)

    # Draw score
    draw_text(f"Score: {score}", 30, WHITE, 10, 10)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()