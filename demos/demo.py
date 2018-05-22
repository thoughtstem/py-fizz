from hy.core.language import fraction
import sys
import math
import pymunk
from pyphysicssandbox import *
import pygame
from pyphysicssandbox import Vec2d
w = 766
h = 520
user_shapes = []
image_bindings = []
pivots = []
connected_shapes = []
click_handled = 2
window('Most Awesome Thing Ever', w, h)


def make_obj226(off_x, off_y):
    obj226 = static_box([int(383 - 383) + int(off_x), int(515 - 5) + int(
        off_y)], 766, 10)
    obj226.color = Color('white')
    obj226.group = 226
    obj226_image = pygame.image.load('./obj226.png')
    image_bindings.append([obj226, obj226_image])
    user_shapes.append(obj226)
    return obj226


obj226 = make_obj226(0, 0)


def make_obj228(off_x, off_y):
    obj228 = static_box([int(761 - 5) + int(off_x), int(260 - 250) + int(
        off_y)], 10, 500)
    obj228.color = Color('white')
    obj228.group = 228
    obj228_image = pygame.image.load('./obj228.png')
    image_bindings.append([obj228, obj228_image])
    user_shapes.append(obj228)
    return obj228


obj228 = make_obj228(0, 0)


def make_obj224(off_x, off_y):
    obj224 = cosmetic_ball([int(383) + int(off_x), +int(260), int(off_y)], 373)
    obj224.color = Color('white')
    obj224.group = 224
    obj224_image = pygame.image.load('./obj224.png')
    image_bindings.append([obj224, obj224_image])
    user_shapes.append(obj224)
    return obj224


obj224 = make_obj224(0, 0)


def make_obj219(off_x, off_y):
    obj219 = static_box([int(679 - 27) + int(off_x), int(260 - 31) + int(
        off_y)], 54, 62)
    obj219.color = Color('white')
    obj219.group = 219
    obj219_image = pygame.image.load('./obj219.png')
    image_bindings.append([obj219, obj219_image])
    user_shapes.append(obj219)

    def on_click_219(keys):
        global click_handled
        f = obj219
        if not f or not f.body:
            return False
            _hy_anon_var_4 = None
        else:
            _hy_anon_var_4 = None
        p = f.body.position
        if mouse_clicked() and obj219.inside(mouse_point()
            ) and obj219.active and click_handled == 0:

            def make_obj2(off_x, off_y):
                obj2 = box([int(p.x + 65 + -65 - 27) + int(off_x), int(p.y +
                    27 + fraction(-99, 2) - 27) + int(off_y)], 54, 54)
                obj2.color = Color('white')
                obj2.group = 2
                obj2_image = pygame.image.load('./obj2.png')
                image_bindings.append([obj2, obj2_image])
                user_shapes.append(obj2)

                def on_click_2(keys):
                    global click_handled
                    f = obj2
                    if not f or not f.body:
                        return False
                        _hy_anon_var_5 = None
                    else:
                        _hy_anon_var_5 = None
                    p = f.body.position
                    if mouse_clicked() and obj2.inside(mouse_point()
                        ) and obj2.active and click_handled == 0:

                        def make_obj1(off_x, off_y):
                            obj1 = box([int(p.x + 22 + -22 - 22) + int(
                                off_x), int(p.y + 30 + -30 - 30) + int(
                                off_y)], 44, 60)
                            obj1.color = Color('white')
                            obj1.group = 1
                            obj1_image = pygame.image.load('./obj1.png')
                            image_bindings.append([obj1, obj1_image])
                            user_shapes.append(obj1)
                            obj1.mass = 10
                            obj1.gravity = 0, -100
                            return obj1
                        obj1 = make_obj1(0, 0)
                        deactivate(f)
                        []
                        click_handled = 2
                        return True
                        _hy_anon_var_7 = None
                    else:
                        _hy_anon_var_7 = None
                    return _hy_anon_var_7
                add_observer(on_click_2)
                return obj2
            obj2 = make_obj2(0, 0)

            def make_obj214(off_x, off_y):
                obj214 = cosmetic_ball([int(p.x + 65 + -65) + int(off_x), +
                    int(p.y + fraction(113, 2) + fraction(-99, 2)), int(
                    off_y)], fraction(5, 2))
                obj214.color = Color('white')
                obj214.group = 214
                obj214_image = pygame.image.load('./obj214.png')
                image_bindings.append([obj214, obj214_image])
                user_shapes.append(obj214)
                return obj214
            obj214 = make_obj214(0, 0)

            def make_obj211(off_x, off_y):
                obj211 = ball([int(p.x + 20 + -65) + int(off_x), +int(p.y +
                    79 + fraction(-99, 2)), int(off_y)], 20)
                obj211.color = Color('white')
                obj211.group = 211
                obj211_image = pygame.image.load('./obj211.png')
                image_bindings.append([obj211, obj211_image])
                user_shapes.append(obj211)
                obj211.mass = 10
                obj211.elasticity = 1.0 * 0
                motor(obj211, 1)
                return obj211
            obj211 = make_obj211(0, 0)

            def make_obj215(off_x, off_y):
                obj215 = cosmetic_ball([int(p.x + fraction(85, 2) + -65) +
                    int(off_x), +int(p.y + 79 + fraction(-99, 2)), int(
                    off_y)], fraction(5, 2))
                obj215.color = Color('white')
                obj215.group = 215
                obj215_image = pygame.image.load('./obj215.png')
                image_bindings.append([obj215, obj215_image])
                user_shapes.append(obj215)
                return obj215
            obj215 = make_obj215(0, 0)

            def make_obj212(off_x, off_y):
                obj212 = ball([int(p.x + 65 + -65) + int(off_x), +int(p.y +
                    79 + fraction(-99, 2)), int(off_y)], 20)
                obj212.color = Color('white')
                obj212.group = 212
                obj212_image = pygame.image.load('./obj212.png')
                image_bindings.append([obj212, obj212_image])
                user_shapes.append(obj212)
                obj212.mass = 10
                obj212.elasticity = 1.0 * 0
                motor(obj212, 1)
                return obj212
            obj212 = make_obj212(0, 0)

            def make_obj216(off_x, off_y):
                obj216 = cosmetic_ball([int(p.x + fraction(175, 2) + -65) +
                    int(off_x), +int(p.y + 79 + fraction(-99, 2)), int(
                    off_y)], fraction(5, 2))
                obj216.color = Color('white')
                obj216.group = 216
                obj216_image = pygame.image.load('./obj216.png')
                image_bindings.append([obj216, obj216_image])
                user_shapes.append(obj216)
                return obj216
            obj216 = make_obj216(0, 0)

            def make_obj213(off_x, off_y):
                obj213 = ball([int(p.x + 110 + -65) + int(off_x), +int(p.y +
                    79 + fraction(-99, 2)), int(off_y)], 20)
                obj213.color = Color('white')
                obj213.group = 213
                obj213_image = pygame.image.load('./obj213.png')
                image_bindings.append([obj213, obj213_image])
                user_shapes.append(obj213)
                obj213.mass = 10
                obj213.elasticity = 1.0 * 0
                motor(obj213, 1)
                return obj213
            obj213 = make_obj213(0, 0)
            deactivate(f)
            p = pin(obj211.body.position, obj211, obj212.body.position, obj212)
            connected_shapes.append([obj211, obj212, p])
            p = pin(obj211.body.position, obj211, obj2.body.position, obj2)
            connected_shapes.append([obj211, obj2, p])
            p = pin(obj212.body.position, obj212, obj213.body.position, obj213)
            connected_shapes.append([obj212, obj213, p])
            p = pin(obj212.body.position, obj212, obj2.body.position, obj2)
            connected_shapes.append([obj212, obj2, p])
            p = pin(obj213.body.position, obj213, obj2.body.position, obj2)
            connected_shapes.append([obj213, obj2, p])
            click_handled = 2
            return True
            _hy_anon_var_16 = None
        else:
            _hy_anon_var_16 = None
        return _hy_anon_var_16
    add_observer(on_click_219)
    return obj219


obj219 = make_obj219(0, 0)


def make_obj210(off_x, off_y):
    obj210 = cosmetic_ball([int(552) + int(off_x), +int(260), int(off_y)], 100)
    obj210.color = Color('white')
    obj210.group = 210
    obj210_image = pygame.image.load('./obj210.png')
    image_bindings.append([obj210, obj210_image])
    user_shapes.append(obj210)
    return obj210


obj210 = make_obj210(0, 0)


