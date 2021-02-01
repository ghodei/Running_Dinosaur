'''Game over interface'''
import sys
import pygame

'''Game over interface'''
def EndGameInterface(screen, config):
    replay_image = pygame.image.load(config.IMAGE_PATHS['replay'])
    replay_image = pygame.transform.scale(replay_image, (35, 31))
    replay_image_rect = replay_image.get_rect()
    replay_image_rect.centerx = config.SCREENSIZE[0] / 2
    replay_image_rect.top = config.SCREENSIZE[1] * 0.52
    gameover_image = pygame.image.load(config.IMAGE_PATHS['gameover'])
    gameover_image = pygame.transform.scale(gameover_image, (190, 15))
    gameover_image_rect = gameover_image.get_rect()
    gameover_image_rect.centerx = config.SCREENSIZE[0] / 2
    gameover_image_rect.centery = config.SCREENSIZE[1] * 0.35
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if replay_image_rect.collidepoint(mouse_pos):
                    return True
        screen.blit(replay_image, replay_image_rect)
        screen.blit(gameover_image, gameover_image_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        clock.tick(config.FPS)