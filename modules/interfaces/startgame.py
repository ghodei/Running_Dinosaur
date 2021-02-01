''' Game start interface'''
import sys
import pygame
from ..sprites import Dinosaur

'''Game start interface'''
def StartGameInterface(screen, sounds, config):
    dinosaur = Dinosaur(config.IMAGE_PATHS['dinosaur'])
    ground = pygame.image.load(config.IMAGE_PATHS['ground']).subsurface((0, 0), (83, 19))
    rect = ground.get_rect()
    rect.left, rect.bottom = config.SCREENSIZE[0]/20, config.SCREENSIZE[1]
    spacebar_image = pygame.image.load(config.IMAGE_PATHS['spacebar'])
    spacebar_image = pygame.transform.scale(spacebar_image, (271, 112))
    spacebar_image_rect = spacebar_image.get_rect()
    spacebar_image_rect.centerx = config.SCREENSIZE[0] / 2
    spacebar_image_rect.centery = config.SCREENSIZE[1] * 0.5
    clock = pygame.time.Clock()
    press_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    press_flag = True
                    dinosaur.jump(sounds)
        dinosaur.update()
        screen.fill(config.BACKGROUND_COLOR)
        screen.blit(ground, rect)
        screen.blit(spacebar_image, spacebar_image_rect)
        dinosaur.draw(screen)
        pygame.display.update()
        clock.tick(config.FPS)
        if (not dinosaur.is_jumping) and press_flag:
            return True