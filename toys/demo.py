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
obj139 = static_box([int(fraction(505, 2) - fraction(505, 2)), int(368 - 5)
    ], 505, 10)
obj139.color = Color('white')
obj139.group = 139
obj139_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj139.png')
image_bindings.append([obj139, obj139_image])
user_shapes.append(obj139)
obj141 = static_box([int(500 - 5), int(fraction(373, 2) - fraction(353, 2))
    ], 10, 353)
obj141.color = Color('white')
obj141.group = 141
obj141_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj141.png')
image_bindings.append([obj141, obj141_image])
user_shapes.append(obj141)
obj137 = cosmetic_ball([int(fraction(505, 2)), int(fraction(373, 2))],
    fraction(485, 2))
obj137.color = Color('white')
obj137.group = 137
obj137_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj137.png')
image_bindings.append([obj137, obj137_image])
user_shapes.append(obj137)
obj132 = ball([int(fraction(865, 2)), int(287)], 20)
obj132.color = Color('white')
obj132.group = 132
obj132_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj132.png')
image_bindings.append([obj132, obj132_image])
user_shapes.append(obj132)
obj128 = cosmetic_ball([int(fraction(865, 2)), int(287)], fraction(21, 2))
obj128.color = Color('white')
obj128.group = 128
obj128_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj128.png')
image_bindings.append([obj128, obj128_image])
user_shapes.append(obj128)
obj126 = ball([int(fraction(785, 2)), int(287)], 20)
obj126.color = Color('white')
obj126.group = 126
obj126_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj126.png')
image_bindings.append([obj126, obj126_image])
user_shapes.append(obj126)
obj122 = cosmetic_ball([int(fraction(785, 2)), int(287)], fraction(21, 2))
obj122.color = Color('white')
obj122.group = 122
obj122_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj122.png')
image_bindings.append([obj122, obj122_image])
user_shapes.append(obj122)
obj120 = ball([int(fraction(705, 2)), int(287)], 20)
obj120.color = Color('white')
obj120.group = 120
obj120_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj120.png')
image_bindings.append([obj120, obj120_image])
user_shapes.append(obj120)
obj116 = cosmetic_ball([int(fraction(705, 2)), int(287)], fraction(21, 2))
obj116.color = Color('white')
obj116.group = 116
obj116_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj116.png')
image_bindings.append([obj116, obj116_image])
user_shapes.append(obj116)
obj114 = ball([int(fraction(625, 2)), int(287)], 20)
obj114.color = Color('white')
obj114.group = 114
obj114_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj114.png')
image_bindings.append([obj114, obj114_image])
user_shapes.append(obj114)
obj110 = cosmetic_ball([int(fraction(625, 2)), int(287)], fraction(21, 2))
obj110.color = Color('white')
obj110.group = 110
obj110_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj110.png')
image_bindings.append([obj110, obj110_image])
user_shapes.append(obj110)
obj108 = ball([int(fraction(545, 2)), int(287)], 20)
obj108.color = Color('white')
obj108.group = 108
obj108_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj108.png')
image_bindings.append([obj108, obj108_image])
user_shapes.append(obj108)
obj104 = cosmetic_ball([int(fraction(545, 2)), int(287)], fraction(21, 2))
obj104.color = Color('white')
obj104.group = 104
obj104_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj104.png')
image_bindings.append([obj104, obj104_image])
user_shapes.append(obj104)
obj102 = ball([int(fraction(465, 2)), int(287)], 20)
obj102.color = Color('white')
obj102.group = 102
obj102_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj102.png')
image_bindings.append([obj102, obj102_image])
user_shapes.append(obj102)
obj98 = cosmetic_ball([int(fraction(465, 2)), int(287)], fraction(21, 2))
obj98.color = Color('white')
obj98.group = 98
obj98_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj98.png')
image_bindings.append([obj98, obj98_image])
user_shapes.append(obj98)
obj96 = ball([int(fraction(385, 2)), int(287)], 20)
obj96.color = Color('white')
obj96.group = 96
obj96_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj96.png')
image_bindings.append([obj96, obj96_image])
user_shapes.append(obj96)
obj92 = cosmetic_ball([int(fraction(385, 2)), int(287)], fraction(21, 2))
obj92.color = Color('white')
obj92.group = 92
obj92_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj92.png')
image_bindings.append([obj92, obj92_image])
user_shapes.append(obj92)
obj90 = ball([int(fraction(305, 2)), int(287)], 20)
obj90.color = Color('white')
obj90.group = 90
obj90_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj90.png')
image_bindings.append([obj90, obj90_image])
user_shapes.append(obj90)
obj86 = cosmetic_ball([int(fraction(305, 2)), int(287)], fraction(21, 2))
obj86.color = Color('white')
obj86.group = 86
obj86_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj86.png')
image_bindings.append([obj86, obj86_image])
user_shapes.append(obj86)
obj84 = ball([int(fraction(225, 2)), int(287)], 20)
obj84.color = Color('white')
obj84.group = 84
obj84_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj84.png')
image_bindings.append([obj84, obj84_image])
user_shapes.append(obj84)
obj80 = cosmetic_ball([int(fraction(225, 2)), int(287)], fraction(21, 2))
obj80.color = Color('white')
obj80.group = 80
obj80_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj80.png')
image_bindings.append([obj80, obj80_image])
user_shapes.append(obj80)
obj78 = ball([int(fraction(145, 2)), int(287)], 20)
obj78.color = Color('white')
obj78.group = 78
obj78_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj78.png')
image_bindings.append([obj78, obj78_image])
user_shapes.append(obj78)
obj74 = cosmetic_ball([int(fraction(145, 2)), int(287)], fraction(21, 2))
obj74.color = Color('white')
obj74.group = 74
obj74_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj74.png')
image_bindings.append([obj74, obj74_image])
user_shapes.append(obj74)
obj73 = cosmetic_ball([int(fraction(505, 2)), int(217)], 50)
obj73.color = Color('white')
obj73.group = 73
obj73_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj73.png')
image_bindings.append([obj73, obj73_image])
user_shapes.append(obj73)
obj70 = ball([int(fraction(785, 2)), int(147)], 20)
obj70.color = Color('white')
obj70.group = 70
obj70_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj70.png')
image_bindings.append([obj70, obj70_image])
user_shapes.append(obj70)
obj66 = cosmetic_ball([int(fraction(785, 2)), int(147)], fraction(21, 2))
obj66.color = Color('white')
obj66.group = 66
obj66_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj66.png')
image_bindings.append([obj66, obj66_image])
user_shapes.append(obj66)
obj64 = ball([int(fraction(705, 2)), int(147)], 20)
obj64.color = Color('white')
obj64.group = 64
obj64_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj64.png')
image_bindings.append([obj64, obj64_image])
user_shapes.append(obj64)
obj60 = cosmetic_ball([int(fraction(705, 2)), int(147)], fraction(21, 2))
obj60.color = Color('white')
obj60.group = 60
obj60_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj60.png')
image_bindings.append([obj60, obj60_image])
user_shapes.append(obj60)
obj58 = ball([int(fraction(625, 2)), int(147)], 20)
obj58.color = Color('white')
obj58.group = 58
obj58_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj58.png')
image_bindings.append([obj58, obj58_image])
user_shapes.append(obj58)
obj54 = cosmetic_ball([int(fraction(625, 2)), int(147)], fraction(21, 2))
obj54.color = Color('white')
obj54.group = 54
obj54_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj54.png')
image_bindings.append([obj54, obj54_image])
user_shapes.append(obj54)
obj52 = ball([int(fraction(545, 2)), int(147)], 20)
obj52.color = Color('white')
obj52.group = 52
obj52_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj52.png')
image_bindings.append([obj52, obj52_image])
user_shapes.append(obj52)
obj48 = cosmetic_ball([int(fraction(545, 2)), int(147)], fraction(21, 2))
obj48.color = Color('white')
obj48.group = 48
obj48_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj48.png')
image_bindings.append([obj48, obj48_image])
user_shapes.append(obj48)
obj46 = ball([int(fraction(465, 2)), int(147)], 20)
obj46.color = Color('white')
obj46.group = 46
obj46_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj46.png')
image_bindings.append([obj46, obj46_image])
user_shapes.append(obj46)
obj42 = cosmetic_ball([int(fraction(465, 2)), int(147)], fraction(21, 2))
obj42.color = Color('white')
obj42.group = 42
obj42_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj42.png')
image_bindings.append([obj42, obj42_image])
user_shapes.append(obj42)
obj40 = ball([int(fraction(385, 2)), int(147)], 20)
obj40.color = Color('white')
obj40.group = 40
obj40_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj40.png')
image_bindings.append([obj40, obj40_image])
user_shapes.append(obj40)
obj36 = cosmetic_ball([int(fraction(385, 2)), int(147)], fraction(21, 2))
obj36.color = Color('white')
obj36.group = 36
obj36_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj36.png')
image_bindings.append([obj36, obj36_image])
user_shapes.append(obj36)
obj34 = ball([int(fraction(305, 2)), int(147)], 20)
obj34.color = Color('white')
obj34.group = 34
obj34_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj34.png')
image_bindings.append([obj34, obj34_image])
user_shapes.append(obj34)
obj30 = cosmetic_ball([int(fraction(305, 2)), int(147)], fraction(21, 2))
obj30.color = Color('white')
obj30.group = 30
obj30_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj30.png')
image_bindings.append([obj30, obj30_image])
user_shapes.append(obj30)
obj28 = ball([int(fraction(225, 2)), int(147)], 20)
obj28.color = Color('white')
obj28.group = 28
obj28_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj28.png')
image_bindings.append([obj28, obj28_image])
user_shapes.append(obj28)
obj24 = cosmetic_ball([int(fraction(225, 2)), int(147)], fraction(21, 2))
obj24.color = Color('white')
obj24.group = 24
obj24_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj24.png')
image_bindings.append([obj24, obj24_image])
user_shapes.append(obj24)
obj23 = cosmetic_ball([int(fraction(505, 2)), int(117)], 10)
obj23.color = Color('white')
obj23.group = 23
obj23_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj23.png')
image_bindings.append([obj23, obj23_image])
user_shapes.append(obj23)
obj21 = cosmetic_ball([int(355), int(fraction(173, 2))], 50)
obj21.color = Color('white')
obj21.group = 21
obj21_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj21.png')
image_bindings.append([obj21, obj21_image])
user_shapes.append(obj21)
obj20 = box([int(fraction(569, 2) - fraction(41, 2)), int(fraction(173, 2) -
    fraction(41, 2))], 41, 41)
