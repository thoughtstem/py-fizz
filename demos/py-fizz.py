from hy.core.language import fraction
import sys
import math
import pymunk
from pyphysicssandbox import *
import pygame
from pyphysicssandbox import Vec2d
w = 520
h = 520
user_shapes = []
image_bindings = []
friends = []
enemies = []
temp_shapes = []
pivots = []
connected_shapes = []
click_handled = 2
the_window = window('Most Awesome Thing Ever', w, h)
game_already_over = False


def create_end_screen(is_won):
    global image_bindings
    global user_shapes
    end_screen_img = pygame.image.load(
        '/Users/thoughtstem/Dev/Python/py-fizz/images/win-screen.png' if
        is_won else
        '/Users/thoughtstem/Dev/Python/py-fizz/images/lose-screen.png')
    end_screen = static_box((w / 2, h / 2), 0, 0)
    image_bindings.append([end_screen, end_screen_img])
    user_shapes.append(end_screen)
    return end_screen


def make_obj24(off_x, off_y):
    obj24 = static_box([int(260 - 260) + int(off_x), int(515 - 5) + int(
        off_y)], 520, 10)
    obj24.color = Color('white')
    obj24.group = 24
    obj24_image = pygame.image.load('./py-fizz-images/obj24.png')
    image_bindings.append([obj24, obj24_image])
    user_shapes.append(obj24)
    return obj24


obj24 = make_obj24(0, 0)


def make_obj26(off_x, off_y):
    obj26 = static_box([int(515 - 5) + int(off_x), int(260 - 250) + int(
        off_y)], 10, 500)
    obj26.color = Color('white')
    obj26.group = 26
    obj26_image = pygame.image.load('./py-fizz-images/obj26.png')
    image_bindings.append([obj26, obj26_image])
    user_shapes.append(obj26)
    return obj26


obj26 = make_obj26(0, 0)


def make_obj22(off_x, off_y):
    obj22 = cosmetic_ball([int(260) + int(off_x), +int(260), int(off_y)], 250)
    obj22.color = Color('white')
    obj22.group = 22
    obj22_image = pygame.image.load('./py-fizz-images/obj22.png')
    image_bindings.append([obj22, obj22_image])
    user_shapes.append(obj22)
    return obj22


obj22 = make_obj22(0, 0)


