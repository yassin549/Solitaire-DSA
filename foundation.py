import pygame
class Foundation:
    def __init__(self, suit):
        self.suit = suit
        self.cards = [] 
        self.rank_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def add_card(self, card):
        if self.can_add_card(card):
            self.cards.append(card)
            return True
        return False
    def move_card(self, from_col_index, card, Piles):
        if from_col_index is None:
            return False
        from_pile = Piles[from_col_index]
        if from_pile.top()!=card:
            return False, Piles
        if card and card.FaceUp and self.can_add_card(card):
            cards_to_move = from_pile.RemoveFrom(card)
            if cards_to_move.Head:
                new_top_card = from_pile.top()
                if from_pile is None:
                    from_pile.Head=None
                if new_top_card and not new_top_card.FaceUp:
                    new_top_card.FlipTheCard()
                self.add_card(card)
                return True, Piles
        return False, Piles
    def can_add_card(self, card):
        
        if not self.cards:
            return card.Suits == self.suit and card.Ranks == 'A'
        expected_rank = self.rank_order[len(self.cards)]
        return card.Suits == self.suit and card.Ranks == expected_rank
    def is_complete(self):
        return len(self.card) == 13
    
    def __repr__(self):
        return f"Foundation({self.suit}): {self.cards}"
    def display_single_foundation(self,screen, foundation, foundation_position):
        font = pygame.font.SysFont(None, 18)
        suit_colors = {
            "Heart": (255, 0, 0),
            "Diamond": (255, 0, 0),
            "Clubs": (0, 0, 0),
            "Spades": (0, 0, 0)
        }

        foundation_x, foundation_y = foundation_position
        if foundation.cards:
            top_card = foundation.cards[-1]
            card_image = top_card.Image
            screen.blit(card_image, (foundation_x, foundation_y))