# import time
# from deck import Deck
# from foundation import Foundation
# from Tableau import Tableau
# from stockpile import Stockpile
# from card import Card


# class SolitaireCLI:
#     def __init__(self):
#         self.deck = Deck()
#         self.foundation = Foundation()
#         self.tableau = Tableau()
#         self.stockpile = Stockpile(self.deck)
#         self.game_complete = False
#         self.setup_game()

#     def setup_game(self):
#         self.tableau.add_initial_cards(self.deck)
#         print("\nWelcome to Solitaire!")
#         print("Game has been set up.")

#     def display_board(self):
#         """Display the current board state to the user."""
#         print("\nCurrent Solitaire Board:")
#         print("\nFoundation:")
#         for suit, pile in self.foundation.piles.items():
#             print(f"{suit.capitalize()}: {pile.top()}")

#         print("\nTableau:")
#         for i, pile in enumerate(self.tableau.piles):
#             print(f"Pile {i+1}: {pile.peek()}")

#         print("\nStockpile: ", "Empty" if not self.stockpile.stock_cards else f"Cards left: {len(self.stockpile.stock_cards)}")

#     def prompt_user(self):
#         """Prompt the user for their next action."""
#         print("\nWhat would you like to do?")
#         print("1. Draw card from Stockpile (D)")
#         print("2. Move card (M)")
#         print("3. Recycle Stockpile (R)")
#         print("4. Exit Game (E)")

#         user_input = input("Enter your choice (D/M/R/E): ").upper()
#         return user_input

#     def draw_from_stockpile(self):
#         """Draw a card from the stockpile."""
#         if self.game_complete:
#             print("Congratulations! You've completed the game!")
#             return
        
#         try:
#             card = self.stockpile.draw_card()
#             print(f"You drew: {card}")
#         except ValueError:
#             print("The stockpile is empty!")

#     def move_card(self):
#         # Prompt the user to choose two piles to move the card between
#         print("\nSelect the pile to move from (1 to 7):")
#         from_pile_index = int(input()) - 1  # Convert to 0-based index
#         print("Select the pile to move to (1 to 7):")
#         to_pile_index = int(input()) - 1  # Convert to 0-based index

#         # Validate if the move is possible
#         if 0 <= from_pile_index < 7 and 0 <= to_pile_index < 7:
#             success = self.tableau.move_card(from_pile_index, to_pile_index)
#             if success:
#                 print(f"Successfully moved card from pile {from_pile_index + 1} to pile {to_pile_index + 1}.")
#             else:
#                 print("Invalid move. Please check the rules.")
#         else:
#             print("Invalid pile selection. Please choose piles between 1 and 7.")

#     def recycle_stockpile(self):
#         """Recycle the stockpile if all cards have been drawn."""
#         if self.game_complete:
#             print("Congratulations! You've completed the game!")
#             return

#         try:
#             self.stockpile.recycle_stockpile()
#             print("Stockpile has been recycled.")
#         except ValueError:
#             print("There are no drawn cards to recycle.")

#     def check_for_game_completion(self):
#         """Check if the game is complete (foundation has all 4 suits)."""
#         if all(pile.size() == 13 for pile in self.foundation.piles.values()):
#             self.game_complete = True
#             print("\nYou have completed the game!")
#             return True
#         return False

#     def run(self):
#         """Main game loop."""
#         while not self.game_complete:
#             self.display_board()
#             action = self.prompt_user()

#             if action == 'D':
#                 self.draw_from_stockpile()
#             elif action == 'M':
#                 self.move_card()
#             elif action == 'R':
#                 self.recycle_stockpile()
#             elif action == 'E':
#                 print("Exiting game. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")
            
#             self.check_for_game_completion()
#             time.sleep(1)  # Slow down the game loop for better readability in the CLI

# # Start the game
# if __name__ == "__main__":
#     game = SolitaireCLI()
#     game.run()
