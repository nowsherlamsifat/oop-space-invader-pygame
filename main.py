import pygame,sys,random
from game_settings import Game_settings
from player_info import Player
from bullet_info import Bullet
from enemy_info import Enemy

gs=Game_settings()
player=Player()
bullet=Bullet()
enemy=Enemy()

pygame.init()


screen=pygame.display.set_mode((gs.width,gs.height))
pygame.display.set_caption(gs.title)

while True:
    screen.blit(gs.bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            
        player.keydown_event(event)
        player.keyup_event(event)
        bullet.bullet_keydown(event,player.positonX)
        
        
    
    """bullet"""
    screen.blit(bullet.image,(bullet.positionX+16,bullet.positionY))
    bullet.movement()
    bullet.reload()
    
    """player"""
    screen.blit(player.image,(player.positonX,player.positonY))
    player.movement()
    
    """enemy"""
    enemy.create_multiple_enemy()
    enemy.show_multiple_enemy(screen,bullet)
    
    pygame.display.update()