obj20.color = Color('white')
obj20.group = 20
obj20_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj20.png')
image_bindings.append([obj20, obj20_image])
user_shapes.append(obj20)
obj16 = box([int(fraction(487, 2) - fraction(41, 2)), int(fraction(173, 2) -
    fraction(41, 2))], 41, 41)
obj16.color = Color('white')
obj16.group = 16
obj16_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj16.png')
image_bindings.append([obj16, obj16_image])
user_shapes.append(obj16)
obj12 = box([int(fraction(405, 2) - fraction(41, 2)), int(fraction(173, 2) -
    fraction(41, 2))], 41, 41)
obj12.color = Color('white')
obj12.group = 12
obj12_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj12.png')
image_bindings.append([obj12, obj12_image])
user_shapes.append(obj12)
obj8 = box([int(fraction(323, 2) - fraction(41, 2)), int(fraction(173, 2) -
    fraction(41, 2))], 41, 41)
obj8.color = Color('white')
obj8.group = 8
obj8_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj8.png')
image_bindings.append([obj8, obj8_image])
user_shapes.append(obj8)
obj4 = box([int(fraction(241, 2) - fraction(41, 2)), int(fraction(173, 2) -
    fraction(41, 2))], 41, 41)
obj4.color = Color('white')
obj4.group = 4
obj4_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj4.png')
image_bindings.append([obj4, obj4_image])
user_shapes.append(obj4)
obj141 = static_box([int(5 - 5), int(fraction(373, 2) - fraction(353, 2))],
    10, 353)
