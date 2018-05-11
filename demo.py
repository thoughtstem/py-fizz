import math

import pymunk

from pyphysicssandbox import *
import pygame
from pymunk import Vec2d

def hit_ball(keys):
#    if mouse_clicked():
#        ball1.hit((0, -400000), ball1.position)

    if constants.K_RIGHT in keys:
        floor.surface_velocity = (100, 0)
    elif constants.K_LEFT in keys:
        floor.surface_velocity = (-100, 0)



window('Shape Methods & Properties', 300, 310)

user_shapes = []
image_bindings = []

obj8_0 = static_box((150, 305), 250, 10)
obj8_0.color = Color("white")
obj8_0.group = 8
obj8_0_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj8.png")
image_bindings.append([obj8_0, obj8_0_image])
user_shapes.append(obj8_0)
obj10_1 = cosmetic_ball((150, 150), 150)
obj10_1.color = Color("white")
obj10_1.group = 10
obj10_1_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj10.png")
image_bindings.append([obj10_1, obj10_1_image])
user_shapes.append(obj10_1)
obj5_2 = ball((75, 100), 50)
obj5_2.color = Color("white")
obj5_2.group = 5
obj5_2_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj5.png")
image_bindings.append([obj5_2, obj5_2_image])
user_shapes.append(obj5_2)
obj3_3 = ball((125, 25), 25)
obj3_3.color = Color("white")
obj3_3.group = 3
obj3_3_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj3.png")
image_bindings.append([obj3_3, obj3_3_image])
user_shapes.append(obj3_3)
obj2_4 = ball((75, 25), 25)
obj2_4.color = Color("white")
obj2_4.group = 2
obj2_4_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj2.png")
image_bindings.append([obj2_4, obj2_4_image])
user_shapes.append(obj2_4)
obj1_5 = ball((25, 25), 25)
obj1_5.color = Color("white")
obj1_5.group = 1
obj1_5_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj1.png")
image_bindings.append([obj1_5, obj1_5_image])
user_shapes.append(obj1_5)

#floor = static_box((0, 590), 600, 10)
#floor.elasticity = 0.0

add_observer(hit_ball)


def flipy(y):
    return -y+600

def image_for(s):
  global image_bindings
  for b in image_bindings:
    if b[0] == s:
      return b[1]
  return False

def test(keys):
  global user_shapes
  for s in user_shapes:
    if(not image_for(s)):
      continue

    if(s.body):
      p = Vec2d(s.body.position.x, s.body.position.y)
    else:
      p = Vec2d(s._x, s._y)

    angle = 0
    if(s.body):
      angle = s.body.angle

    angle_degrees    = math.degrees(angle) 
    rotated_logo_img = pygame.transform.rotate(image_for(s), angle_degrees)
    
    offset = Vec2d(rotated_logo_img.get_size()) / 2.
    p      = p - offset
    
    screen = pygame.display.get_surface()
    screen.blit(rotated_logo_img, p)


add_observer(test)

run()