import pygame
import pygame.freetype  # Import the freetype module.
from window import Window
from dialog import Dialog

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
GAME_FONT = pygame.freetype.Font("Champignon.ttf", 24)
running = True

#Dragging item
dragging = False
draggingStartXPosition = 0
draggingStartYPosition = 0
mouseX = 0
mouseY = 0

def removeItem(items, mouseX, mouseY):
    for item in items:
        if isinstance(item, Window):
            if item.shouldRemoveItem(mouseX, mouseY):
                items.remove(item)
                return

def computeDeltaAndDragItem():
    pass

def dragItem(items, deltaX, deltaY):
    for item in items:
        if isinstance(item, Window):
            if item.shouldDragItem(mouseX, mouseY):
                item.move(item.start[0] + deltaX, item.start[1] + deltaY)
                item.activate(True)
                return

#########
# Init scene
#########
itemsToDraw = []
d1 = Dialog((40, 40), "Hello World")
itemsToDraw.append(d1)

#########
# Main Loop
#########

while running:

    mouseX, mouseY = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and dragging:
            dragging = False
        if event.type == pygame.MOUSEBUTTONDOWN and not dragging:
            dragging = True
            draggingStartXPosition = mouseX
            draggingStartYPosition = mouseY

    if click != (0, 0, 0):
        removeItem(itemsToDraw, mouseX, mouseY)

        if dragging:
            draggingDeltaX = mouseX - draggingStartXPosition
            draggingDeltaY = mouseY - draggingStartYPosition
            if (draggingDeltaX != 0 or draggingDeltaY != 0):
                dragItem(itemsToDraw, draggingDeltaX, draggingDeltaY)
                draggingDeltaX = 0
                draggingDeltaY = 0
            draggingStartXPosition = mouseX
            draggingStartYPosition = mouseY
        else:
            pass
    else:
        pass


    

    screen.fill((255, 255, 255))

    for itemToDraw in itemsToDraw:
        itemToDraw.draw(screen, GAME_FONT)

    # You can use `render` and then blit the text surface ...
    # or just `render_to` the target surface.
    #GAME_FONT.render_to(screen, (40, 350), "Hello World!", (0, 0, 0))

    pygame.display.flip()

pygame.quit()
