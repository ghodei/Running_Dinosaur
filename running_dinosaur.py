'''Running Dinosaur main game'''
from pygame.constants import K_p
from pygame.mixer import pause
import config
import sys
import random
import pygame
from modules import *

'''Main'''
def main(highest_score):
    # Game initialization
    pygame.init()
    screen = pygame.display.set_mode(config.SCREENSIZE)
    pygame.display.set_caption('Running Dinosaur - ghodei')
    # Import audio files
    sounds = {}
    for key, value in config.AUDIO_PATHS.items():
        sounds[key] = pygame.mixer.Sound(value)
    # Start game interface
    StartGameInterface(screen, sounds, config)
    # Define some variables and resources in the game
    score = 0
    score_board = Scoreboard(config.IMAGE_PATHS['numbers'], position=(534, 15), bg_color=config.BACKGROUND_COLOR)
    highest_score = highest_score
    highest_score_board = Scoreboard(config.IMAGE_PATHS['numbers'], position=(435, 15), bg_color=config.BACKGROUND_COLOR, is_highest=True)
    dinosaur = Dinosaur(config.IMAGE_PATHS['dinosaur'])
    ground = Ground(config.IMAGE_PATHS['ground'], position=(0, config.SCREENSIZE[1]))
    cloud_sprites_group = pygame.sprite.Group()
    cactus_sprites_group = pygame.sprite.Group()
    pterodactyl_sprites_group = pygame.sprite.Group()
    add_obstacle_timer = 0
    score_timer = 0
    # Game main loop
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load("resources/audios/music.wav")
    pygame.mixer.music.play(loops=-1)
    pygame.display.update()
    clock.tick(15)
    # Pause variable definition
    def pause():
        pause_image = pygame.image.load(config.IMAGE_PATHS['pause'])
        pause_image = pygame.transform.scale(pause_image, (150, 15))
        pause_image_rect = pause_image.get_rect()
        pause_image_rect.centerx = config.SCREENSIZE[0] / 2
        pause_image_rect.centery = config.SCREENSIZE[1] * 0.45
        paused = True
        while paused:
            pygame.mixer.music.pause()
            screen.blit(pause_image, pause_image_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        paused = False
                        pygame.mixer.music.unpause()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_r:
                        pygame.mixer.music.stop()
                        main(highest_score)
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    dinosaur.jump(sounds)
                elif event.key == pygame.K_DOWN:
                    dinosaur.duck()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                dinosaur.unduck()
        screen.fill(config.BACKGROUND_COLOR)
        # Add clouds randomly
        if len(cloud_sprites_group) < 5 and random.randrange(0, 300) == 10:
            cloud_sprites_group.add(Cloud(config.IMAGE_PATHS['cloud'], position=(config.SCREENSIZE[0], random.randrange(30, 75))))
        # Add cactus and pterodactyl randomly
        add_obstacle_timer += 1
        if add_obstacle_timer > random.randrange(50, 150):
            add_obstacle_timer = 0
            random_value = random.randrange(0, 10)
            if random_value >= 1 and random_value <= 5:
                cactus_sprites_group.add(Cactus(config.IMAGE_PATHS['cactus']))
            else:
                position_ys = [config.SCREENSIZE[1]*0.82, config.SCREENSIZE[1]*0.75, config.SCREENSIZE[1]*0.60, config.SCREENSIZE[1]*0.20]
                pterodactyl_sprites_group.add(Pterodactyl(config.IMAGE_PATHS['pterodactyl'], position=(600, random.choice(position_ys))))
        # Update game resources
        dinosaur.update()
        ground.update()
        cloud_sprites_group.update()
        cactus_sprites_group.update()
        pterodactyl_sprites_group.update()
        score_timer += 1
        if score_timer > (config.FPS//12):
            score_timer = 0
            score += 1
            score = min(score, 99999)
            if score > highest_score:
                highest_score = score
            if score % 100 == 0:
                sounds['points'].play()
        # Check impact
        for item in cactus_sprites_group:
            if pygame.sprite.collide_mask(dinosaur, item):
                dinosaur.die(sounds)
        for item in pterodactyl_sprites_group:
            if pygame.sprite.collide_mask(dinosaur, item):
                dinosaur.die(sounds)
        # Draw game resources on the screen
        ground.draw(screen)
        cloud_sprites_group.draw(screen)
        dinosaur.draw(screen)
        cactus_sprites_group.draw(screen)
        pterodactyl_sprites_group.draw(screen)
        score_board.set(score)
        highest_score_board.set(highest_score)
        score_board.draw(screen)
        highest_score_board.draw(screen)
        # Update screen
        pygame.display.update()
        clock.tick(config.FPS)
        # Check if the game is over
        if dinosaur.is_dead:
            break
    # Game over interface
    return EndGameInterface(screen, config), highest_score

'''Run'''
if __name__ == '__main__':
    highest_score = 0
    while True:
        flag, highest_score = main(highest_score)
        if not flag: break