obj141.color = Color('white')
obj141.group = 141
obj141_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj141.png')
image_bindings.append([obj141, obj141_image])
user_shapes.append(obj141)
obj139 = static_box([int(fraction(505, 2) - fraction(505, 2)), int(5 - 5)],
    505, 10)
obj139.color = Color('white')
obj139.group = 139
obj139_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj139.png')
image_bindings.append([obj139, obj139_image])
user_shapes.append(obj139)
obj132.mass = 10
motor(obj132, -5)
pivot128 = pivot((fraction(865, 2), 287))
pivots.append(pivot128)
pivot128.connect(obj132)
obj126.mass = 10
motor(obj126, -5)
pivot122 = pivot((fraction(785, 2), 287))
pivots.append(pivot122)
pivot122.connect(obj126)
obj120.mass = 10
motor(obj120, -5)
pivot116 = pivot((fraction(705, 2), 287))
pivots.append(pivot116)
pivot116.connect(obj120)
obj114.mass = 10
motor(obj114, -5)
pivot110 = pivot((fraction(625, 2), 287))
pivots.append(pivot110)
pivot110.connect(obj114)
obj108.mass = 10
motor(obj108, -5)
pivot104 = pivot((fraction(545, 2), 287))
pivots.append(pivot104)
pivot104.connect(obj108)
obj102.mass = 10
motor(obj102, -5)
pivot98 = pivot((fraction(465, 2), 287))
pivots.append(pivot98)
pivot98.connect(obj102)
obj96.mass = 10
motor(obj96, -5)
pivot92 = pivot((fraction(385, 2), 287))
pivots.append(pivot92)
pivot92.connect(obj96)
obj90.mass = 10
motor(obj90, -5)
pivot86 = pivot((fraction(305, 2), 287))
pivots.append(pivot86)
pivot86.connect(obj90)
obj84.mass = 10
motor(obj84, -5)
pivot80 = pivot((fraction(225, 2), 287))
pivots.append(pivot80)
pivot80.connect(obj84)
obj78.mass = 10
motor(obj78, -5)
pivot74 = pivot((fraction(145, 2), 287))
pivots.append(pivot74)
pivot74.connect(obj78)
obj70.mass = 10
motor(obj70, 5)
pivot66 = pivot((fraction(785, 2), 147))
pivots.append(pivot66)
pivot66.connect(obj70)
obj64.mass = 10
motor(obj64, 5)
pivot60 = pivot((fraction(705, 2), 147))
pivots.append(pivot60)
pivot60.connect(obj64)
obj58.mass = 10
motor(obj58, 5)
pivot54 = pivot((fraction(625, 2), 147))
pivots.append(pivot54)
pivot54.connect(obj58)
obj52.mass = 10
motor(obj52, 5)
pivot48 = pivot((fraction(545, 2), 147))
pivots.append(pivot48)
pivot48.connect(obj52)
obj46.mass = 10
motor(obj46, 5)
pivot42 = pivot((fraction(465, 2), 147))
pivots.append(pivot42)
pivot42.connect(obj46)
obj40.mass = 10
motor(obj40, 5)
pivot36 = pivot((fraction(385, 2), 147))
pivots.append(pivot36)
pivot36.connect(obj40)
obj34.mass = 10
motor(obj34, 5)
pivot30 = pivot((fraction(305, 2), 147))
pivots.append(pivot30)
pivot30.connect(obj34)
obj28.mass = 10
motor(obj28, 5)
pivot24 = pivot((fraction(225, 2), 147))
pivots.append(pivot24)
pivot24.connect(obj28)
obj20.mass = 10
obj20.hit([0, 0], obj20.position)
obj16.mass = 10
obj16.hit([0, 0], obj16.position)
obj12.mass = 10
obj12.hit([0, 0], obj12.position)
obj8.mass = 10
obj8.hit([0, 0], obj8.position)
obj4.mass = 10
obj4.hit([0, 0], obj4.position)


