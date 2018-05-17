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


def make_obj38(off_x, off_y, debug):
    print('Making ' + 'make_obj38' + '\n' +
        '#(struct:physical 38 505/2 368 () #<box-collider> #(struct:object:image% ...) #f)'
        ) if debug else None
    obj38 = static_box([int(fraction(505, 2) - fraction(505, 2)) + int(
        off_x), int(368 - 5) + int(off_y)], 505, 10)
    obj38.color = Color('white')
    obj38.group = 38
    obj38_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj38.png')
    image_bindings.append([obj38, obj38_image])
    user_shapes.append(obj38)
    return obj38


obj38 = make_obj38(0, 0, False)


def make_obj40(off_x, off_y, debug):
    print('Making ' + 'make_obj40' + '\n' +
        '#(struct:physical 40 500 353/2 () #<box-collider> #(struct:object:image% ...) #f)'
        ) if debug else None
    obj40 = static_box([int(500 - 5) + int(off_x), int(fraction(373, 2) -
        fraction(353, 2)) + int(off_y)], 10, 353)
    obj40.color = Color('white')
    obj40.group = 40
    obj40_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj40.png')
    image_bindings.append([obj40, obj40_image])
    user_shapes.append(obj40)
    return obj40


obj40 = make_obj40(0, 0, False)


def make_obj36(off_x, off_y, debug):
    print('Making ' + 'make_obj36' + '\n' +
        '#(struct:cosmetic 36 485/2 353/2 () #(struct:object:image% ...))'
        ) if debug else None
    obj36 = cosmetic_ball([int(fraction(505, 2)) + int(off_x), +int(
        fraction(373, 2)), int(off_y)], fraction(485, 2))
    obj36.color = Color('white')
    obj36.group = 36
    obj36_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj36.png')
    image_bindings.append([obj36, obj36_image])
    user_shapes.append(obj36)
    return obj36


obj36 = make_obj36(0, 0, False)


def make_obj3(off_x, off_y, debug):
    print('Making ' + 'make_obj3' + '\n' +
        '#(struct:physical 3 20 60 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:445:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj3 = ball([int(fraction(505, 2)) + int(off_x), +int(fraction(413, 2)),
        int(off_y)], 20)
    obj3.color = Color('white')
    obj3.group = 3
    obj3_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj3.png')
    image_bindings.append([obj3, obj3_image])
    user_shapes.append(obj3)
    return obj3


obj3 = make_obj3(0, 0, False)


def make_obj2(off_x, off_y, debug):
    print('Making ' + 'make_obj2' + '\n' +
        '#(struct:physical 2 20 20 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:445:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj2 = ball([int(fraction(505, 2)) + int(off_x), +int(fraction(333, 2)),
        int(off_y)], 20)
    obj2.color = Color('white')
    obj2.group = 2
    obj2_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj2.png')
    image_bindings.append([obj2, obj2_image])
    user_shapes.append(obj2)
    return obj2


obj2 = make_obj2(0, 0, False)


def make_obj7(off_x, off_y, debug):
    print('Making ' + 'make_obj7' + '\n' +
        '#(struct:physical 7 20 60 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:445:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj7 = ball([int(fraction(505, 2)) + int(off_x), +int(fraction(413, 2)),
        int(off_y)], 20)
    obj7.color = Color('white')
    obj7.group = 7
    obj7_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj7.png')
    image_bindings.append([obj7, obj7_image])
    user_shapes.append(obj7)
    return obj7


obj7 = make_obj7(0, 0, False)


def make_obj6(off_x, off_y, debug):
    print('Making ' + 'make_obj6' + '\n' +
        '#(struct:physical 6 20 20 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:445:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj6 = ball([int(fraction(505, 2)) + int(off_x), +int(fraction(333, 2)),
        int(off_y)], 20)
    obj6.color = Color('white')
    obj6.group = 6
    obj6_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj6.png')
    image_bindings.append([obj6, obj6_image])
    user_shapes.append(obj6)
    return obj6


obj6 = make_obj6(0, 0, False)


def make_obj11(off_x, off_y, debug):
    print('Making ' + 'make_obj11' + '\n' +
        '#(struct:physical 11 20 60 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:445:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj11 = ball([int(fraction(505, 2)) + int(off_x), +int(fraction(413, 2)
        ), int(off_y)], 20)
    obj11.color = Color('white')
    obj11.group = 11
    obj11_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj11.png')
    image_bindings.append([obj11, obj11_image])
    user_shapes.append(obj11)
    return obj11


obj11 = make_obj11(0, 0, False)


