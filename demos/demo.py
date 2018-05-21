import sys
import math
import pymunk
from pyphysicssandbox import *
import pygame
from pyphysicssandbox import Vec2d
w = 200
h = 190
user_shapes = []
image_bindings = []
pivots = []
connected_shapes = []
click_handled = 2
window('Most Awesome Thing Ever', w, h)


def make_obj4(off_x, off_y):
    obj4 = static_box([int(100 - 100) + int(off_x), int(185 - 5) + int(
        off_y)], 200, 10)
    obj4.color = Color('white')
    obj4.group = 4
    obj4_image = pygame.image.load('./obj4.png')
    image_bindings.append([obj4, obj4_image])
    user_shapes.append(obj4)
    return obj4


obj4 = make_obj4(0, 0)


def make_obj8(off_x, off_y):
    obj8 = cosmetic_ball([int(100) + int(off_x), +int(130), int(off_y)], 50)
    obj8.color = Color('white')
    obj8.group = 8
    obj8_image = pygame.image.load('./obj8.png')
    image_bindings.append([obj8, obj8_image])
    user_shapes.append(obj8)
    return obj8


obj8 = make_obj8(0, 0)


def make_obj6(off_x, off_y):
    obj6 = cosmetic_ball([int(165) + int(off_x), +int(40), int(off_y)], 25)
    obj6.color = Color('white')
    obj6.group = 6
    obj6_image = pygame.image.load('./obj6.png')
    image_bindings.append([obj6, obj6_image])
    user_shapes.append(obj6)
    return obj6


obj6 = make_obj6(0, 0)


def make_obj2(off_x, off_y):
    obj2 = ball([int(100) + int(off_x), +int(40), int(off_y)], 40)
    obj2.color = Color('white')
    obj2.group = 2
    obj2_image = pygame.image.load('./obj2.png')
    image_bindings.append([obj2, obj2_image])
    user_shapes.append(obj2)
    obj2.mass = 10
    return obj2


obj2 = make_obj2(0, 0)


def make_obj5(off_x, off_y):
    obj5 = cosmetic_ball([int(35) + int(off_x), +int(40), int(off_y)], 25)
    obj5.color = Color('white')
    obj5.group = 5
    obj5_image = pygame.image.load('./obj5.png')
    image_bindings.append([obj5, obj5_image])
    user_shapes.append(obj5)
    return obj5


obj5 = make_obj5(0, 0)


def image_for(s):
    global image_bindings
    for b in image_bindings:
        if b[0] == s:
            return b[1]
            _hy_anon_var_6 = None
        else:
            _hy_anon_var_6 = None
    return False


def draw_images(cosmetic):

    def f(keys):
        global user_shapes
        for s in user_shapes:
            if not image_for(s):
                continue
                _hy_anon_var_8 = None
            else:
                _hy_anon_var_8 = None
            if not cosmetic == s._cosmetic:
                continue
                _hy_anon_var_9 = None
            else:
                _hy_anon_var_9 = None
            if not s.active:
                continue
                _hy_anon_var_10 = None
            else:
                _hy_anon_var_10 = None
            if s.body:
                p = Vec2d(s.body.position.x, s.body.position.y)
                _hy_anon_var_11 = None
            else:
                p = Vec2d(s._x, s._y)
                _hy_anon_var_11 = None
            angle = 0
            if s.body:
                angle = s.body.angle
                _hy_anon_var_12 = None
            else:
                _hy_anon_var_12 = None
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
            if not p.active:
                continue
                _hy_anon_var_15 = None
            else:
                _hy_anon_var_15 = None
            other = j.a
            end = other.position
            screen = pygame.display.get_surface()
            pygame.draw.line(screen, Color('black'), start, end)


def draw_connection_lines(keys):
    for c in connected_shapes:
        start = c[0].body.position
        end = c[1].body.position
        if not c[0].active or not c[1].active:
            deactivate(c[2])
            continue
            _hy_anon_var_17 = None
        else:
            _hy_anon_var_17 = None
        screen = pygame.display.get_surface()
        pygame.draw.line(screen, Color('black'), start, end)


def clear_click(keys):
    global click_handled
    click_handled = max(0, click_handled - 1)


add_observer(clear_click)
add_observer(draw_images(True))
add_observer(draw_pivot_lines)
add_observer(draw_connection_lines)
add_observer(draw_images(False))
run()