def make_obj17(off_x, off_y):
    obj17 = box([int(260 - fraction(101, 2)) + int(off_x), int(260 - 25) +
        int(off_y)], 101, 50)
    obj17.color = Color('white')
    obj17.group = 17
    obj17_image = pygame.image.load('./py-fizz-images/obj17.png')
    image_bindings.append([obj17, obj17_image])
    user_shapes.append(obj17)

    def on_click_17(keys):
        global click_handled
        f = obj17
        if not f or not f.body:
            return False
            _hy_anon_var_5 = None
        else:
            _hy_anon_var_5 = None
        p = f.body.position
        if mouse_clicked() and obj17.inside(mouse_point()
            ) and obj17.active and click_handled == 0:

            def make_obj4(off_x, off_y):
                obj4 = box([int(p.x + 65 + fraction(-331, 2) - fraction(41,
                    2)) + int(off_x), int(p.y + fraction(41, 2) + -43 -
                    fraction(41, 2)) + int(off_y)], 41, 41)
                obj4.color = Color('white')
                obj4.group = 4
                obj4_image = pygame.image.load('./py-fizz-images/obj4.png')
                image_bindings.append([obj4, obj4_image])
                user_shapes.append(obj4)
                obj4.hit([0, 0], obj4.position)
                obj4.hit([-2010000, 0], obj4.position)
                return obj4
            obj4 = make_obj4(0, 0)

            def make_obj8(off_x, off_y):
                obj8 = cosmetic_ball([int(p.x + 65 + fraction(-331, 2)) +
                    int(off_x), +int(p.y + fraction(87, 2) + -43), int(
                    off_y)], fraction(5, 2))
                obj8.color = Color('white')
                obj8.group = 8
                obj8_image = pygame.image.load('./py-fizz-images/obj8.png')
                image_bindings.append([obj8, obj8_image])
                user_shapes.append(obj8)
                return obj8
            obj8 = make_obj8(0, 0)

            def make_obj5(off_x, off_y):
                obj5 = ball([int(p.x + 20 + fraction(-331, 2)) + int(off_x),
                    +int(p.y + 66 + -43), int(off_y)], 20)
                obj5.color = Color('white')
                obj5.group = 5
                obj5_image = pygame.image.load('./py-fizz-images/obj5.png')
                image_bindings.append([obj5, obj5_image])
                user_shapes.append(obj5)
                obj5.elasticity = 1.0 * 0
                motor(obj5, 1)
                obj5.hit([-2010000, 0], obj5.position)
                return obj5
            obj5 = make_obj5(0, 0)

            def make_obj9(off_x, off_y):
                obj9 = cosmetic_ball([int(p.x + fraction(85, 2) + fraction(
                    -331, 2)) + int(off_x), +int(p.y + 66 + -43), int(off_y
                    )], fraction(5, 2))
                obj9.color = Color('white')
                obj9.group = 9
                obj9_image = pygame.image.load('./py-fizz-images/obj9.png')
                image_bindings.append([obj9, obj9_image])
                user_shapes.append(obj9)
                return obj9
            obj9 = make_obj9(0, 0)

            def make_obj6(off_x, off_y):
                obj6 = ball([int(p.x + 65 + fraction(-331, 2)) + int(off_x),
                    +int(p.y + 66 + -43), int(off_y)], 20)
                obj6.color = Color('white')
                obj6.group = 6
                obj6_image = pygame.image.load('./py-fizz-images/obj6.png')
                image_bindings.append([obj6, obj6_image])
                user_shapes.append(obj6)
                obj6.elasticity = 1.0 * 0
                motor(obj6, 1)
                obj6.hit([-2010000, 0], obj6.position)
                return obj6
            obj6 = make_obj6(0, 0)

            def make_obj10(off_x, off_y):
                obj10 = cosmetic_ball([int(p.x + fraction(175, 2) +
                    fraction(-331, 2)) + int(off_x), +int(p.y + 66 + -43),
                    int(off_y)], fraction(5, 2))
                obj10.color = Color('white')
                obj10.group = 10
                obj10_image = pygame.image.load('./py-fizz-images/obj10.png')
                image_bindings.append([obj10, obj10_image])
                user_shapes.append(obj10)
                return obj10
            obj10 = make_obj10(0, 0)

            def make_obj7(off_x, off_y):
                obj7 = ball([int(p.x + 110 + fraction(-331, 2)) + int(off_x
                    ), +int(p.y + 66 + -43), int(off_y)], 20)
                obj7.color = Color('white')
                obj7.group = 7
                obj7_image = pygame.image.load('./py-fizz-images/obj7.png')
                image_bindings.append([obj7, obj7_image])
                user_shapes.append(obj7)
                obj7.elasticity = 1.0 * 0
                motor(obj7, 1)
                obj7.hit([-2010000, 0], obj7.position)
                return obj7
            obj7 = make_obj7(0, 0)

            def make_obj19(off_x, off_y):
                obj19 = cosmetic_ball([int(p.x + fraction(461, 2) +
                    fraction(-331, 2)) + int(off_x), +int(p.y + 43 + -43),
                    int(off_y)], fraction(201, 2))
                obj19.color = Color('white')
                obj19.group = 19
                obj19_image = pygame.image.load('./py-fizz-images/obj19.png')
                image_bindings.append([obj19, obj19_image])
                user_shapes.append(obj19)
                return obj19
            obj19 = make_obj19(0, 0)
            p = pin(obj5.body.position, obj5, obj6.body.position, obj6)
            connected_shapes.append([obj5, obj6, p])
            p = pin(obj5.body.position, obj5, obj4.body.position, obj4)
            connected_shapes.append([obj5, obj4, p])
            p = pin(obj6.body.position, obj6, obj7.body.position, obj7)
            connected_shapes.append([obj6, obj7, p])
            p = pin(obj6.body.position, obj6, obj4.body.position, obj4)
            connected_shapes.append([obj6, obj4, p])
            p = pin(obj7.body.position, obj7, obj4.body.position, obj4)
            connected_shapes.append([obj7, obj4, p])
            click_handled = 2
            return True
            _hy_anon_var_14 = None
        else:
            _hy_anon_var_14 = None
        return _hy_anon_var_14
    add_observer(on_click_17)
    return obj17


