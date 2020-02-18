from stack import Stack
import pygame
class Stockpile:
    def __init__(self, deck):
        self.Cards = deck.Cards[:]
        self.DrawnCards = []
        self.CurrentDrawIndex = 0

    def DrawOneCard(self):
        if not self.Cards and self.DrawnCards:
            self.RecycleDrawnCards()

        if self.Cards:
            DrawnCard = self.Cards.pop(0)
            DrawnCard.FlipTheCard()
            self.DrawnCards.append(DrawnCard)
            self.CurrentDrawIndex = len(self.DrawnCards) - 1
            return DrawnCard
        elif self.DrawnCards:
            self.CurrentDrawIndex = (self.CurrentDrawIndex + 1) % len(self.DrawnCards)
            return self.DrawnCards[self.CurrentDrawIndex]
        return None

    def RecycleDrawnCards(self):
        self.Cards = self.DrawnCards[:]
        self.DrawnCards = []
        self.CurrentDrawIndex = 0

    def MoveCardToTableau(self, tableau, pile_index):
        if not self.DrawnCards:
            return False

        CardToMove = self.DrawnCards[self.CurrentDrawIndex]
        if tableau.Can_Add_Card(pile_index, CardToMove):
            self.DrawnCards.pop(self.CurrentDrawIndex)
            tableau.piles[pile_index].push(CardToMove)
            return True
        return False
    def PrintStockPile(self, screen, stockPile):

        font = pygame.font.SysFont(None, 16) 
        Pile=['StockPile', 'WastePile']
        for i, suit in enumerate(Pile):
            if len(stockPile.Cards)>0 and i==0:
                screen.blit(stockPile.Cards[0].BackImage, ((50+i*100), 20))
                continue
            if len(stockPile.DrawnCards)>0 and i==1:
                screen.blit(stockPile.DrawnCards[-1].Image, ((50+i*100), 20))
                continue
            pygame.draw.rect(screen, (0, 0, 0), ((50 + i * 100), 20, 80, 120), 2)

            text_color = (0, 0, 0) 
            text = font.render(suit, True, text_color)
            text_rect = text.get_rect(center=(50 + i * 100 + 40, 20 + 60))
            screen.blit(text, text_rect)
    def detect_stockpile_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos

            stock_pile_rect = pygame.Rect(50, 20, 80, 120)
            waste_pile_rect = pygame.Rect(150, 20, 80, 120)
            if stock_pile_rect.collidepoint(mouse_x, mouse_y):
                return "StockPile"
            if waste_pile_rect.collidepoint(mouse_x, mouse_y):
                return "WastePile"

        return None
    def get_top_card_from_wastepile_click(self, event, stockpile):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked_area = stockpile.detect_stockpile_click(event)
            if clicked_area == "WastePile" and stockpile.DrawnCards:
                return stockpile.DrawnCards[-1]
        return None
    def start_drag(self, event, stockpile):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked_area = stockpile.detect_stockpile_click(event)
            if clicked_area == "WastePile" and stockpile.DrawnCards:
                return stockpile.DrawnCards[-1]
        return None
    def drag_card(self, screen, card, mouse_x, mouse_y):
        if card:
            screen.blit(card.Image, (mouse_x - card.Image.get_width() // 2, mouse_y - card.Image.get_height() // 2))
    def place_card(self, event, dragged_card, tableau, foundation):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_x, mouse_y = event.pos
            card_width = dragged_card.Image.get_width() 
            card_height = dragged_card.Image.get_height()
            for i, pile in enumerate(tableau.Piles):
                x, y = tableau.column_position[i]
                pile_rect = pygame.Rect(x, y, card_width, card_height)
                pile_rect.height = max(card_height, 500)
                if pile_rect.collidepoint(mouse_x, mouse_y) and tableau.Can_Add_Card(pile, dragged_card):
                    pile.Push(dragged_card)
                    self.DrawnCards.pop() 
                    return True
            for i, foundation_pile in enumerate(foundation.piles):
                pile_rect = pygame.Rect(foundation_pile.x, foundation_pile.y, foundation_pile.width, foundation_pile.height)
                if pile_rect.collidepoint(mouse_x, mouse_y) and foundation.Can_Add_Card(i, dragged_card):
                    foundation.piles[i].push(dragged_card)
                    self.DrawnCards.pop()
                    return True

        return False
    def place_card(self, event, dragged_card, tableau, foundations, foundation_positions):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_x, mouse_y = event.pos
            card_width = dragged_card.Image.get_width()
            card_height = dragged_card.Image.get_height()
            for i, pile in enumerate(tableau.Piles):
                x, y = tableau.column_position[i]
                pile_rect = pygame.Rect(x, y, card_width, card_height)
                
                pile_rect.height = max(card_height, 500)
                if pile_rect.collidepoint(mouse_x, mouse_y) and tableau.Can_Add_Card(pile, dragged_card):
                    dragged_card.FaceUp=True
                    pile.Push(dragged_card)
                    self.DrawnCards.pop()
                    return True
            for i, foundation in enumerate(foundations):
                foundation_x, foundation_y = foundation_positions[i]
                pile_rect = pygame.Rect(foundation_x, foundation_y, card_width, card_height)

                if pile_rect.collidepoint(mouse_x, mouse_y) and foundation.can_add_card(dragged_card):
                    foundation.add_card(dragged_card)
                    self.DrawnCards.pop()
                    return True

        return False
