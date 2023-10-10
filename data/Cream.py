# -----------------------Protect-Yourself-Cream-------------------------------------

# Modules//
import pygame as py
from data.Canvas import *
from data.Menu import *
py.init()


class Cream:

    def __init__(self):
        self.Img = py.image.load(
            "image/Cream.png")
        self.AxisX = 170
        self.AxisY = 50
        self.Velocity = 4
        self.Mass = 5
        self.IsJump = False

        self.rect = py.Rect(self.AxisX, self.AxisY, 120, 120)
        self.Img = py.transform.scale(self.Img, (60, 60))

    def Cast(self):
        self.rect = py.Rect(self.AxisX, self.AxisY, 60, 60)
        Canvas.Canvas.blit(self.Img, (self.rect.x, self.rect.y))

    def Controls(self):
        if  not py.key.get_pressed()[py.K_SPACE] and MyMenu.Startup == True:
            self.AxisY += self.Velocity

        if self.IsJump == False:
            if py.key.get_pressed()[py.K_SPACE]:
                self.IsJump = True
                self.AxisY -= self.Velocity + 2

        if self.IsJump:
            self.Force = (1 / 2)*self.Mass*(self.Velocity**2)
            self.AxisY -= self.Force
            self.Velocity = self.Velocity - 1

        if self.Velocity < 0:
            self.Mass = -1

        if self.Velocity == -6:
            self.IsJump = False
            self.Velocity = 5
            self.Mass = 1


    

Player = Cream()
