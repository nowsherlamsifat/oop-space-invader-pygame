import pygame

class Player():
    def __init__(self):
        self.image=pygame.image.load('photos/player.png')
        self.positonX=350
        self.positonY=480
        self.moveX=0
        
    def keydown_event(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                self.moveX=10
                
            if event.key==pygame.K_LEFT:
                self.moveX=-10
                
    def keyup_event(self,event):
        if event.type==pygame.KEYUP:
            self.moveX=0
            
    def movement(self):
        if self.positonX>736:
            self.positonX=736
        
        if self.positonX<0:
            self.positonX=0
        self.positonX+=self.moveX
