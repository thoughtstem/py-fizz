from hy.core.language import fraction
import sys
import math
import pymunk
from pyphysicssandbox import *
import pygame
from pyphysicssandbox import Vec2d
w = 520
h = 598
user_shapes = []
image_bindings = []
pivots = []
connected_shapes = []
click_handled = 2
window('Most Awesome Thing Ever', w, h)


def make_obj117(off_x, off_y):
    obj117 = static_box([int(260 - 260) + int(off_x), int(593 - 5) + int(
        off_y)], 520, 10)
    obj117.color = Color('white')
    obj117.group = 117
    obj117_image = pygame.image.load('./obj117.png')
    image_bindings.append([obj117, obj117_image])
    user_shapes.append(obj117)
    return obj117


obj117 = make_obj117(0, 0)


def make_obj119(off_x, off_y):
    obj119 = static_box([int(515 - 5) + int(off_x), int(299 - 289) + int(
        off_y)], 10, 578)
    obj119.color = Color('white')
    obj119.group = 119
    obj119_image = pygame.image.load('./obj119.png')
    image_bindings.append([obj119, obj119_image])
    user_shapes.append(obj119)
    return obj119


obj119 = make_obj119(0, 0)


def make_obj115(off_x, off_y):
    obj115 = cosmetic_ball([int(260) + int(off_x), +int(299), int(off_y)], 289)
    obj115.color = Color('white')
    obj115.group = 115
    obj115_image = pygame.image.load('./obj115.png')
    image_bindings.append([obj115, obj115_image])
    user_shapes.append(obj115)
    return obj115


obj115 = make_obj115(0, 0)


def make_obj105(off_x, off_y):
    obj105 = static_ball([int(260) + int(off_x), +int(537), int(off_y)], 1)
    obj105.color = Color('white')
    obj105.group = 105
    obj105_image = pygame.image.load('./obj105.png')
    image_bindings.append([obj105, obj105_image])
    user_shapes.append(obj105)
    return obj105


obj105 = make_obj105(0, 0)


def make_obj102(off_x, off_y):
    obj102 = box([int(260 - fraction(201, 2)) + int(off_x), int(fraction(
        1051, 2) - fraction(11, 2)) + int(off_y)], 201, 11)
    obj102.color = Color('white')
    obj102.group = 102
    obj102_image = pygame.image.load('./obj102.png')
    image_bindings.append([obj102, obj102_image])
    user_shapes.append(obj102)
    obj102.mass = 10
    return obj102


obj102 = make_obj102(0, 0)


def make_obj98(off_x, off_y):
    obj98 = cosmetic_ball([int(260) + int(off_x), +int(fraction(1051, 2)),
        int(off_y)], fraction(21, 2))
    obj98.color = Color('white')
    obj98.group = 98
    obj98_image = pygame.image.load('./obj98.png')
    image_bindings.append([obj98, obj98_image])
    user_shapes.append(obj98)
    global pivot98
    pivot98 = pivot((260, fraction(1051, 2)))
    pivots.append(pivot98)
    return obj98


obj98 = make_obj98(0, 0)


def make_obj2(off_x, off_y):
    obj2 = ball([int(335) + int(off_x), +int(495), int(off_y)], 20)
    obj2.color = Color('white')
    obj2.group = 2
    obj2_image = pygame.image.load('./obj2.png')
    image_bindings.append([obj2, obj2_image])
    user_shapes.append(obj2)
    obj2.mass = 10
    obj2.gravity = 0, 0
    return obj2


obj2 = make_obj2(0, 0)


def make_obj96(off_x, off_y):
    obj96 = cosmetic_ball([int(335) + int(off_x), +int(425), int(off_y)], 50)
    obj96.color = Color('white')
    obj96.group = 96
    obj96_image = pygame.image.load('./obj96.png')
    image_bindings.append([obj96, obj96_image])
    user_shapes.append(obj96)
    return obj96


obj96 = make_obj96(0, 0)


