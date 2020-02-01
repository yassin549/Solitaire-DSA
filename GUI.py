import pygame
import sys
from deck import Deck
from Tableau import Tableau
from foundation import Foundation
from stockpile import Stockpile
import os

def load_background():
    try:
        # Load the background image and scale it to fit the screen size
        background_image = pygame.image.load(os.path.join('Lib', 'bgr.jpg'))  # Adjust path as needed
        background_image = pygame.transform.scale(background_image, (width, height))
        return background_image
    except Exception as e:
        print(f"Error loading background image: {e}")
        sys.exit(1)

def printFoundation(foundations):
    font = pygame.font.SysFont(None, 18)
    suits = ["Heart", "Diamond", "Club", "Spade"]
    for i, suit in enumerate(suits):
        try:
            if len(foundations[i].cards) > 0:
                continue
            pygame.draw.rect(screen, (0, 0, 0), ((350 + i * 100), 20, 80, 120), 2)

            text_color = (0, 0, 0) if suit in ["Spade", "Club"] else (255, 0, 0)
            text = font.render(suit, True, text_color)
            text_rect = text.get_rect(center=(350 + i * 100 + 40, 20 + 60))
            screen.blit(text, text_rect)
        except Exception as e:
            print(f"Error in printFoundation: {e}")

foundation_positions = [((350 + i * 100), 20) for i in range(4)]
pygame.init()

# Initialize Foundations
foundations = [Foundation(suit) for suit in ['Heart', 'Diamond', 'Clubs', 'Spades']]

width, height = 1200, 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Solitaire Game')

# Load the background image
background_image = load_background()

column_positions = [(50 + i * 100, 180) for i in range(7)]
deck = Deck()
tableau = Tableau(column_positions)

# Initialize tableau and stockpile
deck = tableau.InitializeTableau(deck)
stockpiles = Stockpile(deck)

selected_col_index = None
selected_card = None
dragging = False
dragged_card = None
running = True

while running:
    try:
        # Draw the background image on the screen
        screen.blit(background_image, (0, 0))

        # Render stockpile and foundations
        stockpiles.PrintStockPile(screen, stockpiles)
        printFoundation(foundations)
        for i in range(4):
            foundations[i].display_single_foundation(screen, foundations[i], foundation_positions[i])
        tableau.render_tableau(screen)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if stockpiles.detect_stockpile_click(event) == "StockPile":
                    stockpiles.DrawOneCard()
                else:
                    dragged_card = stockpiles.start_drag(event, stockpiles)
                selected_col_index, selected_card = tableau.detect_card_click(event)
                if selected_card and selected_card.FaceUp:
                    dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging and selected_card:
                    mouse_x, mouse_y = event.pos
                    valid_move = False

                    # Check for valid move within tableau
                    for col_index in range(len(tableau.Piles)):
                        x, y = tableau.column_position[col_index]
                        pile_rect = pygame.Rect(x, y, 100, 500)
                        if pile_rect.collidepoint(mouse_x, mouse_y):
                            valid_move = tableau.move_card(selected_col_index, col_index, selected_card)
                            if valid_move:
                                print(f"Moved card from pile {selected_col_index} to pile {col_index}")
                                break

                    # Check for valid move to foundation
                    for col_index in range(len(foundations)):
                        x, y = foundation_positions[col_index]
                        pile_rect = pygame.Rect(x, y, 100, 500)
                        if pile_rect.collidepoint(mouse_x, mouse_y):
                            valid_move, tableau.Piles = foundations[col_index].move_card(selected_col_index, selected_card, tableau.Piles)
                            if valid_move:
                                print(f"Moved card from pile {selected_col_index} to foundation {col_index}")
                                break

                    # Reset after move
                    dragging = False
                    selected_col_index = None
                    selected_card = None

                elif dragged_card:
                    if stockpiles.place_card(event, dragged_card, tableau, foundations, foundation_positions):
                        print("Moved card from waste pile to a valid location.")
                    dragged_card = None

        # Handle dragging
        if dragging and selected_card:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if selected_card.FaceUp:
                screen.blit(selected_card.Image, (mouse_x - selected_card.Image.get_width() // 2, mouse_y - selected_card.Image.get_height() // 2))
        elif dragged_card:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            stockpiles.drag_card(screen, dragged_card, mouse_x, mouse_y)

        pygame.display.flip()

    except Exception as e:
        print(f"Error in game loop: {e}")
        running = False

pygame.quit()
sys.exit()
