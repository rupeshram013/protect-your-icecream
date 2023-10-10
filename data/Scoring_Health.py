# -----------------------Protect-Yourself-Cream-------------------------------------

# Modules//
import pygame as py
from data.Canvas import *
from data.SmallCream import *
from data.Rock import *
py.init()


class Scoring_Health:

    def __init__(self):
        self.Score = 0
        self.Health = Stone.Health
        self.Font = py.font.Font("Font.ttf" , 13)
        self.ScoreImg = py.image.load("image/ScoreBar.png")
        self.HealthImg = py.image.load("image/HealthBar.png")
        self.GodImg = py.image.load("image/God.png")


    def StatScoring(self):

        if py.Rect.colliderect(Coin.rect ,Player.rect):
            self.Score += 10

            if self.Score == 100 :
                Player.Velocity = 6
                Stone.Velocity = 8
                Coin.Velocity = 8

            elif self.Score == 200 :
                Player.Velocity = 8
                Stone.Velocity = 10
                Coin.Velocity = 10     


        if self.Score >= 200 and not self.Score >= 1000 and MyMenu.Startup == True:             
            Stone.Cast1()
        if self.Score >= 500 and not self.Score >= 1000 and MyMenu.Startup == True:
            Stone.Cast2()

    def ScoreBar(self):
        Canvas.Canvas.blit(self.ScoreImg,(0,0))
        ScoreBar = self.Font.render(f"{self.Score}",True,(164,108,108))
        Canvas.Canvas.blit(ScoreBar,(55,7))
        
    def HealthBar(self):
        Canvas.Canvas.blit(self.HealthImg,(350,0))
        ScoreBar = self.Font.render(f"{Stone.Health}",True,(164,108,108))
        Canvas.Canvas.blit(ScoreBar,(410,8))
        

PlayerStats = Scoring_Health()
