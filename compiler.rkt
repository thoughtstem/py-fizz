#lang racket

(provide compile)

(define (program->string p)
  (~a p))

(define (compile p file-name)
  (define final (format (boiler) (program->string p)))
  (with-output-to-file file-name #:exists 'replace
    (lambda () (printf final)))
  (system (string-append "python3 " file-name))
  )


(module+ test
  (compile "circle(random.randint(115,350), 400, \"red\")"
           "./demo.py")
  )



(define (boiler)
  "

__version__ = \"$Id:$\"
__docformat__ = \"reStructuredText\"

import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d
import math, sys, random

    
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

### Physics stuff
space = pymunk.Space()
space.gravity = (0.0, -900.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)

## Balls
balls = []
   
### walls
static_body = space.static_body
static_lines = [
	pymunk.Segment(static_body, (0.0, 0.0), (600.0, 0.0), 0.0),
	pymunk.Segment(static_body, (600.0, 0.0), (600.0, 600.0), 0.0),
	pymunk.Segment(static_body, (600.0, 600.0), (0.0, 600.0), 0.0),
	pymunk.Segment(static_body, (0.0, 600.0), (0.0, 0.0), 0.0),
                ]  

for line in static_lines:
    line.elasticity = 0.95
    line.friction = 0.9
space.add(static_lines)

ticks_to_next_ball = 10


def circle(x,y, r, color):
	global space
	global balls
	mass = 10
	inertia = pymunk.moment_for_circle(mass, 0, r, (0,0))
	body = pymunk.Body(mass, inertia)

	shape = pymunk.Circle(body, r, (0,0))
		
	body.position = x, y
	shape.elasticity = 0.95
	shape.friction = 0.9
	shape.color = pygame.color.THECOLORS[color]
	space.add(body, shape)
	balls.append(shape)

def poly(x,y, color, verts):
	global space
	global balls
	mass = 10
	radius = 25
	inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
	body = pymunk.Body(mass, inertia)

	shape = pymunk.Poly(body,  verts)
		
	body.position = x, y
	shape.elasticity = 0.95
	shape.friction = 0.9
	shape.color = pygame.color.THECOLORS[color]
	space.add(body, shape)
	balls.append(shape)

#vs = [(0, -25),(30, 25),(-30, 25)]
#circle(random.randint(115,350), 400, \"red\")
#poly(random.randint(115,350), 400, \"yellow\", vs)
#poly(random.randint(115,350), 400, \"blue\", vs)
#poly(random.randint(115,350), 400, \"green\", vs)
#poly(random.randint(115,350), 400, \"purple\", vs)

~a

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == KEYDOWN and event.key == K_p:
            pygame.image.save(screen, \"bouncing_balls.png\")
            
    
    ### Clear screen
    screen.fill(THECOLORS[\"white\"])
    
    balls_to_remove = []

    space.debug_draw(draw_options)

    ### Update physics
    dt = 1.0/60.0
    for x in range(1):
        space.step(dt)
    
    ### Flip screen
    pygame.display.flip()
    clock.tick(50)
    pygame.display.set_caption(\"fps: \" + str(clock.get_fps()))
")