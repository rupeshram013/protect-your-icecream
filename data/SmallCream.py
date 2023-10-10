# -----------------------Protect-Yourself-Cream-------------------------------------

# Modules//
import pygame as py
import random as ran
from data.Canvas import *
from data.Cream import *
from data.Menu import *
py.init()


class Cream:

    def __init__(self):
        self.Img = py.image.load(
            "image/Points.png")
        self.AxisX = ran.randint(1,400)
        self.AxisY = 0
        self.rect = py.Rect(self.AxisX,self.AxisY,120,120)        
        self.Img = py.transform.scale(self.Img, (40, 40))
        self.Effect = py.mixer.Sound("audio/Effect.mp3")
        self.Velocity = 6

    def Cast(self):
        self.rect = py.Rect(self.AxisX,self.AxisY,50,50) 
        Canvas.Canvas.blit(self.Img, (self.rect.x, self.rect.y))
       
        if self.AxisY <= 600 and MyMenu.Startup == True:
            self.AxisY += self.Velocity
            
        if py.Rect.colliderect(self.rect,Player.rect) or self.AxisY >= 600 and MyMenu.Startup == True:
            if py.Rect.colliderect(self.rect,Player.rect):
                py.mixer.Sound.play(self.Effect)
            else:
                py.mixer.Sound.stop(self.Effect)

            self.AxisY = -50
            self.AxisX = ran.randint(1,400)
        
        



   


Coin = Cream()
