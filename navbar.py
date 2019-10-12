import pygame
import ui

class NavBar:

    windowHeaderSize = 20
    crossSize = 15
    active = False

    def __init__(self, start, size):
        self.start = start
        self.size = size

    def drawCross(self, screen, color, start, size):
        #Left
        ui.drawLine(screen, color, start, size)
        ui.drawLine(screen, color, (start[0]-1, start[1]), (size[0]-1, size[1]))
        ui.drawLine(screen, color, (start[0]-2, start[1]), (size[0]-2, size[1]))
        #Right
        ui.drawLine(screen, color, (start[0], size[1]), (size[0], start[1]))
        ui.drawLine(screen, color, (start[0]-1, size[1]), (size[0]-1, start[1]))
        ui.drawLine(screen, color, (start[0]-2, size[1]), (size[0]-2, start[1]))

    def draw(self, screen, color):
        if self.active:
            GREEN_ACTIVE = pygame.Color(0, 219, 109)
            pygame.draw.rect(screen, GREEN_ACTIVE, pygame.Rect((self.start[0], self.start[1] + 1), (self.size[0] , self.windowHeaderSize)))
        
        #Top NavBar
        ui.drawLine(screen, color, (self.start[0], self.start[1]), (self.start[0] + self.size[0], self.start[1]))
        #Bottom NavBar
        ui.drawLine(screen, color, (self.start[0], self.start[1] + self.windowHeaderSize), (self.start[0] + self.size[0], self.start[1] + self.windowHeaderSize))

        RED = pygame.Color(242, 157, 180)
        if self.active:
            RED = pygame.Color(234, 37, 7)
        pygame.draw.rect(screen, RED, pygame.Rect((self.start[0], self.start[1] + 1), (self.windowHeaderSize -1 , self.windowHeaderSize -1)))
        self.drawCross(screen, color, (self.start[0] + 5, self.start[1] + 5), (self.start[0] + self.crossSize, self.start[1] + self.crossSize))
    
    def shouldRemoveItem(self, mouseX, mouseY):
        return (self.start[0] < mouseX and self.start[0]+ self.windowHeaderSize > mouseX
        and self.start[1] < mouseY and self.start[1]+ self.windowHeaderSize > mouseY)

    def move(self, mouseX, mouseY):
        self.start = (mouseX, mouseY)

    def activate(self, boolean):
        self.active = boolean
