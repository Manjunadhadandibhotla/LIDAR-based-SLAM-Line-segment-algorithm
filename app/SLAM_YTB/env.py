import math
import pygame


class buildEnvironment:
    def __init__(self, MapDimensions):
        pygame.init()
        self.pointCloud = []
        self.externalMap = pygame.image.load('map1.png')
        self.maph, self.mapw = MapDimensions
        self.MapWindowName = 'RRT path planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        self.map.blit(self.externalMap, (0, 0))
        # colors
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)
