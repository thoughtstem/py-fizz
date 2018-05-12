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

obj138 = static_box((int(0), int(363)), 505, 10)
obj138.color = Color("white")
obj138.group = 138
obj138_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj138.png")
image_bindings.append([obj138, obj138_image])
user_shapes.append(obj138)
obj140 = static_box((int(495), int(10)), 10, 353)
obj140.color = Color("white")
obj140.group = 140
obj140_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj140.png")
image_bindings.append([obj140, obj140_image])
user_shapes.append(obj140)
obj136 = cosmetic_ball((int(505/2), int(373/2)), 485/2)
obj136.color = Color("white")
obj136.group = 136
obj136_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj136.png")
image_bindings.append([obj136, obj136_image])
user_shapes.append(obj136)
obj131 = ball((int(865/2), int(287)), 20)
obj131.color = Color("white")
obj131.group = 131
obj131_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj131.png")
image_bindings.append([obj131, obj131_image])
user_shapes.append(obj131)
obj127 = cosmetic_ball((int(865/2), int(287)), 21/2)
obj127.color = Color("white")
obj127.group = 127
obj127_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj127.png")
image_bindings.append([obj127, obj127_image])
user_shapes.append(obj127)
obj125 = ball((int(785/2), int(287)), 20)
obj125.color = Color("white")
obj125.group = 125
obj125_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj125.png")
image_bindings.append([obj125, obj125_image])
user_shapes.append(obj125)
obj121 = cosmetic_ball((int(785/2), int(287)), 21/2)
obj121.color = Color("white")
obj121.group = 121
obj121_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj121.png")
image_bindings.append([obj121, obj121_image])
user_shapes.append(obj121)
obj119 = ball((int(705/2), int(287)), 20)
obj119.color = Color("white")
obj119.group = 119
obj119_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj119.png")
image_bindings.append([obj119, obj119_image])
user_shapes.append(obj119)
obj115 = cosmetic_ball((int(705/2), int(287)), 21/2)
obj115.color = Color("white")
obj115.group = 115
obj115_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj115.png")
image_bindings.append([obj115, obj115_image])
user_shapes.append(obj115)
obj113 = ball((int(625/2), int(287)), 20)
obj113.color = Color("white")
obj113.group = 113
obj113_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj113.png")
image_bindings.append([obj113, obj113_image])
user_shapes.append(obj113)
obj109 = cosmetic_ball((int(625/2), int(287)), 21/2)
obj109.color = Color("white")
obj109.group = 109
obj109_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj109.png")
image_bindings.append([obj109, obj109_image])
user_shapes.append(obj109)
obj107 = ball((int(545/2), int(287)), 20)
obj107.color = Color("white")
obj107.group = 107
obj107_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj107.png")
image_bindings.append([obj107, obj107_image])
user_shapes.append(obj107)
obj103 = cosmetic_ball((int(545/2), int(287)), 21/2)
obj103.color = Color("white")
obj103.group = 103
obj103_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj103.png")
image_bindings.append([obj103, obj103_image])
user_shapes.append(obj103)
obj101 = ball((int(465/2), int(287)), 20)
obj101.color = Color("white")
obj101.group = 101
obj101_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj101.png")
image_bindings.append([obj101, obj101_image])
user_shapes.append(obj101)
obj97 = cosmetic_ball((int(465/2), int(287)), 21/2)
obj97.color = Color("white")
obj97.group = 97
obj97_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj97.png")
image_bindings.append([obj97, obj97_image])
user_shapes.append(obj97)
obj95 = ball((int(385/2), int(287)), 20)
obj95.color = Color("white")
obj95.group = 95
obj95_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj95.png")
image_bindings.append([obj95, obj95_image])
user_shapes.append(obj95)
obj91 = cosmetic_ball((int(385/2), int(287)), 21/2)
obj91.color = Color("white")
obj91.group = 91
obj91_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj91.png")
image_bindings.append([obj91, obj91_image])
user_shapes.append(obj91)
obj89 = ball((int(305/2), int(287)), 20)
obj89.color = Color("white")
obj89.group = 89
obj89_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj89.png")
image_bindings.append([obj89, obj89_image])
user_shapes.append(obj89)
obj85 = cosmetic_ball((int(305/2), int(287)), 21/2)
obj85.color = Color("white")
obj85.group = 85
obj85_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj85.png")
image_bindings.append([obj85, obj85_image])
user_shapes.append(obj85)
obj83 = ball((int(225/2), int(287)), 20)
obj83.color = Color("white")
obj83.group = 83
obj83_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj83.png")
image_bindings.append([obj83, obj83_image])
user_shapes.append(obj83)
obj79 = cosmetic_ball((int(225/2), int(287)), 21/2)
obj79.color = Color("white")
obj79.group = 79
obj79_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj79.png")
image_bindings.append([obj79, obj79_image])
user_shapes.append(obj79)
obj77 = ball((int(145/2), int(287)), 20)
obj77.color = Color("white")
obj77.group = 77
obj77_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj77.png")
image_bindings.append([obj77, obj77_image])
user_shapes.append(obj77)
obj73 = cosmetic_ball((int(145/2), int(287)), 21/2)
obj73.color = Color("white")
obj73.group = 73
obj73_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj73.png")
image_bindings.append([obj73, obj73_image])
user_shapes.append(obj73)
obj72 = cosmetic_ball((int(505/2), int(217)), 50)
obj72.color = Color("white")
obj72.group = 72
obj72_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj72.png")
image_bindings.append([obj72, obj72_image])
user_shapes.append(obj72)
obj69 = ball((int(785/2), int(147)), 20)
obj69.color = Color("white")
obj69.group = 69
obj69_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj69.png")
image_bindings.append([obj69, obj69_image])
user_shapes.append(obj69)
obj65 = cosmetic_ball((int(785/2), int(147)), 21/2)
obj65.color = Color("white")
obj65.group = 65
obj65_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj65.png")
image_bindings.append([obj65, obj65_image])
user_shapes.append(obj65)
obj63 = ball((int(705/2), int(147)), 20)
obj63.color = Color("white")
obj63.group = 63
obj63_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj63.png")
image_bindings.append([obj63, obj63_image])
user_shapes.append(obj63)
obj59 = cosmetic_ball((int(705/2), int(147)), 21/2)
obj59.color = Color("white")
obj59.group = 59
obj59_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj59.png")
image_bindings.append([obj59, obj59_image])
user_shapes.append(obj59)
obj57 = ball((int(625/2), int(147)), 20)
obj57.color = Color("white")
obj57.group = 57
obj57_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj57.png")
image_bindings.append([obj57, obj57_image])
user_shapes.append(obj57)
obj53 = cosmetic_ball((int(625/2), int(147)), 21/2)
obj53.color = Color("white")
obj53.group = 53
obj53_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj53.png")
image_bindings.append([obj53, obj53_image])
user_shapes.append(obj53)
obj51 = ball((int(545/2), int(147)), 20)
obj51.color = Color("white")
obj51.group = 51
obj51_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj51.png")
image_bindings.append([obj51, obj51_image])
user_shapes.append(obj51)
obj47 = cosmetic_ball((int(545/2), int(147)), 21/2)
obj47.color = Color("white")
obj47.group = 47
obj47_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj47.png")
image_bindings.append([obj47, obj47_image])
user_shapes.append(obj47)
obj45 = ball((int(465/2), int(147)), 20)
obj45.color = Color("white")
obj45.group = 45
obj45_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj45.png")
image_bindings.append([obj45, obj45_image])
user_shapes.append(obj45)
obj41 = cosmetic_ball((int(465/2), int(147)), 21/2)
obj41.color = Color("white")
obj41.group = 41
obj41_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj41.png")
image_bindings.append([obj41, obj41_image])
user_shapes.append(obj41)
obj39 = ball((int(385/2), int(147)), 20)
obj39.color = Color("white")
obj39.group = 39
obj39_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj39.png")
image_bindings.append([obj39, obj39_image])
user_shapes.append(obj39)
obj35 = cosmetic_ball((int(385/2), int(147)), 21/2)
obj35.color = Color("white")
obj35.group = 35
obj35_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj35.png")
image_bindings.append([obj35, obj35_image])
user_shapes.append(obj35)
obj33 = ball((int(305/2), int(147)), 20)
obj33.color = Color("white")
obj33.group = 33
obj33_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj33.png")
image_bindings.append([obj33, obj33_image])
user_shapes.append(obj33)
obj29 = cosmetic_ball((int(305/2), int(147)), 21/2)
obj29.color = Color("white")
obj29.group = 29
obj29_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj29.png")
image_bindings.append([obj29, obj29_image])
user_shapes.append(obj29)
obj27 = ball((int(225/2), int(147)), 20)
obj27.color = Color("white")
obj27.group = 27
obj27_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj27.png")
image_bindings.append([obj27, obj27_image])
user_shapes.append(obj27)
obj23 = cosmetic_ball((int(225/2), int(147)), 21/2)
obj23.color = Color("white")
obj23.group = 23
obj23_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj23.png")
image_bindings.append([obj23, obj23_image])
user_shapes.append(obj23)
obj22 = cosmetic_ball((int(505/2), int(117)), 10)
obj22.color = Color("white")
obj22.group = 22
obj22_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj22.png")
image_bindings.append([obj22, obj22_image])
user_shapes.append(obj22)
obj20 = box((int(314), int(66)), 41, 41)
obj20.color = Color("white")
obj20.group = 20
obj20_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj20.png")
image_bindings.append([obj20, obj20_image])
user_shapes.append(obj20)
obj16 = box((int(273), int(66)), 41, 41)
obj16.color = Color("white")
obj16.group = 16
obj16_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj16.png")
image_bindings.append([obj16, obj16_image])
user_shapes.append(obj16)
obj12 = box((int(232), int(66)), 41, 41)
obj12.color = Color("white")
obj12.group = 12
obj12_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj12.png")
image_bindings.append([obj12, obj12_image])
user_shapes.append(obj12)
obj8 = box((int(191), int(66)), 41, 41)
obj8.color = Color("white")
obj8.group = 8
obj8_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj8.png")
image_bindings.append([obj8, obj8_image])
user_shapes.append(obj8)
obj4 = box((int(150), int(66)), 41, 41)
obj4.color = Color("white")
obj4.group = 4
obj4_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj4.png")
image_bindings.append([obj4, obj4_image])
user_shapes.append(obj4)
obj140 = static_box((int(0), int(10)), 10, 353)
obj140.color = Color("white")
obj140.group = 140
obj140_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj140.png")
image_bindings.append([obj140, obj140_image])
user_shapes.append(obj140)
obj138 = static_box((int(0), int(0)), 505, 10)
obj138.color = Color("white")
obj138.group = 138
obj138_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj138.png")
image_bindings.append([obj138, obj138_image])
user_shapes.append(obj138)