obj17 = make_obj17(0, 0)


def make_obj26(off_x, off_y):
    obj26 = static_box([int(5 - 5) + int(off_x), int(260 - 250) + int(off_y
        )], 10, 500)
    obj26.color = Color('white')
    obj26.group = 26
    obj26_image = pygame.image.load('./py-fizz-images/obj26.png')
    image_bindings.append([obj26, obj26_image])
    user_shapes.append(obj26)
    return obj26


obj26 = make_obj26(0, 0)


def make_obj24(off_x, off_y):
    obj24 = static_box([int(260 - 260) + int(off_x), int(5 - 5) + int(off_y
        )], 520, 10)
    obj24.color = Color('white')
    obj24.group = 24
    obj24_image = pygame.image.load('./py-fizz-images/obj24.png')
    image_bindings.append([obj24, obj24_image])
    user_shapes.append(obj24)
    return obj24


obj24 = make_obj24(0, 0)


def image_for(s):
    global image_bindings
    for b in image_bindings:
        if b[0] == s:
            return b[1]
            _hy_anon_var_19 = None
        else:
            _hy_anon_var_19 = None
    return False


def draw_images(cosmetic):

    def f(keys):
        global user_shapes
        for s in user_shapes:
            if not image_for(s):
                continue
                _hy_anon_var_21 = None
            else:
                _hy_anon_var_21 = None
            if not cosmetic == s._cosmetic:
                continue
                _hy_anon_var_22 = None
            else:
                _hy_anon_var_22 = None
            if not s.active:
                continue
                _hy_anon_var_23 = None
            else:
                _hy_anon_var_23 = None
            if s.body:
                p = Vec2d(s.body.position.x, s.body.position.y)
                _hy_anon_var_24 = None
            else:
                p = Vec2d(s._x, s._y)
                _hy_anon_var_24 = None
            angle = 0
            if s.body:
                angle = s.body.angle
                _hy_anon_var_25 = None
            else:
                _hy_anon_var_25 = None
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
                _hy_anon_var_28 = None
            else:
                _hy_anon_var_28 = None
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
            _hy_anon_var_30 = None
        else:
            _hy_anon_var_30 = None
        screen = pygame.display.get_surface()
        pygame.draw.line(screen, Color('black'), start, end)


def clear_click(keys):
    global click_handled
    click_handled = max(0, click_handled - 1)


def game_over(is_won):
    global game_already_over
    print('Game over!')
    for f in user_shapes:
        f.damping = 0.01
    game_already_over = True
    end_screen = create_end_screen(is_won)


def check_friends_and_enemies(keys):
    global friends
    for f in friends:
        game_over(False) if not f.active and not game_already_over else None
    if 0 == len(enemies):
        return True
        _hy_anon_var_34 = None
    else:
        _hy_anon_var_34 = None
    for f in enemies:
        if f.active or game_already_over:
            return True
            _hy_anon_var_35 = None
        else:
            _hy_anon_var_35 = None
    return game_over(True)


def tick_temp_shapes(keys):
    global temp_shapes
    new_temp_shapes = []
    for f in temp_shapes:
        shape = f[0]
        time_left = f[1]
        new_time_left = time_left - 1
        f[1] = new_time_left
        deactivate(shape) if time_left < 0 else new_temp_shapes.append([
            shape, new_time_left])
    temp_shapes = new_temp_shapes


def take_final_screenshot(keys):
    return take_screenshot() if game_already_over else None


def take_screenshot():
    screen = pygame.display.get_surface()
    return pygame.image.save(screen, 'screenshot.jpg')


add_observer(tick_temp_shapes)
add_observer(clear_click)
add_observer(draw_images(True))
add_observer(draw_pivot_lines)
add_observer(draw_connection_lines)
add_observer(draw_images(False))
add_observer(check_friends_and_enemies)
add_observer(take_final_screenshot)
run()

