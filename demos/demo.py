from hy.core.language import fraction
import math
import pymunk
from pyphysicssandbox import *
import pygame
from pyphysicssandbox import Vec2d
w = 505
h = 373
user_shapes = []
image_bindings = []
pivots = []
connected_shapes = []
window('Most Awesome Thing Ever', 505, 373)
obj47 = static_box([int(fraction(505, 2) - fraction(505, 2)), int(368 - 5)],
    505, 10)
obj47.color = Color('white')
obj47.group = 47
obj47_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj47.png')
image_bindings.append([obj47, obj47_image])
user_shapes.append(obj47)
obj49 = static_box([int(500 - 5), int(fraction(373, 2) - fraction(353, 2))],
    10, 353)
obj49.color = Color('white')
obj49.group = 49
obj49_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj49.png')
image_bindings.append([obj49, obj49_image])
user_shapes.append(obj49)
obj45 = cosmetic_ball([int(fraction(505, 2)), int(fraction(373, 2))],
    fraction(485, 2))
obj45.color = Color('white')
obj45.group = 45
obj45_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj45.png')
image_bindings.append([obj45, obj45_image])
user_shapes.append(obj45)
obj34 = static_ball([int(fraction(505, 2)), int(fraction(639, 2))], 1)
obj34.color = Color('white')
obj34.group = 34
obj34_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj34.png')
image_bindings.append([obj34, obj34_image])
user_shapes.append(obj34)
obj31 = box([int(fraction(505, 2) - fraction(201, 2)), int(308 - fraction(
    11, 2))], 201, 11)
