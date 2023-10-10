# -----------------------Protect-Yourself-Cream-------------------------------------

# Modules//
import pygame as py
from data.Canvas import *
py.init()


class Menu:

    def __init__(self):
        self.Color = (25,25,117)
        self.Startup = False
        self.Font = py.font.Font("Font.ttf",24)
        self.Img = py.image.load("image/StartMenu.png")

    def Casting(self):

        if self.Startup == False:            
            Canvas.Canvas.blit(self.Img,(0,0))

            if py.mouse.get_pressed()[0]:
                py.display.set_icon(Canvas.Icon)
                self.Startup = True


MyMenu = Menu()