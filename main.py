import pygame
from pygame.version import PygameVersion
import screencontroller

pygame.init()

## Loading Resources
background = screencontroller.loadImage("Resources/Images/background.jpg")
gameIcon = screencontroller.loadImage("Resources/Images/game_icon_tag.png")
italianFlagImage = screencontroller.loadImage("Resources/Images/italian_flag.png")
italianFascistLeader = screencontroller.loadImage("Resources/Images/italian_fascist_leader.jpg")



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

## Game cycle.
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    screencontroller.updateDisplay()


pygame.quit()