def make_obj207(off_x, off_y):
    obj207 = static_box([int(421 - 31) + int(off_x), int(260 - 47) + int(
        off_y)], 62, 94)
    obj207.color = Color('white')
    obj207.group = 207
    obj207_image = pygame.image.load('./obj207.png')
    image_bindings.append([obj207, obj207_image])
    user_shapes.append(obj207)

    def on_click_207(keys):
        global click_handled
        f = obj207
        if not f or not f.body:
            return False
            _hy_anon_var_20 = None
        else:
            _hy_anon_var_20 = None
        p = f.body.position
        if mouse_clicked() and obj207.inside(mouse_point()
            ) and obj207.active and click_handled == 0:

            def make_obj5(off_x, off_y):
                obj5 = box([int(p.x + 22 + -154 - 22) + int(off_x), int(p.y +
                    30 + fraction(-259, 2) - 30) + int(off_y)], 44, 60)
                obj5.color = Color('white')
                obj5.group = 5
                obj5_image = pygame.image.load('./obj5.png')
                image_bindings.append([obj5, obj5_image])
                user_shapes.append(obj5)
                obj5.mass = 10
                obj5.gravity = 0, -100

                def on_click_5(keys):
                    global click_handled
                    f = obj5
                    if not f or not f.body:
                        return False
                        _hy_anon_var_21 = None
                    else:
                        _hy_anon_var_21 = None
                    p = f.body.position
                    if mouse_clicked() and obj5.inside(mouse_point()
                        ) and obj5.active and click_handled == 0:

                        def make_obj7(off_x, off_y):
                            obj7 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj7.color = Color('white')
                            obj7.group = 7
                            obj7_image = pygame.image.load('./obj7.png')
                            image_bindings.append([obj7, obj7_image])
                            user_shapes.append(obj7)
                            obj7.mass = 10
                            obj7.hit([-0.24275620700635273, 
                                0.16190398791246807], obj7.position)
                            return obj7
                        obj7 = make_obj7(0, 0)

                        def make_obj8(off_x, off_y):
                            obj8 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj8.color = Color('white')
                            obj8.group = 8
                            obj8_image = pygame.image.load('./obj8.png')
                            image_bindings.append([obj8, obj8_image])
                            user_shapes.append(obj8)
                            obj8.mass = 10
                            obj8.hit([-0.009403227701753197, 
                                0.05949280757329056], obj8.position)
                            return obj8
                        obj8 = make_obj8(0, 0)

                        def make_obj9(off_x, off_y):
                            obj9 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj9.color = Color('white')
                            obj9.group = 9
                            obj9_image = pygame.image.load('./obj9.png')
                            image_bindings.append([obj9, obj9_image])
                            user_shapes.append(obj9)
                            obj9.mass = 10
                            obj9.hit([0.12853325105619534, 
                                -0.21717488152728773], obj9.position)
                            return obj9
                        obj9 = make_obj9(0, 0)

                        def make_obj10(off_x, off_y):
                            obj10 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj10.color = Color('white')
                            obj10.group = 10
                            obj10_image = pygame.image.load('./obj10.png')
                            image_bindings.append([obj10, obj10_image])
                            user_shapes.append(obj10)
                            obj10.mass = 10
                            obj10.hit([0.10095419408717948, 
                                0.06668016602505805], obj10.position)
                            return obj10
                        obj10 = make_obj10(0, 0)

                        def make_obj12(off_x, off_y):
                            obj12 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj12.color = Color('white')
                            obj12.group = 12
                            obj12_image = pygame.image.load('./obj12.png')
                            image_bindings.append([obj12, obj12_image])
                            user_shapes.append(obj12)
                            obj12.mass = 10
                            obj12.hit([0.006123783130605465, 
                                -0.11606670791326909], obj12.position)
                            return obj12
                        obj12 = make_obj12(0, 0)

                        def make_obj13(off_x, off_y):
                            obj13 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj13.color = Color('white')
                            obj13.group = 13
                            obj13_image = pygame.image.load('./obj13.png')
                            image_bindings.append([obj13, obj13_image])
                            user_shapes.append(obj13)
                            obj13.mass = 10
                            obj13.hit([0.1458490417191295, 
                                0.024974597546904453], obj13.position)
                            return obj13
                        obj13 = make_obj13(0, 0)

                        def make_obj14(off_x, off_y):
                            obj14 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj14.color = Color('white')
                            obj14.group = 14
                            obj14_image = pygame.image.load('./obj14.png')
                            image_bindings.append([obj14, obj14_image])
                            user_shapes.append(obj14)
                            obj14.mass = 10
                            obj14.hit([0.0934388012241737, 
                                -0.05059319746759372], obj14.position)
                            return obj14
                        obj14 = make_obj14(0, 0)

                        def make_obj15(off_x, off_y):
                            obj15 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj15.color = Color('white')
                            obj15.group = 15
                            obj15_image = pygame.image.load('./obj15.png')
                            image_bindings.append([obj15, obj15_image])
                            user_shapes.append(obj15)
                            obj15.mass = 10
                            obj15.hit([0.16865365756209033, 
                                0.23993778459426468], obj15.position)
                            return obj15
                        obj15 = make_obj15(0, 0)

                        def make_obj17(off_x, off_y):
                            obj17 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj17.color = Color('white')
                            obj17.group = 17
                            obj17_image = pygame.image.load('./obj17.png')
                            image_bindings.append([obj17, obj17_image])
                            user_shapes.append(obj17)
                            obj17.mass = 10
                            obj17.hit([-0.19881602303444706, 
                                -0.04938902339733131], obj17.position)
                            return obj17
                        obj17 = make_obj17(0, 0)

                        def make_obj18(off_x, off_y):
                            obj18 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj18.color = Color('white')
                            obj18.group = 18
                            obj18_image = pygame.image.load('./obj18.png')
                            image_bindings.append([obj18, obj18_image])
                            user_shapes.append(obj18)
                            obj18.mass = 10
                            obj18.hit([-0.23972164347351105, 
                                0.24410920387010898], obj18.position)
                            return obj18
                        obj18 = make_obj18(0, 0)

                        def make_obj19(off_x, off_y):
                            obj19 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj19.color = Color('white')
                            obj19.group = 19
                            obj19_image = pygame.image.load('./obj19.png')
                            image_bindings.append([obj19, obj19_image])
                            user_shapes.append(obj19)
                            obj19.mass = 10
                            obj19.hit([-0.19774316882960943, 
                                -0.21822916364568892], obj19.position)
                            return obj19
                        obj19 = make_obj19(0, 0)

                        def make_obj20(off_x, off_y):
                            obj20 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj20.color = Color('white')
                            obj20.group = 20
                            obj20_image = pygame.image.load('./obj20.png')
                            image_bindings.append([obj20, obj20_image])
                            user_shapes.append(obj20)
                            obj20.mass = 10
                            obj20.hit([-0.12113929137051399, 
                                -0.10353123327589045], obj20.position)
                            return obj20
                        obj20 = make_obj20(0, 0)

                        def make_obj22(off_x, off_y):
                            obj22 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj22.color = Color('white')
                            obj22.group = 22
                            obj22_image = pygame.image.load('./obj22.png')
                            image_bindings.append([obj22, obj22_image])
                            user_shapes.append(obj22)
                            obj22.mass = 10
                            obj22.hit([0.23639700100072109, 
                                0.12073053131158246], obj22.position)
                            return obj22
                        obj22 = make_obj22(0, 0)

                        def make_obj23(off_x, off_y):
                            obj23 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj23.color = Color('white')
                            obj23.group = 23
                            obj23_image = pygame.image.load('./obj23.png')
                            image_bindings.append([obj23, obj23_image])
                            user_shapes.append(obj23)
                            obj23.mass = 10
                            obj23.hit([0.059646068002651986, 
                                0.13064131191312173], obj23.position)
                            return obj23
                        obj23 = make_obj23(0, 0)

                        def make_obj24(off_x, off_y):
                            obj24 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj24.color = Color('white')
                            obj24.group = 24
                            obj24_image = pygame.image.load('./obj24.png')
                            image_bindings.append([obj24, obj24_image])
                            user_shapes.append(obj24)
                            obj24.mass = 10
                            obj24.hit([0.04411681326485639, 
                                -0.23243756041559682], obj24.position)
                            return obj24
                        obj24 = make_obj24(0, 0)

                        def make_obj25(off_x, off_y):
                            obj25 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj25.color = Color('white')
                            obj25.group = 25
                            obj25_image = pygame.image.load('./obj25.png')
                            image_bindings.append([obj25, obj25_image])
                            user_shapes.append(obj25)
                            obj25.mass = 10
                            obj25.hit([-0.06743201404480703, 
                                -0.07783822894337392], obj25.position)
                            return obj25
                        obj25 = make_obj25(0, 0)
                        deactivate(f)
                        click_handled = 2
                        return True
                        _hy_anon_var_38 = None
                    else:
                        _hy_anon_var_38 = None
                    return _hy_anon_var_38
                add_observer(on_click_5)

                def on_collide_5(arbiter, space, data):
                    f = obj5
                    p = f.body.position
                    friction = arbiter.friction
                    restitution = arbiter.restitution
                    total_impulse = arbiter.total_impulse
                    energy_loss = arbiter.total_ke
                    if friction > 0 and energy_loss > 50000000:

                        def make_obj7(off_x, off_y):
                            obj7 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj7.color = Color('white')
                            obj7.group = 7
                            obj7_image = pygame.image.load('./obj7.png')
                            image_bindings.append([obj7, obj7_image])
                            user_shapes.append(obj7)
                            obj7.mass = 10
                            obj7.hit([-0.24275620700635273, 
                                0.16190398791246807], obj7.position)
                            return obj7
                        obj7 = make_obj7(0, 0)

                        def make_obj8(off_x, off_y):
                            obj8 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj8.color = Color('white')
                            obj8.group = 8
                            obj8_image = pygame.image.load('./obj8.png')
                            image_bindings.append([obj8, obj8_image])
                            user_shapes.append(obj8)
                            obj8.mass = 10
                            obj8.hit([-0.009403227701753197, 
                                0.05949280757329056], obj8.position)
                            return obj8
                        obj8 = make_obj8(0, 0)

                        def make_obj9(off_x, off_y):
                            obj9 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj9.color = Color('white')
                            obj9.group = 9
                            obj9_image = pygame.image.load('./obj9.png')
                            image_bindings.append([obj9, obj9_image])
                            user_shapes.append(obj9)
                            obj9.mass = 10
                            obj9.hit([0.12853325105619534, 
                                -0.21717488152728773], obj9.position)
                            return obj9
                        obj9 = make_obj9(0, 0)

                        def make_obj10(off_x, off_y):
                            obj10 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj10.color = Color('white')
                            obj10.group = 10
                            obj10_image = pygame.image.load('./obj10.png')
                            image_bindings.append([obj10, obj10_image])
                            user_shapes.append(obj10)
                            obj10.mass = 10
                            obj10.hit([0.10095419408717948, 
                                0.06668016602505805], obj10.position)
                            return obj10
                        obj10 = make_obj10(0, 0)

                        def make_obj12(off_x, off_y):
                            obj12 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj12.color = Color('white')
                            obj12.group = 12
                            obj12_image = pygame.image.load('./obj12.png')
                            image_bindings.append([obj12, obj12_image])
                            user_shapes.append(obj12)
                            obj12.mass = 10
                            obj12.hit([0.006123783130605465, 
                                -0.11606670791326909], obj12.position)
                            return obj12
                        obj12 = make_obj12(0, 0)

                        def make_obj13(off_x, off_y):
                            obj13 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj13.color = Color('white')
                            obj13.group = 13
                            obj13_image = pygame.image.load('./obj13.png')
                            image_bindings.append([obj13, obj13_image])
                            user_shapes.append(obj13)
                            obj13.mass = 10
                            obj13.hit([0.1458490417191295, 
                                0.024974597546904453], obj13.position)
                            return obj13
                        obj13 = make_obj13(0, 0)

                        def make_obj14(off_x, off_y):
                            obj14 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj14.color = Color('white')
                            obj14.group = 14
                            obj14_image = pygame.image.load('./obj14.png')
                            image_bindings.append([obj14, obj14_image])
                            user_shapes.append(obj14)
                            obj14.mass = 10
                            obj14.hit([0.0934388012241737, 
                                -0.05059319746759372], obj14.position)
                            return obj14
                        obj14 = make_obj14(0, 0)

                        def make_obj15(off_x, off_y):
                            obj15 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj15.color = Color('white')
                            obj15.group = 15
                            obj15_image = pygame.image.load('./obj15.png')
                            image_bindings.append([obj15, obj15_image])
                            user_shapes.append(obj15)
                            obj15.mass = 10
                            obj15.hit([0.16865365756209033, 
                                0.23993778459426468], obj15.position)
                            return obj15
                        obj15 = make_obj15(0, 0)

                        def make_obj17(off_x, off_y):
                            obj17 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj17.color = Color('white')
                            obj17.group = 17
                            obj17_image = pygame.image.load('./obj17.png')
                            image_bindings.append([obj17, obj17_image])
                            user_shapes.append(obj17)
                            obj17.mass = 10
                            obj17.hit([-0.19881602303444706, 
                                -0.04938902339733131], obj17.position)
                            return obj17
                        obj17 = make_obj17(0, 0)

                        def make_obj18(off_x, off_y):
                            obj18 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj18.color = Color('white')
                            obj18.group = 18
                            obj18_image = pygame.image.load('./obj18.png')
                            image_bindings.append([obj18, obj18_image])
                            user_shapes.append(obj18)
                            obj18.mass = 10
                            obj18.hit([-0.23972164347351105, 
                                0.24410920387010898], obj18.position)
                            return obj18
                        obj18 = make_obj18(0, 0)

                        def make_obj19(off_x, off_y):
                            obj19 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj19.color = Color('white')
                            obj19.group = 19
                            obj19_image = pygame.image.load('./obj19.png')
                            image_bindings.append([obj19, obj19_image])
                            user_shapes.append(obj19)
                            obj19.mass = 10
                            obj19.hit([-0.19774316882960943, 
                                -0.21822916364568892], obj19.position)
                            return obj19
                        obj19 = make_obj19(0, 0)

                        def make_obj20(off_x, off_y):
                            obj20 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj20.color = Color('white')
                            obj20.group = 20
                            obj20_image = pygame.image.load('./obj20.png')
                            image_bindings.append([obj20, obj20_image])
                            user_shapes.append(obj20)
                            obj20.mass = 10
                            obj20.hit([-0.12113929137051399, 
                                -0.10353123327589045], obj20.position)
                            return obj20
                        obj20 = make_obj20(0, 0)

                        def make_obj22(off_x, off_y):
                            obj22 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj22.color = Color('white')
                            obj22.group = 22
                            obj22_image = pygame.image.load('./obj22.png')
                            image_bindings.append([obj22, obj22_image])
                            user_shapes.append(obj22)
                            obj22.mass = 10
                            obj22.hit([0.23639700100072109, 
                                0.12073053131158246], obj22.position)
                            return obj22
                        obj22 = make_obj22(0, 0)

                        def make_obj23(off_x, off_y):
                            obj23 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj23.color = Color('white')
                            obj23.group = 23
                            obj23_image = pygame.image.load('./obj23.png')
                            image_bindings.append([obj23, obj23_image])
                            user_shapes.append(obj23)
                            obj23.mass = 10
                            obj23.hit([0.059646068002651986, 
                                0.13064131191312173], obj23.position)
                            return obj23
                        obj23 = make_obj23(0, 0)

                        def make_obj24(off_x, off_y):
                            obj24 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj24.color = Color('white')
                            obj24.group = 24
                            obj24_image = pygame.image.load('./obj24.png')
                            image_bindings.append([obj24, obj24_image])
                            user_shapes.append(obj24)
                            obj24.mass = 10
                            obj24.hit([0.04411681326485639, 
                                -0.23243756041559682], obj24.position)
                            return obj24
                        obj24 = make_obj24(0, 0)

                        def make_obj25(off_x, off_y):
                            obj25 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj25.color = Color('white')
                            obj25.group = 25
                            obj25_image = pygame.image.load('./obj25.png')
                            image_bindings.append([obj25, obj25_image])
                            user_shapes.append(obj25)
                            obj25.mass = 10
                            obj25.hit([-0.06743201404480703, 
                                -0.07783822894337392], obj25.position)
                            return obj25
                        obj25 = make_obj25(0, 0)
                        _hy_anon_var_56 = deactivate(f)
                    else:
                        _hy_anon_var_56 = None
                    return _hy_anon_var_56
                space = obj5.body.space
                ch = space.add_wildcard_collision_handler(obj5.collision_type)
                ch.post_solve = on_collide_5
                return obj5
            obj5 = make_obj5(0, 0)

            def make_obj28(off_x, off_y):
                obj28 = box([int(p.x + 66 + -154 - 22) + int(off_x), int(p.
                    y + 30 + fraction(-259, 2) - 30) + int(off_y)], 44, 60)
                obj28.color = Color('white')
                obj28.group = 28
                obj28_image = pygame.image.load('./obj28.png')
                image_bindings.append([obj28, obj28_image])
                user_shapes.append(obj28)
                obj28.mass = 10
                obj28.gravity = 0, -100

                def on_click_28(keys):
                    global click_handled
                    f = obj28
                    if not f or not f.body:
                        return False
                        _hy_anon_var_59 = None
                    else:
                        _hy_anon_var_59 = None
                    p = f.body.position
                    if mouse_clicked() and obj28.inside(mouse_point()
                        ) and obj28.active and click_handled == 0:

                        def make_obj30(off_x, off_y):
                            obj30 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj30.color = Color('white')
                            obj30.group = 30
                            obj30_image = pygame.image.load('./obj30.png')
                            image_bindings.append([obj30, obj30_image])
                            user_shapes.append(obj30)
                            obj30.mass = 10
                            obj30.hit([0.1404795529599644, 
                                0.17366689714200673], obj30.position)
                            return obj30
                        obj30 = make_obj30(0, 0)

                        def make_obj31(off_x, off_y):
                            obj31 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj31.color = Color('white')
                            obj31.group = 31
                            obj31_image = pygame.image.load('./obj31.png')
                            image_bindings.append([obj31, obj31_image])
                            user_shapes.append(obj31)
                            obj31.mass = 10
                            obj31.hit([-0.09066683714247822, 
                                0.15009427250353824], obj31.position)
                            return obj31
                        obj31 = make_obj31(0, 0)

                        def make_obj32(off_x, off_y):
                            obj32 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj32.color = Color('white')
                            obj32.group = 32
                            obj32_image = pygame.image.load('./obj32.png')
                            image_bindings.append([obj32, obj32_image])
                            user_shapes.append(obj32)
                            obj32.mass = 10
                            obj32.hit([-0.05906439369669972, 
                                -0.22217300702165474], obj32.position)
                            return obj32
                        obj32 = make_obj32(0, 0)

                        def make_obj33(off_x, off_y):
                            obj33 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj33.color = Color('white')
                            obj33.group = 33
                            obj33_image = pygame.image.load('./obj33.png')
                            image_bindings.append([obj33, obj33_image])
                            user_shapes.append(obj33)
                            obj33.mass = 10
                            obj33.hit([0.24415943789881733, 
                                -0.009835092827142039], obj33.position)
                            return obj33
                        obj33 = make_obj33(0, 0)

                        def make_obj35(off_x, off_y):
                            obj35 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj35.color = Color('white')
                            obj35.group = 35
                            obj35_image = pygame.image.load('./obj35.png')
                            image_bindings.append([obj35, obj35_image])
                            user_shapes.append(obj35)
                            obj35.mass = 10
                            obj35.hit([-0.10184138028021134, 
                                -0.18467874671639392], obj35.position)
                            return obj35
                        obj35 = make_obj35(0, 0)

                        def make_obj36(off_x, off_y):
                            obj36 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj36.color = Color('white')
                            obj36.group = 36
                            obj36_image = pygame.image.load('./obj36.png')
                            image_bindings.append([obj36, obj36_image])
                            user_shapes.append(obj36)
                            obj36.mass = 10
                            obj36.hit([-0.23298145759854075, 
                                0.13408594610865154], obj36.position)
                            return obj36
                        obj36 = make_obj36(0, 0)

                        def make_obj37(off_x, off_y):
                            obj37 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj37.color = Color('white')
                            obj37.group = 37
                            obj37_image = pygame.image.load('./obj37.png')
                            image_bindings.append([obj37, obj37_image])
                            user_shapes.append(obj37)
                            obj37.mass = 10
                            obj37.hit([0.10409714098838285, 
                                0.02431953338870385], obj37.position)
                            return obj37
                        obj37 = make_obj37(0, 0)

                        def make_obj38(off_x, off_y):
                            obj38 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj38.color = Color('white')
                            obj38.group = 38
                            obj38_image = pygame.image.load('./obj38.png')
                            image_bindings.append([obj38, obj38_image])
                            user_shapes.append(obj38)
                            obj38.mass = 10
                            obj38.hit([0.027378199318113194, 
                                -0.0912573120979408], obj38.position)
                            return obj38
                        obj38 = make_obj38(0, 0)

                        def make_obj40(off_x, off_y):
                            obj40 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj40.color = Color('white')
                            obj40.group = 40
                            obj40_image = pygame.image.load('./obj40.png')
                            image_bindings.append([obj40, obj40_image])
                            user_shapes.append(obj40)
                            obj40.mass = 10
                            obj40.hit([0.12583676881018285, 
                                0.22379302874881546], obj40.position)
                            return obj40
                        obj40 = make_obj40(0, 0)

                        def make_obj41(off_x, off_y):
                            obj41 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj41.color = Color('white')
                            obj41.group = 41
                            obj41_image = pygame.image.load('./obj41.png')
                            image_bindings.append([obj41, obj41_image])
                            user_shapes.append(obj41)
                            obj41.mass = 10
                            obj41.hit([0.13856509370299513, 
                                0.10118455091640044], obj41.position)
                            return obj41
                        obj41 = make_obj41(0, 0)

                        def make_obj42(off_x, off_y):
                            obj42 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj42.color = Color('white')
                            obj42.group = 42
                            obj42_image = pygame.image.load('./obj42.png')
                            image_bindings.append([obj42, obj42_image])
                            user_shapes.append(obj42)
                            obj42.mass = 10
                            obj42.hit([-0.09549722887189677, 
                                -0.02938624380909341], obj42.position)
                            return obj42
                        obj42 = make_obj42(0, 0)

                        def make_obj43(off_x, off_y):
                            obj43 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj43.color = Color('white')
                            obj43.group = 43
                            obj43_image = pygame.image.load('./obj43.png')
                            image_bindings.append([obj43, obj43_image])
                            user_shapes.append(obj43)
                            obj43.mass = 10
                            obj43.hit([-0.060381529750152985, 
                                -0.16961123405004308], obj43.position)
                            return obj43
                        obj43 = make_obj43(0, 0)

                        def make_obj45(off_x, off_y):
                            obj45 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj45.color = Color('white')
                            obj45.group = 45
                            obj45_image = pygame.image.load('./obj45.png')
                            image_bindings.append([obj45, obj45_image])
                            user_shapes.append(obj45)
                            obj45.mass = 10
                            obj45.hit([0.007502556676168892, 
                                0.16231312864952047], obj45.position)
                            return obj45
                        obj45 = make_obj45(0, 0)

                        def make_obj46(off_x, off_y):
                            obj46 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj46.color = Color('white')
                            obj46.group = 46
                            obj46_image = pygame.image.load('./obj46.png')
                            image_bindings.append([obj46, obj46_image])
                            user_shapes.append(obj46)
                            obj46.mass = 10
                            obj46.hit([-0.03245839575569756, 
                                -0.22493263643374395], obj46.position)
                            return obj46
                        obj46 = make_obj46(0, 0)

                        def make_obj47(off_x, off_y):
                            obj47 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj47.color = Color('white')
                            obj47.group = 47
                            obj47_image = pygame.image.load('./obj47.png')
                            image_bindings.append([obj47, obj47_image])
                            user_shapes.append(obj47)
                            obj47.mass = 10
                            obj47.hit([0.11773074615932894, 
                                -0.04248056009783327], obj47.position)
                            return obj47
                        obj47 = make_obj47(0, 0)

                        def make_obj48(off_x, off_y):
                            obj48 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj48.color = Color('white')
                            obj48.group = 48
                            obj48_image = pygame.image.load('./obj48.png')
                            image_bindings.append([obj48, obj48_image])
                            user_shapes.append(obj48)
                            obj48.mass = 10
                            obj48.hit([0.014812334110253844, 
                                -0.01598808887077552], obj48.position)
                            return obj48
                        obj48 = make_obj48(0, 0)
                        deactivate(f)
                        click_handled = 2
                        return True
                        _hy_anon_var_76 = None
                    else:
                        _hy_anon_var_76 = None
                    return _hy_anon_var_76
                add_observer(on_click_28)

                def on_collide_28(arbiter, space, data):
                    f = obj28
                    p = f.body.position
                    friction = arbiter.friction
                    restitution = arbiter.restitution
                    total_impulse = arbiter.total_impulse
                    energy_loss = arbiter.total_ke
                    if friction > 0 and energy_loss > 50000000:

                        def make_obj30(off_x, off_y):
                            obj30 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj30.color = Color('white')
                            obj30.group = 30
                            obj30_image = pygame.image.load('./obj30.png')
                            image_bindings.append([obj30, obj30_image])
                            user_shapes.append(obj30)
                            obj30.mass = 10
                            obj30.hit([0.1404795529599644, 
                                0.17366689714200673], obj30.position)
                            return obj30
                        obj30 = make_obj30(0, 0)

                        def make_obj31(off_x, off_y):
                            obj31 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj31.color = Color('white')
                            obj31.group = 31
                            obj31_image = pygame.image.load('./obj31.png')
                            image_bindings.append([obj31, obj31_image])
                            user_shapes.append(obj31)
                            obj31.mass = 10
                            obj31.hit([-0.09066683714247822, 
                                0.15009427250353824], obj31.position)
                            return obj31
                        obj31 = make_obj31(0, 0)

                        def make_obj32(off_x, off_y):
                            obj32 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj32.color = Color('white')
                            obj32.group = 32
                            obj32_image = pygame.image.load('./obj32.png')
                            image_bindings.append([obj32, obj32_image])
                            user_shapes.append(obj32)
                            obj32.mass = 10
                            obj32.hit([-0.05906439369669972, 
                                -0.22217300702165474], obj32.position)
                            return obj32
                        obj32 = make_obj32(0, 0)

                        def make_obj33(off_x, off_y):
                            obj33 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj33.color = Color('white')
                            obj33.group = 33
                            obj33_image = pygame.image.load('./obj33.png')
                            image_bindings.append([obj33, obj33_image])
                            user_shapes.append(obj33)
                            obj33.mass = 10
                            obj33.hit([0.24415943789881733, 
                                -0.009835092827142039], obj33.position)
                            return obj33
                        obj33 = make_obj33(0, 0)

                        def make_obj35(off_x, off_y):
                            obj35 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj35.color = Color('white')
                            obj35.group = 35
                            obj35_image = pygame.image.load('./obj35.png')
                            image_bindings.append([obj35, obj35_image])
                            user_shapes.append(obj35)
                            obj35.mass = 10
                            obj35.hit([-0.10184138028021134, 
                                -0.18467874671639392], obj35.position)
                            return obj35
                        obj35 = make_obj35(0, 0)

                        def make_obj36(off_x, off_y):
                            obj36 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj36.color = Color('white')
                            obj36.group = 36
                            obj36_image = pygame.image.load('./obj36.png')
                            image_bindings.append([obj36, obj36_image])
                            user_shapes.append(obj36)
                            obj36.mass = 10
                            obj36.hit([-0.23298145759854075, 
                                0.13408594610865154], obj36.position)
                            return obj36
                        obj36 = make_obj36(0, 0)

                        def make_obj37(off_x, off_y):
                            obj37 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj37.color = Color('white')
                            obj37.group = 37
                            obj37_image = pygame.image.load('./obj37.png')
                            image_bindings.append([obj37, obj37_image])
                            user_shapes.append(obj37)
                            obj37.mass = 10
                            obj37.hit([0.10409714098838285, 
                                0.02431953338870385], obj37.position)
                            return obj37
                        obj37 = make_obj37(0, 0)

                        def make_obj38(off_x, off_y):
                            obj38 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj38.color = Color('white')
                            obj38.group = 38
                            obj38_image = pygame.image.load('./obj38.png')
                            image_bindings.append([obj38, obj38_image])
                            user_shapes.append(obj38)
                            obj38.mass = 10
                            obj38.hit([0.027378199318113194, 
                                -0.0912573120979408], obj38.position)
                            return obj38
                        obj38 = make_obj38(0, 0)

                        def make_obj40(off_x, off_y):
                            obj40 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj40.color = Color('white')
                            obj40.group = 40
                            obj40_image = pygame.image.load('./obj40.png')
                            image_bindings.append([obj40, obj40_image])
                            user_shapes.append(obj40)
                            obj40.mass = 10
                            obj40.hit([0.12583676881018285, 
                                0.22379302874881546], obj40.position)
                            return obj40
                        obj40 = make_obj40(0, 0)

                        def make_obj41(off_x, off_y):
                            obj41 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj41.color = Color('white')
                            obj41.group = 41
                            obj41_image = pygame.image.load('./obj41.png')
                            image_bindings.append([obj41, obj41_image])
                            user_shapes.append(obj41)
                            obj41.mass = 10
                            obj41.hit([0.13856509370299513, 
                                0.10118455091640044], obj41.position)
                            return obj41
                        obj41 = make_obj41(0, 0)

                        def make_obj42(off_x, off_y):
                            obj42 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj42.color = Color('white')
                            obj42.group = 42
                            obj42_image = pygame.image.load('./obj42.png')
                            image_bindings.append([obj42, obj42_image])
                            user_shapes.append(obj42)
                            obj42.mass = 10
                            obj42.hit([-0.09549722887189677, 
                                -0.02938624380909341], obj42.position)
                            return obj42
                        obj42 = make_obj42(0, 0)

                        def make_obj43(off_x, off_y):
                            obj43 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj43.color = Color('white')
                            obj43.group = 43
                            obj43_image = pygame.image.load('./obj43.png')
                            image_bindings.append([obj43, obj43_image])
                            user_shapes.append(obj43)
                            obj43.mass = 10
                            obj43.hit([-0.060381529750152985, 
                                -0.16961123405004308], obj43.position)
                            return obj43
                        obj43 = make_obj43(0, 0)

                        def make_obj45(off_x, off_y):
                            obj45 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj45.color = Color('white')
                            obj45.group = 45
                            obj45_image = pygame.image.load('./obj45.png')
                            image_bindings.append([obj45, obj45_image])
                            user_shapes.append(obj45)
                            obj45.mass = 10
                            obj45.hit([0.007502556676168892, 
                                0.16231312864952047], obj45.position)
                            return obj45
                        obj45 = make_obj45(0, 0)

                        def make_obj46(off_x, off_y):
                            obj46 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj46.color = Color('white')
                            obj46.group = 46
                            obj46_image = pygame.image.load('./obj46.png')
                            image_bindings.append([obj46, obj46_image])
                            user_shapes.append(obj46)
                            obj46.mass = 10
                            obj46.hit([-0.03245839575569756, 
                                -0.22493263643374395], obj46.position)
                            return obj46
                        obj46 = make_obj46(0, 0)

                        def make_obj47(off_x, off_y):
                            obj47 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj47.color = Color('white')
                            obj47.group = 47
                            obj47_image = pygame.image.load('./obj47.png')
                            image_bindings.append([obj47, obj47_image])
                            user_shapes.append(obj47)
                            obj47.mass = 10
                            obj47.hit([0.11773074615932894, 
                                -0.04248056009783327], obj47.position)
                            return obj47
                        obj47 = make_obj47(0, 0)

                        def make_obj48(off_x, off_y):
                            obj48 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj48.color = Color('white')
                            obj48.group = 48
                            obj48_image = pygame.image.load('./obj48.png')
                            image_bindings.append([obj48, obj48_image])
                            user_shapes.append(obj48)
                            obj48.mass = 10
                            obj48.hit([0.014812334110253844, 
                                -0.01598808887077552], obj48.position)
                            return obj48
                        obj48 = make_obj48(0, 0)
                        _hy_anon_var_94 = deactivate(f)
                    else:
                        _hy_anon_var_94 = None
                    return _hy_anon_var_94
                space = obj28.body.space
                ch = space.add_wildcard_collision_handler(obj28.collision_type)
                ch.post_solve = on_collide_28
                return obj28
            obj28 = make_obj28(0, 0)

            def make_obj51(off_x, off_y):
                obj51 = box([int(p.x + 110 + -154 - 22) + int(off_x), int(p
                    .y + 30 + fraction(-259, 2) - 30) + int(off_y)], 44, 60)
                obj51.color = Color('white')
                obj51.group = 51
                obj51_image = pygame.image.load('./obj51.png')
                image_bindings.append([obj51, obj51_image])
                user_shapes.append(obj51)
                obj51.mass = 10
                obj51.gravity = 0, -100

                def on_click_51(keys):
                    global click_handled
                    f = obj51
                    if not f or not f.body:
                        return False
                        _hy_anon_var_97 = None
                    else:
                        _hy_anon_var_97 = None
                    p = f.body.position
                    if mouse_clicked() and obj51.inside(mouse_point()
                        ) and obj51.active and click_handled == 0:

                        def make_obj53(off_x, off_y):
                            obj53 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj53.color = Color('white')
                            obj53.group = 53
                            obj53_image = pygame.image.load('./obj53.png')
                            image_bindings.append([obj53, obj53_image])
                            user_shapes.append(obj53)
                            obj53.mass = 10
                            obj53.hit([0.007268302028953788, 
                                -0.16425084617551788], obj53.position)
                            return obj53
                        obj53 = make_obj53(0, 0)

                        def make_obj54(off_x, off_y):
                            obj54 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj54.color = Color('white')
                            obj54.group = 54
                            obj54_image = pygame.image.load('./obj54.png')
                            image_bindings.append([obj54, obj54_image])
                            user_shapes.append(obj54)
                            obj54.mass = 10
                            obj54.hit([-0.06248062162100551, 
                                -0.2368753682286657], obj54.position)
                            return obj54
                        obj54 = make_obj54(0, 0)

                        def make_obj55(off_x, off_y):
                            obj55 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj55.color = Color('white')
                            obj55.group = 55
                            obj55_image = pygame.image.load('./obj55.png')
                            image_bindings.append([obj55, obj55_image])
                            user_shapes.append(obj55)
                            obj55.mass = 10
                            obj55.hit([-0.0635396693172518, 
                                0.20940503386227582], obj55.position)
                            return obj55
                        obj55 = make_obj55(0, 0)

                        def make_obj56(off_x, off_y):
                            obj56 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj56.color = Color('white')
                            obj56.group = 56
                            obj56_image = pygame.image.load('./obj56.png')
                            image_bindings.append([obj56, obj56_image])
                            user_shapes.append(obj56)
                            obj56.mass = 10
                            obj56.hit([-0.2287340389044676, 
                                -0.22517858046040515], obj56.position)
                            return obj56
                        obj56 = make_obj56(0, 0)

                        def make_obj58(off_x, off_y):
                            obj58 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj58.color = Color('white')
                            obj58.group = 58
                            obj58_image = pygame.image.load('./obj58.png')
                            image_bindings.append([obj58, obj58_image])
                            user_shapes.append(obj58)
                            obj58.mass = 10
                            obj58.hit([0.1052891696803615, 
                                -0.11141281090068272], obj58.position)
                            return obj58
                        obj58 = make_obj58(0, 0)

                        def make_obj59(off_x, off_y):
                            obj59 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj59.color = Color('white')
                            obj59.group = 59
                            obj59_image = pygame.image.load('./obj59.png')
                            image_bindings.append([obj59, obj59_image])
                            user_shapes.append(obj59)
                            obj59.mass = 10
                            obj59.hit([0.16142791243665988, 
                                0.06726121960448422], obj59.position)
                            return obj59
                        obj59 = make_obj59(0, 0)

                        def make_obj60(off_x, off_y):
                            obj60 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj60.color = Color('white')
                            obj60.group = 60
                            obj60_image = pygame.image.load('./obj60.png')
                            image_bindings.append([obj60, obj60_image])
                            user_shapes.append(obj60)
                            obj60.mass = 10
                            obj60.hit([0.21811881879547484, 
                                0.20204359049095472], obj60.position)
                            return obj60
                        obj60 = make_obj60(0, 0)

                        def make_obj61(off_x, off_y):
                            obj61 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj61.color = Color('white')
                            obj61.group = 61
                            obj61_image = pygame.image.load('./obj61.png')
                            image_bindings.append([obj61, obj61_image])
                            user_shapes.append(obj61)
                            obj61.mass = 10
                            obj61.hit([-0.06756693067818914, 
                                -0.19691156059447784], obj61.position)
                            return obj61
                        obj61 = make_obj61(0, 0)

                        def make_obj63(off_x, off_y):
                            obj63 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj63.color = Color('white')
                            obj63.group = 63
                            obj63_image = pygame.image.load('./obj63.png')
                            image_bindings.append([obj63, obj63_image])
                            user_shapes.append(obj63)
                            obj63.mass = 10
                            obj63.hit([0.19653176385411225, 
                                0.22164394732144227], obj63.position)
                            return obj63
                        obj63 = make_obj63(0, 0)

                        def make_obj64(off_x, off_y):
                            obj64 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj64.color = Color('white')
                            obj64.group = 64
                            obj64_image = pygame.image.load('./obj64.png')
                            image_bindings.append([obj64, obj64_image])
                            user_shapes.append(obj64)
                            obj64.mass = 10
                            obj64.hit([-0.05348929695919474, 
                                0.14732747388633777], obj64.position)
                            return obj64
                        obj64 = make_obj64(0, 0)

                        def make_obj65(off_x, off_y):
                            obj65 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj65.color = Color('white')
                            obj65.group = 65
                            obj65_image = pygame.image.load('./obj65.png')
                            image_bindings.append([obj65, obj65_image])
                            user_shapes.append(obj65)
                            obj65.mass = 10
                            obj65.hit([0.08219828784867284, 
                                -0.015279189841372748], obj65.position)
                            return obj65
                        obj65 = make_obj65(0, 0)

                        def make_obj66(off_x, off_y):
                            obj66 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj66.color = Color('white')
                            obj66.group = 66
                            obj66_image = pygame.image.load('./obj66.png')
                            image_bindings.append([obj66, obj66_image])
                            user_shapes.append(obj66)
                            obj66.mass = 10
                            obj66.hit([-0.1333641234645009, 
                                -0.20870235152777497], obj66.position)
                            return obj66
                        obj66 = make_obj66(0, 0)

                        def make_obj68(off_x, off_y):
                            obj68 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj68.color = Color('white')
                            obj68.group = 68
                            obj68_image = pygame.image.load('./obj68.png')
                            image_bindings.append([obj68, obj68_image])
                            user_shapes.append(obj68)
                            obj68.mass = 10
                            obj68.hit([2.7267380075468584e-05, 
                                0.17911672574846987], obj68.position)
                            return obj68
                        obj68 = make_obj68(0, 0)

                        def make_obj69(off_x, off_y):
                            obj69 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj69.color = Color('white')
                            obj69.group = 69
                            obj69_image = pygame.image.load('./obj69.png')
                            image_bindings.append([obj69, obj69_image])
                            user_shapes.append(obj69)
                            obj69.mass = 10
                            obj69.hit([-0.15721400424384346, 
                                0.05741992102548099], obj69.position)
                            return obj69
                        obj69 = make_obj69(0, 0)

                        def make_obj70(off_x, off_y):
                            obj70 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj70.color = Color('white')
                            obj70.group = 70
                            obj70_image = pygame.image.load('./obj70.png')
                            image_bindings.append([obj70, obj70_image])
                            user_shapes.append(obj70)
                            obj70.mass = 10
                            obj70.hit([-0.14287103845672122, 
                                -0.03813338476040959], obj70.position)
                            return obj70
                        obj70 = make_obj70(0, 0)

                        def make_obj71(off_x, off_y):
                            obj71 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj71.color = Color('white')
                            obj71.group = 71
                            obj71_image = pygame.image.load('./obj71.png')
                            image_bindings.append([obj71, obj71_image])
                            user_shapes.append(obj71)
                            obj71.mass = 10
                            obj71.hit([0.06353749479535015, 
                                0.1373889065759472], obj71.position)
                            return obj71
                        obj71 = make_obj71(0, 0)
                        deactivate(f)
                        click_handled = 2
                        return True
                        _hy_anon_var_114 = None
                    else:
                        _hy_anon_var_114 = None
                    return _hy_anon_var_114
                add_observer(on_click_51)

                def on_collide_51(arbiter, space, data):
                    f = obj51
                    p = f.body.position
                    friction = arbiter.friction
                    restitution = arbiter.restitution
                    total_impulse = arbiter.total_impulse
                    energy_loss = arbiter.total_ke
                    if friction > 0 and energy_loss > 50000000:

                        def make_obj53(off_x, off_y):
                            obj53 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj53.color = Color('white')
                            obj53.group = 53
                            obj53_image = pygame.image.load('./obj53.png')
                            image_bindings.append([obj53, obj53_image])
                            user_shapes.append(obj53)
                            obj53.mass = 10
                            obj53.hit([0.007268302028953788, 
                                -0.16425084617551788], obj53.position)
                            return obj53
                        obj53 = make_obj53(0, 0)

                        def make_obj54(off_x, off_y):
                            obj54 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj54.color = Color('white')
                            obj54.group = 54
                            obj54_image = pygame.image.load('./obj54.png')
                            image_bindings.append([obj54, obj54_image])
                            user_shapes.append(obj54)
                            obj54.mass = 10
                            obj54.hit([-0.06248062162100551, 
                                -0.2368753682286657], obj54.position)
                            return obj54
                        obj54 = make_obj54(0, 0)

                        def make_obj55(off_x, off_y):
                            obj55 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj55.color = Color('white')
                            obj55.group = 55
                            obj55_image = pygame.image.load('./obj55.png')
                            image_bindings.append([obj55, obj55_image])
                            user_shapes.append(obj55)
                            obj55.mass = 10
                            obj55.hit([-0.0635396693172518, 
                                0.20940503386227582], obj55.position)
                            return obj55
                        obj55 = make_obj55(0, 0)

                        def make_obj56(off_x, off_y):
                            obj56 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj56.color = Color('white')
                            obj56.group = 56
                            obj56_image = pygame.image.load('./obj56.png')
                            image_bindings.append([obj56, obj56_image])
                            user_shapes.append(obj56)
                            obj56.mass = 10
                            obj56.hit([-0.2287340389044676, 
                                -0.22517858046040515], obj56.position)
                            return obj56
                        obj56 = make_obj56(0, 0)

                        def make_obj58(off_x, off_y):
                            obj58 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj58.color = Color('white')
                            obj58.group = 58
                            obj58_image = pygame.image.load('./obj58.png')
                            image_bindings.append([obj58, obj58_image])
                            user_shapes.append(obj58)
                            obj58.mass = 10
                            obj58.hit([0.1052891696803615, 
                                -0.11141281090068272], obj58.position)
                            return obj58
                        obj58 = make_obj58(0, 0)

                        def make_obj59(off_x, off_y):
                            obj59 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj59.color = Color('white')
                            obj59.group = 59
                            obj59_image = pygame.image.load('./obj59.png')
                            image_bindings.append([obj59, obj59_image])
                            user_shapes.append(obj59)
                            obj59.mass = 10
                            obj59.hit([0.16142791243665988, 
                                0.06726121960448422], obj59.position)
                            return obj59
                        obj59 = make_obj59(0, 0)

                        def make_obj60(off_x, off_y):
                            obj60 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj60.color = Color('white')
                            obj60.group = 60
                            obj60_image = pygame.image.load('./obj60.png')
                            image_bindings.append([obj60, obj60_image])
                            user_shapes.append(obj60)
                            obj60.mass = 10
                            obj60.hit([0.21811881879547484, 
                                0.20204359049095472], obj60.position)
                            return obj60
                        obj60 = make_obj60(0, 0)

                        def make_obj61(off_x, off_y):
                            obj61 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj61.color = Color('white')
                            obj61.group = 61
                            obj61_image = pygame.image.load('./obj61.png')
                            image_bindings.append([obj61, obj61_image])
                            user_shapes.append(obj61)
                            obj61.mass = 10
                            obj61.hit([-0.06756693067818914, 
                                -0.19691156059447784], obj61.position)
                            return obj61
                        obj61 = make_obj61(0, 0)

                        def make_obj63(off_x, off_y):
                            obj63 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj63.color = Color('white')
                            obj63.group = 63
                            obj63_image = pygame.image.load('./obj63.png')
                            image_bindings.append([obj63, obj63_image])
                            user_shapes.append(obj63)
                            obj63.mass = 10
                            obj63.hit([0.19653176385411225, 
                                0.22164394732144227], obj63.position)
                            return obj63
                        obj63 = make_obj63(0, 0)

                        def make_obj64(off_x, off_y):
                            obj64 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj64.color = Color('white')
                            obj64.group = 64
                            obj64_image = pygame.image.load('./obj64.png')
                            image_bindings.append([obj64, obj64_image])
                            user_shapes.append(obj64)
                            obj64.mass = 10
                            obj64.hit([-0.05348929695919474, 
                                0.14732747388633777], obj64.position)
                            return obj64
                        obj64 = make_obj64(0, 0)

                        def make_obj65(off_x, off_y):
                            obj65 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj65.color = Color('white')
                            obj65.group = 65
                            obj65_image = pygame.image.load('./obj65.png')
                            image_bindings.append([obj65, obj65_image])
                            user_shapes.append(obj65)
                            obj65.mass = 10
                            obj65.hit([0.08219828784867284, 
                                -0.015279189841372748], obj65.position)
                            return obj65
                        obj65 = make_obj65(0, 0)

                        def make_obj66(off_x, off_y):
                            obj66 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj66.color = Color('white')
                            obj66.group = 66
                            obj66_image = pygame.image.load('./obj66.png')
                            image_bindings.append([obj66, obj66_image])
                            user_shapes.append(obj66)
                            obj66.mass = 10
                            obj66.hit([-0.1333641234645009, 
                                -0.20870235152777497], obj66.position)
                            return obj66
                        obj66 = make_obj66(0, 0)

                        def make_obj68(off_x, off_y):
                            obj68 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj68.color = Color('white')
                            obj68.group = 68
                            obj68_image = pygame.image.load('./obj68.png')
                            image_bindings.append([obj68, obj68_image])
                            user_shapes.append(obj68)
                            obj68.mass = 10
                            obj68.hit([2.7267380075468584e-05, 
                                0.17911672574846987], obj68.position)
                            return obj68
                        obj68 = make_obj68(0, 0)

                        def make_obj69(off_x, off_y):
                            obj69 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj69.color = Color('white')
                            obj69.group = 69
                            obj69_image = pygame.image.load('./obj69.png')
                            image_bindings.append([obj69, obj69_image])
                            user_shapes.append(obj69)
                            obj69.mass = 10
                            obj69.hit([-0.15721400424384346, 
                                0.05741992102548099], obj69.position)
                            return obj69
                        obj69 = make_obj69(0, 0)

                        def make_obj70(off_x, off_y):
                            obj70 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj70.color = Color('white')
                            obj70.group = 70
                            obj70_image = pygame.image.load('./obj70.png')
                            image_bindings.append([obj70, obj70_image])
                            user_shapes.append(obj70)
                            obj70.mass = 10
                            obj70.hit([-0.14287103845672122, 
                                -0.03813338476040959], obj70.position)
                            return obj70
                        obj70 = make_obj70(0, 0)

                        def make_obj71(off_x, off_y):
                            obj71 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj71.color = Color('white')
                            obj71.group = 71
                            obj71_image = pygame.image.load('./obj71.png')
                            image_bindings.append([obj71, obj71_image])
                            user_shapes.append(obj71)
                            obj71.mass = 10
                            obj71.hit([0.06353749479535015, 
                                0.1373889065759472], obj71.position)
                            return obj71
                        obj71 = make_obj71(0, 0)
                        _hy_anon_var_132 = deactivate(f)
                    else:
                        _hy_anon_var_132 = None
                    return _hy_anon_var_132
                space = obj51.body.space
                ch = space.add_wildcard_collision_handler(obj51.collision_type)
                ch.post_solve = on_collide_51
                return obj51
            obj51 = make_obj51(0, 0)

            def make_obj74(off_x, off_y):
                obj74 = box([int(p.x + 154 + -154 - 22) + int(off_x), int(p
                    .y + 30 + fraction(-259, 2) - 30) + int(off_y)], 44, 60)
                obj74.color = Color('white')
                obj74.group = 74
                obj74_image = pygame.image.load('./obj74.png')
                image_bindings.append([obj74, obj74_image])
                user_shapes.append(obj74)
                obj74.mass = 10
                obj74.gravity = 0, -100

                def on_click_74(keys):
                    global click_handled
                    f = obj74
                    if not f or not f.body:
                        return False
                        _hy_anon_var_135 = None
                    else:
                        _hy_anon_var_135 = None
                    p = f.body.position
                    if mouse_clicked() and obj74.inside(mouse_point()
                        ) and obj74.active and click_handled == 0:

                        def make_obj76(off_x, off_y):
                            obj76 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj76.color = Color('white')
                            obj76.group = 76
                            obj76_image = pygame.image.load('./obj76.png')
                            image_bindings.append([obj76, obj76_image])
                            user_shapes.append(obj76)
                            obj76.mass = 10
                            obj76.hit([-0.12032945582841681, 
                                -0.1977951878545338], obj76.position)
                            return obj76
                        obj76 = make_obj76(0, 0)

                        def make_obj77(off_x, off_y):
                            obj77 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj77.color = Color('white')
                            obj77.group = 77
                            obj77_image = pygame.image.load('./obj77.png')
                            image_bindings.append([obj77, obj77_image])
                            user_shapes.append(obj77)
                            obj77.mass = 10
                            obj77.hit([0.24568525401468694, 
                                -0.06302318037692956], obj77.position)
                            return obj77
                        obj77 = make_obj77(0, 0)

                        def make_obj78(off_x, off_y):
                            obj78 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj78.color = Color('white')
                            obj78.group = 78
                            obj78_image = pygame.image.load('./obj78.png')
                            image_bindings.append([obj78, obj78_image])
                            user_shapes.append(obj78)
                            obj78.mass = 10
                            obj78.hit([-0.20226520185153046, 
                                -0.23754301723301122], obj78.position)
                            return obj78
                        obj78 = make_obj78(0, 0)

                        def make_obj79(off_x, off_y):
                            obj79 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj79.color = Color('white')
                            obj79.group = 79
                            obj79_image = pygame.image.load('./obj79.png')
                            image_bindings.append([obj79, obj79_image])
                            user_shapes.append(obj79)
                            obj79.mass = 10
                            obj79.hit([0.12792652568517193, 
                                -0.02015251379733038], obj79.position)
                            return obj79
                        obj79 = make_obj79(0, 0)

                        def make_obj81(off_x, off_y):
                            obj81 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj81.color = Color('white')
                            obj81.group = 81
                            obj81_image = pygame.image.load('./obj81.png')
                            image_bindings.append([obj81, obj81_image])
                            user_shapes.append(obj81)
                            obj81.mass = 10
                            obj81.hit([-0.11273375047571493, 
                                0.23939454958170336], obj81.position)
                            return obj81
                        obj81 = make_obj81(0, 0)

                        def make_obj82(off_x, off_y):
                            obj82 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj82.color = Color('white')
                            obj82.group = 82
                            obj82_image = pygame.image.load('./obj82.png')
                            image_bindings.append([obj82, obj82_image])
                            user_shapes.append(obj82)
                            obj82.mass = 10
                            obj82.hit([-0.010966269248394278, 
                                0.1262428815845678], obj82.position)
                            return obj82
                        obj82 = make_obj82(0, 0)

                        def make_obj83(off_x, off_y):
                            obj83 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj83.color = Color('white')
                            obj83.group = 83
                            obj83_image = pygame.image.load('./obj83.png')
                            image_bindings.append([obj83, obj83_image])
                            user_shapes.append(obj83)
                            obj83.mass = 10
                            obj83.hit([0.013687616527784718, 
                                -0.12919454727612106], obj83.position)
                            return obj83
                        obj83 = make_obj83(0, 0)

                        def make_obj84(off_x, off_y):
                            obj84 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj84.color = Color('white')
                            obj84.group = 84
                            obj84_image = pygame.image.load('./obj84.png')
                            image_bindings.append([obj84, obj84_image])
                            user_shapes.append(obj84)
                            obj84.mass = 10
                            obj84.hit([-0.1451849042667216, 
                                0.17819595454837167], obj84.position)
                            return obj84
                        obj84 = make_obj84(0, 0)

                        def make_obj86(off_x, off_y):
                            obj86 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj86.color = Color('white')
                            obj86.group = 86
                            obj86_image = pygame.image.load('./obj86.png')
                            image_bindings.append([obj86, obj86_image])
                            user_shapes.append(obj86)
                            obj86.mass = 10
                            obj86.hit([-0.2451611487179806, 
                                -0.2209183899571712], obj86.position)
                            return obj86
                        obj86 = make_obj86(0, 0)

                        def make_obj87(off_x, off_y):
                            obj87 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj87.color = Color('white')
                            obj87.group = 87
                            obj87_image = pygame.image.load('./obj87.png')
                            image_bindings.append([obj87, obj87_image])
                            user_shapes.append(obj87)
                            obj87.mass = 10
                            obj87.hit([-0.10123328016058594, 
                                -0.03143286053976857], obj87.position)
                            return obj87
                        obj87 = make_obj87(0, 0)

                        def make_obj88(off_x, off_y):
                            obj88 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj88.color = Color('white')
                            obj88.group = 88
                            obj88_image = pygame.image.load('./obj88.png')
                            image_bindings.append([obj88, obj88_image])
                            user_shapes.append(obj88)
                            obj88.mass = 10
                            obj88.hit([-0.21518829436021977, 
                                -0.1505687945332167], obj88.position)
                            return obj88
                        obj88 = make_obj88(0, 0)

                        def make_obj89(off_x, off_y):
                            obj89 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj89.color = Color('white')
                            obj89.group = 89
                            obj89_image = pygame.image.load('./obj89.png')
                            image_bindings.append([obj89, obj89_image])
                            user_shapes.append(obj89)
                            obj89.mass = 10
                            obj89.hit([0.0518800970844599, 
                                0.1645893827626928], obj89.position)
                            return obj89
                        obj89 = make_obj89(0, 0)

                        def make_obj91(off_x, off_y):
                            obj91 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj91.color = Color('white')
                            obj91.group = 91
                            obj91_image = pygame.image.load('./obj91.png')
                            image_bindings.append([obj91, obj91_image])
                            user_shapes.append(obj91)
                            obj91.mass = 10
                            obj91.hit([-0.10513674627720451, 
                                -0.16377310258448247], obj91.position)
                            return obj91
                        obj91 = make_obj91(0, 0)

                        def make_obj92(off_x, off_y):
                            obj92 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj92.color = Color('white')
                            obj92.group = 92
                            obj92_image = pygame.image.load('./obj92.png')
                            image_bindings.append([obj92, obj92_image])
                            user_shapes.append(obj92)
                            obj92.mass = 10
                            obj92.hit([0.13741317125548136, 
                                0.06279126847176442], obj92.position)
                            return obj92
                        obj92 = make_obj92(0, 0)

                        def make_obj93(off_x, off_y):
                            obj93 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj93.color = Color('white')
                            obj93.group = 93
                            obj93_image = pygame.image.load('./obj93.png')
                            image_bindings.append([obj93, obj93_image])
                            user_shapes.append(obj93)
                            obj93.mass = 10
                            obj93.hit([0.23024118002275135, 
                                0.032073411431924825], obj93.position)
                            return obj93
                        obj93 = make_obj93(0, 0)

                        def make_obj94(off_x, off_y):
                            obj94 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj94.color = Color('white')
                            obj94.group = 94
                            obj94_image = pygame.image.load('./obj94.png')
                            image_bindings.append([obj94, obj94_image])
                            user_shapes.append(obj94)
                            obj94.mass = 10
                            obj94.hit([0.20003282246338838, 
                                0.21034364408149342], obj94.position)
                            return obj94
                        obj94 = make_obj94(0, 0)
                        deactivate(f)
                        click_handled = 2
                        return True
                        _hy_anon_var_152 = None
                    else:
                        _hy_anon_var_152 = None
                    return _hy_anon_var_152
                add_observer(on_click_74)

                def on_collide_74(arbiter, space, data):
                    f = obj74
                    p = f.body.position
                    friction = arbiter.friction
                    restitution = arbiter.restitution
                    total_impulse = arbiter.total_impulse
                    energy_loss = arbiter.total_ke
                    if friction > 0 and energy_loss > 50000000:

                        def make_obj76(off_x, off_y):
                            obj76 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj76.color = Color('white')
                            obj76.group = 76
                            obj76_image = pygame.image.load('./obj76.png')
                            image_bindings.append([obj76, obj76_image])
                            user_shapes.append(obj76)
                            obj76.mass = 10
                            obj76.hit([-0.12032945582841681, 
                                -0.1977951878545338], obj76.position)
                            return obj76
                        obj76 = make_obj76(0, 0)

                        def make_obj77(off_x, off_y):
                            obj77 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj77.color = Color('white')
                            obj77.group = 77
                            obj77_image = pygame.image.load('./obj77.png')
                            image_bindings.append([obj77, obj77_image])
                            user_shapes.append(obj77)
                            obj77.mass = 10
                            obj77.hit([0.24568525401468694, 
                                -0.06302318037692956], obj77.position)
                            return obj77
                        obj77 = make_obj77(0, 0)

                        def make_obj78(off_x, off_y):
                            obj78 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj78.color = Color('white')
                            obj78.group = 78
                            obj78_image = pygame.image.load('./obj78.png')
                            image_bindings.append([obj78, obj78_image])
                            user_shapes.append(obj78)
                            obj78.mass = 10
                            obj78.hit([-0.20226520185153046, 
                                -0.23754301723301122], obj78.position)
                            return obj78
                        obj78 = make_obj78(0, 0)

                        def make_obj79(off_x, off_y):
                            obj79 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj79.color = Color('white')
                            obj79.group = 79
                            obj79_image = pygame.image.load('./obj79.png')
                            image_bindings.append([obj79, obj79_image])
                            user_shapes.append(obj79)
                            obj79.mass = 10
                            obj79.hit([0.12792652568517193, 
                                -0.02015251379733038], obj79.position)
                            return obj79
                        obj79 = make_obj79(0, 0)

                        def make_obj81(off_x, off_y):
                            obj81 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj81.color = Color('white')
                            obj81.group = 81
                            obj81_image = pygame.image.load('./obj81.png')
                            image_bindings.append([obj81, obj81_image])
                            user_shapes.append(obj81)
                            obj81.mass = 10
                            obj81.hit([-0.11273375047571493, 
                                0.23939454958170336], obj81.position)
                            return obj81
                        obj81 = make_obj81(0, 0)

                        def make_obj82(off_x, off_y):
                            obj82 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj82.color = Color('white')
                            obj82.group = 82
                            obj82_image = pygame.image.load('./obj82.png')
                            image_bindings.append([obj82, obj82_image])
                            user_shapes.append(obj82)
                            obj82.mass = 10
                            obj82.hit([-0.010966269248394278, 
                                0.1262428815845678], obj82.position)
                            return obj82
                        obj82 = make_obj82(0, 0)

                        def make_obj83(off_x, off_y):
                            obj83 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj83.color = Color('white')
                            obj83.group = 83
                            obj83_image = pygame.image.load('./obj83.png')
                            image_bindings.append([obj83, obj83_image])
                            user_shapes.append(obj83)
                            obj83.mass = 10
                            obj83.hit([0.013687616527784718, 
                                -0.12919454727612106], obj83.position)
                            return obj83
                        obj83 = make_obj83(0, 0)

                        def make_obj84(off_x, off_y):
                            obj84 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj84.color = Color('white')
                            obj84.group = 84
                            obj84_image = pygame.image.load('./obj84.png')
                            image_bindings.append([obj84, obj84_image])
                            user_shapes.append(obj84)
                            obj84.mass = 10
                            obj84.hit([-0.1451849042667216, 
                                0.17819595454837167], obj84.position)
                            return obj84
                        obj84 = make_obj84(0, 0)

                        def make_obj86(off_x, off_y):
                            obj86 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj86.color = Color('white')
                            obj86.group = 86
                            obj86_image = pygame.image.load('./obj86.png')
                            image_bindings.append([obj86, obj86_image])
                            user_shapes.append(obj86)
                            obj86.mass = 10
                            obj86.hit([-0.2451611487179806, 
                                -0.2209183899571712], obj86.position)
                            return obj86
                        obj86 = make_obj86(0, 0)

                        def make_obj87(off_x, off_y):
                            obj87 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj87.color = Color('white')
                            obj87.group = 87
                            obj87_image = pygame.image.load('./obj87.png')
                            image_bindings.append([obj87, obj87_image])
                            user_shapes.append(obj87)
                            obj87.mass = 10
                            obj87.hit([-0.10123328016058594, 
                                -0.03143286053976857], obj87.position)
                            return obj87
                        obj87 = make_obj87(0, 0)

                        def make_obj88(off_x, off_y):
                            obj88 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj88.color = Color('white')
                            obj88.group = 88
                            obj88_image = pygame.image.load('./obj88.png')
                            image_bindings.append([obj88, obj88_image])
                            user_shapes.append(obj88)
                            obj88.mass = 10
                            obj88.hit([-0.21518829436021977, 
                                -0.1505687945332167], obj88.position)
                            return obj88
                        obj88 = make_obj88(0, 0)

                        def make_obj89(off_x, off_y):
                            obj89 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj89.color = Color('white')
                            obj89.group = 89
                            obj89_image = pygame.image.load('./obj89.png')
                            image_bindings.append([obj89, obj89_image])
                            user_shapes.append(obj89)
                            obj89.mass = 10
                            obj89.hit([0.0518800970844599, 
                                0.1645893827626928], obj89.position)
                            return obj89
                        obj89 = make_obj89(0, 0)

                        def make_obj91(off_x, off_y):
                            obj91 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj91.color = Color('white')
                            obj91.group = 91
                            obj91_image = pygame.image.load('./obj91.png')
                            image_bindings.append([obj91, obj91_image])
                            user_shapes.append(obj91)
                            obj91.mass = 10
                            obj91.hit([-0.10513674627720451, 
                                -0.16377310258448247], obj91.position)
                            return obj91
                        obj91 = make_obj91(0, 0)

                        def make_obj92(off_x, off_y):
                            obj92 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj92.color = Color('white')
                            obj92.group = 92
                            obj92_image = pygame.image.load('./obj92.png')
                            image_bindings.append([obj92, obj92_image])
                            user_shapes.append(obj92)
                            obj92.mass = 10
                            obj92.hit([0.13741317125548136, 
                                0.06279126847176442], obj92.position)
                            return obj92
                        obj92 = make_obj92(0, 0)

                        def make_obj93(off_x, off_y):
                            obj93 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj93.color = Color('white')
                            obj93.group = 93
                            obj93_image = pygame.image.load('./obj93.png')
                            image_bindings.append([obj93, obj93_image])
                            user_shapes.append(obj93)
                            obj93.mass = 10
                            obj93.hit([0.23024118002275135, 
                                0.032073411431924825], obj93.position)
                            return obj93
                        obj93 = make_obj93(0, 0)

                        def make_obj94(off_x, off_y):
                            obj94 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj94.color = Color('white')
                            obj94.group = 94
                            obj94_image = pygame.image.load('./obj94.png')
                            image_bindings.append([obj94, obj94_image])
                            user_shapes.append(obj94)
                            obj94.mass = 10
                            obj94.hit([0.20003282246338838, 
                                0.21034364408149342], obj94.position)
                            return obj94
                        obj94 = make_obj94(0, 0)
                        _hy_anon_var_170 = deactivate(f)
                    else:
                        _hy_anon_var_170 = None
                    return _hy_anon_var_170
                space = obj74.body.space
                ch = space.add_wildcard_collision_handler(obj74.collision_type)
                ch.post_solve = on_collide_74
                return obj74
            obj74 = make_obj74(0, 0)

            def make_obj97(off_x, off_y):
                obj97 = box([int(p.x + 198 + -154 - 22) + int(off_x), int(p
                    .y + 30 + fraction(-259, 2) - 30) + int(off_y)], 44, 60)
                obj97.color = Color('white')
                obj97.group = 97
                obj97_image = pygame.image.load('./obj97.png')
                image_bindings.append([obj97, obj97_image])
                user_shapes.append(obj97)
                obj97.mass = 10
                obj97.gravity = 0, -100

                def on_click_97(keys):
                    global click_handled
                    f = obj97
                    if not f or not f.body:
                        return False
                        _hy_anon_var_173 = None
                    else:
                        _hy_anon_var_173 = None
                    p = f.body.position
                    if mouse_clicked() and obj97.inside(mouse_point()
                        ) and obj97.active and click_handled == 0:

                        def make_obj99(off_x, off_y):
                            obj99 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj99.color = Color('white')
                            obj99.group = 99
                            obj99_image = pygame.image.load('./obj99.png')
                            image_bindings.append([obj99, obj99_image])
                            user_shapes.append(obj99)
                            obj99.mass = 10
                            obj99.hit([-0.10011842749655081, 
                                0.24071473955844203], obj99.position)
                            return obj99
                        obj99 = make_obj99(0, 0)

                        def make_obj100(off_x, off_y):
                            obj100 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj100.color = Color('white')
                            obj100.group = 100
                            obj100_image = pygame.image.load('./obj100.png')
                            image_bindings.append([obj100, obj100_image])
                            user_shapes.append(obj100)
                            obj100.mass = 10
                            obj100.hit([0.16895174087070913, 
                                -0.03764248227924952], obj100.position)
                            return obj100
                        obj100 = make_obj100(0, 0)

                        def make_obj101(off_x, off_y):
                            obj101 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj101.color = Color('white')
                            obj101.group = 101
                            obj101_image = pygame.image.load('./obj101.png')
                            image_bindings.append([obj101, obj101_image])
                            user_shapes.append(obj101)
                            obj101.mass = 10
                            obj101.hit([0.10783229952890389, 
                                -0.084794822646613], obj101.position)
                            return obj101
                        obj101 = make_obj101(0, 0)

                        def make_obj102(off_x, off_y):
                            obj102 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj102.color = Color('white')
                            obj102.group = 102
                            obj102_image = pygame.image.load('./obj102.png')
                            image_bindings.append([obj102, obj102_image])
                            user_shapes.append(obj102)
                            obj102.mass = 10
                            obj102.hit([-0.04839891813857827, 
                                -0.21448358372146856], obj102.position)
                            return obj102
                        obj102 = make_obj102(0, 0)

                        def make_obj104(off_x, off_y):
                            obj104 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj104.color = Color('white')
                            obj104.group = 104
                            obj104_image = pygame.image.load('./obj104.png')
                            image_bindings.append([obj104, obj104_image])
                            user_shapes.append(obj104)
                            obj104.mass = 10
                            obj104.hit([0.0017234302029184856, 
                                -0.16776554901041885], obj104.position)
                            return obj104
                        obj104 = make_obj104(0, 0)

                        def make_obj105(off_x, off_y):
                            obj105 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj105.color = Color('white')
                            obj105.group = 105
                            obj105_image = pygame.image.load('./obj105.png')
                            image_bindings.append([obj105, obj105_image])
                            user_shapes.append(obj105)
                            obj105.mass = 10
                            obj105.hit([0.12522860687401854, 
                                -0.20071394712396454], obj105.position)
                            return obj105
                        obj105 = make_obj105(0, 0)

                        def make_obj106(off_x, off_y):
                            obj106 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj106.color = Color('white')
                            obj106.group = 106
                            obj106_image = pygame.image.load('./obj106.png')
                            image_bindings.append([obj106, obj106_image])
                            user_shapes.append(obj106)
                            obj106.mass = 10
                            obj106.hit([-0.05139017901130885, 
                                0.23150124788569748], obj106.position)
                            return obj106
                        obj106 = make_obj106(0, 0)

                        def make_obj107(off_x, off_y):
                            obj107 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj107.color = Color('white')
                            obj107.group = 107
                            obj107_image = pygame.image.load('./obj107.png')
                            image_bindings.append([obj107, obj107_image])
                            user_shapes.append(obj107)
                            obj107.mass = 10
                            obj107.hit([-0.05796299375507577, 
                                0.006860661769057086], obj107.position)
                            return obj107
                        obj107 = make_obj107(0, 0)

                        def make_obj109(off_x, off_y):
                            obj109 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj109.color = Color('white')
                            obj109.group = 109
                            obj109_image = pygame.image.load('./obj109.png')
                            image_bindings.append([obj109, obj109_image])
                            user_shapes.append(obj109)
                            obj109.mass = 10
                            obj109.hit([-0.08078079654425513, 
                                -0.14107059439241038], obj109.position)
                            return obj109
                        obj109 = make_obj109(0, 0)

                        def make_obj110(off_x, off_y):
                            obj110 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj110.color = Color('white')
                            obj110.group = 110
                            obj110_image = pygame.image.load('./obj110.png')
                            image_bindings.append([obj110, obj110_image])
                            user_shapes.append(obj110)
                            obj110.mass = 10
                            obj110.hit([0.2248976792392129, 
                                -0.10569920669901997], obj110.position)
                            return obj110
                        obj110 = make_obj110(0, 0)

                        def make_obj111(off_x, off_y):
                            obj111 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj111.color = Color('white')
                            obj111.group = 111
                            obj111_image = pygame.image.load('./obj111.png')
                            image_bindings.append([obj111, obj111_image])
                            user_shapes.append(obj111)
                            obj111.mass = 10
                            obj111.hit([-0.06693543096132798, 
                                -0.03096914231814013], obj111.position)
                            return obj111
                        obj111 = make_obj111(0, 0)

                        def make_obj112(off_x, off_y):
                            obj112 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj112.color = Color('white')
                            obj112.group = 112
                            obj112_image = pygame.image.load('./obj112.png')
                            image_bindings.append([obj112, obj112_image])
                            user_shapes.append(obj112)
                            obj112.mass = 10
                            obj112.hit([0.24653834949247, 
                                0.08272226590342618], obj112.position)
                            return obj112
                        obj112 = make_obj112(0, 0)

                        def make_obj114(off_x, off_y):
                            obj114 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj114.color = Color('white')
                            obj114.group = 114
                            obj114_image = pygame.image.load('./obj114.png')
                            image_bindings.append([obj114, obj114_image])
                            user_shapes.append(obj114)
                            obj114.mass = 10
                            obj114.hit([-0.041836583219005075, 
                                -0.11909081769895041], obj114.position)
                            return obj114
                        obj114 = make_obj114(0, 0)

                        def make_obj115(off_x, off_y):
                            obj115 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj115.color = Color('white')
                            obj115.group = 115
                            obj115_image = pygame.image.load('./obj115.png')
                            image_bindings.append([obj115, obj115_image])
                            user_shapes.append(obj115)
                            obj115.mass = 10
                            obj115.hit([-0.008347660707382798, 
                                0.11679994007441857], obj115.position)
                            return obj115
                        obj115 = make_obj115(0, 0)

                        def make_obj116(off_x, off_y):
                            obj116 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj116.color = Color('white')
                            obj116.group = 116
                            obj116_image = pygame.image.load('./obj116.png')
                            image_bindings.append([obj116, obj116_image])
                            user_shapes.append(obj116)
                            obj116.mass = 10
                            obj116.hit([0.0728473739354531, 
                                -0.12169095159315454], obj116.position)
                            return obj116
                        obj116 = make_obj116(0, 0)

                        def make_obj117(off_x, off_y):
                            obj117 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj117.color = Color('white')
                            obj117.group = 117
                            obj117_image = pygame.image.load('./obj117.png')
                            image_bindings.append([obj117, obj117_image])
                            user_shapes.append(obj117)
                            obj117.mass = 10
                            obj117.hit([-0.002539956250300346, 
                                0.09646127630582674], obj117.position)
                            return obj117
                        obj117 = make_obj117(0, 0)
                        deactivate(f)
                        click_handled = 2
                        return True
                        _hy_anon_var_190 = None
                    else:
                        _hy_anon_var_190 = None
                    return _hy_anon_var_190
                add_observer(on_click_97)

                def on_collide_97(arbiter, space, data):
                    f = obj97
                    p = f.body.position
                    friction = arbiter.friction
                    restitution = arbiter.restitution
                    total_impulse = arbiter.total_impulse
                    energy_loss = arbiter.total_ke
                    if friction > 0 and energy_loss > 50000000:

                        def make_obj99(off_x, off_y):
                            obj99 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj99.color = Color('white')
                            obj99.group = 99
                            obj99_image = pygame.image.load('./obj99.png')
                            image_bindings.append([obj99, obj99_image])
                            user_shapes.append(obj99)
                            obj99.mass = 10
                            obj99.hit([-0.10011842749655081, 
                                0.24071473955844203], obj99.position)
                            return obj99
                        obj99 = make_obj99(0, 0)

                        def make_obj100(off_x, off_y):
                            obj100 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj100.color = Color('white')
                            obj100.group = 100
                            obj100_image = pygame.image.load('./obj100.png')
                            image_bindings.append([obj100, obj100_image])
                            user_shapes.append(obj100)
                            obj100.mass = 10
                            obj100.hit([0.16895174087070913, 
                                -0.03764248227924952], obj100.position)
                            return obj100
                        obj100 = make_obj100(0, 0)

                        def make_obj101(off_x, off_y):
                            obj101 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj101.color = Color('white')
                            obj101.group = 101
                            obj101_image = pygame.image.load('./obj101.png')
                            image_bindings.append([obj101, obj101_image])
                            user_shapes.append(obj101)
                            obj101.mass = 10
                            obj101.hit([0.10783229952890389, 
                                -0.084794822646613], obj101.position)
                            return obj101
                        obj101 = make_obj101(0, 0)

                        def make_obj102(off_x, off_y):
                            obj102 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj102.color = Color('white')
                            obj102.group = 102
                            obj102_image = pygame.image.load('./obj102.png')
                            image_bindings.append([obj102, obj102_image])
                            user_shapes.append(obj102)
                            obj102.mass = 10
                            obj102.hit([-0.04839891813857827, 
                                -0.21448358372146856], obj102.position)
                            return obj102
                        obj102 = make_obj102(0, 0)

                        def make_obj104(off_x, off_y):
                            obj104 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj104.color = Color('white')
                            obj104.group = 104
                            obj104_image = pygame.image.load('./obj104.png')
                            image_bindings.append([obj104, obj104_image])
                            user_shapes.append(obj104)
                            obj104.mass = 10
                            obj104.hit([0.0017234302029184856, 
                                -0.16776554901041885], obj104.position)
                            return obj104
                        obj104 = make_obj104(0, 0)

                        def make_obj105(off_x, off_y):
                            obj105 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj105.color = Color('white')
                            obj105.group = 105
                            obj105_image = pygame.image.load('./obj105.png')
                            image_bindings.append([obj105, obj105_image])
                            user_shapes.append(obj105)
                            obj105.mass = 10
                            obj105.hit([0.12522860687401854, 
                                -0.20071394712396454], obj105.position)
                            return obj105
                        obj105 = make_obj105(0, 0)

                        def make_obj106(off_x, off_y):
                            obj106 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj106.color = Color('white')
                            obj106.group = 106
                            obj106_image = pygame.image.load('./obj106.png')
                            image_bindings.append([obj106, obj106_image])
                            user_shapes.append(obj106)
                            obj106.mass = 10
                            obj106.hit([-0.05139017901130885, 
                                0.23150124788569748], obj106.position)
                            return obj106
                        obj106 = make_obj106(0, 0)

                        def make_obj107(off_x, off_y):
                            obj107 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj107.color = Color('white')
                            obj107.group = 107
                            obj107_image = pygame.image.load('./obj107.png')
                            image_bindings.append([obj107, obj107_image])
                            user_shapes.append(obj107)
                            obj107.mass = 10
                            obj107.hit([-0.05796299375507577, 
                                0.006860661769057086], obj107.position)
                            return obj107
                        obj107 = make_obj107(0, 0)

                        def make_obj109(off_x, off_y):
                            obj109 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj109.color = Color('white')
                            obj109.group = 109
                            obj109_image = pygame.image.load('./obj109.png')
                            image_bindings.append([obj109, obj109_image])
                            user_shapes.append(obj109)
                            obj109.mass = 10
                            obj109.hit([-0.08078079654425513, 
                                -0.14107059439241038], obj109.position)
                            return obj109
                        obj109 = make_obj109(0, 0)

                        def make_obj110(off_x, off_y):
                            obj110 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj110.color = Color('white')
                            obj110.group = 110
                            obj110_image = pygame.image.load('./obj110.png')
                            image_bindings.append([obj110, obj110_image])
                            user_shapes.append(obj110)
                            obj110.mass = 10
                            obj110.hit([0.2248976792392129, 
                                -0.10569920669901997], obj110.position)
                            return obj110
                        obj110 = make_obj110(0, 0)

                        def make_obj111(off_x, off_y):
                            obj111 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj111.color = Color('white')
                            obj111.group = 111
                            obj111_image = pygame.image.load('./obj111.png')
                            image_bindings.append([obj111, obj111_image])
                            user_shapes.append(obj111)
                            obj111.mass = 10
                            obj111.hit([-0.06693543096132798, 
                                -0.03096914231814013], obj111.position)
                            return obj111
                        obj111 = make_obj111(0, 0)

                        def make_obj112(off_x, off_y):
                            obj112 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj112.color = Color('white')
                            obj112.group = 112
                            obj112_image = pygame.image.load('./obj112.png')
                            image_bindings.append([obj112, obj112_image])
                            user_shapes.append(obj112)
                            obj112.mass = 10
                            obj112.hit([0.24653834949247, 
                                0.08272226590342618], obj112.position)
                            return obj112
                        obj112 = make_obj112(0, 0)

                        def make_obj114(off_x, off_y):
                            obj114 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj114.color = Color('white')
                            obj114.group = 114
                            obj114_image = pygame.image.load('./obj114.png')
                            image_bindings.append([obj114, obj114_image])
                            user_shapes.append(obj114)
                            obj114.mass = 10
                            obj114.hit([-0.041836583219005075, 
                                -0.11909081769895041], obj114.position)
                            return obj114
                        obj114 = make_obj114(0, 0)

                        def make_obj115(off_x, off_y):
                            obj115 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj115.color = Color('white')
                            obj115.group = 115
                            obj115_image = pygame.image.load('./obj115.png')
                            image_bindings.append([obj115, obj115_image])
                            user_shapes.append(obj115)
                            obj115.mass = 10
                            obj115.hit([-0.008347660707382798, 
                                0.11679994007441857], obj115.position)
                            return obj115
                        obj115 = make_obj115(0, 0)

                        def make_obj116(off_x, off_y):
                            obj116 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj116.color = Color('white')
                            obj116.group = 116
                            obj116_image = pygame.image.load('./obj116.png')
                            image_bindings.append([obj116, obj116_image])
                            user_shapes.append(obj116)
                            obj116.mass = 10
                            obj116.hit([0.0728473739354531, 
                                -0.12169095159315454], obj116.position)
                            return obj116
                        obj116 = make_obj116(0, 0)

                        def make_obj117(off_x, off_y):
                            obj117 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj117.color = Color('white')
                            obj117.group = 117
                            obj117_image = pygame.image.load('./obj117.png')
                            image_bindings.append([obj117, obj117_image])
                            user_shapes.append(obj117)
                            obj117.mass = 10
                            obj117.hit([-0.002539956250300346, 
                                0.09646127630582674], obj117.position)
                            return obj117
                        obj117 = make_obj117(0, 0)
                        _hy_anon_var_208 = deactivate(f)
                    else:
                        _hy_anon_var_208 = None
                    return _hy_anon_var_208
                space = obj97.body.space
                ch = space.add_wildcard_collision_handler(obj97.collision_type)
                ch.post_solve = on_collide_97
                return obj97
            obj97 = make_obj97(0, 0)

            def make_obj120(off_x, off_y):
                obj120 = box([int(p.x + 242 + -154 - 22) + int(off_x), int(
                    p.y + 30 + fraction(-259, 2) - 30) + int(off_y)], 44, 60)
                obj120.color = Color('white')
                obj120.group = 120
                obj120_image = pygame.image.load('./obj120.png')
                image_bindings.append([obj120, obj120_image])
                user_shapes.append(obj120)
                obj120.mass = 10
                obj120.gravity = 0, -100

                def on_click_120(keys):
                    global click_handled
                    f = obj120
                    if not f or not f.body:
                        return False
                        _hy_anon_var_211 = None
                    else:
                        _hy_anon_var_211 = None
                    p = f.body.position
                    if mouse_clicked() and obj120.inside(mouse_point()
                        ) and obj120.active and click_handled == 0:

                        def make_obj122(off_x, off_y):
                            obj122 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj122.color = Color('white')
                            obj122.group = 122
                            obj122_image = pygame.image.load('./obj122.png')
                            image_bindings.append([obj122, obj122_image])
                            user_shapes.append(obj122)
                            obj122.mass = 10
                            obj122.hit([0.21086034629469558, 
                                0.1101380615515441], obj122.position)
                            return obj122
                        obj122 = make_obj122(0, 0)

                        def make_obj123(off_x, off_y):
                            obj123 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj123.color = Color('white')
                            obj123.group = 123
                            obj123_image = pygame.image.load('./obj123.png')
                            image_bindings.append([obj123, obj123_image])
                            user_shapes.append(obj123)
                            obj123.mass = 10
                            obj123.hit([-0.1332616372309673, 
                                0.17360753417256458], obj123.position)
                            return obj123
                        obj123 = make_obj123(0, 0)

                        def make_obj124(off_x, off_y):
                            obj124 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj124.color = Color('white')
                            obj124.group = 124
                            obj124_image = pygame.image.load('./obj124.png')
                            image_bindings.append([obj124, obj124_image])
                            user_shapes.append(obj124)
                            obj124.mass = 10
                            obj124.hit([0.2219453063245453, 
                                0.05097053819379582], obj124.position)
                            return obj124
                        obj124 = make_obj124(0, 0)

                        def make_obj125(off_x, off_y):
                            obj125 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj125.color = Color('white')
                            obj125.group = 125
                            obj125_image = pygame.image.load('./obj125.png')
                            image_bindings.append([obj125, obj125_image])
                            user_shapes.append(obj125)
                            obj125.mass = 10
                            obj125.hit([-0.16183176337764754, 
                                0.1678058303435363], obj125.position)
                            return obj125
                        obj125 = make_obj125(0, 0)

                        def make_obj127(off_x, off_y):
                            obj127 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj127.color = Color('white')
                            obj127.group = 127
                            obj127_image = pygame.image.load('./obj127.png')
                            image_bindings.append([obj127, obj127_image])
                            user_shapes.append(obj127)
                            obj127.mass = 10
                            obj127.hit([0.21305194958457857, 
                                0.19116140186357589], obj127.position)
                            return obj127
                        obj127 = make_obj127(0, 0)

                        def make_obj128(off_x, off_y):
                            obj128 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj128.color = Color('white')
                            obj128.group = 128
                            obj128_image = pygame.image.load('./obj128.png')
                            image_bindings.append([obj128, obj128_image])
                            user_shapes.append(obj128)
                            obj128.mass = 10
                            obj128.hit([-0.08186676190893316, 
                                0.16553641039216277], obj128.position)
                            return obj128
                        obj128 = make_obj128(0, 0)

                        def make_obj129(off_x, off_y):
                            obj129 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj129.color = Color('white')
                            obj129.group = 129
                            obj129_image = pygame.image.load('./obj129.png')
                            image_bindings.append([obj129, obj129_image])
                            user_shapes.append(obj129)
                            obj129.mass = 10
                            obj129.hit([-0.007612286154962011, 
                                -0.00942105321669462], obj129.position)
                            return obj129
                        obj129 = make_obj129(0, 0)

                        def make_obj130(off_x, off_y):
                            obj130 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj130.color = Color('white')
                            obj130.group = 130
                            obj130_image = pygame.image.load('./obj130.png')
                            image_bindings.append([obj130, obj130_image])
                            user_shapes.append(obj130)
                            obj130.mass = 10
                            obj130.hit([-0.1679494915142409, 
                                0.06776414092046706], obj130.position)
                            return obj130
                        obj130 = make_obj130(0, 0)

                        def make_obj132(off_x, off_y):
                            obj132 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj132.color = Color('white')
                            obj132.group = 132
                            obj132_image = pygame.image.load('./obj132.png')
                            image_bindings.append([obj132, obj132_image])
                            user_shapes.append(obj132)
                            obj132.mass = 10
                            obj132.hit([-0.18569667442350374, 
                                -0.2053886501167061], obj132.position)
                            return obj132
                        obj132 = make_obj132(0, 0)

                        def make_obj133(off_x, off_y):
                            obj133 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj133.color = Color('white')
                            obj133.group = 133
                            obj133_image = pygame.image.load('./obj133.png')
                            image_bindings.append([obj133, obj133_image])
                            user_shapes.append(obj133)
                            obj133.mass = 10
                            obj133.hit([-0.17752386709325116, 
                                0.07516139504350028], obj133.position)
                            return obj133
                        obj133 = make_obj133(0, 0)

                        def make_obj134(off_x, off_y):
                            obj134 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj134.color = Color('white')
                            obj134.group = 134
                            obj134_image = pygame.image.load('./obj134.png')
                            image_bindings.append([obj134, obj134_image])
                            user_shapes.append(obj134)
                            obj134.mass = 10
                            obj134.hit([0.24041465728223532, 
                                -0.19238968508249485], obj134.position)
                            return obj134
                        obj134 = make_obj134(0, 0)

                        def make_obj135(off_x, off_y):
                            obj135 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj135.color = Color('white')
                            obj135.group = 135
                            obj135_image = pygame.image.load('./obj135.png')
                            image_bindings.append([obj135, obj135_image])
                            user_shapes.append(obj135)
                            obj135.mass = 10
                            obj135.hit([0.04333865200505588, 
                                -0.040338924711220026], obj135.position)
                            return obj135
                        obj135 = make_obj135(0, 0)

                        def make_obj137(off_x, off_y):
                            obj137 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj137.color = Color('white')
                            obj137.group = 137
                            obj137_image = pygame.image.load('./obj137.png')
                            image_bindings.append([obj137, obj137_image])
                            user_shapes.append(obj137)
                            obj137.mass = 10
                            obj137.hit([0.04905985638137217, 
                                0.017309101321802745], obj137.position)
                            return obj137
                        obj137 = make_obj137(0, 0)

                        def make_obj138(off_x, off_y):
                            obj138 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj138.color = Color('white')
                            obj138.group = 138
                            obj138_image = pygame.image.load('./obj138.png')
                            image_bindings.append([obj138, obj138_image])
                            user_shapes.append(obj138)
                            obj138.mass = 10
                            obj138.hit([-0.20045412883499142, 
                                0.21107943528437118], obj138.position)
                            return obj138
                        obj138 = make_obj138(0, 0)

                        def make_obj139(off_x, off_y):
                            obj139 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj139.color = Color('white')
                            obj139.group = 139
                            obj139_image = pygame.image.load('./obj139.png')
                            image_bindings.append([obj139, obj139_image])
                            user_shapes.append(obj139)
                            obj139.mass = 10
                            obj139.hit([0.1777903129068169, 
                                -0.04751006417956513], obj139.position)
                            return obj139
                        obj139 = make_obj139(0, 0)

                        def make_obj140(off_x, off_y):
                            obj140 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj140.color = Color('white')
                            obj140.group = 140
                            obj140_image = pygame.image.load('./obj140.png')
                            image_bindings.append([obj140, obj140_image])
                            user_shapes.append(obj140)
                            obj140.mass = 10
                            obj140.hit([-0.08867819734035642, 
                                -0.1501741299257192], obj140.position)
                            return obj140
                        obj140 = make_obj140(0, 0)
                        deactivate(f)
                        click_handled = 2
                        return True
                        _hy_anon_var_228 = None
                    else:
                        _hy_anon_var_228 = None
                    return _hy_anon_var_228
                add_observer(on_click_120)

                def on_collide_120(arbiter, space, data):
                    f = obj120
                    p = f.body.position
                    friction = arbiter.friction
                    restitution = arbiter.restitution
                    total_impulse = arbiter.total_impulse
                    energy_loss = arbiter.total_ke
                    if friction > 0 and energy_loss > 50000000:

                        def make_obj122(off_x, off_y):
                            obj122 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj122.color = Color('white')
                            obj122.group = 122
                            obj122_image = pygame.image.load('./obj122.png')
                            image_bindings.append([obj122, obj122_image])
                            user_shapes.append(obj122)
                            obj122.mass = 10
                            obj122.hit([0.21086034629469558, 
                                0.1101380615515441], obj122.position)
                            return obj122
                        obj122 = make_obj122(0, 0)

                        def make_obj123(off_x, off_y):
                            obj123 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj123.color = Color('white')
                            obj123.group = 123
                            obj123_image = pygame.image.load('./obj123.png')
                            image_bindings.append([obj123, obj123_image])
                            user_shapes.append(obj123)
                            obj123.mass = 10
                            obj123.hit([-0.1332616372309673, 
                                0.17360753417256458], obj123.position)
                            return obj123
                        obj123 = make_obj123(0, 0)

                        def make_obj124(off_x, off_y):
                            obj124 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj124.color = Color('white')
                            obj124.group = 124
                            obj124_image = pygame.image.load('./obj124.png')
                            image_bindings.append([obj124, obj124_image])
                            user_shapes.append(obj124)
                            obj124.mass = 10
                            obj124.hit([0.2219453063245453, 
                                0.05097053819379582], obj124.position)
                            return obj124
                        obj124 = make_obj124(0, 0)

                        def make_obj125(off_x, off_y):
                            obj125 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj125.color = Color('white')
                            obj125.group = 125
                            obj125_image = pygame.image.load('./obj125.png')
                            image_bindings.append([obj125, obj125_image])
                            user_shapes.append(obj125)
                            obj125.mass = 10
                            obj125.hit([-0.16183176337764754, 
                                0.1678058303435363], obj125.position)
                            return obj125
                        obj125 = make_obj125(0, 0)

                        def make_obj127(off_x, off_y):
                            obj127 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj127.color = Color('white')
                            obj127.group = 127
                            obj127_image = pygame.image.load('./obj127.png')
                            image_bindings.append([obj127, obj127_image])
                            user_shapes.append(obj127)
                            obj127.mass = 10
                            obj127.hit([0.21305194958457857, 
                                0.19116140186357589], obj127.position)
                            return obj127
                        obj127 = make_obj127(0, 0)

                        def make_obj128(off_x, off_y):
                            obj128 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj128.color = Color('white')
                            obj128.group = 128
                            obj128_image = pygame.image.load('./obj128.png')
                            image_bindings.append([obj128, obj128_image])
                            user_shapes.append(obj128)
                            obj128.mass = 10
                            obj128.hit([-0.08186676190893316, 
                                0.16553641039216277], obj128.position)
                            return obj128
                        obj128 = make_obj128(0, 0)

                        def make_obj129(off_x, off_y):
                            obj129 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj129.color = Color('white')
                            obj129.group = 129
                            obj129_image = pygame.image.load('./obj129.png')
                            image_bindings.append([obj129, obj129_image])
                            user_shapes.append(obj129)
                            obj129.mass = 10
                            obj129.hit([-0.007612286154962011, 
                                -0.00942105321669462], obj129.position)
                            return obj129
                        obj129 = make_obj129(0, 0)

                        def make_obj130(off_x, off_y):
                            obj130 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj130.color = Color('white')
                            obj130.group = 130
                            obj130_image = pygame.image.load('./obj130.png')
                            image_bindings.append([obj130, obj130_image])
                            user_shapes.append(obj130)
                            obj130.mass = 10
                            obj130.hit([-0.1679494915142409, 
                                0.06776414092046706], obj130.position)
                            return obj130
                        obj130 = make_obj130(0, 0)

                        def make_obj132(off_x, off_y):
                            obj132 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj132.color = Color('white')
                            obj132.group = 132
                            obj132_image = pygame.image.load('./obj132.png')
                            image_bindings.append([obj132, obj132_image])
                            user_shapes.append(obj132)
                            obj132.mass = 10
                            obj132.hit([-0.18569667442350374, 
                                -0.2053886501167061], obj132.position)
                            return obj132
                        obj132 = make_obj132(0, 0)

                        def make_obj133(off_x, off_y):
                            obj133 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj133.color = Color('white')
                            obj133.group = 133
                            obj133_image = pygame.image.load('./obj133.png')
                            image_bindings.append([obj133, obj133_image])
                            user_shapes.append(obj133)
                            obj133.mass = 10
                            obj133.hit([-0.17752386709325116, 
                                0.07516139504350028], obj133.position)
                            return obj133
                        obj133 = make_obj133(0, 0)

                        def make_obj134(off_x, off_y):
                            obj134 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj134.color = Color('white')
                            obj134.group = 134
                            obj134_image = pygame.image.load('./obj134.png')
                            image_bindings.append([obj134, obj134_image])
                            user_shapes.append(obj134)
                            obj134.mass = 10
                            obj134.hit([0.24041465728223532, 
                                -0.19238968508249485], obj134.position)
                            return obj134
                        obj134 = make_obj134(0, 0)

                        def make_obj135(off_x, off_y):
                            obj135 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj135.color = Color('white')
                            obj135.group = 135
                            obj135_image = pygame.image.load('./obj135.png')
                            image_bindings.append([obj135, obj135_image])
                            user_shapes.append(obj135)
                            obj135.mass = 10
                            obj135.hit([0.04333865200505588, 
                                -0.040338924711220026], obj135.position)
                            return obj135
                        obj135 = make_obj135(0, 0)

                        def make_obj137(off_x, off_y):
                            obj137 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj137.color = Color('white')
                            obj137.group = 137
                            obj137_image = pygame.image.load('./obj137.png')
                            image_bindings.append([obj137, obj137_image])
                            user_shapes.append(obj137)
                            obj137.mass = 10
                            obj137.hit([0.04905985638137217, 
                                0.017309101321802745], obj137.position)
                            return obj137
                        obj137 = make_obj137(0, 0)

                        def make_obj138(off_x, off_y):
                            obj138 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj138.color = Color('white')
                            obj138.group = 138
                            obj138_image = pygame.image.load('./obj138.png')
                            image_bindings.append([obj138, obj138_image])
                            user_shapes.append(obj138)
                            obj138.mass = 10
                            obj138.hit([-0.20045412883499142, 
                                0.21107943528437118], obj138.position)
                            return obj138
                        obj138 = make_obj138(0, 0)

                        def make_obj139(off_x, off_y):
                            obj139 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj139.color = Color('white')
                            obj139.group = 139
                            obj139_image = pygame.image.load('./obj139.png')
                            image_bindings.append([obj139, obj139_image])
                            user_shapes.append(obj139)
                            obj139.mass = 10
                            obj139.hit([0.1777903129068169, 
                                -0.04751006417956513], obj139.position)
                            return obj139
                        obj139 = make_obj139(0, 0)

                        def make_obj140(off_x, off_y):
                            obj140 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj140.color = Color('white')
                            obj140.group = 140
                            obj140_image = pygame.image.load('./obj140.png')
                            image_bindings.append([obj140, obj140_image])
                            user_shapes.append(obj140)
                            obj140.mass = 10
                            obj140.hit([-0.08867819734035642, 
                                -0.1501741299257192], obj140.position)
                            return obj140
                        obj140 = make_obj140(0, 0)
                        _hy_anon_var_246 = deactivate(f)
                    else:
                        _hy_anon_var_246 = None
                    return _hy_anon_var_246
                space = obj120.body.space
                ch = space.add_wildcard_collision_handler(obj120.collision_type
                    )
                ch.post_solve = on_collide_120
                return obj120
            obj120 = make_obj120(0, 0)

            def make_obj143(off_x, off_y):
                obj143 = box([int(p.x + 286 + -154 - 22) + int(off_x), int(
                    p.y + 30 + fraction(-259, 2) - 30) + int(off_y)], 44, 60)
                obj143.color = Color('white')
                obj143.group = 143
                obj143_image = pygame.image.load('./obj143.png')
                image_bindings.append([obj143, obj143_image])
                user_shapes.append(obj143)
                obj143.mass = 10
                obj143.gravity = 0, -100

                def on_click_143(keys):
                    global click_handled
                    f = obj143
                    if not f or not f.body:
                        return False
                        _hy_anon_var_249 = None
                    else:
                        _hy_anon_var_249 = None
                    p = f.body.position
                    if mouse_clicked() and obj143.inside(mouse_point()
                        ) and obj143.active and click_handled == 0:

                        def make_obj145(off_x, off_y):
                            obj145 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj145.color = Color('white')
                            obj145.group = 145
                            obj145_image = pygame.image.load('./obj145.png')
                            image_bindings.append([obj145, obj145_image])
                            user_shapes.append(obj145)
                            obj145.mass = 10
                            obj145.hit([0.1204641305507485, 
                                -0.23683706653819184], obj145.position)
                            return obj145
                        obj145 = make_obj145(0, 0)

                        def make_obj146(off_x, off_y):
                            obj146 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj146.color = Color('white')
                            obj146.group = 146
                            obj146_image = pygame.image.load('./obj146.png')
                            image_bindings.append([obj146, obj146_image])
                            user_shapes.append(obj146)
                            obj146.mass = 10
                            obj146.hit([-0.13971946517975273, 
                                -0.01032039782652694], obj146.position)
                            return obj146
                        obj146 = make_obj146(0, 0)

                        def make_obj147(off_x, off_y):
                            obj147 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj147.color = Color('white')
                            obj147.group = 147
                            obj147_image = pygame.image.load('./obj147.png')
                            image_bindings.append([obj147, obj147_image])
                            user_shapes.append(obj147)
                            obj147.mass = 10
                            obj147.hit([0.08545825823101166, 
                                -0.00728991232260634], obj147.position)
                            return obj147
                        obj147 = make_obj147(0, 0)

                        def make_obj148(off_x, off_y):
                            obj148 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj148.color = Color('white')
                            obj148.group = 148
                            obj148_image = pygame.image.load('./obj148.png')
                            image_bindings.append([obj148, obj148_image])
                            user_shapes.append(obj148)
                            obj148.mass = 10
                            obj148.hit([-0.04602004752312083, 
                                -0.023551310621824223], obj148.position)
                            return obj148
                        obj148 = make_obj148(0, 0)

                        def make_obj150(off_x, off_y):
                            obj150 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj150.color = Color('white')
                            obj150.group = 150
                            obj150_image = pygame.image.load('./obj150.png')
                            image_bindings.append([obj150, obj150_image])
                            user_shapes.append(obj150)
                            obj150.mass = 10
                            obj150.hit([0.0719759992721975, 
                                0.24559424947565517], obj150.position)
                            return obj150
                        obj150 = make_obj150(0, 0)

                        def make_obj151(off_x, off_y):
                            obj151 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj151.color = Color('white')
                            obj151.group = 151
                            obj151_image = pygame.image.load('./obj151.png')
                            image_bindings.append([obj151, obj151_image])
                            user_shapes.append(obj151)
                            obj151.mass = 10
                            obj151.hit([-0.0945903176150252, 
                                0.07276527703161767], obj151.position)
                            return obj151
                        obj151 = make_obj151(0, 0)

                        def make_obj152(off_x, off_y):
                            obj152 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj152.color = Color('white')
                            obj152.group = 152
                            obj152_image = pygame.image.load('./obj152.png')
                            image_bindings.append([obj152, obj152_image])
                            user_shapes.append(obj152)
                            obj152.mass = 10
                            obj152.hit([0.07337582687897892, 
                                0.08646741276262843], obj152.position)
                            return obj152
                        obj152 = make_obj152(0, 0)

                        def make_obj153(off_x, off_y):
                            obj153 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj153.color = Color('white')
                            obj153.group = 153
                            obj153_image = pygame.image.load('./obj153.png')
                            image_bindings.append([obj153, obj153_image])
                            user_shapes.append(obj153)
                            obj153.mass = 10
                            obj153.hit([0.21000538351505993, 
                                0.16404020940427755], obj153.position)
                            return obj153
                        obj153 = make_obj153(0, 0)

                        def make_obj155(off_x, off_y):
                            obj155 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj155.color = Color('white')
                            obj155.group = 155
                            obj155_image = pygame.image.load('./obj155.png')
                            image_bindings.append([obj155, obj155_image])
                            user_shapes.append(obj155)
                            obj155.mass = 10
                            obj155.hit([0.24787880970602683, 
                                -0.2133383593462358], obj155.position)
                            return obj155
                        obj155 = make_obj155(0, 0)

                        def make_obj156(off_x, off_y):
                            obj156 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj156.color = Color('white')
                            obj156.group = 156
                            obj156_image = pygame.image.load('./obj156.png')
                            image_bindings.append([obj156, obj156_image])
                            user_shapes.append(obj156)
                            obj156.mass = 10
                            obj156.hit([0.19059239203185258, 
                                0.09028321173482301], obj156.position)
                            return obj156
                        obj156 = make_obj156(0, 0)

                        def make_obj157(off_x, off_y):
                            obj157 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj157.color = Color('white')
                            obj157.group = 157
                            obj157_image = pygame.image.load('./obj157.png')
                            image_bindings.append([obj157, obj157_image])
                            user_shapes.append(obj157)
                            obj157.mass = 10
                            obj157.hit([0.11961486013137995, 
                                -0.028351476508450463], obj157.position)
                            return obj157
                        obj157 = make_obj157(0, 0)

                        def make_obj158(off_x, off_y):
                            obj158 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj158.color = Color('white')
                            obj158.group = 158
                            obj158_image = pygame.image.load('./obj158.png')
                            image_bindings.append([obj158, obj158_image])
                            user_shapes.append(obj158)
                            obj158.mass = 10
                            obj158.hit([-0.17293658165047154, 
                                0.2426866677074756], obj158.position)
                            return obj158
                        obj158 = make_obj158(0, 0)

                        def make_obj160(off_x, off_y):
                            obj160 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj160.color = Color('white')
                            obj160.group = 160
                            obj160_image = pygame.image.load('./obj160.png')
                            image_bindings.append([obj160, obj160_image])
                            user_shapes.append(obj160)
                            obj160.mass = 10
                            obj160.hit([0.01686176716053106, 
                                0.16277314428165884], obj160.position)
                            return obj160
                        obj160 = make_obj160(0, 0)

                        def make_obj161(off_x, off_y):
                            obj161 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj161.color = Color('white')
                            obj161.group = 161
                            obj161_image = pygame.image.load('./obj161.png')
                            image_bindings.append([obj161, obj161_image])
                            user_shapes.append(obj161)
                            obj161.mass = 10
                            obj161.hit([-0.12637765898521827, 
                                0.20994865630504694], obj161.position)
                            return obj161
                        obj161 = make_obj161(0, 0)

                        def make_obj162(off_x, off_y):
                            obj162 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj162.color = Color('white')
                            obj162.group = 162
                            obj162_image = pygame.image.load('./obj162.png')
                            image_bindings.append([obj162, obj162_image])
                            user_shapes.append(obj162)
                            obj162.mass = 10
                            obj162.hit([-0.1548174708620724, 
                                -0.018292590348249926], obj162.position)
                            return obj162
                        obj162 = make_obj162(0, 0)

                        def make_obj163(off_x, off_y):
                            obj163 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj163.color = Color('white')
                            obj163.group = 163
                            obj163_image = pygame.image.load('./obj163.png')
                            image_bindings.append([obj163, obj163_image])
                            user_shapes.append(obj163)
                            obj163.mass = 10
                            obj163.hit([0.020702679247166345, 
                                0.09264708514571979], obj163.position)
                            return obj163
                        obj163 = make_obj163(0, 0)
                        deactivate(f)
                        click_handled = 2
                        return True
                        _hy_anon_var_266 = None
                    else:
                        _hy_anon_var_266 = None
                    return _hy_anon_var_266
                add_observer(on_click_143)

                def on_collide_143(arbiter, space, data):
                    f = obj143
                    p = f.body.position
                    friction = arbiter.friction
                    restitution = arbiter.restitution
                    total_impulse = arbiter.total_impulse
                    energy_loss = arbiter.total_ke
                    if friction > 0 and energy_loss > 50000000:

                        def make_obj145(off_x, off_y):
                            obj145 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj145.color = Color('white')
                            obj145.group = 145
                            obj145_image = pygame.image.load('./obj145.png')
                            image_bindings.append([obj145, obj145_image])
                            user_shapes.append(obj145)
                            obj145.mass = 10
                            obj145.hit([0.1204641305507485, 
                                -0.23683706653819184], obj145.position)
                            return obj145
                        obj145 = make_obj145(0, 0)

                        def make_obj146(off_x, off_y):
                            obj146 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj146.color = Color('white')
                            obj146.group = 146
                            obj146_image = pygame.image.load('./obj146.png')
                            image_bindings.append([obj146, obj146_image])
                            user_shapes.append(obj146)
                            obj146.mass = 10
                            obj146.hit([-0.13971946517975273, 
                                -0.01032039782652694], obj146.position)
                            return obj146
                        obj146 = make_obj146(0, 0)

                        def make_obj147(off_x, off_y):
                            obj147 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj147.color = Color('white')
                            obj147.group = 147
                            obj147_image = pygame.image.load('./obj147.png')
                            image_bindings.append([obj147, obj147_image])
                            user_shapes.append(obj147)
                            obj147.mass = 10
                            obj147.hit([0.08545825823101166, 
                                -0.00728991232260634], obj147.position)
                            return obj147
                        obj147 = make_obj147(0, 0)

                        def make_obj148(off_x, off_y):
                            obj148 = box([int(p.x + fraction(11, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj148.color = Color('white')
                            obj148.group = 148
                            obj148_image = pygame.image.load('./obj148.png')
                            image_bindings.append([obj148, obj148_image])
                            user_shapes.append(obj148)
                            obj148.mass = 10
                            obj148.hit([-0.04602004752312083, 
                                -0.023551310621824223], obj148.position)
                            return obj148
                        obj148 = make_obj148(0, 0)

                        def make_obj150(off_x, off_y):
                            obj150 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj150.color = Color('white')
                            obj150.group = 150
                            obj150_image = pygame.image.load('./obj150.png')
                            image_bindings.append([obj150, obj150_image])
                            user_shapes.append(obj150)
                            obj150.mass = 10
                            obj150.hit([0.0719759992721975, 
                                0.24559424947565517], obj150.position)
                            return obj150
                        obj150 = make_obj150(0, 0)

                        def make_obj151(off_x, off_y):
                            obj151 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj151.color = Color('white')
                            obj151.group = 151
                            obj151_image = pygame.image.load('./obj151.png')
                            image_bindings.append([obj151, obj151_image])
                            user_shapes.append(obj151)
                            obj151.mass = 10
                            obj151.hit([-0.0945903176150252, 
                                0.07276527703161767], obj151.position)
                            return obj151
                        obj151 = make_obj151(0, 0)

                        def make_obj152(off_x, off_y):
                            obj152 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj152.color = Color('white')
                            obj152.group = 152
                            obj152_image = pygame.image.load('./obj152.png')
                            image_bindings.append([obj152, obj152_image])
                            user_shapes.append(obj152)
                            obj152.mass = 10
                            obj152.hit([0.07337582687897892, 
                                0.08646741276262843], obj152.position)
                            return obj152
                        obj152 = make_obj152(0, 0)

                        def make_obj153(off_x, off_y):
                            obj153 = box([int(p.x + fraction(33, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj153.color = Color('white')
                            obj153.group = 153
                            obj153_image = pygame.image.load('./obj153.png')
                            image_bindings.append([obj153, obj153_image])
                            user_shapes.append(obj153)
                            obj153.mass = 10
                            obj153.hit([0.21000538351505993, 
                                0.16404020940427755], obj153.position)
                            return obj153
                        obj153 = make_obj153(0, 0)

                        def make_obj155(off_x, off_y):
                            obj155 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj155.color = Color('white')
                            obj155.group = 155
                            obj155_image = pygame.image.load('./obj155.png')
                            image_bindings.append([obj155, obj155_image])
                            user_shapes.append(obj155)
                            obj155.mass = 10
                            obj155.hit([0.24787880970602683, 
                                -0.2133383593462358], obj155.position)
                            return obj155
                        obj155 = make_obj155(0, 0)

                        def make_obj156(off_x, off_y):
                            obj156 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj156.color = Color('white')
                            obj156.group = 156
                            obj156_image = pygame.image.load('./obj156.png')
                            image_bindings.append([obj156, obj156_image])
                            user_shapes.append(obj156)
                            obj156.mass = 10
                            obj156.hit([0.19059239203185258, 
                                0.09028321173482301], obj156.position)
                            return obj156
                        obj156 = make_obj156(0, 0)

                        def make_obj157(off_x, off_y):
                            obj157 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj157.color = Color('white')
                            obj157.group = 157
                            obj157_image = pygame.image.load('./obj157.png')
                            image_bindings.append([obj157, obj157_image])
                            user_shapes.append(obj157)
                            obj157.mass = 10
                            obj157.hit([0.11961486013137995, 
                                -0.028351476508450463], obj157.position)
                            return obj157
                        obj157 = make_obj157(0, 0)

                        def make_obj158(off_x, off_y):
                            obj158 = box([int(p.x + fraction(55, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj158.color = Color('white')
                            obj158.group = 158
                            obj158_image = pygame.image.load('./obj158.png')
                            image_bindings.append([obj158, obj158_image])
                            user_shapes.append(obj158)
                            obj158.mass = 10
                            obj158.hit([-0.17293658165047154, 
                                0.2426866677074756], obj158.position)
                            return obj158
                        obj158 = make_obj158(0, 0)

                        def make_obj160(off_x, off_y):
                            obj160 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(15, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj160.color = Color('white')
                            obj160.group = 160
                            obj160_image = pygame.image.load('./obj160.png')
                            image_bindings.append([obj160, obj160_image])
                            user_shapes.append(obj160)
                            obj160.mass = 10
                            obj160.hit([0.01686176716053106, 
                                0.16277314428165884], obj160.position)
                            return obj160
                        obj160 = make_obj160(0, 0)

                        def make_obj161(off_x, off_y):
                            obj161 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(45, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj161.color = Color('white')
                            obj161.group = 161
                            obj161_image = pygame.image.load('./obj161.png')
                            image_bindings.append([obj161, obj161_image])
                            user_shapes.append(obj161)
                            obj161.mass = 10
                            obj161.hit([-0.12637765898521827, 
                                0.20994865630504694], obj161.position)
                            return obj161
                        obj161 = make_obj161(0, 0)

                        def make_obj162(off_x, off_y):
                            obj162 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(75, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj162.color = Color('white')
                            obj162.group = 162
                            obj162_image = pygame.image.load('./obj162.png')
                            image_bindings.append([obj162, obj162_image])
                            user_shapes.append(obj162)
                            obj162.mass = 10
                            obj162.hit([-0.1548174708620724, 
                                -0.018292590348249926], obj162.position)
                            return obj162
                        obj162 = make_obj162(0, 0)

                        def make_obj163(off_x, off_y):
                            obj163 = box([int(p.x + fraction(77, 2) + -22 -
                                fraction(11, 2)) + int(off_x), int(p.y +
                                fraction(105, 2) + -30 - fraction(15, 2)) +
                                int(off_y)], 11, 15)
                            obj163.color = Color('white')
                            obj163.group = 163
                            obj163_image = pygame.image.load('./obj163.png')
                            image_bindings.append([obj163, obj163_image])
                            user_shapes.append(obj163)
                            obj163.mass = 10
                            obj163.hit([0.020702679247166345, 
                                0.09264708514571979], obj163.position)
                            return obj163
                        obj163 = make_obj163(0, 0)
                        _hy_anon_var_284 = deactivate(f)
                    else:
                        _hy_anon_var_284 = None
                    return _hy_anon_var_284
                space = obj143.body.space
                ch = space.add_wildcard_collision_handler(obj143.collision_type
                    )
                ch.post_solve = on_collide_143
                return obj143
            obj143 = make_obj143(0, 0)

            def make_obj167(off_x, off_y):
                obj167 = cosmetic_ball([int(p.x + 154 + -154) + int(off_x),
                    +int(p.y + 110 + fraction(-259, 2)), int(off_y)], 50)
                obj167.color = Color('white')
                obj167.group = 167
                obj167_image = pygame.image.load('./obj167.png')
                image_bindings.append([obj167, obj167_image])
                user_shapes.append(obj167)
                return obj167
            obj167 = make_obj167(0, 0)

            def make_obj2(off_x, off_y):
                obj2 = box([int(p.x + 154 + -154 - 27) + int(off_x), int(p.
                    y + 187 + fraction(-259, 2) - 27) + int(off_y)], 54, 54)
                obj2.color = Color('white')
                obj2.group = 2
                obj2_image = pygame.image.load('./obj2.png')
                image_bindings.append([obj2, obj2_image])
                user_shapes.append(obj2)

                def on_click_2(keys):
                    global click_handled
                    f = obj2
                    if not f or not f.body:
                        return False
                        _hy_anon_var_288 = None
                    else:
                        _hy_anon_var_288 = None
                    p = f.body.position
                    if mouse_clicked() and obj2.inside(mouse_point()
                        ) and obj2.active and click_handled == 0:

                        def make_obj1(off_x, off_y):
                            obj1 = box([int(p.x + 22 + -22 - 22) + int(
                                off_x), int(p.y + 30 + -30 - 30) + int(
                                off_y)], 44, 60)
                            obj1.color = Color('white')
                            obj1.group = 1
                            obj1_image = pygame.image.load('./obj1.png')
                            image_bindings.append([obj1, obj1_image])
                            user_shapes.append(obj1)
                            obj1.mass = 10
                            obj1.gravity = 0, -100
                            return obj1
                        obj1 = make_obj1(0, 0)
                        deactivate(f)
                        []
                        click_handled = 2
                        return True
                        _hy_anon_var_290 = None
                    else:
                        _hy_anon_var_290 = None
                    return _hy_anon_var_290
                add_observer(on_click_2)
                return obj2
            obj2 = make_obj2(0, 0)

            def make_obj202(off_x, off_y):
                obj202 = cosmetic_ball([int(p.x + 154 + -154) + int(off_x),
                    +int(p.y + fraction(433, 2) + fraction(-259, 2)), int(
                    off_y)], fraction(5, 2))
                obj202.color = Color('white')
                obj202.group = 202
                obj202_image = pygame.image.load('./obj202.png')
                image_bindings.append([obj202, obj202_image])
                user_shapes.append(obj202)
                return obj202
            obj202 = make_obj202(0, 0)

            def make_obj199(off_x, off_y):
                obj199 = ball([int(p.x + 109 + -154) + int(off_x), +int(p.y +
                    239 + fraction(-259, 2)), int(off_y)], 20)
                obj199.color = Color('white')
                obj199.group = 199
                obj199_image = pygame.image.load('./obj199.png')
                image_bindings.append([obj199, obj199_image])
                user_shapes.append(obj199)
                obj199.mass = 10
                obj199.elasticity = 1.0 * 0
                motor(obj199, -1)
                return obj199
            obj199 = make_obj199(0, 0)

            def make_obj203(off_x, off_y):
                obj203 = cosmetic_ball([int(p.x + fraction(263, 2) + -154) +
                    int(off_x), +int(p.y + 239 + fraction(-259, 2)), int(
                    off_y)], fraction(5, 2))
                obj203.color = Color('white')
                obj203.group = 203
                obj203_image = pygame.image.load('./obj203.png')
                image_bindings.append([obj203, obj203_image])
                user_shapes.append(obj203)
                return obj203
            obj203 = make_obj203(0, 0)

            def make_obj200(off_x, off_y):
                obj200 = ball([int(p.x + 154 + -154) + int(off_x), +int(p.y +
                    239 + fraction(-259, 2)), int(off_y)], 20)
                obj200.color = Color('white')
                obj200.group = 200
                obj200_image = pygame.image.load('./obj200.png')
                image_bindings.append([obj200, obj200_image])
                user_shapes.append(obj200)
                obj200.mass = 10
                obj200.elasticity = 1.0 * 0
                motor(obj200, -1)
                return obj200
            obj200 = make_obj200(0, 0)

            def make_obj204(off_x, off_y):
                obj204 = cosmetic_ball([int(p.x + fraction(353, 2) + -154) +
                    int(off_x), +int(p.y + 239 + fraction(-259, 2)), int(
                    off_y)], fraction(5, 2))
                obj204.color = Color('white')
                obj204.group = 204
                obj204_image = pygame.image.load('./obj204.png')
                image_bindings.append([obj204, obj204_image])
                user_shapes.append(obj204)
                return obj204
            obj204 = make_obj204(0, 0)

            def make_obj201(off_x, off_y):
                obj201 = ball([int(p.x + 199 + -154) + int(off_x), +int(p.y +
                    239 + fraction(-259, 2)), int(off_y)], 20)
                obj201.color = Color('white')
                obj201.group = 201
                obj201_image = pygame.image.load('./obj201.png')
                image_bindings.append([obj201, obj201_image])
                user_shapes.append(obj201)
                obj201.mass = 10
                obj201.elasticity = 1.0 * 0
                motor(obj201, -1)
                return obj201
            obj201 = make_obj201(0, 0)
            deactivate(f)
            p = spring(obj2.body.position, obj2, obj5.body.position, obj5, 
                100, 20000, 1000)
            connected_shapes.append([obj2, obj5, p])
            p = spring(obj2.body.position, obj2, obj28.body.position, obj28,
                100, 20000, 1000)
            connected_shapes.append([obj2, obj28, p])
            p = spring(obj2.body.position, obj2, obj51.body.position, obj51,
                100, 20000, 1000)
            connected_shapes.append([obj2, obj51, p])
            p = spring(obj2.body.position, obj2, obj74.body.position, obj74,
                100, 20000, 1000)
            connected_shapes.append([obj2, obj74, p])
            p = spring(obj2.body.position, obj2, obj97.body.position, obj97,
                100, 20000, 1000)
            connected_shapes.append([obj2, obj97, p])
            p = spring(obj2.body.position, obj2, obj120.body.position,
                obj120, 100, 20000, 1000)
            connected_shapes.append([obj2, obj120, p])
            p = spring(obj2.body.position, obj2, obj143.body.position,
                obj143, 100, 20000, 1000)
            connected_shapes.append([obj2, obj143, p])
            p = pin(obj199.body.position, obj199, obj200.body.position, obj200)
            connected_shapes.append([obj199, obj200, p])
            p = pin(obj199.body.position, obj199, obj2.body.position, obj2)
            connected_shapes.append([obj199, obj2, p])
            p = pin(obj200.body.position, obj200, obj201.body.position, obj201)
            connected_shapes.append([obj200, obj201, p])
            p = pin(obj200.body.position, obj200, obj2.body.position, obj2)
            connected_shapes.append([obj200, obj2, p])
            p = pin(obj201.body.position, obj201, obj2.body.position, obj2)
            connected_shapes.append([obj201, obj2, p])
            click_handled = 2
            return True
            _hy_anon_var_299 = None
        else:
            _hy_anon_var_299 = None
        return _hy_anon_var_299
    add_observer(on_click_207)
    return obj207


obj207 = make_obj207(0, 0)


def make_obj198(off_x, off_y):
    obj198 = cosmetic_ball([int(290) + int(off_x), +int(260), int(off_y)], 100)
    obj198.color = Color('white')
    obj198.group = 198
    obj198_image = pygame.image.load('./obj198.png')
    image_bindings.append([obj198, obj198_image])
    user_shapes.append(obj198)
    return obj198


obj198 = make_obj198(0, 0)


def make_obj192(off_x, off_y):
    obj192 = ball([int(170) + int(off_x), +int(294), int(off_y)], 20)
    obj192.color = Color('white')
    obj192.group = 192
    obj192_image = pygame.image.load('./obj192.png')
    image_bindings.append([obj192, obj192_image])
    user_shapes.append(obj192)
    obj192.mass = 10
    obj192.elasticity = 1.0 * 0
    motor(obj192, 1)
    return obj192


obj192 = make_obj192(0, 0)


def make_obj195(off_x, off_y):
    obj195 = cosmetic_ball([int(fraction(295, 2)) + int(off_x), +int(294),
        int(off_y)], fraction(5, 2))
    obj195.color = Color('white')
    obj195.group = 195
    obj195_image = pygame.image.load('./obj195.png')
    image_bindings.append([obj195, obj195_image])
    user_shapes.append(obj195)
    return obj195


obj195 = make_obj195(0, 0)


def make_obj191(off_x, off_y):
    obj191 = ball([int(125) + int(off_x), +int(294), int(off_y)], 20)
    obj191.color = Color('white')
    obj191.group = 191
    obj191_image = pygame.image.load('./obj191.png')
    image_bindings.append([obj191, obj191_image])
    user_shapes.append(obj191)
    obj191.mass = 10
    obj191.elasticity = 1.0 * 0
    motor(obj191, 1)
    return obj191


obj191 = make_obj191(0, 0)


def make_obj194(off_x, off_y):
    obj194 = cosmetic_ball([int(fraction(205, 2)) + int(off_x), +int(294),
        int(off_y)], fraction(5, 2))
    obj194.color = Color('white')
    obj194.group = 194
    obj194_image = pygame.image.load('./obj194.png')
    image_bindings.append([obj194, obj194_image])
    user_shapes.append(obj194)
    return obj194


obj194 = make_obj194(0, 0)


def make_obj190(off_x, off_y):
    obj190 = ball([int(80) + int(off_x), +int(294), int(off_y)], 20)
    obj190.color = Color('white')
    obj190.group = 190
    obj190_image = pygame.image.load('./obj190.png')
    image_bindings.append([obj190, obj190_image])
    user_shapes.append(obj190)
    obj190.mass = 10
    obj190.elasticity = 1.0 * 0
    motor(obj190, 1)
    return obj190


obj190 = make_obj190(0, 0)


def make_obj193(off_x, off_y):
    obj193 = cosmetic_ball([int(125) + int(off_x), +int(fraction(543, 2)),
        int(off_y)], fraction(5, 2))
    obj193.color = Color('white')
    obj193.group = 193
    obj193_image = pygame.image.load('./obj193.png')
    image_bindings.append([obj193, obj193_image])
    user_shapes.append(obj193)
    return obj193


obj193 = make_obj193(0, 0)


def make_obj185(off_x, off_y):
    obj185 = box([int(125 - fraction(107, 2)) + int(off_x), int(fraction(
        475, 2) - fraction(63, 2)) + int(off_y)], 107, 63)
    obj185.color = Color('white')
    obj185.group = 185
    obj185_image = pygame.image.load('./obj185.png')
    image_bindings.append([obj185, obj185_image])
    user_shapes.append(obj185)
    motor(obj185, 0)

    def on_click_185(keys):
        global click_handled
        f = obj185
        if not f or not f.body:
            return False
            _hy_anon_var_309 = None
        else:
            _hy_anon_var_309 = None
        p = f.body.position
        if mouse_clicked() and obj185.inside(mouse_point()
            ) and obj185.active and click_handled == 0:

            def make_obj188(off_x, off_y):
                obj188 = cosmetic_ball([int(p.x + 100 + -165) + int(off_x),
                    +int(p.y + 69 + -69), int(off_y)], 100)
                obj188.color = Color('white')
                obj188.group = 188
                obj188_image = pygame.image.load('./obj188.png')
                image_bindings.append([obj188, obj188_image])
                user_shapes.append(obj188)
                return obj188
            obj188 = make_obj188(0, 0)

            def make_obj172(off_x, off_y):
                obj172 = box([int(p.x + 265 + -165 - fraction(41, 2)) + int
                    (off_x), int(p.y + fraction(41, 2) + -69 - fraction(41,
                    2)) + int(off_y)], 41, 41)
                obj172.color = Color('white')
                obj172.group = 172
                obj172_image = pygame.image.load('./obj172.png')
                image_bindings.append([obj172, obj172_image])
                user_shapes.append(obj172)
                obj172.mass = 10
                obj172.hit([0, 0], obj172.position)
                obj172.hit([2004830.5299528847, -515319.8484134258], obj172
                    .position)
                return obj172
            obj172 = make_obj172(0, 0)

            def make_obj176(off_x, off_y):
                obj176 = cosmetic_ball([int(p.x + 265 + -165) + int(off_x),
                    +int(p.y + fraction(87, 2) + -69), int(off_y)],
                    fraction(5, 2))
                obj176.color = Color('white')
                obj176.group = 176
                obj176_image = pygame.image.load('./obj176.png')
                image_bindings.append([obj176, obj176_image])
                user_shapes.append(obj176)
                return obj176
            obj176 = make_obj176(0, 0)

            def make_obj173(off_x, off_y):
                obj173 = ball([int(p.x + 220 + -165) + int(off_x), +int(p.y +
                    66 + -69), int(off_y)], 20)
                obj173.color = Color('white')
                obj173.group = 173
                obj173_image = pygame.image.load('./obj173.png')
                image_bindings.append([obj173, obj173_image])
                user_shapes.append(obj173)
                obj173.mass = 10
                obj173.elasticity = 1.0 * 0
                motor(obj173, 1)
                obj173.hit([2004830.5299528847, -515319.8484134258], obj173
                    .position)
                return obj173
            obj173 = make_obj173(0, 0)

            def make_obj177(off_x, off_y):
                obj177 = cosmetic_ball([int(p.x + fraction(485, 2) + -165) +
                    int(off_x), +int(p.y + 66 + -69), int(off_y)], fraction
                    (5, 2))
                obj177.color = Color('white')
                obj177.group = 177
                obj177_image = pygame.image.load('./obj177.png')
                image_bindings.append([obj177, obj177_image])
                user_shapes.append(obj177)
                return obj177
            obj177 = make_obj177(0, 0)

            def make_obj174(off_x, off_y):
                obj174 = ball([int(p.x + 265 + -165) + int(off_x), +int(p.y +
                    66 + -69), int(off_y)], 20)
                obj174.color = Color('white')
                obj174.group = 174
                obj174_image = pygame.image.load('./obj174.png')
                image_bindings.append([obj174, obj174_image])
                user_shapes.append(obj174)
                obj174.mass = 10
                obj174.elasticity = 1.0 * 0
                motor(obj174, 1)
                obj174.hit([2004830.5299528847, -515319.8484134258], obj174
                    .position)
                return obj174
            obj174 = make_obj174(0, 0)

            def make_obj178(off_x, off_y):
                obj178 = cosmetic_ball([int(p.x + fraction(575, 2) + -165) +
                    int(off_x), +int(p.y + 66 + -69), int(off_y)], fraction
                    (5, 2))
                obj178.color = Color('white')
                obj178.group = 178
                obj178_image = pygame.image.load('./obj178.png')
                image_bindings.append([obj178, obj178_image])
                user_shapes.append(obj178)
                return obj178
            obj178 = make_obj178(0, 0)

            def make_obj175(off_x, off_y):
                obj175 = ball([int(p.x + 310 + -165) + int(off_x), +int(p.y +
                    66 + -69), int(off_y)], 20)
                obj175.color = Color('white')
                obj175.group = 175
                obj175_image = pygame.image.load('./obj175.png')
                image_bindings.append([obj175, obj175_image])
                user_shapes.append(obj175)
                obj175.mass = 10
                obj175.elasticity = 1.0 * 0
                motor(obj175, 1)
                obj175.hit([2004830.5299528847, -515319.8484134258], obj175
                    .position)
                return obj175
            obj175 = make_obj175(0, 0)

            def make_obj186(off_x, off_y):
                obj186 = cosmetic_ball([int(p.x + 265 + -165) + int(off_x),
                    +int(p.y + 112 + -69), int(off_y)], 26)
                obj186.color = Color('white')
                obj186.group = 186
                obj186_image = pygame.image.load('./obj186.png')
                image_bindings.append([obj186, obj186_image])
                user_shapes.append(obj186)
                return obj186
            obj186 = make_obj186(0, 0)
            p = pin(obj173.body.position, obj173, obj174.body.position, obj174)
            connected_shapes.append([obj173, obj174, p])
            p = pin(obj173.body.position, obj173, obj172.body.position, obj172)
            connected_shapes.append([obj173, obj172, p])
            p = pin(obj174.body.position, obj174, obj175.body.position, obj175)
            connected_shapes.append([obj174, obj175, p])
            p = pin(obj174.body.position, obj174, obj172.body.position, obj172)
            connected_shapes.append([obj174, obj172, p])
            p = pin(obj175.body.position, obj175, obj172.body.position, obj172)
            connected_shapes.append([obj175, obj172, p])
            click_handled = 2
            return True
            _hy_anon_var_319 = None
        else:
            _hy_anon_var_319 = None
        return _hy_anon_var_319
    add_observer(on_click_185)
    return obj185


obj185 = make_obj185(0, 0)


def make_obj228(off_x, off_y):
    obj228 = static_box([int(5 - 5) + int(off_x), int(260 - 250) + int(
        off_y)], 10, 500)
    obj228.color = Color('white')
    obj228.group = 228
    obj228_image = pygame.image.load('./obj228.png')
    image_bindings.append([obj228, obj228_image])
    user_shapes.append(obj228)
    return obj228


obj228 = make_obj228(0, 0)


def make_obj226(off_x, off_y):
    obj226 = static_box([int(383 - 383) + int(off_x), int(5 - 5) + int(
        off_y)], 766, 10)
    obj226.color = Color('white')
    obj226.group = 226
    obj226_image = pygame.image.load('./obj226.png')
    image_bindings.append([obj226, obj226_image])
    user_shapes.append(obj226)
    return obj226


obj226 = make_obj226(0, 0)
p = pin(obj192.body.position, obj192, obj185.body.position, obj185)
connected_shapes.append([obj192, obj185, p])
p = pin(obj191.body.position, obj191, obj192.body.position, obj192)
connected_shapes.append([obj191, obj192, p])
p = pin(obj191.body.position, obj191, obj185.body.position, obj185)
connected_shapes.append([obj191, obj185, p])
p = pin(obj190.body.position, obj190, obj191.body.position, obj191)
connected_shapes.append([obj190, obj191, p])
p = pin(obj190.body.position, obj190, obj185.body.position, obj185)
connected_shapes.append([obj190, obj185, p])


def image_for(s):
    global image_bindings
    for b in image_bindings:
        if b[0] == s:
            return b[1]
            _hy_anon_var_324 = None
        else:
            _hy_anon_var_324 = None
    return False


def draw_images(cosmetic):

    def f(keys):
        global user_shapes
        for s in user_shapes:
            if not image_for(s):
                continue
                _hy_anon_var_326 = None
            else:
                _hy_anon_var_326 = None
            if not cosmetic == s._cosmetic:
                continue
                _hy_anon_var_327 = None
            else:
                _hy_anon_var_327 = None
            if not s.active:
                continue
                _hy_anon_var_328 = None
            else:
                _hy_anon_var_328 = None
            if s.body:
                p = Vec2d(s.body.position.x, s.body.position.y)
                _hy_anon_var_329 = None
            else:
                p = Vec2d(s._x, s._y)
                _hy_anon_var_329 = None
            angle = 0
            if s.body:
                angle = s.body.angle
                _hy_anon_var_330 = None
            else:
                _hy_anon_var_330 = None
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
                _hy_anon_var_333 = None
            else:
                _hy_anon_var_333 = None
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
            _hy_anon_var_335 = None
        else:
            _hy_anon_var_335 = None
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

