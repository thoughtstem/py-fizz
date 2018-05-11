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



window('Shape Methods & Properties', 505, 373)

user_shapes = []
image_bindings = []
pivots = []

obj30 = static_box((int(0), int(363)), 505, 10)
obj30.color = Color("white")
obj30.group = 30
obj30_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj30.png")
image_bindings.append([obj30, obj30_image])
user_shapes.append(obj30)
obj32 = static_box((int(495), int(10)), 10, 353)
obj32.color = Color("white")
obj32.group = 32
obj32_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj32.png")
image_bindings.append([obj32, obj32_image])
user_shapes.append(obj32)
obj28 = cosmetic_ball((int(505/2), int(373/2)), 485/2)
obj28.color = Color("white")
obj28.group = 28
obj28_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj28.png")
image_bindings.append([obj28, obj28_image])
user_shapes.append(obj28)
obj22 = ball((int(755/2), int(455/2)), 25)
obj22.color = Color("white")
obj22.group = 22
obj22_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj22.png")
image_bindings.append([obj22, obj22_image])
user_shapes.append(obj22)
obj23 = cosmetic_ball((int(755/2), int(355/2)), 25)
obj23.color = Color("white")
obj23.group = 23
obj23_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj23.png")
image_bindings.append([obj23, obj23_image])
user_shapes.append(obj23)
obj21 = cosmetic_ball((int(755/2), int(273/2)), 16)
obj21.color = Color("white")
obj21.group = 21
obj21_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj21.png")
image_bindings.append([obj21, obj21_image])
user_shapes.append(obj21)
obj18 = ball((int(655/2), int(455/2)), 25)
obj18.color = Color("white")
obj18.group = 18
obj18_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj18.png")
image_bindings.append([obj18, obj18_image])
user_shapes.append(obj18)
obj19 = cosmetic_ball((int(655/2), int(355/2)), 25)
obj19.color = Color("white")
obj19.group = 19
obj19_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj19.png")
image_bindings.append([obj19, obj19_image])
user_shapes.append(obj19)
obj17 = cosmetic_ball((int(655/2), int(273/2)), 16)
obj17.color = Color("white")
obj17.group = 17
obj17_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj17.png")
image_bindings.append([obj17, obj17_image])
user_shapes.append(obj17)
obj14 = ball((int(555/2), int(455/2)), 25)
obj14.color = Color("white")
obj14.group = 14
obj14_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj14.png")
image_bindings.append([obj14, obj14_image])
user_shapes.append(obj14)
obj15 = cosmetic_ball((int(555/2), int(355/2)), 25)
obj15.color = Color("white")
obj15.group = 15
obj15_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj15.png")
image_bindings.append([obj15, obj15_image])
user_shapes.append(obj15)
obj13 = cosmetic_ball((int(555/2), int(273/2)), 16)
obj13.color = Color("white")
obj13.group = 13
obj13_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj13.png")
image_bindings.append([obj13, obj13_image])
user_shapes.append(obj13)
obj10 = ball((int(455/2), int(455/2)), 25)
obj10.color = Color("white")
obj10.group = 10
obj10_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj10.png")
image_bindings.append([obj10, obj10_image])
user_shapes.append(obj10)
obj11 = cosmetic_ball((int(455/2), int(355/2)), 25)
obj11.color = Color("white")
obj11.group = 11
obj11_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj11.png")
image_bindings.append([obj11, obj11_image])
user_shapes.append(obj11)
obj9 = cosmetic_ball((int(455/2), int(273/2)), 16)
obj9.color = Color("white")
obj9.group = 9
obj9_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj9.png")
image_bindings.append([obj9, obj9_image])
user_shapes.append(obj9)
obj6 = ball((int(355/2), int(455/2)), 25)
obj6.color = Color("white")
obj6.group = 6
obj6_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj6.png")
image_bindings.append([obj6, obj6_image])
user_shapes.append(obj6)
obj7 = cosmetic_ball((int(355/2), int(355/2)), 25)
obj7.color = Color("white")
obj7.group = 7
obj7_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj7.png")
image_bindings.append([obj7, obj7_image])
user_shapes.append(obj7)
obj5 = cosmetic_ball((int(355/2), int(273/2)), 16)
obj5.color = Color("white")
obj5.group = 5
obj5_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj5.png")
image_bindings.append([obj5, obj5_image])
user_shapes.append(obj5)
obj2 = ball((int(255/2), int(455/2)), 25)
obj2.color = Color("white")
obj2.group = 2
obj2_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj2.png")
image_bindings.append([obj2, obj2_image])
user_shapes.append(obj2)
obj3 = cosmetic_ball((int(255/2), int(355/2)), 25)
obj3.color = Color("white")
obj3.group = 3
obj3_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj3.png")
image_bindings.append([obj3, obj3_image])
user_shapes.append(obj3)
obj1 = cosmetic_ball((int(255/2), int(273/2)), 16)
obj1.color = Color("white")
obj1.group = 1
obj1_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj1.png")
image_bindings.append([obj1, obj1_image])
user_shapes.append(obj1)
obj32 = static_box((int(0), int(10)), 10, 353)
obj32.color = Color("white")
obj32.group = 32
obj32_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj32.png")
image_bindings.append([obj32, obj32_image])
user_shapes.append(obj32)
obj30 = static_box((int(0), int(0)), 505, 10)
obj30.color = Color("white")
obj30.group = 30
obj30_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj30.png")
image_bindings.append([obj30, obj30_image])
user_shapes.append(obj30)



obj22.hit((-500000, 0), obj22.position)

pivot21 = pivot((755/2,273/2))
pivots.append(pivot21)
pivot21.connect(obj22)
obj18.hit((-500000, 0), obj18.position)

pivot17 = pivot((655/2,273/2))
pivots.append(pivot17)
pivot17.connect(obj18)
obj14.hit((0, 0), obj14.position)

pivot13 = pivot((555/2,273/2))
pivots.append(pivot13)
pivot13.connect(obj14)
obj10.hit((0, 0), obj10.position)

pivot9 = pivot((455/2,273/2))
pivots.append(pivot9)
pivot9.connect(obj10)
obj6.hit((0, 0), obj6.position)

pivot5 = pivot((355/2,273/2))
pivots.append(pivot5)
pivot5.connect(obj6)
obj2.hit((0, 0), obj2.position)

pivot1 = pivot((255/2,273/2))
pivots.append(pivot1)
pivot1.connect(obj2)




add_observer(hit_ball)


def flipy(y):
    return -y+600

def image_for(s):
  global image_bindings
  for b in image_bindings:
    if b[0] == s:
      return b[1]
  return False

def draw_images(keys):
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

def draw_pivot_lines(keys):
  global pivots
  for p in pivots:
    start = p.body.position
    for j in p.shape:
      other = j.a
      end = other.position
      
      screen = pygame.display.get_surface()
      pygame.draw.line(screen, Color("black"), start, end)

      #screen.blit(rotated_logo_img, p)


add_observer(draw_images)
add_observer(draw_pivot_lines)

run()