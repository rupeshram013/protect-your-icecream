# -----------------------Protect-Yourself-Cream-------------------------------------

# Modules//
import pygame as py
from data.Canvas import *
from data.Cream import *
from data.Scoring_Health import *
from data.Rock import *
py.init()


class Cone:

    def __init__(self):
        self.Img = py.image.load(
            "image/EmptyCone2.png")
        self.AxisX = 170
        self.AxisY = 540
        self.rect = py.Rect(self.AxisX,self.AxisY,120,120)  
        self.Img = py.transform.scale(self.Img, (60, 120))      

    def Cast(self):
        Canvas.Canvas.blit(self.Img, (self.rect.x, self.rect.y))

    def ConeGot(self):
        self.rect = py.Rect(self.AxisX,self.AxisY,240,240)
        if Player.rect.bottom >= self.rect.top:
            Stone.Health = 0            
        
        if py.key.get_pressed()[py.K_d] and self.AxisX <= 390:
            self.AxisX += 3
            Player.AxisX += 3
        if py.key.get_pressed()[py.K_a] and self.AxisX >= 0:
            self.AxisX -= 3
            Player.AxisX -= 3

        





Enemy = Cone()