def make_obj10(off_x, off_y, debug):
    print('Making ' + 'make_obj10' + '\n' +
        '#(struct:physical 10 20 20 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:445:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj10 = ball([int(fraction(505, 2)) + int(off_x), +int(fraction(333, 2)
        ), int(off_y)], 20)
    obj10.color = Color('white')
    obj10.group = 10
    obj10_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj10.png')
    image_bindings.append([obj10, obj10_image])
    user_shapes.append(obj10)
    return obj10


obj10 = make_obj10(0, 0, False)


def make_obj15(off_x, off_y, debug):
    print('Making ' + 'make_obj15' + '\n' +
        '#(struct:physical 15 20 60 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:445:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj15 = ball([int(fraction(505, 2)) + int(off_x), +int(fraction(413, 2)
        ), int(off_y)], 20)
    obj15.color = Color('white')
    obj15.group = 15
    obj15_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj15.png')
    image_bindings.append([obj15, obj15_image])
    user_shapes.append(obj15)
    return obj15


obj15 = make_obj15(0, 0, False)


def make_obj14(off_x, off_y, debug):
    print('Making ' + 'make_obj14' + '\n' +
        '#(struct:physical 14 20 20 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:445:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj14 = ball([int(fraction(505, 2)) + int(off_x), +int(fraction(333, 2)
        ), int(off_y)], 20)
    obj14.color = Color('white')
    obj14.group = 14
    obj14_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj14.png')
    image_bindings.append([obj14, obj14_image])
    user_shapes.append(obj14)
    return obj14


obj14 = make_obj14(0, 0, False)


def make_obj30(off_x, off_y, debug):
    print('Making ' + 'make_obj30' + '\n' +
        '#(struct:cosmetic 30 230 43 () #(struct:object:image% ...))'
        ) if debug else None
    obj30 = cosmetic_ball([int(fraction(635, 2)) + int(off_x), +int(
        fraction(433, 2)), int(off_y)], 100)
    obj30.color = Color('white')
    obj30.group = 30
    obj30_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj30.png')
    image_bindings.append([obj30, obj30_image])
    user_shapes.append(obj30)
    return obj30


obj30 = make_obj30(0, 0, False)


def make_obj20(off_x, off_y, debug):
    print('Making ' + 'make_obj20' + '\n' +
        '#(struct:physical 20 110 20 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:363:21> #<procedure:...ery/compiler.rkt:385:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj20 = ball([int(fraction(395, 2)) + int(off_x), +int(fraction(479, 2)
        ), int(off_y)], 20)
    obj20.color = Color('white')
    obj20.group = 20
    obj20_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj20.png')
    image_bindings.append([obj20, obj20_image])
    user_shapes.append(obj20)
    return obj20


obj20 = make_obj20(0, 0, False)


def make_obj27(off_x, off_y, debug):
    print('Making ' + 'make_obj27' + '\n' +
        '#(struct:cosmetic 27 175/2 20 () #(struct:object:image% ...))'
        ) if debug else None
    obj27 = cosmetic_ball([int(175) + int(off_x), +int(fraction(479, 2)),
        int(off_y)], fraction(5, 2))
    obj27.color = Color('white')
    obj27.group = 27
    obj27_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj27.png')
    image_bindings.append([obj27, obj27_image])
    user_shapes.append(obj27)
    return obj27


obj27 = make_obj27(0, 0, False)


def make_obj19(off_x, off_y, debug):
    print('Making ' + 'make_obj19' + '\n' +
        '#(struct:physical 19 65 20 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:363:21> #<procedure:...ery/compiler.rkt:363:21> #<procedure:...ery/compiler.rkt:385:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj19 = ball([int(fraction(305, 2)) + int(off_x), +int(fraction(479, 2)
        ), int(off_y)], 20)
    obj19.color = Color('white')
    obj19.group = 19
    obj19_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj19.png')
    image_bindings.append([obj19, obj19_image])
    user_shapes.append(obj19)
    return obj19


obj19 = make_obj19(0, 0, False)


def make_obj26(off_x, off_y, debug):
    print('Making ' + 'make_obj26' + '\n' +
        '#(struct:cosmetic 26 85/2 20 () #(struct:object:image% ...))'
        ) if debug else None
    obj26 = cosmetic_ball([int(130) + int(off_x), +int(fraction(479, 2)),
        int(off_y)], fraction(5, 2))
    obj26.color = Color('white')
    obj26.group = 26
    obj26_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj26.png')
    image_bindings.append([obj26, obj26_image])
    user_shapes.append(obj26)
    return obj26


obj26 = make_obj26(0, 0, False)


