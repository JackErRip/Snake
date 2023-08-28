import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Snake properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# Food properties
food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True

# Score
score = 0

# Game over flag
game_over = False

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Function to reset the game
def reset_game():
    global snake_pos, snake_body, snake_direction, change_to, food_pos, food_spawn, score, game_over
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    snake_direction = 'RIGHT'
    change_to = snake_direction
    food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
    food_spawn = True
    score = 0
    game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and snake_direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                change_to = 'RIGHT'
            # Additional keybinds
            if event.key == pygame.K_w and snake_direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_s and snake_direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_a and snake_direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_d and snake_direction != 'LEFT':
                change_to = 'RIGHT'
    
    # Changing direction
    if change_to == 'UP' and snake_direction != 'DOWN':
        snake_direction = 'UP'
    if change_to == 'DOWN' and snake_direction != 'UP':
        snake_direction = 'DOWN'
    if change_to == 'LEFT' and snake_direction != 'RIGHT':
        snake_direction = 'LEFT'
    if change_to == 'RIGHT' and snake_direction != 'LEFT':
        snake_direction = 'RIGHT'

    # Moving the snake
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10
    
    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1  # Update the score when the snake eats the food
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        food_spawn = True
    
    # Bounds checking
    if snake_pos[0] < 0:
        snake_pos[0] = WIDTH
    if snake_pos[0] > WIDTH:
        snake_pos[0] = 0
    if snake_pos[1] < 0:
        snake_pos[1] = HEIGHT
    if snake_pos[1] > HEIGHT:
        snake_pos[1] = 0
    
    # Self-hit
    for segment in snake_body[1:]:
        if segment[0] == snake_pos[0] and segment[1] == snake_pos[1]:
            game_over = True
    
    # Draw everything
    win.fill(BLACK)
    for segment in snake_body:
        pygame.draw.rect(win, GREEN, pygame.Rect(segment[0], segment[1], 10, 10))
    pygame.draw.rect(win, WHITE, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # Refresh rate
    fps.tick(24)

# Display the current score on the screen
    font = pygame.font.Font(None, 30)
    score_text = font.render("Score: " + str(score), True, WHITE)
    win.blit(score_text, (10, 10))  # Display the score in the top-left corner

    pygame.display.update()
    fps.tick(30)

# Display game over screen
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over", True, WHITE)
retry_text = font.render("Press 'R' to Retry", True, WHITE)
score_text = font.render("Score: " + str(score), True, WHITE)
win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
win.blit(retry_text, (WIDTH // 2 - retry_text.get_width() // 2, HEIGHT // 2))
win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 50))

# Display "Game Made by: Aldrien Velasco" message
author_text = font.render("Game Made by: Aldrien Velasco", True, WHITE)
win.blit(author_text, (WIDTH // 2 - author_text.get_width() // 2, HEIGHT // 2 + 100))

pygame.display.update()

retry = False
while not retry:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            retry = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
                retry = True


# Quit pygame
pygame.quit()