obj31.color = Color('white')
obj31.group = 31
obj31_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj31.png')
image_bindings.append([obj31, obj31_image])
user_shapes.append(obj31)
obj27 = cosmetic_ball([int(fraction(505, 2)), int(308)], fraction(21, 2))
obj27.color = Color('white')
obj27.group = 27
obj27_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj27.png')
image_bindings.append([obj27, obj27_image])
user_shapes.append(obj27)
obj1 = box([int(fraction(655, 2) - 30), int(fraction(535, 2) - 30)], 60, 60)
obj1.color = Color('white')
obj1.group = 1
obj1_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj1.png')
image_bindings.append([obj1, obj1_image])
user_shapes.append(obj1)
obj25 = cosmetic_ball([int(fraction(655, 2)), int(fraction(425, 2))], 25)
obj25.color = Color('white')
obj25.group = 25
obj25_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj25.png')
image_bindings.append([obj25, obj25_image])
user_shapes.append(obj25)
obj2 = ball([int(fraction(655, 2)), int(fraction(335, 2))], 20)
obj2.color = Color('white')
obj2.group = 2
obj2_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj2.png')
image_bindings.append([obj2, obj2_image])
user_shapes.append(obj2)
obj40 = cosmetic_ball([int(fraction(445, 2)), int(fraction(445, 2))], 75)
obj40.color = Color('white')
obj40.group = 40
obj40_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj40.png')
image_bindings.append([obj40, obj40_image])
user_shapes.append(obj40)
obj39 = cosmetic_ball([int(fraction(505, 2)), int(fraction(245, 2))], 25)
obj39.color = Color('white')
obj39.group = 39
obj39_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj39.png')
image_bindings.append([obj39, obj39_image])
user_shapes.append(obj39)
obj37 = cosmetic_ball([int(275), int(75)], 75)
obj37.color = Color('white')
obj37.group = 37
obj37_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj37.png')
image_bindings.append([obj37, obj37_image])
user_shapes.append(obj37)
obj32 = ball([int(fraction(355, 2)), int(75)], fraction(45, 2))
obj32.color = Color('white')
obj32.group = 32
obj32_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj32.png')
image_bindings.append([obj32, obj32_image])
user_shapes.append(obj32)
obj21 = box([int(275 - fraction(15, 2)), int(209 - fraction(15, 2))], 15, 15)
obj21.color = Color('white')
obj21.group = 21
obj21_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj21.png')
image_bindings.append([obj21, obj21_image])
user_shapes.append(obj21)
obj20 = box([int(275 - fraction(15, 2)), int(194 - fraction(15, 2))], 15, 15)
obj20.color = Color('white')
obj20.group = 20
obj20_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj20.png')
image_bindings.append([obj20, obj20_image])
user_shapes.append(obj20)
obj19 = box([int(275 - fraction(15, 2)), int(179 - fraction(15, 2))], 15, 15)
obj19.color = Color('white')
obj19.group = 19
obj19_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj19.png')
image_bindings.append([obj19, obj19_image])
user_shapes.append(obj19)
obj18 = box([int(275 - fraction(15, 2)), int(164 - fraction(15, 2))], 15, 15)
obj18.color = Color('white')
obj18.group = 18
obj18_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj18.png')
image_bindings.append([obj18, obj18_image])
user_shapes.append(obj18)
obj16 = box([int(260 - fraction(15, 2)), int(209 - fraction(15, 2))], 15, 15)
obj16.color = Color('white')
obj16.group = 16
obj16_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj16.png')
image_bindings.append([obj16, obj16_image])
user_shapes.append(obj16)
obj15 = box([int(260 - fraction(15, 2)), int(194 - fraction(15, 2))], 15, 15)
obj15.color = Color('white')
obj15.group = 15
obj15_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj15.png')
image_bindings.append([obj15, obj15_image])
user_shapes.append(obj15)
obj14 = box([int(260 - fraction(15, 2)), int(179 - fraction(15, 2))], 15, 15)
obj14.color = Color('white')
obj14.group = 14
obj14_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj14.png')
image_bindings.append([obj14, obj14_image])
user_shapes.append(obj14)
obj13 = box([int(260 - fraction(15, 2)), int(164 - fraction(15, 2))], 15, 15)
obj13.color = Color('white')
obj13.group = 13
obj13_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj13.png')
image_bindings.append([obj13, obj13_image])
user_shapes.append(obj13)
obj11 = box([int(245 - fraction(15, 2)), int(209 - fraction(15, 2))], 15, 15)
obj11.color = Color('white')
obj11.group = 11
obj11_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj11.png')
image_bindings.append([obj11, obj11_image])
user_shapes.append(obj11)
obj10 = box([int(245 - fraction(15, 2)), int(194 - fraction(15, 2))], 15, 15)
obj10.color = Color('white')
obj10.group = 10
obj10_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj10.png')
image_bindings.append([obj10, obj10_image])
user_shapes.append(obj10)
obj9 = box([int(245 - fraction(15, 2)), int(179 - fraction(15, 2))], 15, 15)
obj9.color = Color('white')
obj9.group = 9
obj9_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj9.png')
image_bindings.append([obj9, obj9_image])
user_shapes.append(obj9)
obj8 = box([int(245 - fraction(15, 2)), int(164 - fraction(15, 2))], 15, 15)
obj8.color = Color('white')
obj8.group = 8
obj8_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj8.png')
image_bindings.append([obj8, obj8_image])
user_shapes.append(obj8)
obj6 = box([int(230 - fraction(15, 2)), int(209 - fraction(15, 2))], 15, 15)
obj6.color = Color('white')
obj6.group = 6
obj6_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj6.png')
image_bindings.append([obj6, obj6_image])
user_shapes.append(obj6)
obj5 = box([int(230 - fraction(15, 2)), int(194 - fraction(15, 2))], 15, 15)
obj5.color = Color('white')
obj5.group = 5
obj5_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj5.png')
image_bindings.append([obj5, obj5_image])
user_shapes.append(obj5)
obj4 = box([int(230 - fraction(15, 2)), int(179 - fraction(15, 2))], 15, 15)
obj4.color = Color('white')
obj4.group = 4
obj4_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj4.png')
image_bindings.append([obj4, obj4_image])
user_shapes.append(obj4)
obj3 = box([int(230 - fraction(15, 2)), int(164 - fraction(15, 2))], 15, 15)
obj3.color = Color('white')
obj3.group = 3
obj3_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj3.png')
image_bindings.append([obj3, obj3_image])
user_shapes.append(obj3)
obj49 = static_box([int(5 - 5), int(fraction(373, 2) - fraction(353, 2))], 
    10, 353)
