'''Configuration File'''
import os

'''Screen size'''
SCREENSIZE = (600, 150)

'''Frames Per Second'''
FPS = 60

'''Audio resources path'''
AUDIO_PATHS = {
    'music': os.path.join(os.getcwd(), 'resources/audios/music.wav'),
    'points': os.path.join(os.getcwd(), 'resources/audios/points.wav'),
    'jump': os.path.join(os.getcwd(), 'resources/audios/jump.wav'),
    'die': os.path.join(os.getcwd(), 'resources/audios/die.wav'),
    'music_die': os.path.join(os.getcwd(), 'resources/audios/music_die.wav'),
}
'''Image resources path'''
IMAGE_PATHS = {
    'cactus': [
        os.path.join(os.getcwd(), 'resources/images/cactus-big.png'),
        os.path.join(os.getcwd(), 'resources/images/cactus-small.png'),
    ],
    'cloud': os.path.join(os.getcwd(), 'resources/images/cloud.png'),
    'dinosaur': [
        os.path.join(os.getcwd(), 'resources/images/dinosaur.png'),
        os.path.join(os.getcwd(), 'resources/images/dinosaur_ducking.png'),
    ],
    'spacebar': os.path.join(os.getcwd(), 'resources/images/spacebar.png'),
    'gameover': os.path.join(os.getcwd(), 'resources/images/gameover.png'),
    'pause': os.path.join(os.getcwd(), 'resources/images/pause.png'),
    'ground': os.path.join(os.getcwd(), 'resources/images/ground.png'),
    'numbers': os.path.join(os.getcwd(), 'resources/images/numbers.png'),
    'pterodactyl': os.path.join(os.getcwd(), 'resources/images/pterodactyl.png'),
    'replay': os.path.join(os.getcwd(), 'resources/images/replay.png'),
}
'''Background color'''
BACKGROUND_COLOR = (135, 235, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)