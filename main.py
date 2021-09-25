import pygame
from pygame.version import PygameVersion
import screencontroller
import classEditor

pygame.init()

## Loading Resources
background = screencontroller.loadImage("Resources/Images/background.jpg")
background = pygame.transform.scale(background, (1280, 780))
toggleMapNotification = screencontroller.loadImage("Resources/Images/tpmvn.png")
toggleMapNotification = pygame.transform.scale(toggleMapNotification, (230, 80))
gameIcon = screencontroller.loadImage("Resources/Images/game_icon_tag.png")
italianFlagImage = screencontroller.loadImage("Resources/Images/italian_flag.png")
vectorialMap = screencontroller.loadImage("Resources/Images/vectorial-map.png")
vectorialMap = pygame.transform.scale(vectorialMap, (1250, 750))
italianFlagImage = pygame.transform.scale(italianFlagImage, (88, 88))
italianFascistLeader = screencontroller.loadImage("Resources/Images/italian_fascist_leader.jpg")
clock = pygame.time.Clock()


## Transforming Resources in passable classes.

gameIconReference = screencontroller.makeInstanceReference(gameIcon, 0, 0)
italianFlagImageReference = screencontroller.makeInstanceReference(italianFlagImage, 10, 680, "Italian Flag Bottom")
italianFascistLeaderReference = screencontroller.makeInstanceReference(italianFascistLeader, 100, 120, "italian Leader Image")
backgroundReference = screencontroller.makeInstanceReference(background, 0, 0, "Background Image")
toggleMapReference = screencontroller.makeInstanceReference(toggleMapNotification, 1050, 10, "Toggle Map Notification")
vectorialMapReference = screencontroller.makeInstanceReference(vectorialMap, 25, -15, "Vectorial Map")

## Inserting Resources into Game without Updating Screen
screencontroller.insertBackground(backgroundReference)

## Adjustments to the game window
screencontroller.setIcon(gameIconReference)
screencontroller.addCaption("Tight and Decide [1280x728]")
classEditor.changeName(backgroundReference, "Background")
screencontroller.drawImage(italianFlagImageReference)


## Game cycle.
running = True
clicked = False 
type_ = 0 
isMapChanged = False

while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    
    screencontroller.updateDisplay()
    ## Mouse Button Press
    left, middle, right = pygame.mouse.get_pressed()
    
    if middle:
        screencontroller.fixedInfoDisplay()
    
    if right:
        if not isMapChanged:
            isMapChanged = True
            screencontroller.drawImage(vectorialMapReference)
            screencontroller.drawImage(toggleMapReference)
        else:
            isMapChanged = False
            screencontroller.drawImage(backgroundReference)
            

pygame.quit()
