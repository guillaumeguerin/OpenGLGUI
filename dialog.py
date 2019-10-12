from window import Window
import pygame

class Dialog(Window):

    def __init__(self, start, text):
        size = (self.widthMarginSize * 2 + len(text) * self.fontSize, self.heightMarginSize * 4)
        super().__init__(start, size)
        self.text = text

    def writeText(self, screen, font, text, posX, posY):
        text_surface, rect = font.render(text, (0, 0, 0))
        screen.blit(text_surface, (self.start[0] + posX, self.start[1] + posY))
    
    def draw(self, screen, font):
        super().draw(screen, self.start, self.size)
        self.writeText(screen, font, self.text, self.widthMarginSize, 2 * self.windowNavBar.windowHeaderSize)