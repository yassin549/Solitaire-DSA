import os
import pygame
class Card:
    def __init__(self, Suits, Ranks,FaceUp=False):
        self.Ranks = Ranks
        self.Suits = Suits
        self.FaceUp = FaceUp
        self.Image = self.LoadImage()
        self.BackImage=self.LoadBackImage()
        self.color = 'red' if self.Suits in ['Heart', 'Diamond'] else 'black'
    def FlipTheCard(self):
        if self.FaceUp:
            return
        self.FaceUp = True
    def LoadImage(self):
        ImagePath=f"Lib/{self.Ranks}_of_{self.Suits}.png"
        try:
            image = pygame.image.load(ImagePath)
        except pygame.error as e:
            print(f"Error loading image: {e}")

        resized=pygame.transform.scale(image, (80, 120))
        return resized
    def create_rounded_image(image, radius):
        rounded_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        rounded_image = rounded_image.convert_alpha()
        pygame.draw.rect(rounded_image, (255, 255, 255, 0), (0, 0, *image.get_size()))
        rect = pygame.Rect(0, 0, *image.get_size())
        pygame.draw.rect(rounded_image, (255, 255, 255), rect, border_radius=radius)
        mask = pygame.mask.from_surface(rounded_image)
        for x in range(rect.width):
            for y in range(rect.height):
                if mask.get_at((x, y)):
                    rounded_image.set_at((x, y), image.get_at((x, y)))

        return rounded_image
    def LoadBackImage(self):
        ImagePath = os.path.join("Lib", "backside.png")
        image=pygame.image.load(ImagePath)
        resized=pygame.transform.scale(image, (80, 120))
        return resized
    def Display(self):
        if self.FaceUp:
            return f"{self.Ranks} of {self.Suits}"
        else:
            return "Face down"
    def DisplayImage(self):
        return self.Image
    def DisplayCard(self, card, screen, position):
        if card.FaceUp:
            screen.blit(card.Image, position)
        else:
            screen.blit(card.BackImage, position)
def create_rounded_image(image, radius):
        rounded_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        rounded_image = rounded_image.convert_alpha()
        pygame.draw.rect(rounded_image, (255, 255, 255, 0), (0, 0, *image.get_size()))
        rect = pygame.Rect(0, 0, *image.get_size())
        pygame.draw.rect(rounded_image, (255, 255, 255), rect, border_radius=radius)
        mask = pygame.mask.from_surface(rounded_image)
        for x in range(rect.width):
            for y in range(rect.height):
                if mask.get_at((x, y)):
                    rounded_image.set_at((x, y), image.get_at((x, y)))

        return rounded_image