obj49.color = Color('white')
obj49.group = 49
obj49_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj49.png')
image_bindings.append([obj49, obj49_image])
user_shapes.append(obj49)
obj47 = static_box([int(fraction(505, 2) - fraction(505, 2)), int(5 - 5)], 
    505, 10)
obj47.color = Color('white')
obj47.group = 47
obj47_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj47.png')
image_bindings.append([obj47, obj47_image])
user_shapes.append(obj47)
rotary_spring(obj34, obj31, 0, 100000000, 0)
obj31.mass = 10
pivot27 = pivot((fraction(505, 2), 308))
pivots.append(pivot27)
pivot27.connect(obj31)
obj1.mass = 10


def on_collide_1_2(s, f, p):
    try:
        obj3.body.position = p[0] + obj3.body.position[0] + -1 * (w / 2), p[1
            ] + obj3.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_1 = reactivate(obj3)
    except e:
        _hy_anon_var_1 = print(e)
    try:
        obj4.body.position = p[0] + obj4.body.position[0] + -1 * (w / 2), p[1
            ] + obj4.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_2 = reactivate(obj4)
    except e:
        _hy_anon_var_2 = print(e)
    try:
        obj5.body.position = p[0] + obj5.body.position[0] + -1 * (w / 2), p[1
            ] + obj5.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_3 = reactivate(obj5)
    except e:
        _hy_anon_var_3 = print(e)
    try:
        obj6.body.position = p[0] + obj6.body.position[0] + -1 * (w / 2), p[1
            ] + obj6.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_4 = reactivate(obj6)
    except e:
        _hy_anon_var_4 = print(e)
    try:
        obj8.body.position = p[0] + obj8.body.position[0] + -1 * (w / 2), p[1
            ] + obj8.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_5 = reactivate(obj8)
    except e:
        _hy_anon_var_5 = print(e)
    try:
        obj9.body.position = p[0] + obj9.body.position[0] + -1 * (w / 2), p[1
            ] + obj9.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_6 = reactivate(obj9)
    except e:
        _hy_anon_var_6 = print(e)
    try:
        obj10.body.position = p[0] + obj10.body.position[0] + -1 * (w / 2), p[1
            ] + obj10.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_7 = reactivate(obj10)
    except e:
        _hy_anon_var_7 = print(e)
    try:
        obj11.body.position = p[0] + obj11.body.position[0] + -1 * (w / 2), p[1
            ] + obj11.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_8 = reactivate(obj11)
    except e:
        _hy_anon_var_8 = print(e)
    try:
        obj13.body.position = p[0] + obj13.body.position[0] + -1 * (w / 2), p[1
            ] + obj13.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_9 = reactivate(obj13)
    except e:
        _hy_anon_var_9 = print(e)
    try:
        obj14.body.position = p[0] + obj14.body.position[0] + -1 * (w / 2), p[1
            ] + obj14.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_10 = reactivate(obj14)
    except e:
        _hy_anon_var_10 = print(e)
    try:
        obj15.body.position = p[0] + obj15.body.position[0] + -1 * (w / 2), p[1
            ] + obj15.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_11 = reactivate(obj15)
    except e:
        _hy_anon_var_11 = print(e)
    try:
        obj16.body.position = p[0] + obj16.body.position[0] + -1 * (w / 2), p[1
            ] + obj16.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_12 = reactivate(obj16)
    except e:
        _hy_anon_var_12 = print(e)
    try:
        obj18.body.position = p[0] + obj18.body.position[0] + -1 * (w / 2), p[1
            ] + obj18.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_13 = reactivate(obj18)
    except e:
        _hy_anon_var_13 = print(e)
    try:
        obj19.body.position = p[0] + obj19.body.position[0] + -1 * (w / 2), p[1
            ] + obj19.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_14 = reactivate(obj19)
    except e:
        _hy_anon_var_14 = print(e)
    try:
        obj20.body.position = p[0] + obj20.body.position[0] + -1 * (w / 2), p[1
            ] + obj20.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_15 = reactivate(obj20)
    except e:
        _hy_anon_var_15 = print(e)
    try:
        obj21.body.position = p[0] + obj21.body.position[0] + -1 * (w / 2), p[1
            ] + obj21.body.position[1] + -1 * (h / 2)
        deactivate(f)
        _hy_anon_var_16 = reactivate(obj21)
    except e:
        _hy_anon_var_16 = print(e)
    return _hy_anon_var_16