def make_obj18(off_x, off_y, debug):
    print('Making ' + 'make_obj18' + '\n' +
        '#(struct:physical 18 20 20 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:363:21> #<procedure:...ery/compiler.rkt:363:21> #<procedure:...ery/compiler.rkt:385:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj18 = ball([int(fraction(215, 2)) + int(off_x), +int(fraction(479, 2)
        ), int(off_y)], 20)
    obj18.color = Color('white')
    obj18.group = 18
    obj18_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj18.png')
    image_bindings.append([obj18, obj18_image])
    user_shapes.append(obj18)
    return obj18


obj18 = make_obj18(0, 0, False)


def make_obj25(off_x, off_y, debug):
    print('Making ' + 'make_obj25' + '\n' +
        '#(struct:cosmetic 25 65 87/2 () #(struct:object:image% ...))'
        ) if debug else None
    obj25 = cosmetic_ball([int(fraction(305, 2)) + int(off_x), +int(217),
        int(off_y)], fraction(5, 2))
    obj25.color = Color('white')
    obj25.group = 25
    obj25_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj25.png')
    image_bindings.append([obj25, obj25_image])
    user_shapes.append(obj25)
    return obj25


obj25 = make_obj25(0, 0, False)


def make_obj24(off_x, off_y, debug):
    print('Making ' + 'make_obj24' + '\n' +
        '#(struct:physical 24 65 41/2 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:374:21> #<procedure:...ery/compiler.rkt:385:21>) #<box-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj24 = box([int(fraction(305, 2) - fraction(41, 2)) + int(off_x), int(
        194 - fraction(41, 2)) + int(off_y)], 41, 41)
    obj24.color = Color('white')
    obj24.group = 24
    obj24_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj24.png')
    image_bindings.append([obj24, obj24_image])
    user_shapes.append(obj24)
    return obj24


obj24 = make_obj24(0, 0, False)


def make_obj13(off_x, off_y, debug):
    print('Making ' + 'make_obj13' + '\n' +
        '#(struct:physical 13 154 30 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:385:21> #<procedure:...ery/compiler.rkt:419:21> #<procedure:...ery/compiler.rkt:496:21>) #<box-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj13 = box([int(fraction(637, 2) - 22) + int(off_x), int(fraction(287,
        2) - 30) + int(off_y)], 44, 60)
    obj13.color = Color('white')
    obj13.group = 13
    obj13_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj13.png')
    image_bindings.append([obj13, obj13_image])
    user_shapes.append(obj13)
    return obj13


obj13 = make_obj13(0, 0, False)


def make_obj9(off_x, off_y, debug):
    print('Making ' + 'make_obj9' + '\n' +
        '#(struct:physical 9 110 30 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:385:21> #<procedure:...ery/compiler.rkt:419:21> #<procedure:...ery/compiler.rkt:496:21>) #<box-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj9 = box([int(fraction(549, 2) - 22) + int(off_x), int(fraction(287, 
        2) - 30) + int(off_y)], 44, 60)
    obj9.color = Color('white')
    obj9.group = 9
    obj9_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj9.png')
    image_bindings.append([obj9, obj9_image])
    user_shapes.append(obj9)
    return obj9


obj9 = make_obj9(0, 0, False)


def make_obj5(off_x, off_y, debug):
    print('Making ' + 'make_obj5' + '\n' +
        '#(struct:physical 5 66 30 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:385:21> #<procedure:...ery/compiler.rkt:419:21> #<procedure:...ery/compiler.rkt:496:21>) #<box-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj5 = box([int(fraction(461, 2) - 22) + int(off_x), int(fraction(287, 
        2) - 30) + int(off_y)], 44, 60)
    obj5.color = Color('white')
    obj5.group = 5
    obj5_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj5.png')
    image_bindings.append([obj5, obj5_image])
    user_shapes.append(obj5)
    return obj5


obj5 = make_obj5(0, 0, False)


def make_obj1(off_x, off_y, debug):
    print('Making ' + 'make_obj1' + '\n' +
        '#(struct:physical 1 22 30 (#<procedure:...ery/compiler.rkt:306:21> #<procedure:...ery/compiler.rkt:385:21> #<procedure:...ery/compiler.rkt:419:21> #<procedure:...ery/compiler.rkt:496:21>) #<box-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj1 = box([int(fraction(373, 2) - 22) + int(off_x), int(fraction(287, 
        2) - 30) + int(off_y)], 44, 60)
    obj1.color = Color('white')
    obj1.group = 1
    obj1_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj1.png')
    image_bindings.append([obj1, obj1_image])
    user_shapes.append(obj1)
    return obj1