motor(obj131, -5)
pivot127 = pivot((865/2,287))
pivots.append(pivot127)
pivot127.connect(obj131)
motor(obj125, -5)
pivot121 = pivot((785/2,287))
pivots.append(pivot121)
pivot121.connect(obj125)
motor(obj119, -5)
pivot115 = pivot((705/2,287))
pivots.append(pivot115)
pivot115.connect(obj119)
motor(obj113, -5)
pivot109 = pivot((625/2,287))
pivots.append(pivot109)
pivot109.connect(obj113)
motor(obj107, -5)
pivot103 = pivot((545/2,287))
pivots.append(pivot103)
pivot103.connect(obj107)
motor(obj101, -5)
pivot97 = pivot((465/2,287))
pivots.append(pivot97)
pivot97.connect(obj101)
motor(obj95, -5)
pivot91 = pivot((385/2,287))
pivots.append(pivot91)
pivot91.connect(obj95)
motor(obj89, -5)
pivot85 = pivot((305/2,287))
pivots.append(pivot85)
pivot85.connect(obj89)
motor(obj83, -5)
pivot79 = pivot((225/2,287))
pivots.append(pivot79)
pivot79.connect(obj83)
motor(obj77, -5)
pivot73 = pivot((145/2,287))
pivots.append(pivot73)
pivot73.connect(obj77)

