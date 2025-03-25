import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2D Sandbox Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_pos = [400, 300]
player_size = 50
player_color = BLACK
player_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# Inventory class to manage player's items
        class Inventory:
            def __init__(self):
                self.items = []

            def add_item(self, item):
                self.items.append(item)

            def remove_item(self, item):
                if item in self.items:
                    self.items.remove(item)

            def has_item(self, item):
                return item in self.items

            def display_inventory(self):
                print("Inventory:")
                for item in self.items:
                    print(f"- {item}")

        # Example usage
        inventory = Inventory()
        inventory.add_item("Sword")
        inventory.add_item("Shield")
        inventory.display_inventory()
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

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)