from hy.core.language import fraction
import sys
import math
import pymunk
from pyphysicssandbox import *
import pygame
from pyphysicssandbox import Vec2d
w = 505
h = 385
user_shapes = []
image_bindings = []
pivots = []
connected_shapes = []
window('Most Awesome Thing Ever', 505, 385)


def make_obj140(off_x, off_y, debug):
    print('Making ' + 'make_obj140' + '\n' +
        '#(struct:physical 140 505/2 380 () #<box-collider> #(struct:object:image% ...) #f)'
        ) if debug else None
    obj140 = static_box([int(fraction(505, 2) - fraction(505, 2)) + int(
        off_x), int(380 - 5) + int(off_y)], 505, 10)
    obj140.color = Color('white')
    obj140.group = 140
    obj140_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj140.png')
    image_bindings.append([obj140, obj140_image])
    user_shapes.append(obj140)
    return obj140


obj140 = make_obj140(0, 0, False)


def make_obj142(off_x, off_y, debug):
    print('Making ' + 'make_obj142' + '\n' +
        '#(struct:physical 142 500 365/2 () #<box-collider> #(struct:object:image% ...) #f)'
        ) if debug else None
    obj142 = static_box([int(500 - 5) + int(off_x), int(fraction(385, 2) -
        fraction(365, 2)) + int(off_y)], 10, 365)
    obj142.color = Color('white')
    obj142.group = 142
    obj142_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj142.png')
    image_bindings.append([obj142, obj142_image])
    user_shapes.append(obj142)
    return obj142


obj142 = make_obj142(0, 0, False)


def make_obj138(off_x, off_y, debug):
    print('Making ' + 'make_obj138' + '\n' +
        '#(struct:cosmetic 138 485/2 365/2 () #(struct:object:image% ...))'
        ) if debug else None
    obj138 = cosmetic_ball([int(fraction(505, 2)) + int(off_x), +int(
        fraction(385, 2)), int(off_y)], fraction(485, 2))
    obj138.color = Color('white')
    obj138.group = 138
    obj138_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj138.png')
    image_bindings.append([obj138, obj138_image])
    user_shapes.append(obj138)
    return obj138


obj138 = make_obj138(0, 0, False)


def make_obj134(off_x, off_y, debug):
    print('Making ' + 'make_obj134' + '\n' +
        '#(struct:cosmetic 134 312 55 () #(struct:object:image% ...))'
        ) if debug else None
    obj134 = cosmetic_ball([int(fraction(717, 2)) + int(off_x), +int(320),
        int(off_y)], 100)
    obj134.color = Color('white')
    obj134.group = 134
    obj134_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj134.png')
    image_bindings.append([obj134, obj134_image])
    user_shapes.append(obj134)
    return obj134


obj134 = make_obj134(0, 0, False)


def make_obj129(off_x, off_y, debug):
    print('Making ' + 'make_obj129' + '\n' +
        '#(struct:physical 129 164 55 (#<procedure:...ery/compiler.rkt:533:21>) #<box-collider> #(struct:object:image% ...) #f)'
        ) if debug else None
    obj129 = static_box([int(fraction(421, 2) - 48) + int(off_x), int(320 -
        53) + int(off_y)], 96, 106)
    obj129.color = Color('white')
    obj129.group = 129
    obj129_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj129.png')
    image_bindings.append([obj129, obj129_image])
    user_shapes.append(obj129)
    return obj129


obj129 = make_obj129(0, 0, False)


def make_obj127(off_x, off_y, debug):
    print('Making ' + 'make_obj127' + '\n' +
        '#(struct:cosmetic 127 106 55 () #(struct:object:image% ...))'
        ) if debug else None
    obj127 = cosmetic_ball([int(fraction(305, 2)) + int(off_x), +int(320),
        int(off_y)], 10)
    obj127.color = Color('white')
    obj127.group = 127
    obj127_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj127.png')
    image_bindings.append([obj127, obj127_image])
    user_shapes.append(obj127)
    return obj127


obj127 = make_obj127(0, 0, False)


def make_obj122(off_x, off_y, debug):
    print('Making ' + 'make_obj122' + '\n' +
        '#(struct:physical 122 48 55 (#<procedure:...ery/compiler.rkt:533:21>) #<box-collider> #(struct:object:image% ...) #f)'
        ) if debug else None
    obj122 = static_box([int(fraction(189, 2) - 48) + int(off_x), int(320 -
        55) + int(off_y)], 96, 110)
    obj122.color = Color('white')
    obj122.group = 122
    obj122_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj122.png')
    image_bindings.append([obj122, obj122_image])
    user_shapes.append(obj122)
    return obj122


obj122 = make_obj122(0, 0, False)


def make_obj120(off_x, off_y, debug):
    print('Making ' + 'make_obj120' + '\n' +
        '#(struct:cosmetic 120 206 230 () #(struct:object:image% ...))'
        ) if debug else None
    obj120 = cosmetic_ball([int(fraction(505, 2)) + int(off_x), +int(240),
        int(off_y)], 25)
    obj120.color = Color('white')
    obj120.group = 120
    obj120_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj120.png')
    image_bindings.append([obj120, obj120_image])
    user_shapes.append(obj120)
    return obj120


obj120 = make_obj120(0, 0, False)


def make_obj1(off_x, off_y, debug):
    print('Making ' + 'make_obj1' + '\n' +
        '#(struct:physical 1 110 365/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:395:21> #<procedure:...ery/compiler.rkt:395:21> #<procedure:...ery/compiler.rkt:395:21> #<procedure:...ery/compiler.rkt:395:21> #<procedure:...ery/compiler.rkt:395:21>) #<circle-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj1 = ball([int(fraction(505, 2)) + int(off_x), +int(fraction(385, 2)),
        int(off_y)], fraction(45, 2))
    obj1.color = Color('white')
    obj1.group = 1
    obj1_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj1.png')
    image_bindings.append([obj1, obj1_image])
    user_shapes.append(obj1)
    return obj1


obj1 = make_obj1(0, 0, False)


def make_obj118(off_x, off_y, debug):
    print('Making ' + 'make_obj118' + '\n' +
        '#(struct:cosmetic 118 110 110 () #(struct:object:image% ...))'
        ) if debug else None
    obj118 = cosmetic_ball([int(fraction(505, 2)) + int(off_x), +int(120),
        int(off_y)], 50)
    obj118.color = Color('white')
    obj118.group = 118
    obj118_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj118.png')
    image_bindings.append([obj118, obj118_image])
    user_shapes.append(obj118)
    return obj118


obj118 = make_obj118(0, 0, False)


def make_obj94(off_x, off_y, debug):
    print('Making ' + 'make_obj94' + '\n' +
        '#(struct:physical 94 198 30 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:387:21> #<procedure:...ery/compiler.rkt:423:21> #<procedure:...ery/compiler.rkt:533:21> #<procedure:...ery/compiler.rkt:493:21>) #<box-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj94 = box([int(fraction(681, 2) - 22) + int(off_x), int(40 - 30) +
        int(off_y)], 44, 60)
    obj94.color = Color('white')
    obj94.group = 94
    obj94_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj94.png')
    image_bindings.append([obj94, obj94_image])
    user_shapes.append(obj94)
    return obj94


obj94 = make_obj94(0, 0, False)


def make_obj71(off_x, off_y, debug):
    print('Making ' + 'make_obj71' + '\n' +
        '#(struct:physical 71 154 30 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:387:21> #<procedure:...ery/compiler.rkt:423:21> #<procedure:...ery/compiler.rkt:533:21> #<procedure:...ery/compiler.rkt:493:21>) #<box-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj71 = box([int(fraction(593, 2) - 22) + int(off_x), int(40 - 30) +
        int(off_y)], 44, 60)
    obj71.color = Color('white')
    obj71.group = 71
    obj71_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj71.png')
    image_bindings.append([obj71, obj71_image])
    user_shapes.append(obj71)
    return obj71


obj71 = make_obj71(0, 0, False)


def make_obj48(off_x, off_y, debug):
    print('Making ' + 'make_obj48' + '\n' +
        '#(struct:physical 48 110 30 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:387:21> #<procedure:...ery/compiler.rkt:423:21> #<procedure:...ery/compiler.rkt:533:21> #<procedure:...ery/compiler.rkt:493:21>) #<box-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj48 = box([int(fraction(505, 2) - 22) + int(off_x), int(40 - 30) +
        int(off_y)], 44, 60)
    obj48.color = Color('white')
    obj48.group = 48
    obj48_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj48.png')
    image_bindings.append([obj48, obj48_image])
    user_shapes.append(obj48)
    return obj48


obj48 = make_obj48(0, 0, False)


def make_obj25(off_x, off_y, debug):
    print('Making ' + 'make_obj25' + '\n' +
        '#(struct:physical 25 66 30 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:387:21> #<procedure:...ery/compiler.rkt:423:21> #<procedure:...ery/compiler.rkt:533:21> #<procedure:...ery/compiler.rkt:493:21>) #<box-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj25 = box([int(fraction(417, 2) - 22) + int(off_x), int(40 - 30) +
        int(off_y)], 44, 60)
    obj25.color = Color('white')
    obj25.group = 25
    obj25_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj25.png')
    image_bindings.append([obj25, obj25_image])
    user_shapes.append(obj25)
    return obj25


obj25 = make_obj25(0, 0, False)


def make_obj2(off_x, off_y, debug):
    print('Making ' + 'make_obj2' + '\n' +
        '#(struct:physical 2 22 30 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:387:21> #<procedure:...ery/compiler.rkt:423:21> #<procedure:...ery/compiler.rkt:533:21> #<procedure:...ery/compiler.rkt:493:21>) #<box-collider> #(struct:object:image% ...) #t)'
        ) if debug else None
    obj2 = box([int(fraction(329, 2) - 22) + int(off_x), int(40 - 30) + int
        (off_y)], 44, 60)
    obj2.color = Color('white')
    obj2.group = 2
    obj2_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj2.png')
    image_bindings.append([obj2, obj2_image])
    user_shapes.append(obj2)
    return obj2


obj2 = make_obj2(0, 0, False)


def make_obj142(off_x, off_y, debug):
    print('Making ' + 'make_obj142' + '\n' +
        '#(struct:physical 142 5 365/2 () #<box-collider> #(struct:object:image% ...) #f)'
        ) if debug else None
    obj142 = static_box([int(5 - 5) + int(off_x), int(fraction(385, 2) -
        fraction(365, 2)) + int(off_y)], 10, 365)
    obj142.color = Color('white')
    obj142.group = 142
    obj142_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj142.png')
    image_bindings.append([obj142, obj142_image])
    user_shapes.append(obj142)
    return obj142


obj142 = make_obj142(0, 0, False)


def make_obj140(off_x, off_y, debug):
    print('Making ' + 'make_obj140' + '\n' +
        '#(struct:physical 140 505/2 5 () #<box-collider> #(struct:object:image% ...) #f)'
        ) if debug else None
    obj140 = static_box([int(fraction(505, 2) - fraction(505, 2)) + int(
        off_x), int(5 - 5) + int(off_y)], 505, 10)
    obj140.color = Color('white')
    obj140.group = 140
    obj140_image = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizzery/obj140.png')
    image_bindings.append([obj140, obj140_image])
    user_shapes.append(obj140)
    return obj140


obj140 = make_obj140(0, 0, False)


def on_click_129(keys):
    global obj129
    f = obj129
    if not f or not f.body:
        return False
        _hy_anon_var_18 = None
    else:
        _hy_anon_var_18 = None
    p = f.body.position
    if mouse_clicked() and obj129.inside(mouse_point()) and obj129.active:

        def make_obj130(off_x, off_y, debug):
            print('Making ' + 'make_obj130' + '\n' +
                '#(struct:cosmetic 130 48 45/2 () #(struct:object:image% ...))'
                ) if debug else None
            obj130 = cosmetic_ball([int(p.x + 48 + fraction(-141, 2)) + int
                (off_x), +int(p.y + fraction(45, 2) + fraction(-145, 2)),
                int(off_y)], 48)
            obj130.color = Color('white')
            obj130.group = 130
            obj130_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj130.png')
            image_bindings.append([obj130, obj130_image])
            user_shapes.append(obj130)
            return obj130
        obj130 = make_obj130(0, 0, False)

        def make_obj128(off_x, off_y, debug):
            print('Making ' + 'make_obj128' + '\n' +
                '#(struct:physical 128 237/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<circle-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj128 = ball([int(p.x + fraction(237, 2) + fraction(-141, 2)) +
                int(off_x), +int(p.y + fraction(45, 2) + fraction(-145, 2)),
                int(off_y)], fraction(45, 2))
            obj128.color = Color('white')
            obj128.group = 128
            obj128_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj128.png')
            image_bindings.append([obj128, obj128_image])
            user_shapes.append(obj128)
            return obj128
        obj128 = make_obj128(0, 0, False)
        obj128.mass = 10000
        obj128.hit([1000000, -1000000], obj128.position)

        def make_obj132(off_x, off_y, debug):
            print('Making ' + 'make_obj132' + '\n' +
                '#(struct:cosmetic 132 141/2 95 () #(struct:object:image% ...))'
                ) if debug else None
            obj132 = cosmetic_ball([int(p.x + fraction(141, 2) + fraction(
                -141, 2)) + int(off_x), +int(p.y + 95 + fraction(-145, 2)),
                int(off_y)], 50)
            obj132.color = Color('white')
            obj132.group = 132
            obj132_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj132.png')
            image_bindings.append([obj132, obj132_image])
            user_shapes.append(obj132)
            return obj132
        obj132 = make_obj132(0, 0, False)
        return True
        _hy_anon_var_22 = None
    else:
        _hy_anon_var_22 = None
    return _hy_anon_var_22


