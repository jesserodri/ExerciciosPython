# reproduzir um arquivo de audio no python
import pygame
pygame.mixer.init()
pygame.mixer.music.load('tachovendoai.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass