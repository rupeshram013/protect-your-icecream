# -----------------------Protect-Yourself-Cream-------------------------------------

# Modules//
import pygame as py
py.init()


class Display:

    def __init__(self):
        self.Weight = 450
        self.Height = 650
        self.Red = 25
        self.Green = 25
        self.Color = (self.Red, self.Green, 117)
        self.Title = "Protect-Yourself-Cream"
        self.Icon = py.image.load("image/Cream.png")
        self.Icon = py.transform.scale(self.Icon,(32,32))
        self.FrameRate = 120
        self.Running = True

    def Cast(self):
        self.Canvas = py.display.set_mode((self.Weight, self.Height))
        py.display.set_caption(self.Title)

    def FrameLimiter(self):
        self.Canvas.fill(self.Color)
        self.FrameClock = py.time.Clock()
        self.FrameClock.tick(self.FrameRate)

    def ColourMeter(self):
        self.Color = (self.Red, self.Green , 100)
        if self.Red <= 221 or self.Red <= 25:
            self.Red += 0.2
    
        if self.Green <= 205 or self.Green <= 25:
            self.Green += 0.2

Canvas = Display()