obj1 = make_obj1(0, 0, False)


def make_obj40(off_x, off_y, debug):
    print('Making ' + 'make_obj40' + '\n' +
        '#(struct:physical 40 5 353/2 () #<box-collider> #(struct:object:image% ...) #f)'
        ) if debug else None
    obj40 = static_box([int(5 - 5) + int(off_x), int(fraction(373, 2) -
        fraction(353, 2)) + int(off_y)], 10, 353)
    obj40.color = Color('white')
    obj40.group = 40
    obj40_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj40.png')
    image_bindings.append([obj40, obj40_image])
    user_shapes.append(obj40)
    return obj40


obj40 = make_obj40(0, 0, False)


def make_obj38(off_x, off_y, debug):
    print('Making ' + 'make_obj38' + '\n' +
        '#(struct:physical 38 505/2 5 () #<box-collider> #(struct:object:image% ...) #f)'
        ) if debug else None
    obj38 = static_box([int(fraction(505, 2) - fraction(505, 2)) + int(
        off_x), int(5 - 5) + int(off_y)], 505, 10)
    obj38.color = Color('white')
    obj38.group = 38
    obj38_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj38.png')
    image_bindings.append([obj38, obj38_image])
    user_shapes.append(obj38)
    return obj38


obj38 = make_obj38(0, 0, False)
obj3.mass = 10
deactivate(obj3) if 'obj3' in vars() else None
obj2.mass = 10
deactivate(obj2) if 'obj2' in vars() else None
obj7.mass = 10
deactivate(obj7) if 'obj7' in vars() else None
obj6.mass = 10
deactivate(obj6) if 'obj6' in vars() else None
obj11.mass = 10
deactivate(obj11) if 'obj11' in vars() else None
obj10.mass = 10
deactivate(obj10) if 'obj10' in vars() else None
obj15.mass = 10
deactivate(obj15) if 'obj15' in vars() else None
obj14.mass = 10
deactivate(obj14) if 'obj14' in vars() else None
obj20.mass = 10
pin(obj20.body.position, obj20, obj24.body.position, obj24)
connected_shapes.append([obj20, obj24])
motor(obj20, 5)
obj19.mass = 10
pin(obj19.body.position, obj19, obj20.body.position, obj20)
connected_shapes.append([obj19, obj20])
pin(obj19.body.position, obj19, obj24.body.position, obj24)
connected_shapes.append([obj19, obj24])
motor(obj19, 5)
obj18.mass = 10
pin(obj18.body.position, obj18, obj19.body.position, obj19)
connected_shapes.append([obj18, obj19])
pin(obj18.body.position, obj18, obj24.body.position, obj24)
connected_shapes.append([obj18, obj24])
motor(obj18, 5)
obj24.mass = 10
obj24.hit([0, 0], obj24.position)
motor(obj24, 0)
obj13.mass = 10
motor(obj13, 0)
obj13.gravity = 0, -100


def on_click_13(keys):
    global obj13
    f = obj13
    if not f or not f.body:
        return False
        _hy_anon_var_26 = None
    else:
        _hy_anon_var_26 = None
    p = f.body.position
    if mouse_clicked() and obj13.inside(mouse_point()) and obj13.active:
        try:
            deactivate(f)
            _hy_anon_var_27 = make_obj14(p[0] + -1 * (w / 2), p[1] + -1 * (
                h / 2), False)
        except e:
            _hy_anon_var_27 = print(e)
        try:
            deactivate(f)
            _hy_anon_var_28 = make_obj15(p[0] + -1 * (w / 2), p[1] + -1 * (
                h / 2), False)
        except e:
            _hy_anon_var_28 = print(e)
        return True
        _hy_anon_var_29 = None
    else:
        _hy_anon_var_29 = None
    return _hy_anon_var_29


add_observer(on_click_13)
obj9.mass = 10
motor(obj9, 0)
obj9.gravity = 0, -100


def on_click_9(keys):
    global obj9
    f = obj9
    if not f or not f.body:
        return False
        _hy_anon_var_31 = None
    else:
        _hy_anon_var_31 = None
    p = f.body.position
    if mouse_clicked() and obj9.inside(mouse_point()) and obj9.active:
        try:
            deactivate(f)
            _hy_anon_var_32 = make_obj10(p[0] + -1 * (w / 2), p[1] + -1 * (
                h / 2), False)
        except e:
            _hy_anon_var_32 = print(e)
        try:
            deactivate(f)
            _hy_anon_var_33 = make_obj11(p[0] + -1 * (w / 2), p[1] + -1 * (
                h / 2), False)
        except e:
            _hy_anon_var_33 = print(e)
        return True
        _hy_anon_var_34 = None
    else:
        _hy_anon_var_34 = None
    return _hy_anon_var_34


