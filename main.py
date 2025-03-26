import pygame
import sys
from pygame.examples.grid import TILE_SIZE, TILES_HORIZONTAL

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2D Sandbox Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)

# Define tile types
TILE_SIZE = 50
TILE_TYPES = {
    "grass": GREEN,
    "water": BLUE,
    "dirt": BROWN
}

# Create a tile map
tile_map = [
    ["grass", "grass", "grass", "grass", "grass"],
    ["dirt", "water", "water", "grass", "grass"],
    ["grass", "grass", "dirt", "dirt", "water"],
    ["water", "grass", "grass", "dirt", "grass"],
    ["dirt", "dirt", "grass", "water", "grass"]
]

# Player settings
player_pos = [400, 300]
player_size = 50
player_color = BLACK
player_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle the player's movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the tile map
    for row in range(len(tile_map)):
        for col in range(len(tile_map[row])):
            tile_type = tile_map[row][col]
            tile_color = TILE_TYPES[tile_type]
            pygame.draw.rect(screen, tile_color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

