from errno import ENETDOWN
import logging
import pygame
from components import sprites

#initialising logger
logging.basicConfig(level = logging.INFO, format="{asctime}, {funcName}, {message}", style='{')
logger = logging.getLogger("searchingAlg")

def main():
    try:
        logger.info("Starting")
        
        pygame.init()
        #create screen
        screen = pygame.display.set_mode((1225, 600))
        #set window title
        pygame.display.set_caption("Interpolation Search Game")
        #clock controls frames per second (fps)
        clock = pygame.time.Clock()

        vampire = pygame.sprite.GroupSingle()
        vampire.add(sprites.Vampire())

        blueGem = pygame.sprite.GroupSingle()
        blueGem.add(sprites.BlueGem())

        purpleGem = pygame.sprite.GroupSingle()
        purpleGem.add(sprites.PurpleGem())

        diamond = pygame.sprite.GroupSingle()
        diamond.add(sprites.Diamond())

        flower = pygame.sprite.GroupSingle()
        flower.add(sprites.Flower())

        robot = pygame.sprite.GroupSingle()
        robot.add(sprites.Robot())

        redgem = pygame.sprite.GroupSingle()
        redgem.add(sprites.RedGem())

        moon = pygame.sprite.GroupSingle()
        moon.add(sprites.Moon())

        ppf = pygame.sprite.GroupSingle()
        ppf.add(sprites.PPF())

        find_object_font = pygame.font.SysFont('timesnewroman', 20)
        find_object_surface = find_object_font.render('"I want to find the moon"', False, (0, 255, 255))
        find_object_rect = find_object_surface.get_rect(center = (250, 110))
        find_object_timer = pygame.USEREVENT+1
        pygame.time.set_timer(find_object_timer, 2000) #time is in milliseconds

        probe_pos_formula_font = pygame.font.SysFont('timesnewroman', 20)
        probe_pos_formula_surface = probe_pos_formula_font.render('"I will use the Probe Position Formula"', False, (24,255,17))
        probe_pos_formula_rect = find_object_surface.get_rect(center = (250,150))
        probe_pos_formula_timer = pygame.USEREVENT+2
        pygame.time.set_timer(probe_pos_formula_timer, 4000)

        formula_timer = pygame.USEREVENT+3
        pygame.time.set_timer(formula_timer, 6000)

        first_index_font = pygame.font.SysFont('timesnewroman', 20)
        first_index_surface = first_index_font.render('"The index I have calculates is index 3 of this array"', False, (255,0,145))
        first_index_rect = find_object_surface.get_rect(center = (255, 190))
        first_index_timer = pygame.USEREVENT+4
        pygame.time.set_timer(first_index_timer, 8000)

        vampire_move_3_timer = pygame.USEREVENT+5
        pygame.time.set_timer(vampire_move_3_timer, 10000, 1)

        event_type = 0
        show_find_object = False
        show_probe_pos_formula = False
        show_formula = False
        show_first_index = False
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #quits program from running
                    logger.info("Quitting searching game")
                    pygame.quit()
                    exit()

                if event.type == find_object_timer:
                    show_find_object = True

                if event.type == probe_pos_formula_timer:
                    show_probe_pos_formula = True 

                if event.type == formula_timer:
                    show_formula = True

                if event.type == first_index_timer:
                    show_first_index = True

                if event.type == vampire_move_3_timer:
                    print(f"Timer fired vampire")
                    event_type = 1  
                    
        
            screen.fill((0,0,0))
            vampire.draw(screen)
            print(f"Updating vampire")
            vampire.update(event_type)

            blueGem.draw(screen)
            blueGem.update()

            purpleGem.draw(screen)
            purpleGem.update()

            diamond.draw(screen)
            diamond.update()

            flower.draw(screen)
            flower.update()

            robot.draw(screen)
            robot.update()

            redgem.draw(screen)
            redgem.update()

            moon.draw(screen)
            moon.update()

            if show_find_object:
                screen.blit(find_object_surface, find_object_rect)

            if show_probe_pos_formula:
                screen.blit(probe_pos_formula_surface, probe_pos_formula_rect)   
                
            if show_formula:    
                ppf.draw(screen)
                ppf.update()

            if show_first_index:
                screen.blit(first_index_surface, first_index_rect)
        


            # display screen and sprites       
            pygame.display.update()

            clock.tick(60)

    except Exception as error:
        logger.error(error)
        raise error 

    finally:
        logger.info(":D")      




if __name__ == "__main__":
    try:
        main()

    except Exception as error:
        logger.error(error)

    finally:
        logger.info(f":D")