add_collision(obj2, obj1, on_collide_1_2) if 'obj1' in vars() else None
obj2.mass = 10
obj2.gravity = 0, 0
obj32.mass = 10000
obj32.hit([0, 1500000], obj32.position)
obj21.mass = 10
deactivate(obj21) if 'obj21' in vars() else None
obj20.mass = 10
deactivate(obj20) if 'obj20' in vars() else None
obj19.mass = 10
deactivate(obj19) if 'obj19' in vars() else None
obj18.mass = 10
deactivate(obj18) if 'obj18' in vars() else None
obj16.mass = 10
deactivate(obj16) if 'obj16' in vars() else None
obj15.mass = 10
deactivate(obj15) if 'obj15' in vars() else None
obj14.mass = 10
deactivate(obj14) if 'obj14' in vars() else None
obj13.mass = 10
deactivate(obj13) if 'obj13' in vars() else None
obj11.mass = 10
deactivate(obj11) if 'obj11' in vars() else None
obj10.mass = 10
deactivate(obj10) if 'obj10' in vars() else None
obj9.mass = 10
deactivate(obj9) if 'obj9' in vars() else None
obj8.mass = 10
deactivate(obj8) if 'obj8' in vars() else None
obj6.mass = 10
deactivate(obj6) if 'obj6' in vars() else None
obj5.mass = 10
deactivate(obj5) if 'obj5' in vars() else None
obj4.mass = 10
deactivate(obj4) if 'obj4' in vars() else None
obj3.mass = 10
deactivate(obj3) if 'obj3' in vars() else None


def image_for(s):
    global image_bindings
    for b in image_bindings:
        if b[0] == s:
            return b[1]
            _hy_anon_var_18 = None
        else:
            _hy_anon_var_18 = None
    return False


def draw_images(cosmetic):

    def f(keys):
        global user_shapes
        for s in user_shapes:
            if not image_for(s):
                continue
                _hy_anon_var_20 = None
            else:
                _hy_anon_var_20 = None
            if not cosmetic == s._cosmetic:
                continue
                _hy_anon_var_21 = None
            else:
                _hy_anon_var_21 = None
            if not s.active:
                continue
                _hy_anon_var_22 = None
            else:
                _hy_anon_var_22 = None
            if s.body:
                p = Vec2d(s.body.position.x, s.body.position.y)
                _hy_anon_var_23 = None
            else:
                p = Vec2d(s._x, s._y)
                _hy_anon_var_23 = None
            angle = 0
            if s.body:
                angle = s.body.angle
                _hy_anon_var_24 = None
            else:
                _hy_anon_var_24 = None
            angle_degrees = math.degrees(angle)
            rotated_logo_img = pygame.transform.rotate(image_for(s), -1 *
                angle_degrees)
            offset = Vec2d(rotated_logo_img.get_size()) / 2
            p = p - offset
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
            pygame.draw.line(screen, Color('black'), start, end)


def draw_connection_lines(keys):
    global pivots
    for c in connected_shapes:
        start = c[0].body.position
        end = c[1].body.position
        if not c[0].active or not c[0].active:
            continue
            _hy_anon_var_28 = None
        else:
            _hy_anon_var_28 = None
        screen = pygame.display.get_surface()
        pygame.draw.line(screen, Color('black'), start, end)


add_observer(draw_images(True))
add_observer(draw_pivot_lines)
add_observer(draw_connection_lines)
add_observer(draw_images(False))
run()

