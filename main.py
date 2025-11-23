import os
import pygame

def main():
    try:
        pygame.mixer.init()  
    except pygame.error as e:
        print("audio initialization failed")

if __name__ == "__main__":
    main()