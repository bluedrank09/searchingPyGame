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


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #quits program from running
                    logger.info("Quitting searching game")
                    pygame.quit()
                    exit()

            vampire.draw(screen)
            vampire.update()

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
