"""
An example of using shape methods and properties.  The screencast developing this code can be found
here: http://youtu.be/_eyE4xX_Gi8?hd=1
"""

import math

import pymunk

from pyphysicssandbox import *
import pygame
from pymunk import Vec2d

def hit_ball(keys):
    if mouse_clicked():
        ball1.hit((0, -400000), ball1.position)

    if constants.K_RIGHT in keys:
        floor.surface_velocity = (100, 0)
    elif constants.K_LEFT in keys:
        floor.surface_velocity = (-100, 0)



window('Shape Methods & Properties', 300, 300)

ball1 = ball((100, 100), 25)
ball1.color = Color('blue')
ball1.group = 1
ball1.elasticity = 0.0


floor = static_box((0, 290), 300, 10)
floor.elasticity = 0.0

add_observer(hit_ball)

logo_img = pygame.image.load("wheel.png")

def flipy(y):
    """Small hack to convert chipmunk physics to pygame coordinates"""
    return -y+600

def test(keys):
    p = ball1.body.position
    p = Vec2d(p.x, p.y)
    
    angle_degrees    = math.degrees(ball1.body.angle) 
    rotated_logo_img = pygame.transform.rotate(logo_img, angle_degrees)
    
    offset = Vec2d(rotated_logo_img.get_size()) / 2.
    p      = p - offset
    
    screen = pygame.display.get_surface()
    screen.blit(rotated_logo_img, p)


add_observer(test)

run()