add_observer(on_click_129)


def on_click_122(keys):
    global obj122
    f = obj122
    if not f or not f.body:
        return False
        _hy_anon_var_24 = None
    else:
        _hy_anon_var_24 = None
    p = f.body.position
    if mouse_clicked() and obj122.inside(mouse_point()) and obj122.active:

        def make_obj123(off_x, off_y, debug):
            print('Making ' + 'make_obj123' + '\n' +
                '#(struct:cosmetic 123 48 30 () #(struct:object:image% ...))'
                ) if debug else None
            obj123 = cosmetic_ball([int(p.x + 48 + -70) + int(off_x), +int(
                p.y + 30 + -80), int(off_y)], 48)
            obj123.color = Color('white')
            obj123.group = 123
            obj123_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj123.png')
            image_bindings.append([obj123, obj123_image])
            user_shapes.append(obj123)
            return obj123
        obj123 = make_obj123(0, 0, False)

        def make_obj121(off_x, off_y, debug):
            print('Making ' + 'make_obj121' + '\n' +
                '#(struct:physical 121 118 30 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:387:21> #<procedure:...ery/compiler.rkt:423:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj121 = box([int(p.x + 118 + -70 - 22) + int(off_x), int(p.y +
                30 + -80 - 30) + int(off_y)], 44, 60)
            obj121.color = Color('white')
            obj121.group = 121
            obj121_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj121.png')
            image_bindings.append([obj121, obj121_image])
            user_shapes.append(obj121)
            return obj121
        obj121 = make_obj121(0, 0, False)
        obj121.mass = 10
        motor
        obj121
        0
        obj121.gravity = 0, -100
        obj121.hit([1000000, -1000000], obj121.position)

        def make_obj125(off_x, off_y, debug):
            print('Making ' + 'make_obj125' + '\n' +
                '#(struct:cosmetic 125 70 110 () #(struct:object:image% ...))'
                ) if debug else None
            obj125 = cosmetic_ball([int(p.x + 70 + -70) + int(off_x), +int(
                p.y + 110 + -80), int(off_y)], 50)
            obj125.color = Color('white')
            obj125.group = 125
            obj125_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj125.png')
            image_bindings.append([obj125, obj125_image])
            user_shapes.append(obj125)
            return obj125
        obj125 = make_obj125(0, 0, False)
        return True
        _hy_anon_var_28 = None
    else:
        _hy_anon_var_28 = None
    return _hy_anon_var_28


add_observer(on_click_122)
obj1.mass = 10000
p = spring(obj1.body.position, obj1, obj2.body.position, obj2, 100, 20000, 1000
    )
connected_shapes.append([obj1, obj2, p])
p = spring(obj1.body.position, obj1, obj25.body.position, obj25, 100, 20000,
    1000)
connected_shapes.append([obj1, obj25, p])
p = spring(obj1.body.position, obj1, obj48.body.position, obj48, 100, 20000,
    1000)
connected_shapes.append([obj1, obj48, p])
p = spring(obj1.body.position, obj1, obj71.body.position, obj71, 100, 20000,
    1000)
connected_shapes.append([obj1, obj71, p])
p = spring(obj1.body.position, obj1, obj94.body.position, obj94, 100, 20000,
    1000)
connected_shapes.append([obj1, obj94, p])
obj94.mass = 10
motor(obj94, 0)
obj94.gravity = 0, -100


