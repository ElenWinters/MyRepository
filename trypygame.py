import pygame

def load_audio(file_name):
    pygame.mixer.init()
    return pygame.mixer.Sound(file_name)