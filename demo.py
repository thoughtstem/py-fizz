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
connected_shapes = []

obj29 = static_box((int(0), int(363)), 505, 10)
obj29.color = Color("white")
obj29.group = 29
obj29_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj29.png")
image_bindings.append([obj29, obj29_image])
user_shapes.append(obj29)
obj31 = static_box((int(495), int(10)), 10, 353)
obj31.color = Color("white")
obj31.group = 31
obj31_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj31.png")
image_bindings.append([obj31, obj31_image])
user_shapes.append(obj31)
obj27 = cosmetic_ball((int(505/2), int(373/2)), 485/2)
obj27.color = Color("white")
obj27.group = 27
obj27_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj27.png")
image_bindings.append([obj27, obj27_image])
user_shapes.append(obj27)
obj17 = box((int(232), int(299)), 41, 41)
obj17.color = Color("white")
obj17.group = 17
obj17_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj17.png")
image_bindings.append([obj17, obj17_image])
user_shapes.append(obj17)
obj23 = cosmetic_ball((int(505/2), int(249)), 50)
obj23.color = Color("white")
obj23.group = 23
obj23_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj23.png")
image_bindings.append([obj23, obj23_image])
user_shapes.append(obj23)
obj21 = box((int(593/2), int(139)), 44, 60)
obj21.color = Color("white")
obj21.group = 21
obj21_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj21.png")
image_bindings.append([obj21, obj21_image])
user_shapes.append(obj21)
obj20 = box((int(505/2), int(139)), 44, 60)
obj20.color = Color("white")
obj20.group = 20
obj20_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj20.png")
image_bindings.append([obj20, obj20_image])
user_shapes.append(obj20)
obj19 = box((int(417/2), int(139)), 44, 60)
obj19.color = Color("white")
obj19.group = 19
obj19_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj19.png")
image_bindings.append([obj19, obj19_image])
user_shapes.append(obj19)
obj18 = box((int(329/2), int(139)), 44, 60)
obj18.color = Color("white")
obj18.group = 18
obj18_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj18.png")
image_bindings.append([obj18, obj18_image])
user_shapes.append(obj18)
obj13 = cosmetic_ball((int(505/2), int(129)), 10)
obj13.color = Color("white")
obj13.group = 13
obj13_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj13.png")
image_bindings.append([obj13, obj13_image])
user_shapes.append(obj13)
obj3 = ball((int(595/2), int(99)), 20)
obj3.color = Color("white")
obj3.group = 3
obj3_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj3.png")
image_bindings.append([obj3, obj3_image])
user_shapes.append(obj3)
obj10 = cosmetic_ball((int(275), int(99)), 5/2)
obj10.color = Color("white")
obj10.group = 10
obj10_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj10.png")
image_bindings.append([obj10, obj10_image])
user_shapes.append(obj10)
obj2 = ball((int(505/2), int(99)), 20)
obj2.color = Color("white")
obj2.group = 2
obj2_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj2.png")
image_bindings.append([obj2, obj2_image])
user_shapes.append(obj2)
obj9 = cosmetic_ball((int(230), int(99)), 5/2)
obj9.color = Color("white")
obj9.group = 9
obj9_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj9.png")
image_bindings.append([obj9, obj9_image])
user_shapes.append(obj9)
obj1 = ball((int(415/2), int(99)), 20)
obj1.color = Color("white")
obj1.group = 1
obj1_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj1.png")
image_bindings.append([obj1, obj1_image])
user_shapes.append(obj1)
obj8 = cosmetic_ball((int(505/2), int(153/2)), 5/2)
obj8.color = Color("white")
obj8.group = 8
obj8_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj8.png")
image_bindings.append([obj8, obj8_image])
user_shapes.append(obj8)
obj7 = box((int(232), int(33)), 41, 41)
obj7.color = Color("white")
obj7.group = 7
obj7_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj7.png")
image_bindings.append([obj7, obj7_image])
user_shapes.append(obj7)
obj31 = static_box((int(0), int(10)), 10, 353)
obj31.color = Color("white")
obj31.group = 31
obj31_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj31.png")
image_bindings.append([obj31, obj31_image])
user_shapes.append(obj31)
obj29 = static_box((int(0), int(0)), 505, 10)
obj29.color = Color("white")
obj29.group = 29
obj29_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj29.png")
image_bindings.append([obj29, obj29_image])
user_shapes.append(obj29)



obj17.hit((0, 0), obj17.position)
spring(obj17.body.position, obj17, obj18.body.position, obj18, 100, 20000, 1000)
connected_shapes.append([obj17, obj18])
spring(obj17.body.position, obj17, obj19.body.position, obj19, 100, 20000, 1000)
connected_shapes.append([obj17, obj19])
spring(obj17.body.position, obj17, obj20.body.position, obj20, 100, 20000, 1000)
connected_shapes.append([obj17, obj20])
spring(obj17.body.position, obj17, obj21.body.position, obj21, 100, 20000, 1000)
connected_shapes.append([obj17, obj21])

obj21.gravity = (0,-100)
obj20.gravity = (0,-100)
obj19.gravity = (0,-100)
obj18.gravity = (0,-100)

obj3.hit((0, 0), obj3.position)
pin(obj3.body.position,obj3,obj7.body.position,obj7)
connected_shapes.append([obj3, obj7])
motor(obj3, 1)

obj2.hit((0, 0), obj2.position)
pin(obj2.body.position,obj2,obj3.body.position,obj3)
connected_shapes.append([obj2, obj3])
pin(obj2.body.position,obj2,obj7.body.position,obj7)
connected_shapes.append([obj2, obj7])
motor(obj2, 1)

obj1.hit((0, 0), obj1.position)
pin(obj1.body.position,obj1,obj2.body.position,obj2)
connected_shapes.append([obj1, obj2])
pin(obj1.body.position,obj1,obj7.body.position,obj7)
connected_shapes.append([obj1, obj7])
motor(obj1, 1)

obj7.hit((0, 0), obj7.position)




add_observer(hit_ball)


def flipy(y):
    return -y+600

def image_for(s):
  global image_bindings
  for b in image_bindings:
    if b[0] == s:
      return b[1]
  return False

def draw_images(cosmetic):
  def f(keys):
    global user_shapes
    for s in user_shapes:
      if(not image_for(s)):
        continue

      if(not (s._cosmetic == cosmetic)):
        continue

      if(s.body):
        p = Vec2d(s.body.position.x, s.body.position.y)
      else:
        p = Vec2d(s._x, s._y)

      angle = 0
      if(s.body):
        angle = s.body.angle

      angle_degrees    = math.degrees(angle) 
      rotated_logo_img = pygame.transform.rotate(image_for(s), -angle_degrees)
    
      offset = Vec2d(rotated_logo_img.get_size()) / 2.
      p      = p - offset
     
      screen = pygame.display.get_surface()
      screen.blit(rotated_logo_img, p)
  return f

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

def draw_connection_lines(keys):
  global pivots
  for c in connected_shapes:
    start = c[0].body.position
    end   = c[1].body.position
   
    screen = pygame.display.get_surface()
    pygame.draw.line(screen, Color("black"), start, end)

 

add_observer(draw_images(True))
add_observer(draw_pivot_lines)
add_observer(draw_connection_lines)
add_observer(draw_images(False))

run()