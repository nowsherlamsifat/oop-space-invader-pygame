import pygame,random,math

class Enemy():
    def __init__(self):
        self.number=6
        self.image=[]
        self.positionX=[]
        self.positionY=[]
        self.moveX=[]
        self.moveY=[]
        
    def create_multiple_enemy(self):
        for i in range(self.number):
            self.image.append(pygame.image.load('photos/alien.png'))
            self.positionX.append(random.randint(0,735))
            self.positionY.append(random.randint(20,200))
            self.moveX.append(5)
            self.moveY.append(20)
        
        
    def movement(self,i):
        if self.positionX[i]>736:
            self.moveX[i]*=-1
            self.positionY[i]+=self.moveY[i]
            
        if self.positionX[i]<0:
            self.moveX[i]*=-1
            self.positionY[i]+=self.moveY[i]
        
        self.positionX[i]+=self.moveX[i]
        
    def enemy_collision(self,enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow((enemyX-bulletX), 2)) +
                            (math.pow((enemyY-bulletY), 2)))
        if distance < 27:
            return True
        else:
            return False
    
    def check_collision(self,bulletX,bulletY,bullet):
        for i in range(self.number):
            collision=self.enemy_collision(self.positionX[i],self.positionY[i],bulletX,bulletY)
            
            if collision:
                    bullet.bullet_state='ready'
                    self.positionX[i]=random.randint(0,735)
                    self.positionY[i]=random.randrange(20,300)
    
    def show_multiple_enemy(self,screen,bullet):
        
        for i in range(self.number):
            screen.blit(self.image[i],(self.positionX[i],self.positionY[i]))
            self.movement(i)
            self.enemy_collision(self.positionX[i],self.positionX[i],bullet.positionX,bullet.positionY)
            self.check_collision(bullet.positionX,bullet.positionY,bullet)
