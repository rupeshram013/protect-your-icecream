# -----------------------Protect-Yourself-Cream-------------------------------------

# Modules//
import pygame as py
from data.Menu import *
from data.Canvas import *
from data.Cone import *
from data.Cream import *
from data.Scoring_Health import *
from data.Rock import *
from data.SmallCream import *
from data.Exit import *


if __name__ == "__main__":
    py.init()
    py.display.set_icon(Canvas.Icon)

    py.mixer.music.load("audio/Theme.mp3")
    py.mixer.music.play(-1)

    def Stats():
        PlayerStats.StatScoring()

        PlayerStats.ScoreBar()
        PlayerStats.HealthBar()

    
    Canvas.Cast()
    
    def MainDisplay():
        Canvas.FrameLimiter()
        if MyMenu.Startup == True:
            Canvas.ColourMeter()

    def MainSmallCream():
        Coin.Cast()

    def MainEnemy():
        Enemy.Cast()
        Enemy.ConeGot()

    def MainPlayer():
        Player.Cast()
        Player.Controls()

    def Loop():
        while Canvas.Running:
            for Event in py.event.get():
                if Event.type == py.QUIT:
                    Canvas.Running = False

            MainDisplay()
            MainEnemy()
            MainPlayer()
            MainSmallCream()
            Stats()
            MyMenu.Casting()
            MyExit.Casting()

            py.display.update()

        py.quit()

    Loop()