def make_obj1(off_x, off_y):
    obj1 = box([int(335 - 30) + int(off_x), int(345 - 30) + int(off_y)], 60, 60
        )
    obj1.color = Color('white')
    obj1.group = 1
    obj1_image = pygame.image.load('./obj1.png')
    image_bindings.append([obj1, obj1_image])
    user_shapes.append(obj1)
    obj1.mass = 10

    def on_collide_1(arbiter, space, data):
        f = obj1
        p = f.body.position
        friction = arbiter.friction
        restitution = arbiter.restitution
        total_impulse = arbiter.total_impulse
        energy_loss = arbiter.total_ke
        if friction > 0 and energy_loss > 0:

            def make_obj3(off_x, off_y):
                obj3 = box([int(p.x + fraction(15, 2) + -30 - fraction(15, 
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj3.color = Color('white')
                obj3.group = 3
                obj3_image = pygame.image.load('./obj3.png')
                image_bindings.append([obj3, obj3_image])
                user_shapes.append(obj3)
                obj3.mass = 10
                obj3.hit([6730.694160793071, 7194.535759385544], obj3.position)
                return obj3
            obj3 = make_obj3(0, 0)

            def make_obj4(off_x, off_y):
                obj4 = box([int(p.x + fraction(15, 2) + -30 - fraction(15, 
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj4.color = Color('white')
                obj4.group = 4
                obj4_image = pygame.image.load('./obj4.png')
                image_bindings.append([obj4, obj4_image])
                user_shapes.append(obj4)
                obj4.mass = 10
                obj4.hit([1606.960509495766, -41131.50577884009], obj4.position
                    )
                return obj4
            obj4 = make_obj4(0, 0)

            def make_obj5(off_x, off_y):
                obj5 = box([int(p.x + fraction(15, 2) + -30 - fraction(15, 
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj5.color = Color('white')
                obj5.group = 5
                obj5_image = pygame.image.load('./obj5.png')
                image_bindings.append([obj5, obj5_image])
                user_shapes.append(obj5)
                obj5.mass = 10
                obj5.hit([48820.35512817881, 4136.797939532902], obj5.position)
                return obj5
            obj5 = make_obj5(0, 0)

            def make_obj6(off_x, off_y):
                obj6 = box([int(p.x + fraction(15, 2) + -30 - fraction(15, 
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj6.color = Color('white')
                obj6.group = 6
                obj6_image = pygame.image.load('./obj6.png')
                image_bindings.append([obj6, obj6_image])
                user_shapes.append(obj6)
                obj6.mass = 10
                obj6.hit([24191.571034455395, 4300.6373323808875], obj6.
                    position)
                return obj6
            obj6 = make_obj6(0, 0)

            def make_obj8(off_x, off_y):
                obj8 = box([int(p.x + fraction(45, 2) + -30 - fraction(15, 
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj8.color = Color('white')
                obj8.group = 8
                obj8_image = pygame.image.load('./obj8.png')
                image_bindings.append([obj8, obj8_image])
                user_shapes.append(obj8)
                obj8.mass = 10
                obj8.hit([-30777.980667031363, -13189.95813920891], obj8.
                    position)
                return obj8
            obj8 = make_obj8(0, 0)

            def make_obj9(off_x, off_y):
                obj9 = box([int(p.x + fraction(45, 2) + -30 - fraction(15, 
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj9.color = Color('white')
                obj9.group = 9
                obj9_image = pygame.image.load('./obj9.png')
                image_bindings.append([obj9, obj9_image])
                user_shapes.append(obj9)
                obj9.mass = 10
                obj9.hit([9426.669883715767, 7974.526113528169], obj9.position)
                return obj9
            obj9 = make_obj9(0, 0)

            def make_obj10(off_x, off_y):
                obj10 = box([int(p.x + fraction(45, 2) + -30 - fraction(15,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj10.color = Color('white')
                obj10.group = 10
                obj10_image = pygame.image.load('./obj10.png')
                image_bindings.append([obj10, obj10_image])
                user_shapes.append(obj10)
                obj10.mass = 10
                obj10.hit([-9798.186118254132, 25953.89597080891], obj10.
                    position)
                return obj10
            obj10 = make_obj10(0, 0)

            def make_obj11(off_x, off_y):
                obj11 = box([int(p.x + fraction(45, 2) + -30 - fraction(15,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj11.color = Color('white')
                obj11.group = 11
                obj11_image = pygame.image.load('./obj11.png')
                image_bindings.append([obj11, obj11_image])
                user_shapes.append(obj11)
                obj11.mass = 10
                obj11.hit([-47608.039901236145, -27284.407633160423], obj11
                    .position)
                return obj11
            obj11 = make_obj11(0, 0)

            def make_obj13(off_x, off_y):
                obj13 = box([int(p.x + fraction(75, 2) + -30 - fraction(15,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj13.color = Color('white')
                obj13.group = 13
                obj13_image = pygame.image.load('./obj13.png')
                image_bindings.append([obj13, obj13_image])
                user_shapes.append(obj13)
                obj13.mass = 10
                obj13.hit([-11758.944542580393, 26021.840449548996], obj13.
                    position)
                return obj13
            obj13 = make_obj13(0, 0)

            def make_obj14(off_x, off_y):
                obj14 = box([int(p.x + fraction(75, 2) + -30 - fraction(15,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj14.color = Color('white')
                obj14.group = 14
                obj14_image = pygame.image.load('./obj14.png')
                image_bindings.append([obj14, obj14_image])
                user_shapes.append(obj14)
                obj14.mass = 10
                obj14.hit([31469.49167029334, -47316.45470993187], obj14.
                    position)
                return obj14
            obj14 = make_obj14(0, 0)

            def make_obj15(off_x, off_y):
                obj15 = box([int(p.x + fraction(75, 2) + -30 - fraction(15,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj15.color = Color('white')
                obj15.group = 15
                obj15_image = pygame.image.load('./obj15.png')
                image_bindings.append([obj15, obj15_image])
                user_shapes.append(obj15)
                obj15.mass = 10
                obj15.hit([-22861.67211253843, 35805.52852888357], obj15.
                    position)
                return obj15
            obj15 = make_obj15(0, 0)

            def make_obj16(off_x, off_y):
                obj16 = box([int(p.x + fraction(75, 2) + -30 - fraction(15,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj16.color = Color('white')
                obj16.group = 16
                obj16_image = pygame.image.load('./obj16.png')
                image_bindings.append([obj16, obj16_image])
                user_shapes.append(obj16)
                obj16.mass = 10
                obj16.hit([-27034.921786576444, -27481.544557065066], obj16
                    .position)
                return obj16
            obj16 = make_obj16(0, 0)

            def make_obj18(off_x, off_y):
                obj18 = box([int(p.x + fraction(105, 2) + -30 - fraction(15,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj18.color = Color('white')
                obj18.group = 18
                obj18_image = pygame.image.load('./obj18.png')
                image_bindings.append([obj18, obj18_image])
                user_shapes.append(obj18)
                obj18.mass = 10
                obj18.hit([-9263.31971463991, 43681.376796617726], obj18.
                    position)
                return obj18
            obj18 = make_obj18(0, 0)

            def make_obj19(off_x, off_y):
                obj19 = box([int(p.x + fraction(105, 2) + -30 - fraction(15,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj19.color = Color('white')
                obj19.group = 19
                obj19_image = pygame.image.load('./obj19.png')
                image_bindings.append([obj19, obj19_image])
                user_shapes.append(obj19)
                obj19.mass = 10
                obj19.hit([23895.46441153079, 26167.186592420287], obj19.
                    position)
                return obj19
            obj19 = make_obj19(0, 0)

            def make_obj20(off_x, off_y):
                obj20 = box([int(p.x + fraction(105, 2) + -30 - fraction(15,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj20.color = Color('white')
                obj20.group = 20
                obj20_image = pygame.image.load('./obj20.png')
                image_bindings.append([obj20, obj20_image])
                user_shapes.append(obj20)
                obj20.mass = 10
                obj20.hit([36092.22136605113, -38401.47563896769], obj20.
                    position)
                return obj20
            obj20 = make_obj20(0, 0)

            def make_obj21(off_x, off_y):
                obj21 = box([int(p.x + fraction(105, 2) + -30 - fraction(15,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 15, 15)
                obj21.color = Color('white')
                obj21.group = 21
                obj21_image = pygame.image.load('./obj21.png')
                image_bindings.append([obj21, obj21_image])
                user_shapes.append(obj21)
                obj21.mass = 10
                obj21.hit([42111.36150620022, -20162.253708985812], obj21.
                    position)
                return obj21
            obj21 = make_obj21(0, 0)
            _hy_anon_var_25 = deactivate(f)
        else:
            _hy_anon_var_25 = None
        return _hy_anon_var_25
    space = obj1.body.space
    ch = space.add_wildcard_collision_handler(obj1.collision_type)
    ch.post_solve = on_collide_1
    return obj1


obj1 = make_obj1(0, 0)


def make_obj94(off_x, off_y):
    obj94 = cosmetic_ball([int(335) + int(off_x), +int(265), int(off_y)], 50)
    obj94.color = Color('white')
    obj94.group = 94
    obj94_image = pygame.image.load('./obj94.png')
    image_bindings.append([obj94, obj94_image])
    user_shapes.append(obj94)
    return obj94


obj94 = make_obj94(0, 0)


def make_obj70(off_x, off_y):
    obj70 = box([int(379 - 22) + int(off_x), int(185 - 30) + int(off_y)], 
        44, 60)
    obj70.color = Color('white')
    obj70.group = 70
    obj70_image = pygame.image.load('./obj70.png')
    image_bindings.append([obj70, obj70_image])
    user_shapes.append(obj70)
    obj70.mass = 10
    obj70.gravity = 0, -100

    def on_click_70(keys):
        global click_handled
        f = obj70
        if not f or not f.body:
            return False
            _hy_anon_var_29 = None
        else:
            _hy_anon_var_29 = None
        p = f.body.position
        if mouse_clicked() and obj70.inside(mouse_point()
            ) and obj70.active and click_handled == 0:

            def make_obj72(off_x, off_y):
                obj72 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj72.color = Color('white')
                obj72.group = 72
                obj72_image = pygame.image.load('./obj72.png')
                image_bindings.append([obj72, obj72_image])
                user_shapes.append(obj72)
                obj72.mass = 10
                obj72.hit([-0.17485956588545573, 0.1812217345447561], obj72
                    .position)
                return obj72
            obj72 = make_obj72(0, 0)

            def make_obj73(off_x, off_y):
                obj73 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj73.color = Color('white')
                obj73.group = 73
                obj73_image = pygame.image.load('./obj73.png')
                image_bindings.append([obj73, obj73_image])
                user_shapes.append(obj73)
                obj73.mass = 10
                obj73.hit([-0.14142894044453735, -0.2389216257016403],
                    obj73.position)
                return obj73
            obj73 = make_obj73(0, 0)

            def make_obj74(off_x, off_y):
                obj74 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj74.color = Color('white')
                obj74.group = 74
                obj74_image = pygame.image.load('./obj74.png')
                image_bindings.append([obj74, obj74_image])
                user_shapes.append(obj74)
                obj74.mass = 10
                obj74.hit([-0.1888010388404634, -0.14365234560791584],
                    obj74.position)
                return obj74
            obj74 = make_obj74(0, 0)

            def make_obj75(off_x, off_y):
                obj75 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj75.color = Color('white')
                obj75.group = 75
                obj75_image = pygame.image.load('./obj75.png')
                image_bindings.append([obj75, obj75_image])
                user_shapes.append(obj75)
                obj75.mass = 10
                obj75.hit([-0.13304312845528374, 0.018641684525057323],
                    obj75.position)
                return obj75
            obj75 = make_obj75(0, 0)

            def make_obj77(off_x, off_y):
                obj77 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj77.color = Color('white')
                obj77.group = 77
                obj77_image = pygame.image.load('./obj77.png')
                image_bindings.append([obj77, obj77_image])
                user_shapes.append(obj77)
                obj77.mass = 10
                obj77.hit([0.14776713720885215, -0.1805158496245967], obj77
                    .position)
                return obj77
            obj77 = make_obj77(0, 0)

            def make_obj78(off_x, off_y):
                obj78 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj78.color = Color('white')
                obj78.group = 78
                obj78_image = pygame.image.load('./obj78.png')
                image_bindings.append([obj78, obj78_image])
                user_shapes.append(obj78)
                obj78.mass = 10
                obj78.hit([-0.06821468278967169, 0.11808465422634229],
                    obj78.position)
                return obj78
            obj78 = make_obj78(0, 0)

            def make_obj79(off_x, off_y):
                obj79 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj79.color = Color('white')
                obj79.group = 79
                obj79_image = pygame.image.load('./obj79.png')
                image_bindings.append([obj79, obj79_image])
                user_shapes.append(obj79)
                obj79.mass = 10
                obj79.hit([0.043684547787156414, -0.07778507242428487],
                    obj79.position)
                return obj79
            obj79 = make_obj79(0, 0)

            def make_obj80(off_x, off_y):
                obj80 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj80.color = Color('white')
                obj80.group = 80
                obj80_image = pygame.image.load('./obj80.png')
                image_bindings.append([obj80, obj80_image])
                user_shapes.append(obj80)
                obj80.mass = 10
                obj80.hit([0.05100185892274295, 0.09939347502632134], obj80
                    .position)
                return obj80
            obj80 = make_obj80(0, 0)

            def make_obj82(off_x, off_y):
                obj82 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj82.color = Color('white')
                obj82.group = 82
                obj82_image = pygame.image.load('./obj82.png')
                image_bindings.append([obj82, obj82_image])
                user_shapes.append(obj82)
                obj82.mass = 10
                obj82.hit([0.07059765855882155, 0.14734468263287426], obj82
                    .position)
                return obj82
            obj82 = make_obj82(0, 0)

            def make_obj83(off_x, off_y):
                obj83 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj83.color = Color('white')
                obj83.group = 83
                obj83_image = pygame.image.load('./obj83.png')
                image_bindings.append([obj83, obj83_image])
                user_shapes.append(obj83)
                obj83.mass = 10
                obj83.hit([0.0880425797805322, 0.01784572906603843], obj83.
                    position)
                return obj83
            obj83 = make_obj83(0, 0)

            def make_obj84(off_x, off_y):
                obj84 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj84.color = Color('white')
                obj84.group = 84
                obj84_image = pygame.image.load('./obj84.png')
                image_bindings.append([obj84, obj84_image])
                user_shapes.append(obj84)
                obj84.mass = 10
                obj84.hit([0.21285470336996448, 0.04849181407743541], obj84
                    .position)
                return obj84
            obj84 = make_obj84(0, 0)

            def make_obj85(off_x, off_y):
                obj85 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj85.color = Color('white')
                obj85.group = 85
                obj85_image = pygame.image.load('./obj85.png')
                image_bindings.append([obj85, obj85_image])
                user_shapes.append(obj85)
                obj85.mass = 10
                obj85.hit([-0.026780956557588387, 0.05621990950166744],
                    obj85.position)
                return obj85
            obj85 = make_obj85(0, 0)

            def make_obj87(off_x, off_y):
                obj87 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj87.color = Color('white')
                obj87.group = 87
                obj87_image = pygame.image.load('./obj87.png')
                image_bindings.append([obj87, obj87_image])
                user_shapes.append(obj87)
                obj87.mass = 10
                obj87.hit([-0.20534033030522725, -0.03609117341855633],
                    obj87.position)
                return obj87
            obj87 = make_obj87(0, 0)

            def make_obj88(off_x, off_y):
                obj88 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj88.color = Color('white')
                obj88.group = 88
                obj88_image = pygame.image.load('./obj88.png')
                image_bindings.append([obj88, obj88_image])
                user_shapes.append(obj88)
                obj88.mass = 10
                obj88.hit([0.17622270543461732, -0.18778566307374694],
                    obj88.position)
                return obj88
            obj88 = make_obj88(0, 0)

            def make_obj89(off_x, off_y):
                obj89 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj89.color = Color('white')
                obj89.group = 89
                obj89_image = pygame.image.load('./obj89.png')
                image_bindings.append([obj89, obj89_image])
                user_shapes.append(obj89)
                obj89.mass = 10
                obj89.hit([-0.1805229927526746, -0.04716526631041787],
                    obj89.position)
                return obj89
            obj89 = make_obj89(0, 0)

            def make_obj90(off_x, off_y):
                obj90 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj90.color = Color('white')
                obj90.group = 90
                obj90_image = pygame.image.load('./obj90.png')
                image_bindings.append([obj90, obj90_image])
                user_shapes.append(obj90)
                obj90.mass = 10
                obj90.hit([0.008784700028416192, -0.04364314339537492],
                    obj90.position)
                return obj90
            obj90 = make_obj90(0, 0)
            deactivate(f)
            click_handled = 2
            return True
            _hy_anon_var_46 = None
        else:
            _hy_anon_var_46 = None
        return _hy_anon_var_46
    add_observer(on_click_70)

    def on_collide_70(arbiter, space, data):
        f = obj70
        p = f.body.position
        friction = arbiter.friction
        restitution = arbiter.restitution
        total_impulse = arbiter.total_impulse
        energy_loss = arbiter.total_ke
        if friction > 0 and energy_loss > 50000000:

            def make_obj72(off_x, off_y):
                obj72 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj72.color = Color('white')
                obj72.group = 72
                obj72_image = pygame.image.load('./obj72.png')
                image_bindings.append([obj72, obj72_image])
                user_shapes.append(obj72)
                obj72.mass = 10
                obj72.hit([-0.17485956588545573, 0.1812217345447561], obj72
                    .position)
                return obj72
            obj72 = make_obj72(0, 0)

            def make_obj73(off_x, off_y):
                obj73 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj73.color = Color('white')
                obj73.group = 73
                obj73_image = pygame.image.load('./obj73.png')
                image_bindings.append([obj73, obj73_image])
                user_shapes.append(obj73)
                obj73.mass = 10
                obj73.hit([-0.14142894044453735, -0.2389216257016403],
                    obj73.position)
                return obj73
            obj73 = make_obj73(0, 0)

            def make_obj74(off_x, off_y):
                obj74 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj74.color = Color('white')
                obj74.group = 74
                obj74_image = pygame.image.load('./obj74.png')
                image_bindings.append([obj74, obj74_image])
                user_shapes.append(obj74)
                obj74.mass = 10
                obj74.hit([-0.1888010388404634, -0.14365234560791584],
                    obj74.position)
                return obj74
            obj74 = make_obj74(0, 0)

            def make_obj75(off_x, off_y):
                obj75 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj75.color = Color('white')
                obj75.group = 75
                obj75_image = pygame.image.load('./obj75.png')
                image_bindings.append([obj75, obj75_image])
                user_shapes.append(obj75)
                obj75.mass = 10
                obj75.hit([-0.13304312845528374, 0.018641684525057323],
                    obj75.position)
                return obj75
            obj75 = make_obj75(0, 0)

            def make_obj77(off_x, off_y):
                obj77 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj77.color = Color('white')
                obj77.group = 77
                obj77_image = pygame.image.load('./obj77.png')
                image_bindings.append([obj77, obj77_image])
                user_shapes.append(obj77)
                obj77.mass = 10
                obj77.hit([0.14776713720885215, -0.1805158496245967], obj77
                    .position)
                return obj77
            obj77 = make_obj77(0, 0)

            def make_obj78(off_x, off_y):
                obj78 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj78.color = Color('white')
                obj78.group = 78
                obj78_image = pygame.image.load('./obj78.png')
                image_bindings.append([obj78, obj78_image])
                user_shapes.append(obj78)
                obj78.mass = 10
                obj78.hit([-0.06821468278967169, 0.11808465422634229],
                    obj78.position)
                return obj78
            obj78 = make_obj78(0, 0)

            def make_obj79(off_x, off_y):
                obj79 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj79.color = Color('white')
                obj79.group = 79
                obj79_image = pygame.image.load('./obj79.png')
                image_bindings.append([obj79, obj79_image])
                user_shapes.append(obj79)
                obj79.mass = 10
                obj79.hit([0.043684547787156414, -0.07778507242428487],
                    obj79.position)
                return obj79
            obj79 = make_obj79(0, 0)

            def make_obj80(off_x, off_y):
                obj80 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj80.color = Color('white')
                obj80.group = 80
                obj80_image = pygame.image.load('./obj80.png')
                image_bindings.append([obj80, obj80_image])
                user_shapes.append(obj80)
                obj80.mass = 10
                obj80.hit([0.05100185892274295, 0.09939347502632134], obj80
                    .position)
                return obj80
            obj80 = make_obj80(0, 0)

            def make_obj82(off_x, off_y):
                obj82 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj82.color = Color('white')
                obj82.group = 82
                obj82_image = pygame.image.load('./obj82.png')
                image_bindings.append([obj82, obj82_image])
                user_shapes.append(obj82)
                obj82.mass = 10
                obj82.hit([0.07059765855882155, 0.14734468263287426], obj82
                    .position)
                return obj82
            obj82 = make_obj82(0, 0)

            def make_obj83(off_x, off_y):
                obj83 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj83.color = Color('white')
                obj83.group = 83
                obj83_image = pygame.image.load('./obj83.png')
                image_bindings.append([obj83, obj83_image])
                user_shapes.append(obj83)
                obj83.mass = 10
                obj83.hit([0.0880425797805322, 0.01784572906603843], obj83.
                    position)
                return obj83
            obj83 = make_obj83(0, 0)

            def make_obj84(off_x, off_y):
                obj84 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj84.color = Color('white')
                obj84.group = 84
                obj84_image = pygame.image.load('./obj84.png')
                image_bindings.append([obj84, obj84_image])
                user_shapes.append(obj84)
                obj84.mass = 10
                obj84.hit([0.21285470336996448, 0.04849181407743541], obj84
                    .position)
                return obj84
            obj84 = make_obj84(0, 0)

            def make_obj85(off_x, off_y):
                obj85 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj85.color = Color('white')
                obj85.group = 85
                obj85_image = pygame.image.load('./obj85.png')
                image_bindings.append([obj85, obj85_image])
                user_shapes.append(obj85)
                obj85.mass = 10
                obj85.hit([-0.026780956557588387, 0.05621990950166744],
                    obj85.position)
                return obj85
            obj85 = make_obj85(0, 0)

            def make_obj87(off_x, off_y):
                obj87 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj87.color = Color('white')
                obj87.group = 87
                obj87_image = pygame.image.load('./obj87.png')
                image_bindings.append([obj87, obj87_image])
                user_shapes.append(obj87)
                obj87.mass = 10
                obj87.hit([-0.20534033030522725, -0.03609117341855633],
                    obj87.position)
                return obj87
            obj87 = make_obj87(0, 0)

            def make_obj88(off_x, off_y):
                obj88 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj88.color = Color('white')
                obj88.group = 88
                obj88_image = pygame.image.load('./obj88.png')
                image_bindings.append([obj88, obj88_image])
                user_shapes.append(obj88)
                obj88.mass = 10
                obj88.hit([0.17622270543461732, -0.18778566307374694],
                    obj88.position)
                return obj88
            obj88 = make_obj88(0, 0)

            def make_obj89(off_x, off_y):
                obj89 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj89.color = Color('white')
                obj89.group = 89
                obj89_image = pygame.image.load('./obj89.png')
                image_bindings.append([obj89, obj89_image])
                user_shapes.append(obj89)
                obj89.mass = 10
                obj89.hit([-0.1805229927526746, -0.04716526631041787],
                    obj89.position)
                return obj89
            obj89 = make_obj89(0, 0)

            def make_obj90(off_x, off_y):
                obj90 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj90.color = Color('white')
                obj90.group = 90
                obj90_image = pygame.image.load('./obj90.png')
                image_bindings.append([obj90, obj90_image])
                user_shapes.append(obj90)
                obj90.mass = 10
                obj90.hit([0.008784700028416192, -0.04364314339537492],
                    obj90.position)
                return obj90
            obj90 = make_obj90(0, 0)
            _hy_anon_var_64 = deactivate(f)
        else:
            _hy_anon_var_64 = None
        return _hy_anon_var_64
    space = obj70.body.space
    ch = space.add_wildcard_collision_handler(obj70.collision_type)
    ch.post_solve = on_collide_70
    return obj70


obj70 = make_obj70(0, 0)


def make_obj47(off_x, off_y):
    obj47 = box([int(335 - 22) + int(off_x), int(185 - 30) + int(off_y)], 
        44, 60)
    obj47.color = Color('white')
    obj47.group = 47
    obj47_image = pygame.image.load('./obj47.png')
    image_bindings.append([obj47, obj47_image])
    user_shapes.append(obj47)
    obj47.mass = 10
    obj47.gravity = 0, -100

    def on_click_47(keys):
        global click_handled
        f = obj47
        if not f or not f.body:
            return False
            _hy_anon_var_67 = None
        else:
            _hy_anon_var_67 = None
        p = f.body.position
        if mouse_clicked() and obj47.inside(mouse_point()
            ) and obj47.active and click_handled == 0:

            def make_obj49(off_x, off_y):
                obj49 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj49.color = Color('white')
                obj49.group = 49
                obj49_image = pygame.image.load('./obj49.png')
                image_bindings.append([obj49, obj49_image])
                user_shapes.append(obj49)
                obj49.mass = 10
                obj49.hit([0.17484990061930833, -0.16906063355612844],
                    obj49.position)
                return obj49
            obj49 = make_obj49(0, 0)

            def make_obj50(off_x, off_y):
                obj50 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj50.color = Color('white')
                obj50.group = 50
                obj50_image = pygame.image.load('./obj50.png')
                image_bindings.append([obj50, obj50_image])
                user_shapes.append(obj50)
                obj50.mass = 10
                obj50.hit([-0.23306338756279663, 0.1755213314919819], obj50
                    .position)
                return obj50
            obj50 = make_obj50(0, 0)

            def make_obj51(off_x, off_y):
                obj51 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj51.color = Color('white')
                obj51.group = 51
                obj51_image = pygame.image.load('./obj51.png')
                image_bindings.append([obj51, obj51_image])
                user_shapes.append(obj51)
                obj51.mass = 10
                obj51.hit([-0.03147368297132802, 0.007143684077515811],
                    obj51.position)
                return obj51
            obj51 = make_obj51(0, 0)

            def make_obj52(off_x, off_y):
                obj52 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj52.color = Color('white')
                obj52.group = 52
                obj52_image = pygame.image.load('./obj52.png')
                image_bindings.append([obj52, obj52_image])
                user_shapes.append(obj52)
                obj52.mass = 10
                obj52.hit([-0.11465448428600392, -0.17749300306163368],
                    obj52.position)
                return obj52
            obj52 = make_obj52(0, 0)

            def make_obj54(off_x, off_y):
                obj54 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj54.color = Color('white')
                obj54.group = 54
                obj54_image = pygame.image.load('./obj54.png')
                image_bindings.append([obj54, obj54_image])
                user_shapes.append(obj54)
                obj54.mass = 10
                obj54.hit([-0.19474932644699233, -0.10935547348250133],
                    obj54.position)
                return obj54
            obj54 = make_obj54(0, 0)

            def make_obj55(off_x, off_y):
                obj55 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj55.color = Color('white')
                obj55.group = 55
                obj55_image = pygame.image.load('./obj55.png')
                image_bindings.append([obj55, obj55_image])
                user_shapes.append(obj55)
                obj55.mass = 10
                obj55.hit([0.1302398925390788, 0.14144018767856975], obj55.
                    position)
                return obj55
            obj55 = make_obj55(0, 0)

            def make_obj56(off_x, off_y):
                obj56 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj56.color = Color('white')
                obj56.group = 56
                obj56_image = pygame.image.load('./obj56.png')
                image_bindings.append([obj56, obj56_image])
                user_shapes.append(obj56)
                obj56.mass = 10
                obj56.hit([0.1748252509542863, -0.16586796438799625], obj56
                    .position)
                return obj56
            obj56 = make_obj56(0, 0)

            def make_obj57(off_x, off_y):
                obj57 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj57.color = Color('white')
                obj57.group = 57
                obj57_image = pygame.image.load('./obj57.png')
                image_bindings.append([obj57, obj57_image])
                user_shapes.append(obj57)
                obj57.mass = 10
                obj57.hit([-0.20910205202950788, -0.08832679429835946],
                    obj57.position)
                return obj57
            obj57 = make_obj57(0, 0)

            def make_obj59(off_x, off_y):
                obj59 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj59.color = Color('white')
                obj59.group = 59
                obj59_image = pygame.image.load('./obj59.png')
                image_bindings.append([obj59, obj59_image])
                user_shapes.append(obj59)
                obj59.mass = 10
                obj59.hit([-0.07658570060269573, 0.13323211337259966],
                    obj59.position)
                return obj59
            obj59 = make_obj59(0, 0)

            def make_obj60(off_x, off_y):
                obj60 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj60.color = Color('white')
                obj60.group = 60
                obj60_image = pygame.image.load('./obj60.png')
                image_bindings.append([obj60, obj60_image])
                user_shapes.append(obj60)
                obj60.mass = 10
                obj60.hit([-0.23998791396559357, 0.11667842400938094],
                    obj60.position)
                return obj60
            obj60 = make_obj60(0, 0)

            def make_obj61(off_x, off_y):
                obj61 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj61.color = Color('white')
                obj61.group = 61
                obj61_image = pygame.image.load('./obj61.png')
                image_bindings.append([obj61, obj61_image])
                user_shapes.append(obj61)
                obj61.mass = 10
                obj61.hit([0.2024586794691639, -0.008639717892990728],
                    obj61.position)
                return obj61
            obj61 = make_obj61(0, 0)

            def make_obj62(off_x, off_y):
                obj62 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj62.color = Color('white')
                obj62.group = 62
                obj62_image = pygame.image.load('./obj62.png')
                image_bindings.append([obj62, obj62_image])
                user_shapes.append(obj62)
                obj62.mass = 10
                obj62.hit([-0.12702210303875555, 0.247845817136562], obj62.
                    position)
                return obj62
            obj62 = make_obj62(0, 0)

            def make_obj64(off_x, off_y):
                obj64 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj64.color = Color('white')
                obj64.group = 64
                obj64_image = pygame.image.load('./obj64.png')
                image_bindings.append([obj64, obj64_image])
                user_shapes.append(obj64)
                obj64.mass = 10
                obj64.hit([0.045732886067694156, -0.13250979293650875],
                    obj64.position)
                return obj64
            obj64 = make_obj64(0, 0)

            def make_obj65(off_x, off_y):
                obj65 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj65.color = Color('white')
                obj65.group = 65
                obj65_image = pygame.image.load('./obj65.png')
                image_bindings.append([obj65, obj65_image])
                user_shapes.append(obj65)
                obj65.mass = 10
                obj65.hit([-0.07342787326150518, 0.18407186395184788],
                    obj65.position)
                return obj65
            obj65 = make_obj65(0, 0)

            def make_obj66(off_x, off_y):
                obj66 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj66.color = Color('white')
                obj66.group = 66
                obj66_image = pygame.image.load('./obj66.png')
                image_bindings.append([obj66, obj66_image])
                user_shapes.append(obj66)
                obj66.mass = 10
                obj66.hit([0.18429740095368113, -0.2258783017710519], obj66
                    .position)
                return obj66
            obj66 = make_obj66(0, 0)

            def make_obj67(off_x, off_y):
                obj67 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj67.color = Color('white')
                obj67.group = 67
                obj67_image = pygame.image.load('./obj67.png')
                image_bindings.append([obj67, obj67_image])
                user_shapes.append(obj67)
                obj67.mass = 10
                obj67.hit([0.0715798226624269, -0.0859765170335573], obj67.
                    position)
                return obj67
            obj67 = make_obj67(0, 0)
            deactivate(f)
            click_handled = 2
            return True
            _hy_anon_var_84 = None
        else:
            _hy_anon_var_84 = None
        return _hy_anon_var_84
    add_observer(on_click_47)

    def on_collide_47(arbiter, space, data):
        f = obj47
        p = f.body.position
        friction = arbiter.friction
        restitution = arbiter.restitution
        total_impulse = arbiter.total_impulse
        energy_loss = arbiter.total_ke
        if friction > 0 and energy_loss > 50000000:

            def make_obj49(off_x, off_y):
                obj49 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj49.color = Color('white')
                obj49.group = 49
                obj49_image = pygame.image.load('./obj49.png')
                image_bindings.append([obj49, obj49_image])
                user_shapes.append(obj49)
                obj49.mass = 10
                obj49.hit([0.17484990061930833, -0.16906063355612844],
                    obj49.position)
                return obj49
            obj49 = make_obj49(0, 0)

            def make_obj50(off_x, off_y):
                obj50 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj50.color = Color('white')
                obj50.group = 50
                obj50_image = pygame.image.load('./obj50.png')
                image_bindings.append([obj50, obj50_image])
                user_shapes.append(obj50)
                obj50.mass = 10
                obj50.hit([-0.23306338756279663, 0.1755213314919819], obj50
                    .position)
                return obj50
            obj50 = make_obj50(0, 0)

            def make_obj51(off_x, off_y):
                obj51 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj51.color = Color('white')
                obj51.group = 51
                obj51_image = pygame.image.load('./obj51.png')
                image_bindings.append([obj51, obj51_image])
                user_shapes.append(obj51)
                obj51.mass = 10
                obj51.hit([-0.03147368297132802, 0.007143684077515811],
                    obj51.position)
                return obj51
            obj51 = make_obj51(0, 0)

            def make_obj52(off_x, off_y):
                obj52 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj52.color = Color('white')
                obj52.group = 52
                obj52_image = pygame.image.load('./obj52.png')
                image_bindings.append([obj52, obj52_image])
                user_shapes.append(obj52)
                obj52.mass = 10
                obj52.hit([-0.11465448428600392, -0.17749300306163368],
                    obj52.position)
                return obj52
            obj52 = make_obj52(0, 0)

            def make_obj54(off_x, off_y):
                obj54 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj54.color = Color('white')
                obj54.group = 54
                obj54_image = pygame.image.load('./obj54.png')
                image_bindings.append([obj54, obj54_image])
                user_shapes.append(obj54)
                obj54.mass = 10
                obj54.hit([-0.19474932644699233, -0.10935547348250133],
                    obj54.position)
                return obj54
            obj54 = make_obj54(0, 0)

            def make_obj55(off_x, off_y):
                obj55 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj55.color = Color('white')
                obj55.group = 55
                obj55_image = pygame.image.load('./obj55.png')
                image_bindings.append([obj55, obj55_image])
                user_shapes.append(obj55)
                obj55.mass = 10
                obj55.hit([0.1302398925390788, 0.14144018767856975], obj55.
                    position)
                return obj55
            obj55 = make_obj55(0, 0)

            def make_obj56(off_x, off_y):
                obj56 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj56.color = Color('white')
                obj56.group = 56
                obj56_image = pygame.image.load('./obj56.png')
                image_bindings.append([obj56, obj56_image])
                user_shapes.append(obj56)
                obj56.mass = 10
                obj56.hit([0.1748252509542863, -0.16586796438799625], obj56
                    .position)
                return obj56
            obj56 = make_obj56(0, 0)

            def make_obj57(off_x, off_y):
                obj57 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj57.color = Color('white')
                obj57.group = 57
                obj57_image = pygame.image.load('./obj57.png')
                image_bindings.append([obj57, obj57_image])
                user_shapes.append(obj57)
                obj57.mass = 10
                obj57.hit([-0.20910205202950788, -0.08832679429835946],
                    obj57.position)
                return obj57
            obj57 = make_obj57(0, 0)

            def make_obj59(off_x, off_y):
                obj59 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj59.color = Color('white')
                obj59.group = 59
                obj59_image = pygame.image.load('./obj59.png')
                image_bindings.append([obj59, obj59_image])
                user_shapes.append(obj59)
                obj59.mass = 10
                obj59.hit([-0.07658570060269573, 0.13323211337259966],
                    obj59.position)
                return obj59
            obj59 = make_obj59(0, 0)

            def make_obj60(off_x, off_y):
                obj60 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj60.color = Color('white')
                obj60.group = 60
                obj60_image = pygame.image.load('./obj60.png')
                image_bindings.append([obj60, obj60_image])
                user_shapes.append(obj60)
                obj60.mass = 10
                obj60.hit([-0.23998791396559357, 0.11667842400938094],
                    obj60.position)
                return obj60
            obj60 = make_obj60(0, 0)

            def make_obj61(off_x, off_y):
                obj61 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj61.color = Color('white')
                obj61.group = 61
                obj61_image = pygame.image.load('./obj61.png')
                image_bindings.append([obj61, obj61_image])
                user_shapes.append(obj61)
                obj61.mass = 10
                obj61.hit([0.2024586794691639, -0.008639717892990728],
                    obj61.position)
                return obj61
            obj61 = make_obj61(0, 0)

            def make_obj62(off_x, off_y):
                obj62 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj62.color = Color('white')
                obj62.group = 62
                obj62_image = pygame.image.load('./obj62.png')
                image_bindings.append([obj62, obj62_image])
                user_shapes.append(obj62)
                obj62.mass = 10
                obj62.hit([-0.12702210303875555, 0.247845817136562], obj62.
                    position)
                return obj62
            obj62 = make_obj62(0, 0)

            def make_obj64(off_x, off_y):
                obj64 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj64.color = Color('white')
                obj64.group = 64
                obj64_image = pygame.image.load('./obj64.png')
                image_bindings.append([obj64, obj64_image])
                user_shapes.append(obj64)
                obj64.mass = 10
                obj64.hit([0.045732886067694156, -0.13250979293650875],
                    obj64.position)
                return obj64
            obj64 = make_obj64(0, 0)

            def make_obj65(off_x, off_y):
                obj65 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj65.color = Color('white')
                obj65.group = 65
                obj65_image = pygame.image.load('./obj65.png')
                image_bindings.append([obj65, obj65_image])
                user_shapes.append(obj65)
                obj65.mass = 10
                obj65.hit([-0.07342787326150518, 0.18407186395184788],
                    obj65.position)
                return obj65
            obj65 = make_obj65(0, 0)

            def make_obj66(off_x, off_y):
                obj66 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj66.color = Color('white')
                obj66.group = 66
                obj66_image = pygame.image.load('./obj66.png')
                image_bindings.append([obj66, obj66_image])
                user_shapes.append(obj66)
                obj66.mass = 10
                obj66.hit([0.18429740095368113, -0.2258783017710519], obj66
                    .position)
                return obj66
            obj66 = make_obj66(0, 0)

            def make_obj67(off_x, off_y):
                obj67 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj67.color = Color('white')
                obj67.group = 67
                obj67_image = pygame.image.load('./obj67.png')
                image_bindings.append([obj67, obj67_image])
                user_shapes.append(obj67)
                obj67.mass = 10
                obj67.hit([0.0715798226624269, -0.0859765170335573], obj67.
                    position)
                return obj67
            obj67 = make_obj67(0, 0)
            _hy_anon_var_102 = deactivate(f)
        else:
            _hy_anon_var_102 = None
        return _hy_anon_var_102
    space = obj47.body.space
    ch = space.add_wildcard_collision_handler(obj47.collision_type)
    ch.post_solve = on_collide_47
    return obj47


obj47 = make_obj47(0, 0)


def make_obj24(off_x, off_y):
    obj24 = box([int(291 - 22) + int(off_x), int(185 - 30) + int(off_y)], 
        44, 60)
    obj24.color = Color('white')
    obj24.group = 24
    obj24_image = pygame.image.load('./obj24.png')
    image_bindings.append([obj24, obj24_image])
    user_shapes.append(obj24)
    obj24.mass = 10
    obj24.gravity = 0, -100

    def on_click_24(keys):
        global click_handled
        f = obj24
        if not f or not f.body:
            return False
            _hy_anon_var_105 = None
        else:
            _hy_anon_var_105 = None
        p = f.body.position
        if mouse_clicked() and obj24.inside(mouse_point()
            ) and obj24.active and click_handled == 0:

            def make_obj26(off_x, off_y):
                obj26 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj26.color = Color('white')
                obj26.group = 26
                obj26_image = pygame.image.load('./obj26.png')
                image_bindings.append([obj26, obj26_image])
                user_shapes.append(obj26)
                obj26.mass = 10
                obj26.hit([-0.06712396185886674, 0.17733100286797826],
                    obj26.position)
                return obj26
            obj26 = make_obj26(0, 0)

            def make_obj27(off_x, off_y):
                obj27 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj27.color = Color('white')
                obj27.group = 27
                obj27_image = pygame.image.load('./obj27.png')
                image_bindings.append([obj27, obj27_image])
                user_shapes.append(obj27)
                obj27.mass = 10
                obj27.hit([0.08501236296318743, 0.03388351040141896], obj27
                    .position)
                return obj27
            obj27 = make_obj27(0, 0)

            def make_obj28(off_x, off_y):
                obj28 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj28.color = Color('white')
                obj28.group = 28
                obj28_image = pygame.image.load('./obj28.png')
                image_bindings.append([obj28, obj28_image])
                user_shapes.append(obj28)
                obj28.mass = 10
                obj28.hit([-0.16086747275209853, 0.23656167443954118],
                    obj28.position)
                return obj28
            obj28 = make_obj28(0, 0)

            def make_obj29(off_x, off_y):
                obj29 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj29.color = Color('white')
                obj29.group = 29
                obj29_image = pygame.image.load('./obj29.png')
                image_bindings.append([obj29, obj29_image])
                user_shapes.append(obj29)
                obj29.mass = 10
                obj29.hit([0.1779244923983455, -0.04499915064308402], obj29
                    .position)
                return obj29
            obj29 = make_obj29(0, 0)

            def make_obj31(off_x, off_y):
                obj31 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj31.color = Color('white')
                obj31.group = 31
                obj31_image = pygame.image.load('./obj31.png')
                image_bindings.append([obj31, obj31_image])
                user_shapes.append(obj31)
                obj31.mass = 10
                obj31.hit([0.04858903985156687, 0.10670794260111921], obj31
                    .position)
                return obj31
            obj31 = make_obj31(0, 0)

            def make_obj32(off_x, off_y):
                obj32 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj32.color = Color('white')
                obj32.group = 32
                obj32_image = pygame.image.load('./obj32.png')
                image_bindings.append([obj32, obj32_image])
                user_shapes.append(obj32)
                obj32.mass = 10
                obj32.hit([-0.03695696899365855, 0.10278667995697577],
                    obj32.position)
                return obj32
            obj32 = make_obj32(0, 0)

            def make_obj33(off_x, off_y):
                obj33 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj33.color = Color('white')
                obj33.group = 33
                obj33_image = pygame.image.load('./obj33.png')
                image_bindings.append([obj33, obj33_image])
                user_shapes.append(obj33)
                obj33.mass = 10
                obj33.hit([-0.0787471448721844, -0.15377047261788004],
                    obj33.position)
                return obj33
            obj33 = make_obj33(0, 0)

            def make_obj34(off_x, off_y):
                obj34 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj34.color = Color('white')
                obj34.group = 34
                obj34_image = pygame.image.load('./obj34.png')
                image_bindings.append([obj34, obj34_image])
                user_shapes.append(obj34)
                obj34.mass = 10
                obj34.hit([0.20547819864923728, -0.16618779210072493],
                    obj34.position)
                return obj34
            obj34 = make_obj34(0, 0)

            def make_obj36(off_x, off_y):
                obj36 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj36.color = Color('white')
                obj36.group = 36
                obj36_image = pygame.image.load('./obj36.png')
                image_bindings.append([obj36, obj36_image])
                user_shapes.append(obj36)
                obj36.mass = 10
                obj36.hit([0.17757392591689175, 0.2034745775914547], obj36.
                    position)
                return obj36
            obj36 = make_obj36(0, 0)

            def make_obj37(off_x, off_y):
                obj37 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj37.color = Color('white')
                obj37.group = 37
                obj37_image = pygame.image.load('./obj37.png')
                image_bindings.append([obj37, obj37_image])
                user_shapes.append(obj37)
                obj37.mass = 10
                obj37.hit([-0.12387265562208191, 0.2262745377526395], obj37
                    .position)
                return obj37
            obj37 = make_obj37(0, 0)

            def make_obj38(off_x, off_y):
                obj38 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj38.color = Color('white')
                obj38.group = 38
                obj38_image = pygame.image.load('./obj38.png')
                image_bindings.append([obj38, obj38_image])
                user_shapes.append(obj38)
                obj38.mass = 10
                obj38.hit([0.10899638446775456, 0.20305945869450637], obj38
                    .position)
                return obj38
            obj38 = make_obj38(0, 0)

            def make_obj39(off_x, off_y):
                obj39 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj39.color = Color('white')
                obj39.group = 39
                obj39_image = pygame.image.load('./obj39.png')
                image_bindings.append([obj39, obj39_image])
                user_shapes.append(obj39)
                obj39.mass = 10
                obj39.hit([-0.03167532456304584, 0.203829279494586], obj39.
                    position)
                return obj39
            obj39 = make_obj39(0, 0)

            def make_obj41(off_x, off_y):
                obj41 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj41.color = Color('white')
                obj41.group = 41
                obj41_image = pygame.image.load('./obj41.png')
                image_bindings.append([obj41, obj41_image])
                user_shapes.append(obj41)
                obj41.mass = 10
                obj41.hit([-0.11809339049817649, 0.007665305653210663],
                    obj41.position)
                return obj41
            obj41 = make_obj41(0, 0)

            def make_obj42(off_x, off_y):
                obj42 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj42.color = Color('white')
                obj42.group = 42
                obj42_image = pygame.image.load('./obj42.png')
                image_bindings.append([obj42, obj42_image])
                user_shapes.append(obj42)
                obj42.mass = 10
                obj42.hit([0.06415129833469868, -0.04767424541438067],
                    obj42.position)
                return obj42
            obj42 = make_obj42(0, 0)

            def make_obj43(off_x, off_y):
                obj43 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj43.color = Color('white')
                obj43.group = 43
                obj43_image = pygame.image.load('./obj43.png')
                image_bindings.append([obj43, obj43_image])
                user_shapes.append(obj43)
                obj43.mass = 10
                obj43.hit([0.13916840240057277, 0.10276367291222421], obj43
                    .position)
                return obj43
            obj43 = make_obj43(0, 0)

            def make_obj44(off_x, off_y):
                obj44 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj44.color = Color('white')
                obj44.group = 44
                obj44_image = pygame.image.load('./obj44.png')
                image_bindings.append([obj44, obj44_image])
                user_shapes.append(obj44)
                obj44.mass = 10
                obj44.hit([-0.12336230002328716, -0.1827529063477657],
                    obj44.position)
                return obj44
            obj44 = make_obj44(0, 0)
            deactivate(f)
            click_handled = 2
            return True
            _hy_anon_var_122 = None
        else:
            _hy_anon_var_122 = None
        return _hy_anon_var_122
    add_observer(on_click_24)

    def on_collide_24(arbiter, space, data):
        f = obj24
        p = f.body.position
        friction = arbiter.friction
        restitution = arbiter.restitution
        total_impulse = arbiter.total_impulse
        energy_loss = arbiter.total_ke
        if friction > 0 and energy_loss > 50000000:

            def make_obj26(off_x, off_y):
                obj26 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj26.color = Color('white')
                obj26.group = 26
                obj26_image = pygame.image.load('./obj26.png')
                image_bindings.append([obj26, obj26_image])
                user_shapes.append(obj26)
                obj26.mass = 10
                obj26.hit([-0.06712396185886674, 0.17733100286797826],
                    obj26.position)
                return obj26
            obj26 = make_obj26(0, 0)

            def make_obj27(off_x, off_y):
                obj27 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj27.color = Color('white')
                obj27.group = 27
                obj27_image = pygame.image.load('./obj27.png')
                image_bindings.append([obj27, obj27_image])
                user_shapes.append(obj27)
                obj27.mass = 10
                obj27.hit([0.08501236296318743, 0.03388351040141896], obj27
                    .position)
                return obj27
            obj27 = make_obj27(0, 0)

            def make_obj28(off_x, off_y):
                obj28 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj28.color = Color('white')
                obj28.group = 28
                obj28_image = pygame.image.load('./obj28.png')
                image_bindings.append([obj28, obj28_image])
                user_shapes.append(obj28)
                obj28.mass = 10
                obj28.hit([-0.16086747275209853, 0.23656167443954118],
                    obj28.position)
                return obj28
            obj28 = make_obj28(0, 0)

            def make_obj29(off_x, off_y):
                obj29 = box([int(p.x + fraction(11, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj29.color = Color('white')
                obj29.group = 29
                obj29_image = pygame.image.load('./obj29.png')
                image_bindings.append([obj29, obj29_image])
                user_shapes.append(obj29)
                obj29.mass = 10
                obj29.hit([0.1779244923983455, -0.04499915064308402], obj29
                    .position)
                return obj29
            obj29 = make_obj29(0, 0)

            def make_obj31(off_x, off_y):
                obj31 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj31.color = Color('white')
                obj31.group = 31
                obj31_image = pygame.image.load('./obj31.png')
                image_bindings.append([obj31, obj31_image])
                user_shapes.append(obj31)
                obj31.mass = 10
                obj31.hit([0.04858903985156687, 0.10670794260111921], obj31
                    .position)
                return obj31
            obj31 = make_obj31(0, 0)

            def make_obj32(off_x, off_y):
                obj32 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj32.color = Color('white')
                obj32.group = 32
                obj32_image = pygame.image.load('./obj32.png')
                image_bindings.append([obj32, obj32_image])
                user_shapes.append(obj32)
                obj32.mass = 10
                obj32.hit([-0.03695696899365855, 0.10278667995697577],
                    obj32.position)
                return obj32
            obj32 = make_obj32(0, 0)

            def make_obj33(off_x, off_y):
                obj33 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj33.color = Color('white')
                obj33.group = 33
                obj33_image = pygame.image.load('./obj33.png')
                image_bindings.append([obj33, obj33_image])
                user_shapes.append(obj33)
                obj33.mass = 10
                obj33.hit([-0.0787471448721844, -0.15377047261788004],
                    obj33.position)
                return obj33
            obj33 = make_obj33(0, 0)

            def make_obj34(off_x, off_y):
                obj34 = box([int(p.x + fraction(33, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj34.color = Color('white')
                obj34.group = 34
                obj34_image = pygame.image.load('./obj34.png')
                image_bindings.append([obj34, obj34_image])
                user_shapes.append(obj34)
                obj34.mass = 10
                obj34.hit([0.20547819864923728, -0.16618779210072493],
                    obj34.position)
                return obj34
            obj34 = make_obj34(0, 0)

            def make_obj36(off_x, off_y):
                obj36 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj36.color = Color('white')
                obj36.group = 36
                obj36_image = pygame.image.load('./obj36.png')
                image_bindings.append([obj36, obj36_image])
                user_shapes.append(obj36)
                obj36.mass = 10
                obj36.hit([0.17757392591689175, 0.2034745775914547], obj36.
                    position)
                return obj36
            obj36 = make_obj36(0, 0)

            def make_obj37(off_x, off_y):
                obj37 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj37.color = Color('white')
                obj37.group = 37
                obj37_image = pygame.image.load('./obj37.png')
                image_bindings.append([obj37, obj37_image])
                user_shapes.append(obj37)
                obj37.mass = 10
                obj37.hit([-0.12387265562208191, 0.2262745377526395], obj37
                    .position)
                return obj37
            obj37 = make_obj37(0, 0)

            def make_obj38(off_x, off_y):
                obj38 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj38.color = Color('white')
                obj38.group = 38
                obj38_image = pygame.image.load('./obj38.png')
                image_bindings.append([obj38, obj38_image])
                user_shapes.append(obj38)
                obj38.mass = 10
                obj38.hit([0.10899638446775456, 0.20305945869450637], obj38
                    .position)
                return obj38
            obj38 = make_obj38(0, 0)

            def make_obj39(off_x, off_y):
                obj39 = box([int(p.x + fraction(55, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj39.color = Color('white')
                obj39.group = 39
                obj39_image = pygame.image.load('./obj39.png')
                image_bindings.append([obj39, obj39_image])
                user_shapes.append(obj39)
                obj39.mass = 10
                obj39.hit([-0.03167532456304584, 0.203829279494586], obj39.
                    position)
                return obj39
            obj39 = make_obj39(0, 0)

            def make_obj41(off_x, off_y):
                obj41 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(15, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj41.color = Color('white')
                obj41.group = 41
                obj41_image = pygame.image.load('./obj41.png')
                image_bindings.append([obj41, obj41_image])
                user_shapes.append(obj41)
                obj41.mass = 10
                obj41.hit([-0.11809339049817649, 0.007665305653210663],
                    obj41.position)
                return obj41
            obj41 = make_obj41(0, 0)

            def make_obj42(off_x, off_y):
                obj42 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(45, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj42.color = Color('white')
                obj42.group = 42
                obj42_image = pygame.image.load('./obj42.png')
                image_bindings.append([obj42, obj42_image])
                user_shapes.append(obj42)
                obj42.mass = 10
                obj42.hit([0.06415129833469868, -0.04767424541438067],
                    obj42.position)
                return obj42
            obj42 = make_obj42(0, 0)

            def make_obj43(off_x, off_y):
                obj43 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(75, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj43.color = Color('white')
                obj43.group = 43
                obj43_image = pygame.image.load('./obj43.png')
                image_bindings.append([obj43, obj43_image])
                user_shapes.append(obj43)
                obj43.mass = 10
                obj43.hit([0.13916840240057277, 0.10276367291222421], obj43
                    .position)
                return obj43
            obj43 = make_obj43(0, 0)

            def make_obj44(off_x, off_y):
                obj44 = box([int(p.x + fraction(77, 2) + -22 - fraction(11,
                    2)) + int(off_x), int(p.y + fraction(105, 2) + -30 -
                    fraction(15, 2)) + int(off_y)], 11, 15)
                obj44.color = Color('white')
                obj44.group = 44
                obj44_image = pygame.image.load('./obj44.png')
                image_bindings.append([obj44, obj44_image])
                user_shapes.append(obj44)
                obj44.mass = 10
                obj44.hit([-0.12336230002328716, -0.1827529063477657],
                    obj44.position)
                return obj44
            obj44 = make_obj44(0, 0)
            _hy_anon_var_140 = deactivate(f)
        else:
            _hy_anon_var_140 = None
        return _hy_anon_var_140
    space = obj24.body.space
    ch = space.add_wildcard_collision_handler(obj24.collision_type)
    ch.post_solve = on_collide_24
    return obj24


obj24 = make_obj24(0, 0)


def make_obj111(off_x, off_y):
    obj111 = cosmetic_ball([int(194) + int(off_x), +int(335), int(off_y)], 75)
    obj111.color = Color('white')
    obj111.group = 111
    obj111_image = pygame.image.load('./obj111.png')
    image_bindings.append([obj111, obj111_image])
    user_shapes.append(obj111)
    return obj111


obj111 = make_obj111(0, 0)


def make_obj110(off_x, off_y):
    obj110 = cosmetic_ball([int(260) + int(off_x), +int(130), int(off_y)], 25)
    obj110.color = Color('white')
    obj110.group = 110
    obj110_image = pygame.image.load('./obj110.png')
    image_bindings.append([obj110, obj110_image])
    user_shapes.append(obj110)
    return obj110


obj110 = make_obj110(0, 0)


def make_obj108(off_x, off_y):
    obj108 = cosmetic_ball([int(fraction(565, 2)) + int(off_x), +int(
        fraction(165, 2)), int(off_y)], 75)
    obj108.color = Color('white')
    obj108.group = 108
    obj108_image = pygame.image.load('./obj108.png')
    image_bindings.append([obj108, obj108_image])
    user_shapes.append(obj108)
    return obj108


obj108 = make_obj108(0, 0)


def make_obj103(off_x, off_y):
    obj103 = ball([int(185) + int(off_x), +int(fraction(165, 2)), int(off_y
        )], fraction(45, 2))
    obj103.color = Color('white')
    obj103.group = 103
    obj103_image = pygame.image.load('./obj103.png')
    image_bindings.append([obj103, obj103_image])
    user_shapes.append(obj103)
    obj103.mass = 10000
    obj103.hit([0, 1500000], obj103.position)
    return obj103


obj103 = make_obj103(0, 0)


def make_obj119(off_x, off_y):
    obj119 = static_box([int(5 - 5) + int(off_x), int(299 - 289) + int(
        off_y)], 10, 578)
    obj119.color = Color('white')
    obj119.group = 119
    obj119_image = pygame.image.load('./obj119.png')
    image_bindings.append([obj119, obj119_image])
    user_shapes.append(obj119)
    return obj119


obj119 = make_obj119(0, 0)


def make_obj117(off_x, off_y):
    obj117 = static_box([int(260 - 260) + int(off_x), int(5 - 5) + int(
        off_y)], 520, 10)
    obj117.color = Color('white')
    obj117.group = 117
    obj117_image = pygame.image.load('./obj117.png')
    image_bindings.append([obj117, obj117_image])
    user_shapes.append(obj117)
    return obj117


obj117 = make_obj117(0, 0)
rotary_spring(obj105, obj102, 0, 100000000, 0)
pivot98.connect(obj102)
p = spring(obj1.body.position, obj1, obj24.body.position, obj24, 100, 20000,
    1000)
connected_shapes.append([obj1, obj24, p])
p = spring(obj1.body.position, obj1, obj47.body.position, obj47, 100, 20000,
    1000)
connected_shapes.append([obj1, obj47, p])
p = spring(obj1.body.position, obj1, obj70.body.position, obj70, 100, 20000,
    1000)
connected_shapes.append([obj1, obj70, p])


def image_for(s):
    global image_bindings
    for b in image_bindings:
        if b[0] == s:
            return b[1]
            _hy_anon_var_149 = None
        else:
            _hy_anon_var_149 = None
    return False


def draw_images(cosmetic):

    def f(keys):
        global user_shapes
        for s in user_shapes:
            if not image_for(s):
                continue
                _hy_anon_var_151 = None
            else:
                _hy_anon_var_151 = None
            if not cosmetic == s._cosmetic:
                continue
                _hy_anon_var_152 = None
            else:
                _hy_anon_var_152 = None
            if not s.active:
                continue
                _hy_anon_var_153 = None
            else:
                _hy_anon_var_153 = None
            if s.body:
                p = Vec2d(s.body.position.x, s.body.position.y)
                _hy_anon_var_154 = None
            else:
                p = Vec2d(s._x, s._y)
                _hy_anon_var_154 = None
            angle = 0
            if s.body:
                angle = s.body.angle
                _hy_anon_var_155 = None
            else:
                _hy_anon_var_155 = None
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
                _hy_anon_var_158 = None
            else:
                _hy_anon_var_158 = None
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
            _hy_anon_var_160 = None
        else:
            _hy_anon_var_160 = None
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

