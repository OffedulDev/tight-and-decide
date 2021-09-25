import pygame
from pygame.version import PygameVersion
import screencontroller
import classEditor

pygame.init()

## Loading Resources
background = screencontroller.loadImage("Resources/Images/background.jpg")
gameIcon = screencontroller.loadImage("Resources/Images/game_icon_tag.png")
italianFlagImage = screencontroller.loadImage("Resources/Images/italian_flag.png")
italianFascistLeader = screencontroller.loadImage("Resources/Images/italian_fascist_leader.jpg")
clock = pygame.time.Clock()


## Transforming Resources in passable classes.

gameIconReference = screencontroller.makeInstanceReference(gameIcon, 0, 0)
italianFlagImageReference = screencontroller.makeInstanceReference(italianFlagImage, 100, 120)
italianFascistLeaderReference = screencontroller.makeInstanceReference(italianFascistLeader, 100, 120)
backgroundReference = screencontroller.makeInstanceReference(background, 0, 0)

## Inserting Resources into Game without Updating Screen
screencontroller.insertBackground(backgroundReference)

## Adjustments to the game window
screencontroller.setIcon(gameIconReference)
screencontroller.addCaption("Tight and Decide [1920x1080]")
classEditor.changeName(backgroundReference, "Peppino non Mangia Carote")

## Game cycle.
running = True
clicked = False 
type_ = 0 


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not clicked: screencontroller.drawImage(italianFlagImageReference)
    
    screencontroller.updateDisplay()
    ## Mouse Button Press
    left, middle, right = pygame.mouse.get_pressed()
    
    if middle:
        screencontroller.fixedInfoDisplay()
        clock.tick(2)

    if left:
        screencontroller.makeFont(
            "Verdana",
            14,
            "This is a text that was created with your left click!",
            False,
            False,
            (234, 45, 65),
            100,
            100,
            backgroundReference
            )
        classEditor.changeName(backgroundReference, "Peppino Mangia Carote")
        clock.tick(5)

    else:
        continue

        


pygame.quit()
