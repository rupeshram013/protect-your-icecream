# -----------------------Protect-Yourself-Cream-------------------------------------

# Modules//
import pygame as py
import random as ran
from data.Cream import *

py.init()


class Rock:

    def __init__(self):
        self.Img = py.image.load(
            "image/Stone.png")
        self.AxisX1 = ran.randint(1,200)
        self.AxisX2 = ran.randint(200,400)
        self.AxisY1 = 0
        self.AxisY2 = 0
        self.rect1 = py.Rect(self.AxisX1,self.AxisY1,120,120)        
        self.rect2 = py.Rect(self.AxisX2,self.AxisY2,120,120)        
        self.Img = py.transform.scale(self.Img, (40, 40))
        self.Effect = py.mixer.Sound("audio/Effect2.mp3")
        self.Velocity = 6

        self.Health = 100

    def Cast1(self):
        self.rect1 = py.Rect(self.AxisX1,self.AxisY1,50,50) 
        Canvas.Canvas.blit(self.Img, (self.rect1.x, self.rect1.y))

        if self.AxisY1 <= 600:
            self.AxisY1 += self.Velocity
        
        if self.AxisY1 >= 600:
            self.AxisY1 = -50
            self.AxisX1 = ran.randint(1,400)
        if py.Rect.colliderect(self.rect1,Player.rect) and MyMenu.Startup == True:
            self.Health -= 10
            self.AxisY1 = -50
            self.AxisX1 = ran.randint(1,400)
            py.mixer.Sound.play(self.Effect)
        

    def Cast2(self):
        self.rect2 = py.Rect(self.AxisX2,self.AxisY2,50,50) 
        Canvas.Canvas.blit(self.Img, (self.rect2.x, self.rect2.y))

        if self.AxisY2 <= 600:
            self.AxisY2 += self.Velocity
        
        if self.AxisY2 >= 600:
            self.AxisY2 = -50
            self.AxisX2 = ran.randint(1,400)

        if py.Rect.colliderect(self.rect2,Player.rect) and MyMenu.Startup == True:
            py.mixer.Sound.play(self.Effect)
            self.Health -= 10
            self.AxisY2 = -50
            self.AxisX2 = ran.randint(1,400)
        
Stone = Rock()
