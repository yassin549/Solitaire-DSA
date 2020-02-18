import pygame
from stack import Stack

class Tableau:
    def __init__(self, column_position):
        self.Piles = [Stack() for _ in range(7)]
        self.column_position = column_position
        
    def InitializeTableau(self, deck):
        for i in range(7):
            for j in range(i + 1):
                card = deck.Deal()
                if card is None:
                    raise ValueError("Deck ran out of cards")
                if j == i:
                    card.FlipTheCard()
                self.Piles[i].Push(card)
        return deck

    def Can_Add_Card(self, to_pile, CardToAdd):
        if to_pile.Head is None and CardToAdd.Ranks == 'K':
            return True
        if not CardToAdd:
            return False
        if not to_pile:
            return CardToAdd.Ranks == 'K'
        
        top_card = to_pile.top() 
        if not top_card:
            return False
        
        opposite_color = CardToAdd.color != top_card.color
        rank_order = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        card_to_move_index = rank_order.index(CardToAdd.Ranks)
        top_card_index = rank_order.index(top_card.Ranks)
        correct_rank = (card_to_move_index + 1 == top_card_index)
        
        return opposite_color and correct_rank

    def DisplayTableau(self):
        for i, pile in enumerate(self.Piles):
            print(f"Pile {i + 1}:")
            pile.DisplayStack()

    def GetTopCard(self, PileIndex):
        return self.Piles[PileIndex].top()

    def MoveCardToFoundation(self, FromPileIndex, foundation):
        FromPile = self.Piles[FromPileIndex]
        CardToMove = FromPile.top()

        if CardToMove and foundation.add_card(CardToMove):
            FromPile.Pop()
            NewTopCard = FromPile.top()
            if NewTopCard and not NewTopCard.FaceUp:
                NewTopCard.FlipTheCard()
            return True
        return False

    def render_tableau(self, screen):
        for col_index in range(len(self.Piles)):
            pile = self.Piles[col_index]
            current = pile.Head
            x, y = self.column_position[col_index]
            y_offset = 30
            if pile.lengthofstack(pile) > 10:
                i = 15
            i = 0
            while current:
                card = current.Data
                card_y = y + i * y_offset
                card.DisplayCard(card, screen, (x, card_y))
                current = current.Next
                i += 1

    def detect_card_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            for col_index, pile in enumerate(self.Piles):
                current = pile.Head
                i = 0
                x, y = self.column_position[col_index]
                y_offset = 30
                while current:
                    card = current.Data
                    card_rect = pygame.Rect(x, y + i * y_offset, card.Image.get_width(), card.Image.get_height())
                    if card.FaceUp and card_rect.collidepoint(mouse_x, mouse_y):
                        return col_index, card
                    current = current.Next
                    i += 1
        return None, None

    def move_card(self, from_col_index, to_col_index, card):
        if from_col_index is None or to_col_index is None:
            return False
        from_pile = self.Piles[from_col_index]
        to_pile = self.Piles[to_col_index]
        if card and card.FaceUp and self.Can_Add_Card(to_pile, card):
            cards_to_move = from_pile.RemoveFrom(card)
            if not from_pile.IsEmpty():
                from_pile.top().FlipTheCard()
            if self.Can_Add_Card(to_pile, card) and to_pile.Head is None:
                to_pile.PushStack(cards_to_move)
                return True
            
            if cards_to_move.Head:
                to_pile.PushStack(cards_to_move)
                new_top_card = from_pile.top()
                if from_pile is None:
                    from_pile.Head = None
                if new_top_card and not new_top_card.FaceUp:
                    new_top_card.FlipTheCard()
                if to_pile.top() and not to_pile.top().FaceUp:
                    to_pile.top().FlipTheCard()

                return True
        return False
