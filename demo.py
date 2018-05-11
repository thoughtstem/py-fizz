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



window('Shape Methods & Properties', 320, 320)

user_shapes = []
image_bindings = []

obj11_0 = static_box((10, 310), 300, 10)
obj11_0.color = Color("white")
obj11_0.group = 11
obj11_0_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj11.png")
image_bindings.append([obj11_0, obj11_0_image])
user_shapes.append(obj11_0)
obj13_1 = static_box((310, 10), 10, 300)
obj13_1.color = Color("white")
obj13_1.group = 13
obj13_1_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj13.png")
image_bindings.append([obj13_1, obj13_1_image])
user_shapes.append(obj13_1)
obj8_2 = cosmetic_ball((160, 160), 150)
obj8_2.color = Color("white")
obj8_2.group = 8
obj8_2_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj8.png")
image_bindings.append([obj8_2, obj8_2_image])
user_shapes.append(obj8_2)
obj6_3 = ball((160, 185), 50)
obj6_3.color = Color("white")
obj6_3.group = 6
obj6_3_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj6.png")
image_bindings.append([obj6_3, obj6_3_image])
user_shapes.append(obj6_3)
obj3_4 = ball((210, 110), 25)
obj3_4.color = Color("white")
obj3_4.group = 3
obj3_4_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj3.png")
image_bindings.append([obj3_4, obj3_4_image])
user_shapes.append(obj3_4)
obj2_5 = ball((160, 110), 25)
obj2_5.color = Color("white")
obj2_5.group = 2
obj2_5_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj2.png")
image_bindings.append([obj2_5, obj2_5_image])
user_shapes.append(obj2_5)
obj1_6 = ball((110, 110), 25)
obj1_6.color = Color("white")
obj1_6.group = 1
obj1_6_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj1.png")
image_bindings.append([obj1_6, obj1_6_image])
user_shapes.append(obj1_6)
obj13_7 = static_box((0, 10), 10, 300)
obj13_7.color = Color("white")
obj13_7.group = 13
obj13_7_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj13.png")
image_bindings.append([obj13_7, obj13_7_image])
user_shapes.append(obj13_7)
obj11_8 = static_box((10, 0), 300, 10)
obj11_8.color = Color("white")
obj11_8.group = 11
obj11_8_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj11.png")
image_bindings.append([obj11_8, obj11_8_image])
user_shapes.append(obj11_8)

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