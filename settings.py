import pygame
from pygame.locals import *
from queue import PriorityQueue
import random
import pygame

WIDTH =600
RANDOM_RATE = 2
ROWS =5

pygame.init()
WIN = pygame.display.set_mode((WIDTH+180,WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm - Group 5")
font = pygame.font.SysFont('Constantia', 26)
font1 = pygame.font.SysFont('Constantia', 30)
a = font1.render("A",True,"red")
star = font1.render("Star",True,"red")
algo = font1.render("Algorithm",True,"red")
nhom5 = font1.render("Group 5",True,"red")
finding = font.render("Finding....",True,"red")

RED = (255, 0, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SILVER = (0,128,0)
PINK = (255, 0, 255)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
