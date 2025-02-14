import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird Pygame Demo")

# Load assets
bird_img = pygame.image.load('assets/images/bird.png')
pipe_img = pygame.image.load('assets/images/pipe.png')
top_pipe_img = pygame.transform.flip(pipe_img, False, True)

# Bird settings
bird_x, bird_y = 100, height // 2
bird_speed = 0
gravity = 0.5
jump_strength = -10

# Pipe settings
pipe_width = 80
pipe_height = 450
pipe_gap = 200
pipe_speed = 5
center_y = height // 2 - 100
y_variation = 150

# Floor settings
floor_height = 50

# Function to generate a new pipe's y position
def get_random_pipe_y():
    return random.randint(center_y - y_variation, center_y + y_variation)

pipes = []

# Timer settings
pipe_spawn_time = 2000  # Time in milliseconds between pipe spawns
last_pipe_spawn_time = pygame.time.get_ticks()

# Function to spawn pipes
def spawn_pipe():
    current_time = pygame.time.get_ticks()
    if current_time - last_pipe_spawn_time > pipe_spawn_time:
        pipe_y = get_random_pipe_y()
        pipes.append((width, pipe_y))
        return current_time
    return last_pipe_spawn_time
    
# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = jump_strength

    # Update bird position
    bird_speed += gravity
    bird_y += bird_speed

    # Bird collision with floor
    if bird_y + bird_img.get_height() > height - floor_height:
        bird_y = height - floor_height - bird_img.get_height()
        bird_speed = 0

    # Spawn new pipes at regular intervals
    last_pipe_spawn_time = spawn_pipe()
    
    # Update pipe positions
    pipes = [(x - pipe_speed, y) for x, y in pipes if x - pipe_speed > -pipe_width]

    # Fill the screen with a color (e.g., off-white)
    screen.fill((200, 200, 200))

    # Draw bird
    screen.blit(bird_img, (bird_x, bird_y))

    # Draw pipes
    for pipe_x, pipe_y in pipes:
        screen.blit(top_pipe_img, (pipe_x, pipe_y - pipe_height))
        screen.blit(pipe_img, (pipe_x, pipe_y + pipe_gap))

        # Create rectangles for collision detection
        bird_rect = pygame.Rect(
            bird_x + bird_img.get_width() * 0.15,  # Adjust x position
            bird_y + bird_img.get_height() * 0.15,  # Adjust y position
            bird_img.get_width() * 0.7,  # New width
            bird_img.get_height() * 0.7  # New height
        )
        top_pipe_rect = pygame.Rect(pipe_x, pipe_y - pipe_height, pipe_width, pipe_height)
        bottom_pipe_rect = pygame.Rect(pipe_x, pipe_y + pipe_gap, pipe_width, pipe_height)

        # Check for collisions
        if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
            print("Collision detected!")
            running = False

    # Draw floor
    pygame.draw.rect(screen, (100, 100, 100), (0, height - floor_height, width, floor_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Freeze game on collision
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.flip()