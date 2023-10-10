# -----------------------Protect-Yourself-Cream-------------------------------------

# Modules//
import pygame as py
from data.Canvas import *
from data.Rock import *
from data.Scoring_Health import *
from data.Menu import *
from data.Cream import *
py.init()


class Menu:

    def __init__(self):
        self.Color = (25,25,117)
        self.Startup = False
        self.Font = py.font.Font("Font.ttf",34)
        self.Img = py.image.load("image/ExitMenu.png")

    def Casting(self):

        if Stone.Health <= 0 :            
            Canvas.Canvas.blit(self.Img,(0,0))
            ScoringBar = self.Font.render(f"{PlayerStats.Score}",True,(151,151,254))
            Canvas.Canvas.blit(ScoringBar,(250,157))
            MyMenu.Startup = False
            if PlayerStats.Score >= 1000:
                Canvas.Canvas.blit(PlayerStats.GodImg,(0,0))

            if py.mouse.get_pressed()[0]:
                Player.AxisY = 0
                Stone.Health = 100
                PlayerStats.Score = 0
                MyMenu.Startup = True           


            if py.key.get_pressed()[py.K_ESCAPE]:
                Canvas.Running = False
        

MyExit = Menu()