from errno import ENETDOWN
import logging
from pickle import TRUE
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
        find_object_surface = find_object_font.render('"I want to find the robot"', False, (0, 255, 255))
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
        first_index_surface = first_index_font.render('"The index I have calculates is index 4 of this array"', False, (255,0,145))
        first_index_rect = find_object_surface.get_rect(center = (255, 190))
        first_index_timer = pygame.USEREVENT+4
        pygame.time.set_timer(first_index_timer, 8000)

        vampire_move_3_timer = pygame.USEREVENT+5
        pygame.time.set_timer(vampire_move_3_timer, 10000, 1)

        dang_bro_1_font = pygame.font.SysFont('timesnewroman', 20)
        dang_bro_1_surface = dang_bro_1_font.render('"Dang bro, this isnt it"', False, (255,111,13))
        dang_bro_1_rect = dang_bro_1_surface.get_rect(center = (470, 350))
        dang_bro_1_timer = pygame.USEREVENT+6
        pygame.time.set_timer(dang_bro_1_timer, 12000, 1)

        destory_1_to_4_timer = pygame.USEREVENT+7
        pygame.time.set_timer(destory_1_to_4_timer, 12500, 1)

        second_index_font = pygame.font.SysFont('timesnewroman', 20)
        second_index_surface = second_index_font.render('"The next index I have calculated is index 5 of this array"', False, (255,0,0))
        second_index_rect = second_index_surface.get_rect(center = (470, 380))
        second_index_timer = pygame.USEREVENT+8
        pygame.time.set_timer(second_index_timer, 14700, 1)

        vampire_move_to_5_timer = pygame.USEREVENT+9
        pygame.time.set_timer(vampire_move_to_5_timer, 16700, 1)

        found_it_font = pygame.font.SysFont('timesnewroman', 20)
        found_it_surface = found_it_font.render('"Found it"', False, (216,191,216))
        found_it_rect = found_it_surface.get_rect(center = (750, 410))
        found_it_timer = pygame.USEREVENT+10
        pygame.time.set_timer(found_it_timer, 18700, 1)

        event_type = 0
        show_find_object = False
        show_probe_pos_formula = False
        show_formula = False
        show_first_index = False
        show_dang_bro_1 = False
        show_second_index = False
        show_found_it = False

        
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

                if event.type == dang_bro_1_timer:
                    show_dang_bro_1 = True

                if event.type == destory_1_to_4_timer:
                    diamond.update("Kill")
                    blueGem.update("Killit")
                    purpleGem.update("KillPurple")
                    redgem.update("KillRed")
                    moon.update("KillMoon")  

                if event.type == second_index_timer:
                    show_second_index = True  

                if event.type == vampire_move_to_5_timer:
                    print(f"Timer fired vampire 2")
                    event_type = 2    

                if event.type == found_it_timer:
                    show_found_it = True        
                    
            screen.fill((0,0,0))
            vampire.draw(screen)
            print(f"Updating vampire")
            vampire.update(event_type)

            blueGem.draw(screen)
            blueGem.update(None)

            purpleGem.draw(screen)
            purpleGem.update(None)

            diamond.draw(screen)
            diamond.update(None)

            flower.draw(screen)
            flower.update()

            robot.draw(screen)
            robot.update()

            redgem.draw(screen)
            redgem.update(None)

            moon.draw(screen)
            moon.update(None)

            if show_find_object:
                screen.blit(find_object_surface, find_object_rect)

            if show_probe_pos_formula:
                screen.blit(probe_pos_formula_surface, probe_pos_formula_rect)   
                
            if show_formula:    
                ppf.draw(screen)
                ppf.update()

            if show_first_index:
                screen.blit(first_index_surface, first_index_rect)

            if show_dang_bro_1:
                screen.blit(dang_bro_1_surface, dang_bro_1_rect) 

            if show_second_index:
                screen.blit(second_index_surface, second_index_rect) 

            if show_found_it:
                screen.blit(found_it_surface, found_it_rect)         
        


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
