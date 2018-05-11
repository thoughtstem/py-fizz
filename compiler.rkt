#lang racket

(provide compile)

(define (program->string p)
  (~a p))

(define (compile p file-name w h)
  (define final (format (boiler)
                        w h
                        (program->string p)))
  (with-output-to-file file-name #:exists 'replace
    (lambda () (printf final)))
  (system (string-append "PYTHONPATH=/Users/thoughtstem/Dev/Python/py-fizzery/pygame/pyphysicssandbox /usr/local/bin/python3 " file-name)))






(define (boiler)
  "import math

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



window('Shape Methods & Properties', ~a, ~a)

user_shapes = []
image_bindings = []

~a

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

run()"
  )