def image_for(s):
    global image_bindings
    for b in image_bindings:
        if b[0] == s:
            return b[1]
            _hy_anon_var_1 = None
        else:
            _hy_anon_var_1 = None
    return False


def draw_images(cosmetic):

    def f(keys):
        global user_shapes
        for s in user_shapes:
            if not image_for(s):
                continue
                _hy_anon_var_3 = None
            else:
                _hy_anon_var_3 = None
            if not cosmetic == s._cosmetic:
                continue
                _hy_anon_var_4 = None
            else:
                _hy_anon_var_4 = None
            if not s.active:
                continue
                _hy_anon_var_5 = None
            else:
                _hy_anon_var_5 = None
            if s.body:
                p = Vec2d(s.body.position.x, s.body.position.y)
                _hy_anon_var_6 = None
            else:
                p = Vec2d(s._x, s._y)
                _hy_anon_var_6 = None
            angle = 0
            if s.body:
                angle = s.body.angle
                _hy_anon_var_7 = None
            else:
                _hy_anon_var_7 = None
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
            _hy_anon_var_11 = None
        else:
            _hy_anon_var_11 = None
        screen = pygame.display.get_surface()
        pygame.draw.line(screen, Color('black'), start, end)


add_observer(draw_images(True))
add_observer(draw_pivot_lines)
add_observer(draw_connection_lines)
add_observer(draw_images(False))
run()