def on_click_94(keys):
    global obj94
    f = obj94
    if not f or not f.body:
        return False
        _hy_anon_var_30 = None
    else:
        _hy_anon_var_30 = None
    p = f.body.position
    if mouse_clicked() and obj94.inside(mouse_point()) and obj94.active:

        def make_obj96(off_x, off_y, debug):
            print('Making ' + 'make_obj96' + '\n' +
                '#(struct:physical 96 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj96 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj96.color = Color('white')
            obj96.group = 96
            obj96_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj96.png')
            image_bindings.append([obj96, obj96_image])
            user_shapes.append(obj96)
            return obj96
        obj96 = make_obj96(0, 0, False)
        obj96.mass = 10
        obj96.hit([36492.24305767253, -10423.823089374971], obj96.position)

        def make_obj97(off_x, off_y, debug):
            print('Making ' + 'make_obj97' + '\n' +
                '#(struct:physical 97 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj97 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj97.color = Color('white')
            obj97.group = 97
            obj97_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj97.png')
            image_bindings.append([obj97, obj97_image])
            user_shapes.append(obj97)
            return obj97
        obj97 = make_obj97(0, 0, False)
        obj97.mass = 10
        obj97.hit([27731.80756909214, -10461.787594494366], obj97.position)

        def make_obj98(off_x, off_y, debug):
            print('Making ' + 'make_obj98' + '\n' +
                '#(struct:physical 98 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj98 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj98.color = Color('white')
            obj98.group = 98
            obj98_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj98.png')
            image_bindings.append([obj98, obj98_image])
            user_shapes.append(obj98)
            return obj98
        obj98 = make_obj98(0, 0, False)
        obj98.mass = 10
        obj98.hit([-21311.793903087528, 2354.0389234293543], obj98.position)

        def make_obj99(off_x, off_y, debug):
            print('Making ' + 'make_obj99' + '\n' +
                '#(struct:physical 99 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj99 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj99.color = Color('white')
            obj99.group = 99
            obj99_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj99.png')
            image_bindings.append([obj99, obj99_image])
            user_shapes.append(obj99)
            return obj99
        obj99 = make_obj99(0, 0, False)
        obj99.mass = 10
        obj99.hit([8849.007575910917, 48827.088334605665], obj99.position)

        def make_obj101(off_x, off_y, debug):
            print('Making ' + 'make_obj101' + '\n' +
                '#(struct:physical 101 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj101 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj101.color = Color('white')
            obj101.group = 101
            obj101_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj101.png')
            image_bindings.append([obj101, obj101_image])
            user_shapes.append(obj101)
            return obj101
        obj101 = make_obj101(0, 0, False)
        obj101.mass = 10
        obj101.hit([35197.26817520145, -49307.96261319337], obj101.position)

        def make_obj102(off_x, off_y, debug):
            print('Making ' + 'make_obj102' + '\n' +
                '#(struct:physical 102 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj102 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj102.color = Color('white')
            obj102.group = 102
            obj102_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj102.png')
            image_bindings.append([obj102, obj102_image])
            user_shapes.append(obj102)
            return obj102
        obj102 = make_obj102(0, 0, False)
        obj102.mass = 10
        obj102.hit([-6916.924621611906, -24196.83307710599], obj102.position)

        def make_obj103(off_x, off_y, debug):
            print('Making ' + 'make_obj103' + '\n' +
                '#(struct:physical 103 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj103 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj103.color = Color('white')
            obj103.group = 103
            obj103_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj103.png')
            image_bindings.append([obj103, obj103_image])
            user_shapes.append(obj103)
            return obj103
        obj103 = make_obj103(0, 0, False)
        obj103.mass = 10
        obj103.hit([-31744.42248485048, 33544.33287801716], obj103.position)

        def make_obj104(off_x, off_y, debug):
            print('Making ' + 'make_obj104' + '\n' +
                '#(struct:physical 104 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj104 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(105, 2) + -30 - fraction
                (15, 2)) + int(off_y)], 11, 15)
            obj104.color = Color('white')
            obj104.group = 104
            obj104_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj104.png')
            image_bindings.append([obj104, obj104_image])
            user_shapes.append(obj104)
            return obj104
        obj104 = make_obj104(0, 0, False)
        obj104.mass = 10
        obj104.hit([-17393.734356830064, 28265.587957399504], obj104.position)

        def make_obj106(off_x, off_y, debug):
            print('Making ' + 'make_obj106' + '\n' +
                '#(struct:physical 106 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj106 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj106.color = Color('white')
            obj106.group = 106
            obj106_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj106.png')
            image_bindings.append([obj106, obj106_image])
            user_shapes.append(obj106)
            return obj106
        obj106 = make_obj106(0, 0, False)
        obj106.mass = 10
        obj106.hit([-16026.131327598196, -38945.84882090254], obj106.position)

        def make_obj107(off_x, off_y, debug):
            print('Making ' + 'make_obj107' + '\n' +
                '#(struct:physical 107 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj107 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj107.color = Color('white')
            obj107.group = 107
            obj107_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj107.png')
            image_bindings.append([obj107, obj107_image])
            user_shapes.append(obj107)
            return obj107
        obj107 = make_obj107(0, 0, False)
        obj107.mass = 10
        obj107.hit([11231.602992902845, -12431.705786333136], obj107.position)

        def make_obj108(off_x, off_y, debug):
            print('Making ' + 'make_obj108' + '\n' +
                '#(struct:physical 108 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj108 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj108.color = Color('white')
            obj108.group = 108
            obj108_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj108.png')
            image_bindings.append([obj108, obj108_image])
            user_shapes.append(obj108)
            return obj108
        obj108 = make_obj108(0, 0, False)
        obj108.mass = 10
        obj108.hit([-13885.768430363343, 11142.545686487458], obj108.position)

        def make_obj109(off_x, off_y, debug):
            print('Making ' + 'make_obj109' + '\n' +
                '#(struct:physical 109 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj109 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(105, 2) + -30 - fraction
                (15, 2)) + int(off_y)], 11, 15)
            obj109.color = Color('white')
            obj109.group = 109
            obj109_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj109.png')
            image_bindings.append([obj109, obj109_image])
            user_shapes.append(obj109)
            return obj109
        obj109 = make_obj109(0, 0, False)
        obj109.mass = 10
        obj109.hit([13959.594490843752, -1529.6449228576676], obj109.position)

        def make_obj111(off_x, off_y, debug):
            print('Making ' + 'make_obj111' + '\n' +
                '#(struct:physical 111 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj111 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj111.color = Color('white')
            obj111.group = 111
            obj111_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj111.png')
            image_bindings.append([obj111, obj111_image])
            user_shapes.append(obj111)
            return obj111
        obj111 = make_obj111(0, 0, False)
        obj111.mass = 10
        obj111.hit([20895.42735979169, 32834.532933678216], obj111.position)

        def make_obj112(off_x, off_y, debug):
            print('Making ' + 'make_obj112' + '\n' +
                '#(struct:physical 112 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj112 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj112.color = Color('white')
            obj112.group = 112
            obj112_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj112.png')
            image_bindings.append([obj112, obj112_image])
            user_shapes.append(obj112)
            return obj112
        obj112 = make_obj112(0, 0, False)
        obj112.mass = 10
        obj112.hit([5650.352145375982, 16966.077156584724], obj112.position)

        def make_obj113(off_x, off_y, debug):
            print('Making ' + 'make_obj113' + '\n' +
                '#(struct:physical 113 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj113 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj113.color = Color('white')
            obj113.group = 113
            obj113_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj113.png')
            image_bindings.append([obj113, obj113_image])
            user_shapes.append(obj113)
            return obj113
        obj113 = make_obj113(0, 0, False)
        obj113.mass = 10
        obj113.hit([10450.180986346139, 46635.88162517719], obj113.position)

        def make_obj114(off_x, off_y, debug):
            print('Making ' + 'make_obj114' + '\n' +
                '#(struct:physical 114 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj114 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(105, 2) + -30 - fraction
                (15, 2)) + int(off_y)], 11, 15)
            obj114.color = Color('white')
            obj114.group = 114
            obj114_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj114.png')
            image_bindings.append([obj114, obj114_image])
            user_shapes.append(obj114)
            return obj114
        obj114 = make_obj114(0, 0, False)
        obj114.mass = 10
        obj114.hit([-29327.500914251475, -18978.244729217815], obj114.position)
        deactivate(f)
        return True
        _hy_anon_var_47 = None
    else:
        _hy_anon_var_47 = None
    return _hy_anon_var_47


add_observer(on_click_94)


def on_collide_94(arbiter, space, data):
    f = obj94
    p = f.body.position
    friction = arbiter.friction
    restitution = arbiter.restitution
    total_impulse = arbiter.total_impulse
    energy_loss = arbiter.total_ke
    if friction > 0 and energy_loss > 50000000:

        def make_obj96(off_x, off_y, debug):
            print('Making ' + 'make_obj96' + '\n' +
                '#(struct:physical 96 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj96 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj96.color = Color('white')
            obj96.group = 96
            obj96_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj96.png')
            image_bindings.append([obj96, obj96_image])
            user_shapes.append(obj96)
            return obj96
        obj96 = make_obj96(0, 0, False)
        obj96.mass = 10
        obj96.hit([36492.24305767253, -10423.823089374971], obj96.position)

        def make_obj97(off_x, off_y, debug):
            print('Making ' + 'make_obj97' + '\n' +
                '#(struct:physical 97 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj97 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj97.color = Color('white')
            obj97.group = 97
            obj97_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj97.png')
            image_bindings.append([obj97, obj97_image])
            user_shapes.append(obj97)
            return obj97
        obj97 = make_obj97(0, 0, False)
        obj97.mass = 10
        obj97.hit([27731.80756909214, -10461.787594494366], obj97.position)

        def make_obj98(off_x, off_y, debug):
            print('Making ' + 'make_obj98' + '\n' +
                '#(struct:physical 98 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj98 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj98.color = Color('white')
            obj98.group = 98
            obj98_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj98.png')
            image_bindings.append([obj98, obj98_image])
            user_shapes.append(obj98)
            return obj98
        obj98 = make_obj98(0, 0, False)
        obj98.mass = 10
        obj98.hit([-21311.793903087528, 2354.0389234293543], obj98.position)

        def make_obj99(off_x, off_y, debug):
            print('Making ' + 'make_obj99' + '\n' +
                '#(struct:physical 99 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj99 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj99.color = Color('white')
            obj99.group = 99
            obj99_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj99.png')
            image_bindings.append([obj99, obj99_image])
            user_shapes.append(obj99)
            return obj99
        obj99 = make_obj99(0, 0, False)
        obj99.mass = 10
        obj99.hit([8849.007575910917, 48827.088334605665], obj99.position)

        def make_obj101(off_x, off_y, debug):
            print('Making ' + 'make_obj101' + '\n' +
                '#(struct:physical 101 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj101 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj101.color = Color('white')
            obj101.group = 101
            obj101_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj101.png')
            image_bindings.append([obj101, obj101_image])
            user_shapes.append(obj101)
            return obj101
        obj101 = make_obj101(0, 0, False)
        obj101.mass = 10
        obj101.hit([35197.26817520145, -49307.96261319337], obj101.position)

        def make_obj102(off_x, off_y, debug):
            print('Making ' + 'make_obj102' + '\n' +
                '#(struct:physical 102 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj102 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj102.color = Color('white')
            obj102.group = 102
            obj102_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj102.png')
            image_bindings.append([obj102, obj102_image])
            user_shapes.append(obj102)
            return obj102
        obj102 = make_obj102(0, 0, False)
        obj102.mass = 10
        obj102.hit([-6916.924621611906, -24196.83307710599], obj102.position)

        def make_obj103(off_x, off_y, debug):
            print('Making ' + 'make_obj103' + '\n' +
                '#(struct:physical 103 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj103 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj103.color = Color('white')
            obj103.group = 103
            obj103_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj103.png')
            image_bindings.append([obj103, obj103_image])
            user_shapes.append(obj103)
            return obj103
        obj103 = make_obj103(0, 0, False)
        obj103.mass = 10
        obj103.hit([-31744.42248485048, 33544.33287801716], obj103.position)

        def make_obj104(off_x, off_y, debug):
            print('Making ' + 'make_obj104' + '\n' +
                '#(struct:physical 104 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj104 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(105, 2) + -30 - fraction
                (15, 2)) + int(off_y)], 11, 15)
            obj104.color = Color('white')
            obj104.group = 104
            obj104_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj104.png')
            image_bindings.append([obj104, obj104_image])
            user_shapes.append(obj104)
            return obj104
        obj104 = make_obj104(0, 0, False)
        obj104.mass = 10
        obj104.hit([-17393.734356830064, 28265.587957399504], obj104.position)

        def make_obj106(off_x, off_y, debug):
            print('Making ' + 'make_obj106' + '\n' +
                '#(struct:physical 106 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj106 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj106.color = Color('white')
            obj106.group = 106
            obj106_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj106.png')
            image_bindings.append([obj106, obj106_image])
            user_shapes.append(obj106)
            return obj106
        obj106 = make_obj106(0, 0, False)
        obj106.mass = 10
        obj106.hit([-16026.131327598196, -38945.84882090254], obj106.position)

        def make_obj107(off_x, off_y, debug):
            print('Making ' + 'make_obj107' + '\n' +
                '#(struct:physical 107 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj107 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj107.color = Color('white')
            obj107.group = 107
            obj107_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj107.png')
            image_bindings.append([obj107, obj107_image])
            user_shapes.append(obj107)
            return obj107
        obj107 = make_obj107(0, 0, False)
        obj107.mass = 10
        obj107.hit([11231.602992902845, -12431.705786333136], obj107.position)

        def make_obj108(off_x, off_y, debug):
            print('Making ' + 'make_obj108' + '\n' +
                '#(struct:physical 108 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj108 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj108.color = Color('white')
            obj108.group = 108
            obj108_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj108.png')
            image_bindings.append([obj108, obj108_image])
            user_shapes.append(obj108)
            return obj108
        obj108 = make_obj108(0, 0, False)
        obj108.mass = 10
        obj108.hit([-13885.768430363343, 11142.545686487458], obj108.position)

        def make_obj109(off_x, off_y, debug):
            print('Making ' + 'make_obj109' + '\n' +
                '#(struct:physical 109 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj109 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(105, 2) + -30 - fraction
                (15, 2)) + int(off_y)], 11, 15)
            obj109.color = Color('white')
            obj109.group = 109
            obj109_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj109.png')
            image_bindings.append([obj109, obj109_image])
            user_shapes.append(obj109)
            return obj109
        obj109 = make_obj109(0, 0, False)
        obj109.mass = 10
        obj109.hit([13959.594490843752, -1529.6449228576676], obj109.position)

        def make_obj111(off_x, off_y, debug):
            print('Making ' + 'make_obj111' + '\n' +
                '#(struct:physical 111 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj111 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj111.color = Color('white')
            obj111.group = 111
            obj111_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj111.png')
            image_bindings.append([obj111, obj111_image])
            user_shapes.append(obj111)
            return obj111
        obj111 = make_obj111(0, 0, False)
        obj111.mass = 10
        obj111.hit([20895.42735979169, 32834.532933678216], obj111.position)

        def make_obj112(off_x, off_y, debug):
            print('Making ' + 'make_obj112' + '\n' +
                '#(struct:physical 112 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj112 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj112.color = Color('white')
            obj112.group = 112
            obj112_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj112.png')
            image_bindings.append([obj112, obj112_image])
            user_shapes.append(obj112)
            return obj112
        obj112 = make_obj112(0, 0, False)
        obj112.mass = 10
        obj112.hit([5650.352145375982, 16966.077156584724], obj112.position)

        def make_obj113(off_x, off_y, debug):
            print('Making ' + 'make_obj113' + '\n' +
                '#(struct:physical 113 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj113 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(
                15, 2)) + int(off_y)], 11, 15)
            obj113.color = Color('white')
            obj113.group = 113
            obj113_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj113.png')
            image_bindings.append([obj113, obj113_image])
            user_shapes.append(obj113)
            return obj113
        obj113 = make_obj113(0, 0, False)
        obj113.mass = 10
        obj113.hit([10450.180986346139, 46635.88162517719], obj113.position)

        def make_obj114(off_x, off_y, debug):
            print('Making ' + 'make_obj114' + '\n' +
                '#(struct:physical 114 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj114 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)
                ) + int(off_x), int(p.y + fraction(105, 2) + -30 - fraction
                (15, 2)) + int(off_y)], 11, 15)
            obj114.color = Color('white')
            obj114.group = 114
            obj114_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj114.png')
            image_bindings.append([obj114, obj114_image])
            user_shapes.append(obj114)
            return obj114
        obj114 = make_obj114(0, 0, False)
        obj114.mass = 10
        obj114.hit([-29327.500914251475, -18978.244729217815], obj114.position)
        _hy_anon_var_65 = deactivate(f)
    else:
        _hy_anon_var_65 = None
    return _hy_anon_var_65


space = obj94.body.space
ch = space.add_wildcard_collision_handler(obj94.collision_type)
ch.post_solve = on_collide_94
obj71.mass = 10
motor(obj71, 0)
obj71.gravity = 0, -100


def on_click_71(keys):
    global obj71
    f = obj71
    if not f or not f.body:
        return False
        _hy_anon_var_67 = None
    else:
        _hy_anon_var_67 = None
    p = f.body.position
    if mouse_clicked() and obj71.inside(mouse_point()) and obj71.active:

        def make_obj73(off_x, off_y, debug):
            print('Making ' + 'make_obj73' + '\n' +
                '#(struct:physical 73 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj73 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj73.color = Color('white')
            obj73.group = 73
            obj73_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj73.png')
            image_bindings.append([obj73, obj73_image])
            user_shapes.append(obj73)
            return obj73
        obj73 = make_obj73(0, 0, False)
        obj73.mass = 10
        obj73.hit([49594.90683761907, 29261.976454055664], obj73.position)

        def make_obj74(off_x, off_y, debug):
            print('Making ' + 'make_obj74' + '\n' +
                '#(struct:physical 74 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj74 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj74.color = Color('white')
            obj74.group = 74
            obj74_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj74.png')
            image_bindings.append([obj74, obj74_image])
            user_shapes.append(obj74)
            return obj74
        obj74 = make_obj74(0, 0, False)
        obj74.mass = 10
        obj74.hit([22041.5708107517, 48662.64323280887], obj74.position)

        def make_obj75(off_x, off_y, debug):
            print('Making ' + 'make_obj75' + '\n' +
                '#(struct:physical 75 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj75 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj75.color = Color('white')
            obj75.group = 75
            obj75_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj75.png')
            image_bindings.append([obj75, obj75_image])
            user_shapes.append(obj75)
            return obj75
        obj75 = make_obj75(0, 0, False)
        obj75.mass = 10
        obj75.hit([48569.45721023882, 8105.1646466074235], obj75.position)

        def make_obj76(off_x, off_y, debug):
            print('Making ' + 'make_obj76' + '\n' +
                '#(struct:physical 76 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj76 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj76.color = Color('white')
            obj76.group = 76
            obj76_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj76.png')
            image_bindings.append([obj76, obj76_image])
            user_shapes.append(obj76)
            return obj76
        obj76 = make_obj76(0, 0, False)
        obj76.mass = 10
        obj76.hit([-16199.45072324149, 49636.03451016714], obj76.position)

        def make_obj78(off_x, off_y, debug):
            print('Making ' + 'make_obj78' + '\n' +
                '#(struct:physical 78 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj78 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj78.color = Color('white')
            obj78.group = 78
            obj78_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj78.png')
            image_bindings.append([obj78, obj78_image])
            user_shapes.append(obj78)
            return obj78
        obj78 = make_obj78(0, 0, False)
        obj78.mass = 10
        obj78.hit([-7481.5401239693965, 43843.29033070347], obj78.position)

        def make_obj79(off_x, off_y, debug):
            print('Making ' + 'make_obj79' + '\n' +
                '#(struct:physical 79 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj79 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj79.color = Color('white')
            obj79.group = 79
            obj79_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj79.png')
            image_bindings.append([obj79, obj79_image])
            user_shapes.append(obj79)
            return obj79
        obj79 = make_obj79(0, 0, False)
        obj79.mass = 10
        obj79.hit([27978.188735307966, -211.44969947206118], obj79.position)

        def make_obj80(off_x, off_y, debug):
            print('Making ' + 'make_obj80' + '\n' +
                '#(struct:physical 80 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj80 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj80.color = Color('white')
            obj80.group = 80
            obj80_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj80.png')
            image_bindings.append([obj80, obj80_image])
            user_shapes.append(obj80)
            return obj80
        obj80 = make_obj80(0, 0, False)
        obj80.mass = 10
        obj80.hit([-28893.160356622502, -33591.5233909704], obj80.position)

        def make_obj81(off_x, off_y, debug):
            print('Making ' + 'make_obj81' + '\n' +
                '#(struct:physical 81 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj81 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj81.color = Color('white')
            obj81.group = 81
            obj81_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj81.png')
            image_bindings.append([obj81, obj81_image])
            user_shapes.append(obj81)
            return obj81
        obj81 = make_obj81(0, 0, False)
        obj81.mass = 10
        obj81.hit([19481.18413614256, -43450.47458487067], obj81.position)

        def make_obj83(off_x, off_y, debug):
            print('Making ' + 'make_obj83' + '\n' +
                '#(struct:physical 83 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj83 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj83.color = Color('white')
            obj83.group = 83
            obj83_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj83.png')
            image_bindings.append([obj83, obj83_image])
            user_shapes.append(obj83)
            return obj83
        obj83 = make_obj83(0, 0, False)
        obj83.mass = 10
        obj83.hit([40041.68604236812, -42315.24085662563], obj83.position)

        def make_obj84(off_x, off_y, debug):
            print('Making ' + 'make_obj84' + '\n' +
                '#(struct:physical 84 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj84 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj84.color = Color('white')
            obj84.group = 84
            obj84_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj84.png')
            image_bindings.append([obj84, obj84_image])
            user_shapes.append(obj84)
            return obj84
        obj84 = make_obj84(0, 0, False)
        obj84.mass = 10
        obj84.hit([-31301.36616776794, -21291.148878764117], obj84.position)

        def make_obj85(off_x, off_y, debug):
            print('Making ' + 'make_obj85' + '\n' +
                '#(struct:physical 85 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj85 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj85.color = Color('white')
            obj85.group = 85
            obj85_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj85.png')
            image_bindings.append([obj85, obj85_image])
            user_shapes.append(obj85)
            return obj85
        obj85 = make_obj85(0, 0, False)
        obj85.mass = 10
        obj85.hit([-37718.49543448702, -2542.2976419324696], obj85.position)

        def make_obj86(off_x, off_y, debug):
            print('Making ' + 'make_obj86' + '\n' +
                '#(struct:physical 86 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj86 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj86.color = Color('white')
            obj86.group = 86
            obj86_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj86.png')
            image_bindings.append([obj86, obj86_image])
            user_shapes.append(obj86)
            return obj86
        obj86 = make_obj86(0, 0, False)
        obj86.mass = 10
        obj86.hit([-27075.271245943477, -19418.434249012338], obj86.position)

        def make_obj88(off_x, off_y, debug):
            print('Making ' + 'make_obj88' + '\n' +
                '#(struct:physical 88 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj88 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj88.color = Color('white')
            obj88.group = 88
            obj88_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj88.png')
            image_bindings.append([obj88, obj88_image])
            user_shapes.append(obj88)
            return obj88
        obj88 = make_obj88(0, 0, False)
        obj88.mass = 10
        obj88.hit([-14664.756495102622, -49096.885535901456], obj88.position)

        def make_obj89(off_x, off_y, debug):
            print('Making ' + 'make_obj89' + '\n' +
                '#(struct:physical 89 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj89 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj89.color = Color('white')
            obj89.group = 89
            obj89_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj89.png')
            image_bindings.append([obj89, obj89_image])
            user_shapes.append(obj89)
            return obj89
        obj89 = make_obj89(0, 0, False)
        obj89.mass = 10
        obj89.hit([-39012.14702393081, 20791.37298851405], obj89.position)

        def make_obj90(off_x, off_y, debug):
            print('Making ' + 'make_obj90' + '\n' +
                '#(struct:physical 90 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj90 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj90.color = Color('white')
            obj90.group = 90
            obj90_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj90.png')
            image_bindings.append([obj90, obj90_image])
            user_shapes.append(obj90)
            return obj90
        obj90 = make_obj90(0, 0, False)
        obj90.mass = 10
        obj90.hit([9748.920618504177, 11591.730502219863], obj90.position)

        def make_obj91(off_x, off_y, debug):
            print('Making ' + 'make_obj91' + '\n' +
                '#(struct:physical 91 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj91 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj91.color = Color('white')
            obj91.group = 91
            obj91_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj91.png')
            image_bindings.append([obj91, obj91_image])
            user_shapes.append(obj91)
            return obj91
        obj91 = make_obj91(0, 0, False)
        obj91.mass = 10
        obj91.hit([23196.359007815525, 4662.493725726083], obj91.position)
        deactivate(f)
        return True
        _hy_anon_var_84 = None
    else:
        _hy_anon_var_84 = None
    return _hy_anon_var_84


add_observer(on_click_71)


def on_collide_71(arbiter, space, data):
    f = obj71
    p = f.body.position
    friction = arbiter.friction
    restitution = arbiter.restitution
    total_impulse = arbiter.total_impulse
    energy_loss = arbiter.total_ke
    if friction > 0 and energy_loss > 50000000:

        def make_obj73(off_x, off_y, debug):
            print('Making ' + 'make_obj73' + '\n' +
                '#(struct:physical 73 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj73 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj73.color = Color('white')
            obj73.group = 73
            obj73_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj73.png')
            image_bindings.append([obj73, obj73_image])
            user_shapes.append(obj73)
            return obj73
        obj73 = make_obj73(0, 0, False)
        obj73.mass = 10
        obj73.hit([49594.90683761907, 29261.976454055664], obj73.position)

        def make_obj74(off_x, off_y, debug):
            print('Making ' + 'make_obj74' + '\n' +
                '#(struct:physical 74 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj74 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj74.color = Color('white')
            obj74.group = 74
            obj74_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj74.png')
            image_bindings.append([obj74, obj74_image])
            user_shapes.append(obj74)
            return obj74
        obj74 = make_obj74(0, 0, False)
        obj74.mass = 10
        obj74.hit([22041.5708107517, 48662.64323280887], obj74.position)

        def make_obj75(off_x, off_y, debug):
            print('Making ' + 'make_obj75' + '\n' +
                '#(struct:physical 75 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj75 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj75.color = Color('white')
            obj75.group = 75
            obj75_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj75.png')
            image_bindings.append([obj75, obj75_image])
            user_shapes.append(obj75)
            return obj75
        obj75 = make_obj75(0, 0, False)
        obj75.mass = 10
        obj75.hit([48569.45721023882, 8105.1646466074235], obj75.position)

        def make_obj76(off_x, off_y, debug):
            print('Making ' + 'make_obj76' + '\n' +
                '#(struct:physical 76 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj76 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj76.color = Color('white')
            obj76.group = 76
            obj76_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj76.png')
            image_bindings.append([obj76, obj76_image])
            user_shapes.append(obj76)
            return obj76
        obj76 = make_obj76(0, 0, False)
        obj76.mass = 10
        obj76.hit([-16199.45072324149, 49636.03451016714], obj76.position)

        def make_obj78(off_x, off_y, debug):
            print('Making ' + 'make_obj78' + '\n' +
                '#(struct:physical 78 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj78 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj78.color = Color('white')
            obj78.group = 78
            obj78_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj78.png')
            image_bindings.append([obj78, obj78_image])
            user_shapes.append(obj78)
            return obj78
        obj78 = make_obj78(0, 0, False)
        obj78.mass = 10
        obj78.hit([-7481.5401239693965, 43843.29033070347], obj78.position)

        def make_obj79(off_x, off_y, debug):
            print('Making ' + 'make_obj79' + '\n' +
                '#(struct:physical 79 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj79 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj79.color = Color('white')
            obj79.group = 79
            obj79_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj79.png')
            image_bindings.append([obj79, obj79_image])
            user_shapes.append(obj79)
            return obj79
        obj79 = make_obj79(0, 0, False)
        obj79.mass = 10
        obj79.hit([27978.188735307966, -211.44969947206118], obj79.position)

        def make_obj80(off_x, off_y, debug):
            print('Making ' + 'make_obj80' + '\n' +
                '#(struct:physical 80 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj80 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj80.color = Color('white')
            obj80.group = 80
            obj80_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj80.png')
            image_bindings.append([obj80, obj80_image])
            user_shapes.append(obj80)
            return obj80
        obj80 = make_obj80(0, 0, False)
        obj80.mass = 10
        obj80.hit([-28893.160356622502, -33591.5233909704], obj80.position)

        def make_obj81(off_x, off_y, debug):
            print('Making ' + 'make_obj81' + '\n' +
                '#(struct:physical 81 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj81 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj81.color = Color('white')
            obj81.group = 81
            obj81_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj81.png')
            image_bindings.append([obj81, obj81_image])
            user_shapes.append(obj81)
            return obj81
        obj81 = make_obj81(0, 0, False)
        obj81.mass = 10
        obj81.hit([19481.18413614256, -43450.47458487067], obj81.position)

        def make_obj83(off_x, off_y, debug):
            print('Making ' + 'make_obj83' + '\n' +
                '#(struct:physical 83 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj83 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj83.color = Color('white')
            obj83.group = 83
            obj83_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj83.png')
            image_bindings.append([obj83, obj83_image])
            user_shapes.append(obj83)
            return obj83
        obj83 = make_obj83(0, 0, False)
        obj83.mass = 10
        obj83.hit([40041.68604236812, -42315.24085662563], obj83.position)

        def make_obj84(off_x, off_y, debug):
            print('Making ' + 'make_obj84' + '\n' +
                '#(struct:physical 84 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj84 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj84.color = Color('white')
            obj84.group = 84
            obj84_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj84.png')
            image_bindings.append([obj84, obj84_image])
            user_shapes.append(obj84)
            return obj84
        obj84 = make_obj84(0, 0, False)
        obj84.mass = 10
        obj84.hit([-31301.36616776794, -21291.148878764117], obj84.position)

        def make_obj85(off_x, off_y, debug):
            print('Making ' + 'make_obj85' + '\n' +
                '#(struct:physical 85 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj85 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj85.color = Color('white')
            obj85.group = 85
            obj85_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj85.png')
            image_bindings.append([obj85, obj85_image])
            user_shapes.append(obj85)
            return obj85
        obj85 = make_obj85(0, 0, False)
        obj85.mass = 10
        obj85.hit([-37718.49543448702, -2542.2976419324696], obj85.position)

        def make_obj86(off_x, off_y, debug):
            print('Making ' + 'make_obj86' + '\n' +
                '#(struct:physical 86 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj86 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj86.color = Color('white')
            obj86.group = 86
            obj86_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj86.png')
            image_bindings.append([obj86, obj86_image])
            user_shapes.append(obj86)
            return obj86
        obj86 = make_obj86(0, 0, False)
        obj86.mass = 10
        obj86.hit([-27075.271245943477, -19418.434249012338], obj86.position)

        def make_obj88(off_x, off_y, debug):
            print('Making ' + 'make_obj88' + '\n' +
                '#(struct:physical 88 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj88 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj88.color = Color('white')
            obj88.group = 88
            obj88_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj88.png')
            image_bindings.append([obj88, obj88_image])
            user_shapes.append(obj88)
            return obj88
        obj88 = make_obj88(0, 0, False)
        obj88.mass = 10
        obj88.hit([-14664.756495102622, -49096.885535901456], obj88.position)

        def make_obj89(off_x, off_y, debug):
            print('Making ' + 'make_obj89' + '\n' +
                '#(struct:physical 89 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj89 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj89.color = Color('white')
            obj89.group = 89
            obj89_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj89.png')
            image_bindings.append([obj89, obj89_image])
            user_shapes.append(obj89)
            return obj89
        obj89 = make_obj89(0, 0, False)
        obj89.mass = 10
        obj89.hit([-39012.14702393081, 20791.37298851405], obj89.position)

        def make_obj90(off_x, off_y, debug):
            print('Making ' + 'make_obj90' + '\n' +
                '#(struct:physical 90 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj90 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj90.color = Color('white')
            obj90.group = 90
            obj90_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj90.png')
            image_bindings.append([obj90, obj90_image])
            user_shapes.append(obj90)
            return obj90
        obj90 = make_obj90(0, 0, False)
        obj90.mass = 10
        obj90.hit([9748.920618504177, 11591.730502219863], obj90.position)

        def make_obj91(off_x, off_y, debug):
            print('Making ' + 'make_obj91' + '\n' +
                '#(struct:physical 91 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj91 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj91.color = Color('white')
            obj91.group = 91
            obj91_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj91.png')
            image_bindings.append([obj91, obj91_image])
            user_shapes.append(obj91)
            return obj91
        obj91 = make_obj91(0, 0, False)
        obj91.mass = 10
        obj91.hit([23196.359007815525, 4662.493725726083], obj91.position)
        _hy_anon_var_102 = deactivate(f)
    else:
        _hy_anon_var_102 = None
    return _hy_anon_var_102


space = obj71.body.space
ch = space.add_wildcard_collision_handler(obj71.collision_type)
ch.post_solve = on_collide_71
obj48.mass = 10
motor(obj48, 0)
obj48.gravity = 0, -100


def on_click_48(keys):
    global obj48
    f = obj48
    if not f or not f.body:
        return False
        _hy_anon_var_104 = None
    else:
        _hy_anon_var_104 = None
    p = f.body.position
    if mouse_clicked() and obj48.inside(mouse_point()) and obj48.active:

        def make_obj50(off_x, off_y, debug):
            print('Making ' + 'make_obj50' + '\n' +
                '#(struct:physical 50 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj50 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj50.color = Color('white')
            obj50.group = 50
            obj50_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj50.png')
            image_bindings.append([obj50, obj50_image])
            user_shapes.append(obj50)
            return obj50
        obj50 = make_obj50(0, 0, False)
        obj50.mass = 10
        obj50.hit([26714.999637734145, 1683.0351087430827], obj50.position)

        def make_obj51(off_x, off_y, debug):
            print('Making ' + 'make_obj51' + '\n' +
                '#(struct:physical 51 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj51 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj51.color = Color('white')
            obj51.group = 51
            obj51_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj51.png')
            image_bindings.append([obj51, obj51_image])
            user_shapes.append(obj51)
            return obj51
        obj51 = make_obj51(0, 0, False)
        obj51.mass = 10
        obj51.hit([30469.013363484948, -38869.471215840895], obj51.position)

        def make_obj52(off_x, off_y, debug):
            print('Making ' + 'make_obj52' + '\n' +
                '#(struct:physical 52 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj52 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj52.color = Color('white')
            obj52.group = 52
            obj52_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj52.png')
            image_bindings.append([obj52, obj52_image])
            user_shapes.append(obj52)
            return obj52
        obj52 = make_obj52(0, 0, False)
        obj52.mass = 10
        obj52.hit([35931.893012913366, 20383.06091904563], obj52.position)

        def make_obj53(off_x, off_y, debug):
            print('Making ' + 'make_obj53' + '\n' +
                '#(struct:physical 53 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj53 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj53.color = Color('white')
            obj53.group = 53
            obj53_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj53.png')
            image_bindings.append([obj53, obj53_image])
            user_shapes.append(obj53)
            return obj53
        obj53 = make_obj53(0, 0, False)
        obj53.mass = 10
        obj53.hit([17950.846495520338, 5913.292809847029], obj53.position)

        def make_obj55(off_x, off_y, debug):
            print('Making ' + 'make_obj55' + '\n' +
                '#(struct:physical 55 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj55 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj55.color = Color('white')
            obj55.group = 55
            obj55_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj55.png')
            image_bindings.append([obj55, obj55_image])
            user_shapes.append(obj55)
            return obj55
        obj55 = make_obj55(0, 0, False)
        obj55.mass = 10
        obj55.hit([5988.11021668998, 15800.436745977699], obj55.position)

        def make_obj56(off_x, off_y, debug):
            print('Making ' + 'make_obj56' + '\n' +
                '#(struct:physical 56 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj56 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj56.color = Color('white')
            obj56.group = 56
            obj56_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj56.png')
            image_bindings.append([obj56, obj56_image])
            user_shapes.append(obj56)
            return obj56
        obj56 = make_obj56(0, 0, False)
        obj56.mass = 10
        obj56.hit([19178.721492452096, -10344.671213927584], obj56.position)

        def make_obj57(off_x, off_y, debug):
            print('Making ' + 'make_obj57' + '\n' +
                '#(struct:physical 57 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj57 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj57.color = Color('white')
            obj57.group = 57
            obj57_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj57.png')
            image_bindings.append([obj57, obj57_image])
            user_shapes.append(obj57)
            return obj57
        obj57 = make_obj57(0, 0, False)
        obj57.mass = 10
        obj57.hit([-25765.193057982287, 19035.895322325232], obj57.position)

        def make_obj58(off_x, off_y, debug):
            print('Making ' + 'make_obj58' + '\n' +
                '#(struct:physical 58 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj58 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj58.color = Color('white')
            obj58.group = 58
            obj58_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj58.png')
            image_bindings.append([obj58, obj58_image])
            user_shapes.append(obj58)
            return obj58
        obj58 = make_obj58(0, 0, False)
        obj58.mass = 10
        obj58.hit([-14970.019882024295, -7414.763593643627], obj58.position)

        def make_obj60(off_x, off_y, debug):
            print('Making ' + 'make_obj60' + '\n' +
                '#(struct:physical 60 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj60 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj60.color = Color('white')
            obj60.group = 60
            obj60_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj60.png')
            image_bindings.append([obj60, obj60_image])
            user_shapes.append(obj60)
            return obj60
        obj60 = make_obj60(0, 0, False)
        obj60.mass = 10
        obj60.hit([-35136.269174596295, -39400.37472529289], obj60.position)

        def make_obj61(off_x, off_y, debug):
            print('Making ' + 'make_obj61' + '\n' +
                '#(struct:physical 61 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj61 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj61.color = Color('white')
            obj61.group = 61
            obj61_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj61.png')
            image_bindings.append([obj61, obj61_image])
            user_shapes.append(obj61)
            return obj61
        obj61 = make_obj61(0, 0, False)
        obj61.mass = 10
        obj61.hit([49349.006513271815, 14115.748260187844], obj61.position)

        def make_obj62(off_x, off_y, debug):
            print('Making ' + 'make_obj62' + '\n' +
                '#(struct:physical 62 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj62 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj62.color = Color('white')
            obj62.group = 62
            obj62_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj62.png')
            image_bindings.append([obj62, obj62_image])
            user_shapes.append(obj62)
            return obj62
        obj62 = make_obj62(0, 0, False)
        obj62.mass = 10
        obj62.hit([7350.236440275148, -15504.239971023497], obj62.position)

        def make_obj63(off_x, off_y, debug):
            print('Making ' + 'make_obj63' + '\n' +
                '#(struct:physical 63 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj63 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj63.color = Color('white')
            obj63.group = 63
            obj63_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj63.png')
            image_bindings.append([obj63, obj63_image])
            user_shapes.append(obj63)
            return obj63
        obj63 = make_obj63(0, 0, False)
        obj63.mass = 10
        obj63.hit([48187.48671631266, 39598.61356683813], obj63.position)

        def make_obj65(off_x, off_y, debug):
            print('Making ' + 'make_obj65' + '\n' +
                '#(struct:physical 65 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj65 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj65.color = Color('white')
            obj65.group = 65
            obj65_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj65.png')
            image_bindings.append([obj65, obj65_image])
            user_shapes.append(obj65)
            return obj65
        obj65 = make_obj65(0, 0, False)
        obj65.mass = 10
        obj65.hit([-3193.6135292685576, -44830.48548566666], obj65.position)

        def make_obj66(off_x, off_y, debug):
            print('Making ' + 'make_obj66' + '\n' +
                '#(struct:physical 66 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj66 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj66.color = Color('white')
            obj66.group = 66
            obj66_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj66.png')
            image_bindings.append([obj66, obj66_image])
            user_shapes.append(obj66)
            return obj66
        obj66 = make_obj66(0, 0, False)
        obj66.mass = 10
        obj66.hit([-15833.124749662806, 999.673364668175], obj66.position)

        def make_obj67(off_x, off_y, debug):
            print('Making ' + 'make_obj67' + '\n' +
                '#(struct:physical 67 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj67 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj67.color = Color('white')
            obj67.group = 67
            obj67_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj67.png')
            image_bindings.append([obj67, obj67_image])
            user_shapes.append(obj67)
            return obj67
        obj67 = make_obj67(0, 0, False)
        obj67.mass = 10
        obj67.hit([-22837.911208692363, -4858.49683419041], obj67.position)

        def make_obj68(off_x, off_y, debug):
            print('Making ' + 'make_obj68' + '\n' +
                '#(struct:physical 68 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj68 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj68.color = Color('white')
            obj68.group = 68
            obj68_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj68.png')
            image_bindings.append([obj68, obj68_image])
            user_shapes.append(obj68)
            return obj68
        obj68 = make_obj68(0, 0, False)
        obj68.mass = 10
        obj68.hit([22383.746936875265, 6394.778944112833], obj68.position)
        deactivate(f)
        return True
        _hy_anon_var_121 = None
    else:
        _hy_anon_var_121 = None
    return _hy_anon_var_121


add_observer(on_click_48)


def on_collide_48(arbiter, space, data):
    f = obj48
    p = f.body.position
    friction = arbiter.friction
    restitution = arbiter.restitution
    total_impulse = arbiter.total_impulse
    energy_loss = arbiter.total_ke
    if friction > 0 and energy_loss > 50000000:

        def make_obj50(off_x, off_y, debug):
            print('Making ' + 'make_obj50' + '\n' +
                '#(struct:physical 50 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj50 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj50.color = Color('white')
            obj50.group = 50
            obj50_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj50.png')
            image_bindings.append([obj50, obj50_image])
            user_shapes.append(obj50)
            return obj50
        obj50 = make_obj50(0, 0, False)
        obj50.mass = 10
        obj50.hit([26714.999637734145, 1683.0351087430827], obj50.position)

        def make_obj51(off_x, off_y, debug):
            print('Making ' + 'make_obj51' + '\n' +
                '#(struct:physical 51 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj51 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj51.color = Color('white')
            obj51.group = 51
            obj51_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj51.png')
            image_bindings.append([obj51, obj51_image])
            user_shapes.append(obj51)
            return obj51
        obj51 = make_obj51(0, 0, False)
        obj51.mass = 10
        obj51.hit([30469.013363484948, -38869.471215840895], obj51.position)

        def make_obj52(off_x, off_y, debug):
            print('Making ' + 'make_obj52' + '\n' +
                '#(struct:physical 52 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj52 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj52.color = Color('white')
            obj52.group = 52
            obj52_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj52.png')
            image_bindings.append([obj52, obj52_image])
            user_shapes.append(obj52)
            return obj52
        obj52 = make_obj52(0, 0, False)
        obj52.mass = 10
        obj52.hit([35931.893012913366, 20383.06091904563], obj52.position)

        def make_obj53(off_x, off_y, debug):
            print('Making ' + 'make_obj53' + '\n' +
                '#(struct:physical 53 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj53 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj53.color = Color('white')
            obj53.group = 53
            obj53_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj53.png')
            image_bindings.append([obj53, obj53_image])
            user_shapes.append(obj53)
            return obj53
        obj53 = make_obj53(0, 0, False)
        obj53.mass = 10
        obj53.hit([17950.846495520338, 5913.292809847029], obj53.position)

        def make_obj55(off_x, off_y, debug):
            print('Making ' + 'make_obj55' + '\n' +
                '#(struct:physical 55 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj55 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj55.color = Color('white')
            obj55.group = 55
            obj55_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj55.png')
            image_bindings.append([obj55, obj55_image])
            user_shapes.append(obj55)
            return obj55
        obj55 = make_obj55(0, 0, False)
        obj55.mass = 10
        obj55.hit([5988.11021668998, 15800.436745977699], obj55.position)

        def make_obj56(off_x, off_y, debug):
            print('Making ' + 'make_obj56' + '\n' +
                '#(struct:physical 56 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj56 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj56.color = Color('white')
            obj56.group = 56
            obj56_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj56.png')
            image_bindings.append([obj56, obj56_image])
            user_shapes.append(obj56)
            return obj56
        obj56 = make_obj56(0, 0, False)
        obj56.mass = 10
        obj56.hit([19178.721492452096, -10344.671213927584], obj56.position)

        def make_obj57(off_x, off_y, debug):
            print('Making ' + 'make_obj57' + '\n' +
                '#(struct:physical 57 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj57 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj57.color = Color('white')
            obj57.group = 57
            obj57_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj57.png')
            image_bindings.append([obj57, obj57_image])
            user_shapes.append(obj57)
            return obj57
        obj57 = make_obj57(0, 0, False)
        obj57.mass = 10
        obj57.hit([-25765.193057982287, 19035.895322325232], obj57.position)

        def make_obj58(off_x, off_y, debug):
            print('Making ' + 'make_obj58' + '\n' +
                '#(struct:physical 58 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj58 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj58.color = Color('white')
            obj58.group = 58
            obj58_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj58.png')
            image_bindings.append([obj58, obj58_image])
            user_shapes.append(obj58)
            return obj58
        obj58 = make_obj58(0, 0, False)
        obj58.mass = 10
        obj58.hit([-14970.019882024295, -7414.763593643627], obj58.position)

        def make_obj60(off_x, off_y, debug):
            print('Making ' + 'make_obj60' + '\n' +
                '#(struct:physical 60 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj60 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj60.color = Color('white')
            obj60.group = 60
            obj60_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj60.png')
            image_bindings.append([obj60, obj60_image])
            user_shapes.append(obj60)
            return obj60
        obj60 = make_obj60(0, 0, False)
        obj60.mass = 10
        obj60.hit([-35136.269174596295, -39400.37472529289], obj60.position)

        def make_obj61(off_x, off_y, debug):
            print('Making ' + 'make_obj61' + '\n' +
                '#(struct:physical 61 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj61 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj61.color = Color('white')
            obj61.group = 61
            obj61_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj61.png')
            image_bindings.append([obj61, obj61_image])
            user_shapes.append(obj61)
            return obj61
        obj61 = make_obj61(0, 0, False)
        obj61.mass = 10
        obj61.hit([49349.006513271815, 14115.748260187844], obj61.position)

        def make_obj62(off_x, off_y, debug):
            print('Making ' + 'make_obj62' + '\n' +
                '#(struct:physical 62 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj62 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj62.color = Color('white')
            obj62.group = 62
            obj62_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj62.png')
            image_bindings.append([obj62, obj62_image])
            user_shapes.append(obj62)
            return obj62
        obj62 = make_obj62(0, 0, False)
        obj62.mass = 10
        obj62.hit([7350.236440275148, -15504.239971023497], obj62.position)

        def make_obj63(off_x, off_y, debug):
            print('Making ' + 'make_obj63' + '\n' +
                '#(struct:physical 63 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj63 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj63.color = Color('white')
            obj63.group = 63
            obj63_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj63.png')
            image_bindings.append([obj63, obj63_image])
            user_shapes.append(obj63)
            return obj63
        obj63 = make_obj63(0, 0, False)
        obj63.mass = 10
        obj63.hit([48187.48671631266, 39598.61356683813], obj63.position)

        def make_obj65(off_x, off_y, debug):
            print('Making ' + 'make_obj65' + '\n' +
                '#(struct:physical 65 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj65 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj65.color = Color('white')
            obj65.group = 65
            obj65_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj65.png')
            image_bindings.append([obj65, obj65_image])
            user_shapes.append(obj65)
            return obj65
        obj65 = make_obj65(0, 0, False)
        obj65.mass = 10
        obj65.hit([-3193.6135292685576, -44830.48548566666], obj65.position)

        def make_obj66(off_x, off_y, debug):
            print('Making ' + 'make_obj66' + '\n' +
                '#(struct:physical 66 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj66 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj66.color = Color('white')
            obj66.group = 66
            obj66_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj66.png')
            image_bindings.append([obj66, obj66_image])
            user_shapes.append(obj66)
            return obj66
        obj66 = make_obj66(0, 0, False)
        obj66.mass = 10
        obj66.hit([-15833.124749662806, 999.673364668175], obj66.position)

        def make_obj67(off_x, off_y, debug):
            print('Making ' + 'make_obj67' + '\n' +
                '#(struct:physical 67 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj67 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj67.color = Color('white')
            obj67.group = 67
            obj67_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj67.png')
            image_bindings.append([obj67, obj67_image])
            user_shapes.append(obj67)
            return obj67
        obj67 = make_obj67(0, 0, False)
        obj67.mass = 10
        obj67.hit([-22837.911208692363, -4858.49683419041], obj67.position)

        def make_obj68(off_x, off_y, debug):
            print('Making ' + 'make_obj68' + '\n' +
                '#(struct:physical 68 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj68 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj68.color = Color('white')
            obj68.group = 68
            obj68_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj68.png')
            image_bindings.append([obj68, obj68_image])
            user_shapes.append(obj68)
            return obj68
        obj68 = make_obj68(0, 0, False)
        obj68.mass = 10
        obj68.hit([22383.746936875265, 6394.778944112833], obj68.position)
        _hy_anon_var_139 = deactivate(f)
    else:
        _hy_anon_var_139 = None
    return _hy_anon_var_139


space = obj48.body.space
ch = space.add_wildcard_collision_handler(obj48.collision_type)
ch.post_solve = on_collide_48
obj25.mass = 10
motor(obj25, 0)
obj25.gravity = 0, -100


def on_click_25(keys):
    global obj25
    f = obj25
    if not f or not f.body:
        return False
        _hy_anon_var_141 = None
    else:
        _hy_anon_var_141 = None
    p = f.body.position
    if mouse_clicked() and obj25.inside(mouse_point()) and obj25.active:

        def make_obj27(off_x, off_y, debug):
            print('Making ' + 'make_obj27' + '\n' +
                '#(struct:physical 27 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj27 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj27.color = Color('white')
            obj27.group = 27
            obj27_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj27.png')
            image_bindings.append([obj27, obj27_image])
            user_shapes.append(obj27)
            return obj27
        obj27 = make_obj27(0, 0, False)
        obj27.mass = 10
        obj27.hit([29393.39720500323, 14941.429395186104], obj27.position)

        def make_obj28(off_x, off_y, debug):
            print('Making ' + 'make_obj28' + '\n' +
                '#(struct:physical 28 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj28 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj28.color = Color('white')
            obj28.group = 28
            obj28_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj28.png')
            image_bindings.append([obj28, obj28_image])
            user_shapes.append(obj28)
            return obj28
        obj28 = make_obj28(0, 0, False)
        obj28.mass = 10
        obj28.hit([16047.150487501014, -22616.491910123805], obj28.position)

        def make_obj29(off_x, off_y, debug):
            print('Making ' + 'make_obj29' + '\n' +
                '#(struct:physical 29 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj29 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj29.color = Color('white')
            obj29.group = 29
            obj29_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj29.png')
            image_bindings.append([obj29, obj29_image])
            user_shapes.append(obj29)
            return obj29
        obj29 = make_obj29(0, 0, False)
        obj29.mass = 10
        obj29.hit([32075.8781330154, -49002.8360608476], obj29.position)

        def make_obj30(off_x, off_y, debug):
            print('Making ' + 'make_obj30' + '\n' +
                '#(struct:physical 30 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj30 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj30.color = Color('white')
            obj30.group = 30
            obj30_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj30.png')
            image_bindings.append([obj30, obj30_image])
            user_shapes.append(obj30)
            return obj30
        obj30 = make_obj30(0, 0, False)
        obj30.mass = 10
        obj30.hit([27651.830541803676, 10125.662085166608], obj30.position)

        def make_obj32(off_x, off_y, debug):
            print('Making ' + 'make_obj32' + '\n' +
                '#(struct:physical 32 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj32 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj32.color = Color('white')
            obj32.group = 32
            obj32_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj32.png')
            image_bindings.append([obj32, obj32_image])
            user_shapes.append(obj32)
            return obj32
        obj32 = make_obj32(0, 0, False)
        obj32.mass = 10
        obj32.hit([5181.050085848772, -41857.13143234219], obj32.position)

        def make_obj33(off_x, off_y, debug):
            print('Making ' + 'make_obj33' + '\n' +
                '#(struct:physical 33 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj33 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj33.color = Color('white')
            obj33.group = 33
            obj33_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj33.png')
            image_bindings.append([obj33, obj33_image])
            user_shapes.append(obj33)
            return obj33
        obj33 = make_obj33(0, 0, False)
        obj33.mass = 10
        obj33.hit([43910.67308220548, 13391.130553873998], obj33.position)

        def make_obj34(off_x, off_y, debug):
            print('Making ' + 'make_obj34' + '\n' +
                '#(struct:physical 34 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj34 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj34.color = Color('white')
            obj34.group = 34
            obj34_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj34.png')
            image_bindings.append([obj34, obj34_image])
            user_shapes.append(obj34)
            return obj34
        obj34 = make_obj34(0, 0, False)
        obj34.mass = 10
        obj34.hit([31467.295890952824, -28546.411739115985], obj34.position)

        def make_obj35(off_x, off_y, debug):
            print('Making ' + 'make_obj35' + '\n' +
                '#(struct:physical 35 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj35 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj35.color = Color('white')
            obj35.group = 35
            obj35_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj35.png')
            image_bindings.append([obj35, obj35_image])
            user_shapes.append(obj35)
            return obj35
        obj35 = make_obj35(0, 0, False)
        obj35.mass = 10
        obj35.hit([-27401.128131764624, -41937.15705138833], obj35.position)

        def make_obj37(off_x, off_y, debug):
            print('Making ' + 'make_obj37' + '\n' +
                '#(struct:physical 37 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj37 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj37.color = Color('white')
            obj37.group = 37
            obj37_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj37.png')
            image_bindings.append([obj37, obj37_image])
            user_shapes.append(obj37)
            return obj37
        obj37 = make_obj37(0, 0, False)
        obj37.mass = 10
        obj37.hit([46840.37299426217, 42215.363630278895], obj37.position)

        def make_obj38(off_x, off_y, debug):
            print('Making ' + 'make_obj38' + '\n' +
                '#(struct:physical 38 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj38 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj38.color = Color('white')
            obj38.group = 38
            obj38_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj38.png')
            image_bindings.append([obj38, obj38_image])
            user_shapes.append(obj38)
            return obj38
        obj38 = make_obj38(0, 0, False)
        obj38.mass = 10
        obj38.hit([6950.228741776111, 44397.68056262229], obj38.position)

        def make_obj39(off_x, off_y, debug):
            print('Making ' + 'make_obj39' + '\n' +
                '#(struct:physical 39 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj39 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj39.color = Color('white')
            obj39.group = 39
            obj39_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj39.png')
            image_bindings.append([obj39, obj39_image])
            user_shapes.append(obj39)
            return obj39
        obj39 = make_obj39(0, 0, False)
        obj39.mass = 10
        obj39.hit([26735.006054137193, -1168.4781506293075], obj39.position)

        def make_obj40(off_x, off_y, debug):
            print('Making ' + 'make_obj40' + '\n' +
                '#(struct:physical 40 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj40 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj40.color = Color('white')
            obj40.group = 40
            obj40_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj40.png')
            image_bindings.append([obj40, obj40_image])
            user_shapes.append(obj40)
            return obj40
        obj40 = make_obj40(0, 0, False)
        obj40.mass = 10
        obj40.hit([46654.03429047186, 46797.61825453132], obj40.position)

        def make_obj42(off_x, off_y, debug):
            print('Making ' + 'make_obj42' + '\n' +
                '#(struct:physical 42 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj42 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj42.color = Color('white')
            obj42.group = 42
            obj42_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj42.png')
            image_bindings.append([obj42, obj42_image])
            user_shapes.append(obj42)
            return obj42
        obj42 = make_obj42(0, 0, False)
        obj42.mass = 10
        obj42.hit([-46898.85334925761, 21380.94351329755], obj42.position)

        def make_obj43(off_x, off_y, debug):
            print('Making ' + 'make_obj43' + '\n' +
                '#(struct:physical 43 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj43 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj43.color = Color('white')
            obj43.group = 43
            obj43_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj43.png')
            image_bindings.append([obj43, obj43_image])
            user_shapes.append(obj43)
            return obj43
        obj43 = make_obj43(0, 0, False)
        obj43.mass = 10
        obj43.hit([20102.36947827341, -6890.163927607726], obj43.position)

        def make_obj44(off_x, off_y, debug):
            print('Making ' + 'make_obj44' + '\n' +
                '#(struct:physical 44 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj44 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj44.color = Color('white')
            obj44.group = 44
            obj44_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj44.png')
            image_bindings.append([obj44, obj44_image])
            user_shapes.append(obj44)
            return obj44
        obj44 = make_obj44(0, 0, False)
        obj44.mass = 10
        obj44.hit([-34976.51006912675, -22628.081102539054], obj44.position)

        def make_obj45(off_x, off_y, debug):
            print('Making ' + 'make_obj45' + '\n' +
                '#(struct:physical 45 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj45 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj45.color = Color('white')
            obj45.group = 45
            obj45_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj45.png')
            image_bindings.append([obj45, obj45_image])
            user_shapes.append(obj45)
            return obj45
        obj45 = make_obj45(0, 0, False)
        obj45.mass = 10
        obj45.hit([-44317.59205601624, 5429.15552604579], obj45.position)
        deactivate(f)
        return True
        _hy_anon_var_158 = None
    else:
        _hy_anon_var_158 = None
    return _hy_anon_var_158


add_observer(on_click_25)


def on_collide_25(arbiter, space, data):
    f = obj25
    p = f.body.position
    friction = arbiter.friction
    restitution = arbiter.restitution
    total_impulse = arbiter.total_impulse
    energy_loss = arbiter.total_ke
    if friction > 0 and energy_loss > 50000000:

        def make_obj27(off_x, off_y, debug):
            print('Making ' + 'make_obj27' + '\n' +
                '#(struct:physical 27 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj27 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj27.color = Color('white')
            obj27.group = 27
            obj27_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj27.png')
            image_bindings.append([obj27, obj27_image])
            user_shapes.append(obj27)
            return obj27
        obj27 = make_obj27(0, 0, False)
        obj27.mass = 10
        obj27.hit([29393.39720500323, 14941.429395186104], obj27.position)

        def make_obj28(off_x, off_y, debug):
            print('Making ' + 'make_obj28' + '\n' +
                '#(struct:physical 28 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj28 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj28.color = Color('white')
            obj28.group = 28
            obj28_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj28.png')
            image_bindings.append([obj28, obj28_image])
            user_shapes.append(obj28)
            return obj28
        obj28 = make_obj28(0, 0, False)
        obj28.mass = 10
        obj28.hit([16047.150487501014, -22616.491910123805], obj28.position)

        def make_obj29(off_x, off_y, debug):
            print('Making ' + 'make_obj29' + '\n' +
                '#(struct:physical 29 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj29 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj29.color = Color('white')
            obj29.group = 29
            obj29_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj29.png')
            image_bindings.append([obj29, obj29_image])
            user_shapes.append(obj29)
            return obj29
        obj29 = make_obj29(0, 0, False)
        obj29.mass = 10
        obj29.hit([32075.8781330154, -49002.8360608476], obj29.position)

        def make_obj30(off_x, off_y, debug):
            print('Making ' + 'make_obj30' + '\n' +
                '#(struct:physical 30 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj30 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj30.color = Color('white')
            obj30.group = 30
            obj30_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj30.png')
            image_bindings.append([obj30, obj30_image])
            user_shapes.append(obj30)
            return obj30
        obj30 = make_obj30(0, 0, False)
        obj30.mass = 10
        obj30.hit([27651.830541803676, 10125.662085166608], obj30.position)

        def make_obj32(off_x, off_y, debug):
            print('Making ' + 'make_obj32' + '\n' +
                '#(struct:physical 32 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj32 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj32.color = Color('white')
            obj32.group = 32
            obj32_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj32.png')
            image_bindings.append([obj32, obj32_image])
            user_shapes.append(obj32)
            return obj32
        obj32 = make_obj32(0, 0, False)
        obj32.mass = 10
        obj32.hit([5181.050085848772, -41857.13143234219], obj32.position)

        def make_obj33(off_x, off_y, debug):
            print('Making ' + 'make_obj33' + '\n' +
                '#(struct:physical 33 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj33 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj33.color = Color('white')
            obj33.group = 33
            obj33_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj33.png')
            image_bindings.append([obj33, obj33_image])
            user_shapes.append(obj33)
            return obj33
        obj33 = make_obj33(0, 0, False)
        obj33.mass = 10
        obj33.hit([43910.67308220548, 13391.130553873998], obj33.position)

        def make_obj34(off_x, off_y, debug):
            print('Making ' + 'make_obj34' + '\n' +
                '#(struct:physical 34 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj34 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj34.color = Color('white')
            obj34.group = 34
            obj34_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj34.png')
            image_bindings.append([obj34, obj34_image])
            user_shapes.append(obj34)
            return obj34
        obj34 = make_obj34(0, 0, False)
        obj34.mass = 10
        obj34.hit([31467.295890952824, -28546.411739115985], obj34.position)

        def make_obj35(off_x, off_y, debug):
            print('Making ' + 'make_obj35' + '\n' +
                '#(struct:physical 35 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj35 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj35.color = Color('white')
            obj35.group = 35
            obj35_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj35.png')
            image_bindings.append([obj35, obj35_image])
            user_shapes.append(obj35)
            return obj35
        obj35 = make_obj35(0, 0, False)
        obj35.mass = 10
        obj35.hit([-27401.128131764624, -41937.15705138833], obj35.position)

        def make_obj37(off_x, off_y, debug):
            print('Making ' + 'make_obj37' + '\n' +
                '#(struct:physical 37 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj37 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj37.color = Color('white')
            obj37.group = 37
            obj37_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj37.png')
            image_bindings.append([obj37, obj37_image])
            user_shapes.append(obj37)
            return obj37
        obj37 = make_obj37(0, 0, False)
        obj37.mass = 10
        obj37.hit([46840.37299426217, 42215.363630278895], obj37.position)

        def make_obj38(off_x, off_y, debug):
            print('Making ' + 'make_obj38' + '\n' +
                '#(struct:physical 38 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj38 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj38.color = Color('white')
            obj38.group = 38
            obj38_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj38.png')
            image_bindings.append([obj38, obj38_image])
            user_shapes.append(obj38)
            return obj38
        obj38 = make_obj38(0, 0, False)
        obj38.mass = 10
        obj38.hit([6950.228741776111, 44397.68056262229], obj38.position)

        def make_obj39(off_x, off_y, debug):
            print('Making ' + 'make_obj39' + '\n' +
                '#(struct:physical 39 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj39 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj39.color = Color('white')
            obj39.group = 39
            obj39_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj39.png')
            image_bindings.append([obj39, obj39_image])
            user_shapes.append(obj39)
            return obj39
        obj39 = make_obj39(0, 0, False)
        obj39.mass = 10
        obj39.hit([26735.006054137193, -1168.4781506293075], obj39.position)

        def make_obj40(off_x, off_y, debug):
            print('Making ' + 'make_obj40' + '\n' +
                '#(struct:physical 40 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj40 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj40.color = Color('white')
            obj40.group = 40
            obj40_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj40.png')
            image_bindings.append([obj40, obj40_image])
            user_shapes.append(obj40)
            return obj40
        obj40 = make_obj40(0, 0, False)
        obj40.mass = 10
        obj40.hit([46654.03429047186, 46797.61825453132], obj40.position)

        def make_obj42(off_x, off_y, debug):
            print('Making ' + 'make_obj42' + '\n' +
                '#(struct:physical 42 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj42 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj42.color = Color('white')
            obj42.group = 42
            obj42_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj42.png')
            image_bindings.append([obj42, obj42_image])
            user_shapes.append(obj42)
            return obj42
        obj42 = make_obj42(0, 0, False)
        obj42.mass = 10
        obj42.hit([-46898.85334925761, 21380.94351329755], obj42.position)

        def make_obj43(off_x, off_y, debug):
            print('Making ' + 'make_obj43' + '\n' +
                '#(struct:physical 43 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj43 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj43.color = Color('white')
            obj43.group = 43
            obj43_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj43.png')
            image_bindings.append([obj43, obj43_image])
            user_shapes.append(obj43)
            return obj43
        obj43 = make_obj43(0, 0, False)
        obj43.mass = 10
        obj43.hit([20102.36947827341, -6890.163927607726], obj43.position)

        def make_obj44(off_x, off_y, debug):
            print('Making ' + 'make_obj44' + '\n' +
                '#(struct:physical 44 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj44 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj44.color = Color('white')
            obj44.group = 44
            obj44_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj44.png')
            image_bindings.append([obj44, obj44_image])
            user_shapes.append(obj44)
            return obj44
        obj44 = make_obj44(0, 0, False)
        obj44.mass = 10
        obj44.hit([-34976.51006912675, -22628.081102539054], obj44.position)

        def make_obj45(off_x, off_y, debug):
            print('Making ' + 'make_obj45' + '\n' +
                '#(struct:physical 45 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj45 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj45.color = Color('white')
            obj45.group = 45
            obj45_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj45.png')
            image_bindings.append([obj45, obj45_image])
            user_shapes.append(obj45)
            return obj45
        obj45 = make_obj45(0, 0, False)
        obj45.mass = 10
        obj45.hit([-44317.59205601624, 5429.15552604579], obj45.position)
        _hy_anon_var_176 = deactivate(f)
    else:
        _hy_anon_var_176 = None
    return _hy_anon_var_176


space = obj25.body.space
ch = space.add_wildcard_collision_handler(obj25.collision_type)
ch.post_solve = on_collide_25
obj2.mass = 10
motor(obj2, 0)
obj2.gravity = 0, -100


def on_click_2(keys):
    global obj2
    f = obj2
    if not f or not f.body:
        return False
        _hy_anon_var_178 = None
    else:
        _hy_anon_var_178 = None
    p = f.body.position
    if mouse_clicked() and obj2.inside(mouse_point()) and obj2.active:

        def make_obj4(off_x, off_y, debug):
            print('Making ' + 'make_obj4' + '\n' +
                '#(struct:physical 4 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj4 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj4.color = Color('white')
            obj4.group = 4
            obj4_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj4.png')
            image_bindings.append([obj4, obj4_image])
            user_shapes.append(obj4)
            return obj4
        obj4 = make_obj4(0, 0, False)
        obj4.mass = 10
        obj4.hit([47373.16496987322, -20665.113790506417], obj4.position)

        def make_obj5(off_x, off_y, debug):
            print('Making ' + 'make_obj5' + '\n' +
                '#(struct:physical 5 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj5 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj5.color = Color('white')
            obj5.group = 5
            obj5_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj5.png')
            image_bindings.append([obj5, obj5_image])
            user_shapes.append(obj5)
            return obj5
        obj5 = make_obj5(0, 0, False)
        obj5.mass = 10
        obj5.hit([19823.802384396768, -12856.43167191599], obj5.position)

        def make_obj6(off_x, off_y, debug):
            print('Making ' + 'make_obj6' + '\n' +
                '#(struct:physical 6 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj6 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj6.color = Color('white')
            obj6.group = 6
            obj6_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj6.png')
            image_bindings.append([obj6, obj6_image])
            user_shapes.append(obj6)
            return obj6
        obj6 = make_obj6(0, 0, False)
        obj6.mass = 10
        obj6.hit([40523.00612181083, 3744.072508711157], obj6.position)

        def make_obj7(off_x, off_y, debug):
            print('Making ' + 'make_obj7' + '\n' +
                '#(struct:physical 7 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj7 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj7.color = Color('white')
            obj7.group = 7
            obj7_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj7.png')
            image_bindings.append([obj7, obj7_image])
            user_shapes.append(obj7)
            return obj7
        obj7 = make_obj7(0, 0, False)
        obj7.mass = 10
        obj7.hit([-15569.97761096697, 45210.848400335875], obj7.position)

        def make_obj9(off_x, off_y, debug):
            print('Making ' + 'make_obj9' + '\n' +
                '#(struct:physical 9 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj9 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj9.color = Color('white')
            obj9.group = 9
            obj9_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj9.png')
            image_bindings.append([obj9, obj9_image])
            user_shapes.append(obj9)
            return obj9
        obj9 = make_obj9(0, 0, False)
        obj9.mass = 10
        obj9.hit([7468.374668020282, 29758.006983824424], obj9.position)

        def make_obj10(off_x, off_y, debug):
            print('Making ' + 'make_obj10' + '\n' +
                '#(struct:physical 10 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj10 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj10.color = Color('white')
            obj10.group = 10
            obj10_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj10.png')
            image_bindings.append([obj10, obj10_image])
            user_shapes.append(obj10)
            return obj10
        obj10 = make_obj10(0, 0, False)
        obj10.mass = 10
        obj10.hit([13827.980676717125, 24535.563635499508], obj10.position)

        def make_obj11(off_x, off_y, debug):
            print('Making ' + 'make_obj11' + '\n' +
                '#(struct:physical 11 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj11 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj11.color = Color('white')
            obj11.group = 11
            obj11_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj11.png')
            image_bindings.append([obj11, obj11_image])
            user_shapes.append(obj11)
            return obj11
        obj11 = make_obj11(0, 0, False)
        obj11.mass = 10
        obj11.hit([28831.132477353225, -10561.454435061321], obj11.position)

        def make_obj12(off_x, off_y, debug):
            print('Making ' + 'make_obj12' + '\n' +
                '#(struct:physical 12 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj12 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj12.color = Color('white')
            obj12.group = 12
            obj12_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj12.png')
            image_bindings.append([obj12, obj12_image])
            user_shapes.append(obj12)
            return obj12
        obj12 = make_obj12(0, 0, False)
        obj12.mass = 10
        obj12.hit([32125.356346851724, -33656.90526567313], obj12.position)

        def make_obj14(off_x, off_y, debug):
            print('Making ' + 'make_obj14' + '\n' +
                '#(struct:physical 14 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj14 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj14.color = Color('white')
            obj14.group = 14
            obj14_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj14.png')
            image_bindings.append([obj14, obj14_image])
            user_shapes.append(obj14)
            return obj14
        obj14 = make_obj14(0, 0, False)
        obj14.mass = 10
        obj14.hit([-25698.69583131017, -239.37333603148727], obj14.position)

        def make_obj15(off_x, off_y, debug):
            print('Making ' + 'make_obj15' + '\n' +
                '#(struct:physical 15 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj15 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj15.color = Color('white')
            obj15.group = 15
            obj15_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj15.png')
            image_bindings.append([obj15, obj15_image])
            user_shapes.append(obj15)
            return obj15
        obj15 = make_obj15(0, 0, False)
        obj15.mass = 10
        obj15.hit([-7650.75010511931, -24489.711852245975], obj15.position)

        def make_obj16(off_x, off_y, debug):
            print('Making ' + 'make_obj16' + '\n' +
                '#(struct:physical 16 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj16 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj16.color = Color('white')
            obj16.group = 16
            obj16_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj16.png')
            image_bindings.append([obj16, obj16_image])
            user_shapes.append(obj16)
            return obj16
        obj16 = make_obj16(0, 0, False)
        obj16.mass = 10
        obj16.hit([-33137.12035131665, 14250.65467230422], obj16.position)

        def make_obj17(off_x, off_y, debug):
            print('Making ' + 'make_obj17' + '\n' +
                '#(struct:physical 17 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj17 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj17.color = Color('white')
            obj17.group = 17
            obj17_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj17.png')
            image_bindings.append([obj17, obj17_image])
            user_shapes.append(obj17)
            return obj17
        obj17 = make_obj17(0, 0, False)
        obj17.mass = 10
        obj17.hit([39384.21497398912, 35288.74957469756], obj17.position)

        def make_obj19(off_x, off_y, debug):
            print('Making ' + 'make_obj19' + '\n' +
                '#(struct:physical 19 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj19 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj19.color = Color('white')
            obj19.group = 19
            obj19_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj19.png')
            image_bindings.append([obj19, obj19_image])
            user_shapes.append(obj19)
            return obj19
        obj19 = make_obj19(0, 0, False)
        obj19.mass = 10
        obj19.hit([41165.38284867995, 40533.200705169176], obj19.position)

        def make_obj20(off_x, off_y, debug):
            print('Making ' + 'make_obj20' + '\n' +
                '#(struct:physical 20 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj20 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj20.color = Color('white')
            obj20.group = 20
            obj20_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj20.png')
            image_bindings.append([obj20, obj20_image])
            user_shapes.append(obj20)
            return obj20
        obj20 = make_obj20(0, 0, False)
        obj20.mass = 10
        obj20.hit([7054.211447778158, 30272.736865265586], obj20.position)

        def make_obj21(off_x, off_y, debug):
            print('Making ' + 'make_obj21' + '\n' +
                '#(struct:physical 21 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj21 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj21.color = Color('white')
            obj21.group = 21
            obj21_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj21.png')
            image_bindings.append([obj21, obj21_image])
            user_shapes.append(obj21)
            return obj21
        obj21 = make_obj21(0, 0, False)
        obj21.mass = 10
        obj21.hit([40636.34040121893, 3106.5961220702156], obj21.position)

        def make_obj22(off_x, off_y, debug):
            print('Making ' + 'make_obj22' + '\n' +
                '#(struct:physical 22 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj22 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj22.color = Color('white')
            obj22.group = 22
            obj22_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj22.png')
            image_bindings.append([obj22, obj22_image])
            user_shapes.append(obj22)
            return obj22
        obj22 = make_obj22(0, 0, False)
        obj22.mass = 10
        obj22.hit([-8867.336470728267, 25054.692735750257], obj22.position)
        deactivate(f)
        return True
        _hy_anon_var_195 = None
    else:
        _hy_anon_var_195 = None
    return _hy_anon_var_195


add_observer(on_click_2)


def on_collide_2(arbiter, space, data):
    f = obj2
    p = f.body.position
    friction = arbiter.friction
    restitution = arbiter.restitution
    total_impulse = arbiter.total_impulse
    energy_loss = arbiter.total_ke
    if friction > 0 and energy_loss > 50000000:

        def make_obj4(off_x, off_y, debug):
            print('Making ' + 'make_obj4' + '\n' +
                '#(struct:physical 4 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj4 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj4.color = Color('white')
            obj4.group = 4
            obj4_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj4.png')
            image_bindings.append([obj4, obj4_image])
            user_shapes.append(obj4)
            return obj4
        obj4 = make_obj4(0, 0, False)
        obj4.mass = 10
        obj4.hit([47373.16496987322, -20665.113790506417], obj4.position)

        def make_obj5(off_x, off_y, debug):
            print('Making ' + 'make_obj5' + '\n' +
                '#(struct:physical 5 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj5 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj5.color = Color('white')
            obj5.group = 5
            obj5_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj5.png')
            image_bindings.append([obj5, obj5_image])
            user_shapes.append(obj5)
            return obj5
        obj5 = make_obj5(0, 0, False)
        obj5.mass = 10
        obj5.hit([19823.802384396768, -12856.43167191599], obj5.position)

        def make_obj6(off_x, off_y, debug):
            print('Making ' + 'make_obj6' + '\n' +
                '#(struct:physical 6 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj6 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj6.color = Color('white')
            obj6.group = 6
            obj6_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj6.png')
            image_bindings.append([obj6, obj6_image])
            user_shapes.append(obj6)
            return obj6
        obj6 = make_obj6(0, 0, False)
        obj6.mass = 10
        obj6.hit([40523.00612181083, 3744.072508711157], obj6.position)

        def make_obj7(off_x, off_y, debug):
            print('Making ' + 'make_obj7' + '\n' +
                '#(struct:physical 7 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj7 = box([int(p.x + fraction(11, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj7.color = Color('white')
            obj7.group = 7
            obj7_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj7.png')
            image_bindings.append([obj7, obj7_image])
            user_shapes.append(obj7)
            return obj7
        obj7 = make_obj7(0, 0, False)
        obj7.mass = 10
        obj7.hit([-15569.97761096697, 45210.848400335875], obj7.position)

        def make_obj9(off_x, off_y, debug):
            print('Making ' + 'make_obj9' + '\n' +
                '#(struct:physical 9 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj9 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj9.color = Color('white')
            obj9.group = 9
            obj9_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj9.png')
            image_bindings.append([obj9, obj9_image])
            user_shapes.append(obj9)
            return obj9
        obj9 = make_obj9(0, 0, False)
        obj9.mass = 10
        obj9.hit([7468.374668020282, 29758.006983824424], obj9.position)

        def make_obj10(off_x, off_y, debug):
            print('Making ' + 'make_obj10' + '\n' +
                '#(struct:physical 10 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj10 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj10.color = Color('white')
            obj10.group = 10
            obj10_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj10.png')
            image_bindings.append([obj10, obj10_image])
            user_shapes.append(obj10)
            return obj10
        obj10 = make_obj10(0, 0, False)
        obj10.mass = 10
        obj10.hit([13827.980676717125, 24535.563635499508], obj10.position)

        def make_obj11(off_x, off_y, debug):
            print('Making ' + 'make_obj11' + '\n' +
                '#(struct:physical 11 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj11 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj11.color = Color('white')
            obj11.group = 11
            obj11_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj11.png')
            image_bindings.append([obj11, obj11_image])
            user_shapes.append(obj11)
            return obj11
        obj11 = make_obj11(0, 0, False)
        obj11.mass = 10
        obj11.hit([28831.132477353225, -10561.454435061321], obj11.position)

        def make_obj12(off_x, off_y, debug):
            print('Making ' + 'make_obj12' + '\n' +
                '#(struct:physical 12 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj12 = box([int(p.x + fraction(33, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj12.color = Color('white')
            obj12.group = 12
            obj12_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj12.png')
            image_bindings.append([obj12, obj12_image])
            user_shapes.append(obj12)
            return obj12
        obj12 = make_obj12(0, 0, False)
        obj12.mass = 10
        obj12.hit([32125.356346851724, -33656.90526567313], obj12.position)

        def make_obj14(off_x, off_y, debug):
            print('Making ' + 'make_obj14' + '\n' +
                '#(struct:physical 14 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj14 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj14.color = Color('white')
            obj14.group = 14
            obj14_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj14.png')
            image_bindings.append([obj14, obj14_image])
            user_shapes.append(obj14)
            return obj14
        obj14 = make_obj14(0, 0, False)
        obj14.mass = 10
        obj14.hit([-25698.69583131017, -239.37333603148727], obj14.position)

        def make_obj15(off_x, off_y, debug):
            print('Making ' + 'make_obj15' + '\n' +
                '#(struct:physical 15 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj15 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj15.color = Color('white')
            obj15.group = 15
            obj15_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj15.png')
            image_bindings.append([obj15, obj15_image])
            user_shapes.append(obj15)
            return obj15
        obj15 = make_obj15(0, 0, False)
        obj15.mass = 10
        obj15.hit([-7650.75010511931, -24489.711852245975], obj15.position)

        def make_obj16(off_x, off_y, debug):
            print('Making ' + 'make_obj16' + '\n' +
                '#(struct:physical 16 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj16 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj16.color = Color('white')
            obj16.group = 16
            obj16_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj16.png')
            image_bindings.append([obj16, obj16_image])
            user_shapes.append(obj16)
            return obj16
        obj16 = make_obj16(0, 0, False)
        obj16.mass = 10
        obj16.hit([-33137.12035131665, 14250.65467230422], obj16.position)

        def make_obj17(off_x, off_y, debug):
            print('Making ' + 'make_obj17' + '\n' +
                '#(struct:physical 17 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj17 = box([int(p.x + fraction(55, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj17.color = Color('white')
            obj17.group = 17
            obj17_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj17.png')
            image_bindings.append([obj17, obj17_image])
            user_shapes.append(obj17)
            return obj17
        obj17 = make_obj17(0, 0, False)
        obj17.mass = 10
        obj17.hit([39384.21497398912, 35288.74957469756], obj17.position)

        def make_obj19(off_x, off_y, debug):
            print('Making ' + 'make_obj19' + '\n' +
                '#(struct:physical 19 11/2 15/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj19 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(15, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj19.color = Color('white')
            obj19.group = 19
            obj19_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj19.png')
            image_bindings.append([obj19, obj19_image])
            user_shapes.append(obj19)
            return obj19
        obj19 = make_obj19(0, 0, False)
        obj19.mass = 10
        obj19.hit([41165.38284867995, 40533.200705169176], obj19.position)

        def make_obj20(off_x, off_y, debug):
            print('Making ' + 'make_obj20' + '\n' +
                '#(struct:physical 20 11/2 45/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj20 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(45, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj20.color = Color('white')
            obj20.group = 20
            obj20_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj20.png')
            image_bindings.append([obj20, obj20_image])
            user_shapes.append(obj20)
            return obj20
        obj20 = make_obj20(0, 0, False)
        obj20.mass = 10
        obj20.hit([7054.211447778158, 30272.736865265586], obj20.position)

        def make_obj21(off_x, off_y, debug):
            print('Making ' + 'make_obj21' + '\n' +
                '#(struct:physical 21 11/2 75/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj21 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(75, 2) + -30 - fraction(15, 
                2)) + int(off_y)], 11, 15)
            obj21.color = Color('white')
            obj21.group = 21
            obj21_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj21.png')
            image_bindings.append([obj21, obj21_image])
            user_shapes.append(obj21)
            return obj21
        obj21 = make_obj21(0, 0, False)
        obj21.mass = 10
        obj21.hit([40636.34040121893, 3106.5961220702156], obj21.position)

        def make_obj22(off_x, off_y, debug):
            print('Making ' + 'make_obj22' + '\n' +
                '#(struct:physical 22 11/2 105/2 (#<procedure:...ery/compiler.rkt:305:21> #<procedure:...ery/compiler.rkt:375:21>) #<box-collider> #(struct:object:image% ...) #t)'
                ) if debug else None
            obj22 = box([int(p.x + fraction(77, 2) + -22 - fraction(11, 2)) +
                int(off_x), int(p.y + fraction(105, 2) + -30 - fraction(15,
                2)) + int(off_y)], 11, 15)
            obj22.color = Color('white')
            obj22.group = 22
            obj22_image = pygame.image.load(
                '/Users/thoughtstem/Dev/Python/py-fizzery/obj22.png')
            image_bindings.append([obj22, obj22_image])
            user_shapes.append(obj22)
            return obj22
        obj22 = make_obj22(0, 0, False)
        obj22.mass = 10
        obj22.hit([-8867.336470728267, 25054.692735750257], obj22.position)
        _hy_anon_var_213 = deactivate(f)
    else:
        _hy_anon_var_213 = None
    return _hy_anon_var_213


space = obj2.body.space
ch = space.add_wildcard_collision_handler(obj2.collision_type)
ch.post_solve = on_collide_2


def image_for(s):
    global image_bindings
    for b in image_bindings:
        if b[0] == s:
            return b[1]
            _hy_anon_var_215 = None
        else:
            _hy_anon_var_215 = None
    return False


def draw_images(cosmetic):

    def f(keys):
        global user_shapes
        for s in user_shapes:
            if not image_for(s):
                continue
                _hy_anon_var_217 = None
            else:
                _hy_anon_var_217 = None
            if not cosmetic == s._cosmetic:
                continue
                _hy_anon_var_218 = None
            else:
                _hy_anon_var_218 = None
            if not s.active:
                continue
                _hy_anon_var_219 = None
            else:
                _hy_anon_var_219 = None
            if s.body:
                p = Vec2d(s.body.position.x, s.body.position.y)
                _hy_anon_var_220 = None
            else:
                p = Vec2d(s._x, s._y)
                _hy_anon_var_220 = None
            angle = 0
            if s.body:
                angle = s.body.angle
                _hy_anon_var_221 = None
            else:
                _hy_anon_var_221 = None
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
                _hy_anon_var_224 = None
            else:
                _hy_anon_var_224 = None
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
            _hy_anon_var_226 = None
        else:
            _hy_anon_var_226 = None
        screen = pygame.display.get_surface()
        pygame.draw.line(screen, Color('black'), start, end)


def test_ball(keys):
    if constants.K_b in keys:
        obj146 = ball([int(300) + int(off_x), +int(300), int(off_y)], 10)
        obj146.color = Color('white')
        obj146.group = 146
        obj146_image = pygame.image.load(
            '/Users/thoughtstem/Dev/Python/py-fizzery/obj146.png')
        image_bindings.append([obj146, obj146_image])
        user_shapes.append(obj146)
        _hy_anon_var_228 = obj146
    else:
        _hy_anon_var_228 = None
    return _hy_anon_var_228


add_observer(draw_images(True))
add_observer(draw_pivot_lines)
add_observer(draw_connection_lines)
add_observer(draw_images(False))
run()

