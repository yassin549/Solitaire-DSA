# import unittest
# from deck import Deck
# from foundation import Foundation
# from Tableau import Tableau
# from stockpile import Stockpile
# from card import Card

# class SolitaireGameTests(unittest.TestCase):
    
#     def setUp(self):
#         # Setup objects needed for each test
#         self.deck = Deck()
#         self.foundation = Foundation()
#         self.tableau = Tableau()
#         self.stockpile = Stockpile(self.deck)  # Pass the deck to Stockpile
    
#     # (rest of the tests remain the same)

        
#     # 1. Deck and Card Tests
#     def test_deck_initialization(self):
#         # Check deck has 52 cards initially
#         self.assertEqual(len(self.deck.cards), 52)
    
#     def test_deck_shuffling(self):
#         # Shuffle and ensure order is different
#         original_order = self.deck.cards[:]
#         self.deck.shuffle()
#         self.assertNotEqual(original_order, self.deck.cards)
    
#     def test_deck_drawing(self):
#         # Draw a card and ensure deck size decreases
#         initial_size = len(self.deck.cards)
#         card = self.deck.draw()
#         self.assertEqual(len(self.deck.cards), initial_size - 1)
#         self.assertIsInstance(card, Card)
    
#     # 2. Foundation Tests
#     def test_add_card_to_foundation(self):
#         # Adding a valid starting Ace to foundation
#         ace_card = Card("hearts", 1)
#         self.foundation.add_card(ace_card)
#         self.assertEqual(self.foundation.piles["hearts"].peek(), ace_card)
    
#     def test_invalid_card_to_foundation(self):
#         # Attempting to add an invalid card (non-Ace to empty foundation)
#         non_ace_card = Card("hearts", 5)
#         with self.assertRaises(ValueError):
#             self.foundation.add_card(non_ace_card)
    
#     def test_complete_foundation(self):
#         # Adding cards in sequence to check completion condition
#         for rank in range(1, 14):
#             self.foundation.add_card(Card("hearts", rank))
#         self.assertTrue(self.foundation.is_game_complete())
    
#     # 3. Tableau Tests
#     def test_tableau_initial_setup(self):
#         # Check tableau has cards arranged as per Solitaire rules
#         self.tableau.add_initial_cards(self.deck)
#         for i, pile in enumerate(self.tableau.piles):
#             self.assertEqual(len(pile), i + 1)
#             self.assertTrue(pile.peek().face_up)
    
#     def test_valid_tableau_move(self):
#         # Attempting a valid move in tableau
#         card1 = Card("hearts", 5)
#         card2 = Card("spades", 6)
#         card2.flip()
#         self.tableau.piles[0].push(card1)
#         self.tableau.piles[1].push(card2)
#         self.tableau.move_card(0, 1)
#         self.assertEqual(self.tableau.piles[1].peek(), card1)
    
#     def test_invalid_tableau_move(self):
#         # Attempting an invalid move in tableau
#         card1 = Card("hearts", 5)
#         card2 = Card("hearts", 6)
#         self.tableau.piles[0].push(card1)
#         self.tableau.piles[1].push(card2)
#         with self.assertRaises(ValueError):
#             self.tableau.move_card(0, 1)
    
#     # 4. Stockpile Tests
#     def test_draw_from_stockpile(self):
#         # Draw a card and check stockpile behavior
#         self.stockpile.add_stockpile(self.deck)
#         initial_size = len(self.stockpile.drawn_cards)
#         self.stockpile.draw_card()
#         self.assertEqual(len(self.stockpile.drawn_cards), initial_size + 1)
    
#     def test_recycle_stockpile(self):
#         # Test recycling when stockpile is empty
#         self.stockpile.add_stockpile(self.deck)
#         for _ in range(len(self.deck.cards)):
#             self.stockpile.draw_card()
#         self.stockpile.recycle_stockpile()
#         self.assertTrue(len(self.stockpile.stock_cards) > 0)
    
#     def test_empty_stockpile_draw(self):
#         # Attempting to draw from an empty stockpile
#         with self.assertRaises(ValueError):
#             self.stockpile.draw_card()
    
# if __name__ == "__main__":
#     unittest.main()