add_observer(on_click_9)
obj5.mass = 10
motor(obj5, 0)
obj5.gravity = 0, -100


def on_click_5(keys):
    global obj5
    f = obj5
    if not f or not f.body:
        return False
        _hy_anon_var_36 = None
    else:
        _hy_anon_var_36 = None
    p = f.body.position
    if mouse_clicked() and obj5.inside(mouse_point()) and obj5.active:
        try:
            deactivate(f)
            _hy_anon_var_37 = make_obj6(p[0] + -1 * (w / 2), p[1] + -1 * (h /
                2), False)
        except e:
            _hy_anon_var_37 = print(e)
        try:
            deactivate(f)
            _hy_anon_var_38 = make_obj7(p[0] + -1 * (w / 2), p[1] + -1 * (h /
                2), False)
        except e:
            _hy_anon_var_38 = print(e)
        return True
        _hy_anon_var_39 = None
    else:
        _hy_anon_var_39 = None
    return _hy_anon_var_39


add_observer(on_click_5)
obj1.mass = 10
motor(obj1, 0)
obj1.gravity = 0, -100


def on_click_1(keys):
    global obj1
    f = obj1
    if not f or not f.body:
        return False
        _hy_anon_var_41 = None
    else:
        _hy_anon_var_41 = None
    p = f.body.position
    if mouse_clicked() and obj1.inside(mouse_point()) and obj1.active:
        try:
            deactivate(f)
            _hy_anon_var_42 = make_obj2(p[0] + -1 * (w / 2), p[1] + -1 * (h /
                2), False)
        except e:
            _hy_anon_var_42 = print(e)
        try:
            deactivate(f)
            _hy_anon_var_43 = make_obj3(p[0] + -1 * (w / 2), p[1] + -1 * (h /
                2), False)
        except e:
            _hy_anon_var_43 = print(e)
        return True
        _hy_anon_var_44 = None
    else:
        _hy_anon_var_44 = None
    return _hy_anon_var_44


add_observer(on_click_1)


def image_for(s):
    global image_bindings
    for b in image_bindings:
        if b[0] == s:
            return b[1]
            _hy_anon_var_46 = None
        else:
            _hy_anon_var_46 = None
    return False


def draw_images(cosmetic):

    def f(keys):
        global user_shapes
        for s in user_shapes:
            if not image_for(s):
                continue
                _hy_anon_var_48 = None
            else:
                _hy_anon_var_48 = None
            if not cosmetic == s._cosmetic:
                continue
                _hy_anon_var_49 = None
            else:
                _hy_anon_var_49 = None
            if not s.active:
                continue
                _hy_anon_var_50 = None
            else:
                _hy_anon_var_50 = None
            if s.body:
                p = Vec2d(s.body.position.x, s.body.position.y)
                _hy_anon_var_51 = None
            else:
                p = Vec2d(s._x, s._y)
                _hy_anon_var_51 = None
            angle = 0
            if s.body:
                angle = s.body.angle
                _hy_anon_var_52 = None
            else:
                _hy_anon_var_52 = None
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
            if not p.active or not j.active:
                continue
                _hy_anon_var_55 = None
            else:
                _hy_anon_var_55 = None
            other = j.a
            end = other.position
            screen = pygame.display.get_surface()
            pygame.draw.line(screen, Color('black'), start, end)


def draw_connection_lines(keys):
    global pivots
    for c in connected_shapes:
        start = c[0].body.position
        end = c[1].body.position
        if not c[0].active or not c[1].active:
            continue
            _hy_anon_var_57 = None
        else:
            _hy_anon_var_57 = None
        screen = pygame.display.get_surface()
        pygame.draw.line(screen, Color('black'), start, end)


def test_ball(keys):
    if constants.K_b in keys:
        obj44 = ball([int(300) + int(off_x), +int(300), int(off_y)], 10)
        obj44.color = Color('white')
        obj44.group = 44
        obj44_image = pygame.image.load(
            '/Users/thoughtstem/Dev/Python/py-fizzery/obj44.png')
        image_bindings.append([obj44, obj44_image])
        user_shapes.append(obj44)
        _hy_anon_var_59 = obj44
    else:
        _hy_anon_var_59 = None
    return _hy_anon_var_59


add_observer(draw_images(True))
add_observer(draw_pivot_lines)
add_observer(draw_connection_lines)
add_observer(draw_images(False))
run()