motor(obj69, 5)
pivot65 = pivot((785/2,147))
pivots.append(pivot65)
pivot65.connect(obj69)
motor(obj63, 5)
pivot59 = pivot((705/2,147))
pivots.append(pivot59)
pivot59.connect(obj63)
motor(obj57, 5)
pivot53 = pivot((625/2,147))
pivots.append(pivot53)
pivot53.connect(obj57)
motor(obj51, 5)
pivot47 = pivot((545/2,147))
pivots.append(pivot47)
pivot47.connect(obj51)
motor(obj45, 5)
pivot41 = pivot((465/2,147))
pivots.append(pivot41)
pivot41.connect(obj45)
motor(obj39, 5)
pivot35 = pivot((385/2,147))
pivots.append(pivot35)
pivot35.connect(obj39)
motor(obj33, 5)
pivot29 = pivot((305/2,147))
pivots.append(pivot29)
pivot29.connect(obj33)
motor(obj27, 5)
pivot23 = pivot((225/2,147))
pivots.append(pivot23)
pivot23.connect(obj27)

obj20.hit((0, 0), obj20.position)
obj16.hit((0, 0), obj16.position)
obj12.hit((0, 0), obj12.position)
obj8.hit((0, 0), obj8.position)
obj4.hit((0, 0), obj4.position)




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
    rotated_logo_img = pygame.transform.rotate(image_for(s), -angle_degrees)
    
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