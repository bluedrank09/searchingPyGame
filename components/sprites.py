import pygame

#creating ryan sprite
# class Ryan(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load('graphics/ryan/ryan1.png').convert_alpha()
#         self.rect = self.image.get_rect(midbottom = (80, 300))

#creating vampire sprite
class Vampire(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        _vampire = pygame.image.load('graphics/vampire/vampire.png').convert_alpha() 
        self.image = pygame.transform.scale(_vampire, (_vampire.get_width()-88, _vampire.get_height()-200))
        #print(f"vampire  width is {_vampire.get_width()} height is {_vampire.get_height()}")
        self.rect = self.image.get_rect(midbottom = (80, 200))  

    def update(self, event_type):
        print(f"Updating vampire")
        if event_type == 1 :

            if self.rect.x < 529:
                self.rect.x += 10

            if self.rect.y < 400: 
                self.rect.y += 10

#creating diamond sprite
class Diamond(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        _diamond = pygame.image.load('graphics/diamond/diamond.png').convert_alpha()
        self.image = pygame.transform.scale(_diamond, (_diamond.get_width()-1729, _diamond.get_height()-1387))
        #print(f"diamond width is {_diamond.get_width()} height is {_diamond.get_height()}")
        self.rect = self.image.get_rect(midbottom = (100,570))
         
#creating bluegem sprite
class BlueGem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        _bluegem = pygame.image.load('graphics/blueGem/diamond_blue.png').convert_alpha()
        self.image = pygame.transform.scale(_bluegem, (_bluegem.get_width()-1699, _bluegem.get_height()-1357))
        #print(f"bluegem width is {_bluegem.get_width()} height is {_bluegem.get_height()}")
        self.rect = self.image.get_rect(midbottom = (225,570)) 

#creating purplegem sprite
class PurpleGem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        _purplegem = pygame.image.load('graphics/purpleGem/diamond_violet.png').convert_alpha()
        self.image = pygame.transform.scale(_purplegem, (_purplegem.get_width()-1684, _purplegem.get_height()-1342))
        #print(f"purplegem width is {_purplegem.get_width()} height is {_purplegem.get_height()}")
        self.rect = self.image.get_rect(midbottom = (370,570))  
                                             

#creating redgem sprite
class RedGem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        _redgem = pygame.image.load('graphics/redGem/diamond_red.png').convert_alpha()
        self.image = pygame.transform.scale(_redgem, (_redgem.get_width()-1668, _redgem.get_height()-1326))
        #print(f"redgem width is {_redgem.get_width()} height is {_redgem.get_height()}")
        self.rect = self.image.get_rect(midbottom = (529,570))  
        
        

#creating moon sprite
class Moon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        _moon = pygame.image.load('graphics/moon/Moon.png').convert_alpha()
        self.image = pygame.transform.scale(_moon, (_moon.get_width()-300, _moon.get_height()-300))
        print(f"Moon width is {_moon.get_width()} height is {_moon.get_height()}")
        self.rect = self.image.get_rect(midbottom = (712,570))  
        
        
#creating robot sprite
class Robot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        _robot = pygame.image.load('graphics/robot/robot.png').convert_alpha()
        self.image = pygame.transform.scale(_robot, (_robot.get_width()-50, _robot.get_height()-50))
        #print(f"ROBOT width is {_robot.get_width()} height is {_robot.get_height()}")
        self.rect = self.image.get_rect(midbottom = (900,570))  

#creating flower sprite
class Flower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        _flower = pygame.image.load('graphics/flower/flower.png').convert_alpha()
        self.image = pygame.transform.scale(_flower, (_flower.get_width()+130, _flower.get_height()+130))
        #print(f"flower width is {_flower.get_width()} height is {_flower.get_height()}")
        self.rect = self.image.get_rect(midbottom = (1080,650))

#creating ppf sprite
class PPF(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        _ppf = pygame.image.load('graphics/ppf/probePositionFormula.jpeg').convert_alpha()
        self.image = pygame.transform.scale(_ppf, (_ppf.get_width()-770, _ppf.get_height()-40))
        print(f"ppf width is {_ppf.get_width()} height is {_ppf.get_height()}")
        self.rect = self.image.get_rect(midbottom = (950,170))                
               


