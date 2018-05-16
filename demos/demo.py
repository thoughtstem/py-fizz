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
obj107 = static_box([int(fraction(505, 2) - fraction(505, 2)), int(368 - 5)
    ], 505, 10)
obj107.color = Color('white')
obj107.group = 107
obj107_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj107.png')
image_bindings.append([obj107, obj107_image])
user_shapes.append(obj107)
obj109 = static_box([int(500 - 5), int(fraction(373, 2) - fraction(353, 2))
    ], 10, 353)
obj109.color = Color('white')
obj109.group = 109
obj109_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj109.png')
image_bindings.append([obj109, obj109_image])
user_shapes.append(obj109)
obj105 = cosmetic_ball([int(fraction(505, 2)), int(fraction(373, 2))],
    fraction(485, 2))
obj105.color = Color('white')
obj105.group = 105
obj105_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj105.png')
image_bindings.append([obj105, obj105_image])
user_shapes.append(obj105)
obj20 = box([int(269 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj20.color = Color('white')
obj20.group = 20
obj20_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj20.png')
image_bindings.append([obj20, obj20_image])
user_shapes.append(obj20)
obj19 = box([int(269 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj19.color = Color('white')
obj19.group = 19
obj19_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj19.png')
image_bindings.append([obj19, obj19_image])
user_shapes.append(obj19)
obj18 = box([int(269 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj18.color = Color('white')
obj18.group = 18
obj18_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj18.png')
image_bindings.append([obj18, obj18_image])
user_shapes.append(obj18)
obj17 = box([int(269 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj17.color = Color('white')
obj17.group = 17
obj17_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj17.png')
image_bindings.append([obj17, obj17_image])
user_shapes.append(obj17)
obj15 = box([int(258 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj15.color = Color('white')
obj15.group = 15
obj15_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj15.png')
image_bindings.append([obj15, obj15_image])
user_shapes.append(obj15)
obj14 = box([int(258 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj14.color = Color('white')
obj14.group = 14
obj14_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj14.png')
image_bindings.append([obj14, obj14_image])
user_shapes.append(obj14)
obj13 = box([int(258 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj13.color = Color('white')
obj13.group = 13
obj13_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj13.png')
image_bindings.append([obj13, obj13_image])
user_shapes.append(obj13)
obj12 = box([int(258 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj12.color = Color('white')
obj12.group = 12
obj12_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj12.png')
image_bindings.append([obj12, obj12_image])
user_shapes.append(obj12)
obj10 = box([int(247 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj10.color = Color('white')
obj10.group = 10
obj10_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj10.png')
image_bindings.append([obj10, obj10_image])
user_shapes.append(obj10)
obj9 = box([int(247 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj9.color = Color('white')
obj9.group = 9
obj9_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj9.png')
image_bindings.append([obj9, obj9_image])
user_shapes.append(obj9)
obj8 = box([int(247 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj8.color = Color('white')
obj8.group = 8
obj8_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj8.png')
image_bindings.append([obj8, obj8_image])
user_shapes.append(obj8)
obj7 = box([int(247 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj7.color = Color('white')
obj7.group = 7
obj7_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj7.png')
image_bindings.append([obj7, obj7_image])
user_shapes.append(obj7)
obj5 = box([int(236 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj5.color = Color('white')
obj5.group = 5
obj5_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj5.png')
image_bindings.append([obj5, obj5_image])
user_shapes.append(obj5)
obj4 = box([int(236 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj4.color = Color('white')
obj4.group = 4
obj4_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj4.png')
image_bindings.append([obj4, obj4_image])
user_shapes.append(obj4)
obj3 = box([int(236 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj3.color = Color('white')
obj3.group = 3
obj3_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj3.png')
image_bindings.append([obj3, obj3_image])
user_shapes.append(obj3)
obj2 = box([int(236 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj2.color = Color('white')
obj2.group = 2
obj2_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj2.png')
image_bindings.append([obj2, obj2_image])
user_shapes.append(obj2)
obj42 = box([int(269 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj42.color = Color('white')
obj42.group = 42
obj42_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj42.png')
image_bindings.append([obj42, obj42_image])
user_shapes.append(obj42)
obj41 = box([int(269 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj41.color = Color('white')
obj41.group = 41
obj41_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj41.png')
image_bindings.append([obj41, obj41_image])
user_shapes.append(obj41)
obj40 = box([int(269 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj40.color = Color('white')
obj40.group = 40
obj40_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj40.png')
image_bindings.append([obj40, obj40_image])
user_shapes.append(obj40)
obj39 = box([int(269 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj39.color = Color('white')
obj39.group = 39
obj39_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj39.png')
image_bindings.append([obj39, obj39_image])
user_shapes.append(obj39)
obj37 = box([int(258 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj37.color = Color('white')
obj37.group = 37
obj37_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj37.png')
image_bindings.append([obj37, obj37_image])
user_shapes.append(obj37)
obj36 = box([int(258 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj36.color = Color('white')
obj36.group = 36
obj36_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj36.png')
image_bindings.append([obj36, obj36_image])
user_shapes.append(obj36)
obj35 = box([int(258 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj35.color = Color('white')
obj35.group = 35
obj35_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj35.png')
image_bindings.append([obj35, obj35_image])
user_shapes.append(obj35)
obj34 = box([int(258 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj34.color = Color('white')
obj34.group = 34
obj34_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj34.png')
image_bindings.append([obj34, obj34_image])
user_shapes.append(obj34)
obj32 = box([int(247 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj32.color = Color('white')
obj32.group = 32
obj32_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj32.png')
image_bindings.append([obj32, obj32_image])
user_shapes.append(obj32)
obj31 = box([int(247 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj31.color = Color('white')
obj31.group = 31
obj31_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj31.png')
image_bindings.append([obj31, obj31_image])
user_shapes.append(obj31)
obj30 = box([int(247 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj30.color = Color('white')
obj30.group = 30
obj30_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj30.png')
image_bindings.append([obj30, obj30_image])
user_shapes.append(obj30)
obj29 = box([int(247 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj29.color = Color('white')
obj29.group = 29
obj29_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj29.png')
image_bindings.append([obj29, obj29_image])
user_shapes.append(obj29)
obj27 = box([int(236 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj27.color = Color('white')
obj27.group = 27
obj27_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj27.png')
image_bindings.append([obj27, obj27_image])
user_shapes.append(obj27)
obj26 = box([int(236 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj26.color = Color('white')
obj26.group = 26
obj26_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj26.png')
image_bindings.append([obj26, obj26_image])
user_shapes.append(obj26)
obj25 = box([int(236 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj25.color = Color('white')
obj25.group = 25
obj25_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj25.png')
image_bindings.append([obj25, obj25_image])
user_shapes.append(obj25)
obj24 = box([int(236 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj24.color = Color('white')
obj24.group = 24
obj24_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj24.png')
image_bindings.append([obj24, obj24_image])
user_shapes.append(obj24)
obj64 = box([int(269 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj64.color = Color('white')
obj64.group = 64
obj64_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj64.png')
image_bindings.append([obj64, obj64_image])
user_shapes.append(obj64)
obj63 = box([int(269 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj63.color = Color('white')
obj63.group = 63
obj63_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj63.png')
image_bindings.append([obj63, obj63_image])
user_shapes.append(obj63)
obj62 = box([int(269 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj62.color = Color('white')
obj62.group = 62
obj62_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj62.png')
image_bindings.append([obj62, obj62_image])
user_shapes.append(obj62)
obj61 = box([int(269 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj61.color = Color('white')
obj61.group = 61
obj61_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj61.png')
image_bindings.append([obj61, obj61_image])
user_shapes.append(obj61)
obj59 = box([int(258 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj59.color = Color('white')
obj59.group = 59
obj59_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj59.png')
image_bindings.append([obj59, obj59_image])
user_shapes.append(obj59)
obj58 = box([int(258 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj58.color = Color('white')
obj58.group = 58
obj58_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj58.png')
image_bindings.append([obj58, obj58_image])
user_shapes.append(obj58)
obj57 = box([int(258 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj57.color = Color('white')
obj57.group = 57
obj57_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj57.png')
image_bindings.append([obj57, obj57_image])
user_shapes.append(obj57)
obj56 = box([int(258 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj56.color = Color('white')
obj56.group = 56
obj56_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj56.png')
image_bindings.append([obj56, obj56_image])
user_shapes.append(obj56)
obj54 = box([int(247 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj54.color = Color('white')
obj54.group = 54
obj54_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj54.png')
image_bindings.append([obj54, obj54_image])
user_shapes.append(obj54)
obj53 = box([int(247 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj53.color = Color('white')
obj53.group = 53
obj53_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj53.png')
image_bindings.append([obj53, obj53_image])
user_shapes.append(obj53)
obj52 = box([int(247 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj52.color = Color('white')
obj52.group = 52
obj52_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj52.png')
image_bindings.append([obj52, obj52_image])
user_shapes.append(obj52)
obj51 = box([int(247 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj51.color = Color('white')
obj51.group = 51
obj51_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj51.png')
image_bindings.append([obj51, obj51_image])
user_shapes.append(obj51)
obj49 = box([int(236 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj49.color = Color('white')
obj49.group = 49
obj49_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj49.png')
image_bindings.append([obj49, obj49_image])
user_shapes.append(obj49)
obj48 = box([int(236 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj48.color = Color('white')
obj48.group = 48
obj48_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj48.png')
image_bindings.append([obj48, obj48_image])
user_shapes.append(obj48)
obj47 = box([int(236 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj47.color = Color('white')
obj47.group = 47
obj47_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj47.png')
image_bindings.append([obj47, obj47_image])
user_shapes.append(obj47)
obj46 = box([int(236 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj46.color = Color('white')
obj46.group = 46
obj46_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj46.png')
image_bindings.append([obj46, obj46_image])
user_shapes.append(obj46)
obj86 = box([int(269 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj86.color = Color('white')
obj86.group = 86
obj86_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj86.png')
image_bindings.append([obj86, obj86_image])
user_shapes.append(obj86)
obj85 = box([int(269 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj85.color = Color('white')
obj85.group = 85
obj85_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj85.png')
image_bindings.append([obj85, obj85_image])
user_shapes.append(obj85)
obj84 = box([int(269 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj84.color = Color('white')
obj84.group = 84
obj84_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj84.png')
image_bindings.append([obj84, obj84_image])
user_shapes.append(obj84)
obj83 = box([int(269 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj83.color = Color('white')
obj83.group = 83
obj83_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj83.png')
image_bindings.append([obj83, obj83_image])
user_shapes.append(obj83)
obj81 = box([int(258 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj81.color = Color('white')
obj81.group = 81
obj81_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj81.png')
image_bindings.append([obj81, obj81_image])
user_shapes.append(obj81)
obj80 = box([int(258 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj80.color = Color('white')
obj80.group = 80
obj80_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj80.png')
image_bindings.append([obj80, obj80_image])
user_shapes.append(obj80)
obj79 = box([int(258 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj79.color = Color('white')
obj79.group = 79
obj79_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj79.png')
image_bindings.append([obj79, obj79_image])
user_shapes.append(obj79)
obj78 = box([int(258 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj78.color = Color('white')
obj78.group = 78
obj78_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj78.png')
image_bindings.append([obj78, obj78_image])
user_shapes.append(obj78)
obj76 = box([int(247 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj76.color = Color('white')
obj76.group = 76
obj76_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj76.png')
image_bindings.append([obj76, obj76_image])
user_shapes.append(obj76)
obj75 = box([int(247 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj75.color = Color('white')
obj75.group = 75
obj75_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj75.png')
image_bindings.append([obj75, obj75_image])
user_shapes.append(obj75)
obj74 = box([int(247 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj74.color = Color('white')
obj74.group = 74
obj74_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj74.png')
image_bindings.append([obj74, obj74_image])
user_shapes.append(obj74)
obj73 = box([int(247 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj73.color = Color('white')
obj73.group = 73
obj73_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj73.png')
image_bindings.append([obj73, obj73_image])
user_shapes.append(obj73)
obj71 = box([int(236 - fraction(11, 2)), int(209 - fraction(15, 2))], 11, 15)
obj71.color = Color('white')
obj71.group = 71
obj71_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj71.png')
image_bindings.append([obj71, obj71_image])
user_shapes.append(obj71)
obj70 = box([int(236 - fraction(11, 2)), int(194 - fraction(15, 2))], 11, 15)
obj70.color = Color('white')
obj70.group = 70
obj70_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj70.png')
image_bindings.append([obj70, obj70_image])
user_shapes.append(obj70)
obj69 = box([int(236 - fraction(11, 2)), int(179 - fraction(15, 2))], 11, 15)
obj69.color = Color('white')
obj69.group = 69
obj69_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj69.png')
image_bindings.append([obj69, obj69_image])
user_shapes.append(obj69)
obj68 = box([int(236 - fraction(11, 2)), int(164 - fraction(15, 2))], 11, 15)
obj68.color = Color('white')
obj68.group = 68
obj68_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj68.png')
image_bindings.append([obj68, obj68_image])
user_shapes.append(obj68)
obj92 = ball([int(fraction(595, 2)), int(fraction(479, 2))], 20)
obj92.color = Color('white')
obj92.group = 92
obj92_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj92.png')
image_bindings.append([obj92, obj92_image])
user_shapes.append(obj92)
obj99 = cosmetic_ball([int(275), int(fraction(479, 2))], fraction(5, 2))
obj99.color = Color('white')
obj99.group = 99
obj99_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj99.png')
image_bindings.append([obj99, obj99_image])
user_shapes.append(obj99)
obj91 = ball([int(fraction(505, 2)), int(fraction(479, 2))], 20)
obj91.color = Color('white')
obj91.group = 91
obj91_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj91.png')
image_bindings.append([obj91, obj91_image])
user_shapes.append(obj91)
obj98 = cosmetic_ball([int(230), int(fraction(479, 2))], fraction(5, 2))
obj98.color = Color('white')
obj98.group = 98
obj98_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj98.png')
image_bindings.append([obj98, obj98_image])
user_shapes.append(obj98)
obj90 = ball([int(fraction(415, 2)), int(fraction(479, 2))], 20)
obj90.color = Color('white')
obj90.group = 90
obj90_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj90.png')
image_bindings.append([obj90, obj90_image])
user_shapes.append(obj90)
obj97 = cosmetic_ball([int(fraction(505, 2)), int(217)], fraction(5, 2))
obj97.color = Color('white')
obj97.group = 97
obj97_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj97.png')
image_bindings.append([obj97, obj97_image])
user_shapes.append(obj97)
obj96 = box([int(fraction(505, 2) - fraction(41, 2)), int(194 - fraction(41,
    2))], 41, 41)
obj96.color = Color('white')
obj96.group = 96
obj96_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj96.png')
image_bindings.append([obj96, obj96_image])
user_shapes.append(obj96)
obj67 = box([int(fraction(637, 2) - 22), int(fraction(287, 2) - 30)], 44, 60)
obj67.color = Color('white')
obj67.group = 67
obj67_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj67.png')
image_bindings.append([obj67, obj67_image])
user_shapes.append(obj67)
obj45 = box([int(fraction(549, 2) - 22), int(fraction(287, 2) - 30)], 44, 60)
obj45.color = Color('white')
obj45.group = 45
obj45_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj45.png')
image_bindings.append([obj45, obj45_image])
user_shapes.append(obj45)
obj23 = box([int(fraction(461, 2) - 22), int(fraction(287, 2) - 30)], 44, 60)
obj23.color = Color('white')
obj23.group = 23
obj23_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj23.png')
image_bindings.append([obj23, obj23_image])
user_shapes.append(obj23)
obj1 = box([int(fraction(373, 2) - 22), int(fraction(287, 2) - 30)], 44, 60)
obj1.color = Color('white')
obj1.group = 1
obj1_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj1.png')
image_bindings.append([obj1, obj1_image])
user_shapes.append(obj1)
obj109 = static_box([int(5 - 5), int(fraction(373, 2) - fraction(353, 2))],
    10, 353)
obj109.color = Color('white')
obj109.group = 109
obj109_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj109.png')
image_bindings.append([obj109, obj109_image])
user_shapes.append(obj109)
obj107 = static_box([int(fraction(505, 2) - fraction(505, 2)), int(5 - 5)],
    505, 10)
obj107.color = Color('white')
obj107.group = 107
obj107_image = pygame.image.load(
    '/Users/thoughtstem/Dev/Python/py-fizzery/obj107.png')
image_bindings.append([obj107, obj107_image])
user_shapes.append(obj107)
obj20.mass = 10
obj19.mass = 10
obj18.mass = 10
obj17.mass = 10
obj15.mass = 10
obj14.mass = 10
obj13.mass = 10
obj12.mass = 10
obj10.mass = 10
obj9.mass = 10
obj8.mass = 10
obj7.mass = 10
obj5.mass = 10
obj4.mass = 10
obj3.mass = 10
obj2.mass = 10
obj42.mass = 10
obj41.mass = 10
obj40.mass = 10
obj39.mass = 10
obj37.mass = 10
obj36.mass = 10
obj35.mass = 10
obj34.mass = 10
obj32.mass = 10
obj31.mass = 10
obj30.mass = 10
obj29.mass = 10
obj27.mass = 10
obj26.mass = 10
obj25.mass = 10
obj24.mass = 10
obj64.mass = 10
obj63.mass = 10
obj62.mass = 10
obj61.mass = 10
obj59.mass = 10
obj58.mass = 10
obj57.mass = 10
obj56.mass = 10
obj54.mass = 10
obj53.mass = 10
obj52.mass = 10
obj51.mass = 10
obj49.mass = 10
obj48.mass = 10
obj47.mass = 10
obj46.mass = 10
obj86.mass = 10
obj85.mass = 10
obj84.mass = 10
obj83.mass = 10
obj81.mass = 10
obj80.mass = 10
obj79.mass = 10
obj78.mass = 10
obj76.mass = 10
obj75.mass = 10
obj74.mass = 10
obj73.mass = 10
obj71.mass = 10
obj70.mass = 10
obj69.mass = 10
obj68.mass = 10
obj92.mass = 10
pin(obj92.body.position, obj92, obj96.body.position, obj96)
connected_shapes.append([obj92, obj96])
motor(obj92, 1)
obj91.mass = 10
pin(obj91.body.position, obj91, obj92.body.position, obj92)
connected_shapes.append([obj91, obj92])
pin(obj91.body.position, obj91, obj96.body.position, obj96)
connected_shapes.append([obj91, obj96])
motor(obj91, 1)
obj90.mass = 10
pin(obj90.body.position, obj90, obj91.body.position, obj91)
connected_shapes.append([obj90, obj91])
pin(obj90.body.position, obj90, obj96.body.position, obj96)
connected_shapes.append([obj90, obj96])
motor(obj90, 1)
obj96.mass = 10
obj96.hit([0, 0], obj96.position)
motor(obj96, 0)
obj67.mass = 10
motor(obj67, 0)
obj67.gravity = 0, -100


def on_click_67(keys):
    global obj67
    f = obj67
    p = f.body.position
    if mouse_clicked() or obj67.inside(mouse_point()):
        try:
            obj68.body.position = p[0] + obj68.body.position[0] + -1 * (w / 2
                ), p[1] + obj68.body.position[1] + -1 * (h / 2)
            _hy_anon_var_1 = None
        except:
            _hy_anon_var_1 = print('Exception')
        try:
            obj69.body.position = p[0] + obj69.body.position[0] + -1 * (w / 2
                ), p[1] + obj69.body.position[1] + -1 * (h / 2)
            _hy_anon_var_2 = None
        except:
            _hy_anon_var_2 = print('Exception')
        try:
            obj70.body.position = p[0] + obj70.body.position[0] + -1 * (w / 2
                ), p[1] + obj70.body.position[1] + -1 * (h / 2)
            _hy_anon_var_3 = None
        except:
            _hy_anon_var_3 = print('Exception')
        try:
            obj71.body.position = p[0] + obj71.body.position[0] + -1 * (w / 2
                ), p[1] + obj71.body.position[1] + -1 * (h / 2)
            _hy_anon_var_4 = None
        except:
            _hy_anon_var_4 = print('Exception')
        try:
            obj73.body.position = p[0] + obj73.body.position[0] + -1 * (w / 2
                ), p[1] + obj73.body.position[1] + -1 * (h / 2)
            _hy_anon_var_5 = None
        except:
            _hy_anon_var_5 = print('Exception')
        try:
            obj74.body.position = p[0] + obj74.body.position[0] + -1 * (w / 2
                ), p[1] + obj74.body.position[1] + -1 * (h / 2)
            _hy_anon_var_6 = None
        except:
            _hy_anon_var_6 = print('Exception')
        try:
            obj75.body.position = p[0] + obj75.body.position[0] + -1 * (w / 2
                ), p[1] + obj75.body.position[1] + -1 * (h / 2)
            _hy_anon_var_7 = None
        except:
            _hy_anon_var_7 = print('Exception')
        try:
            obj76.body.position = p[0] + obj76.body.position[0] + -1 * (w / 2
                ), p[1] + obj76.body.position[1] + -1 * (h / 2)
            _hy_anon_var_8 = None
        except:
            _hy_anon_var_8 = print('Exception')
        try:
            obj78.body.position = p[0] + obj78.body.position[0] + -1 * (w / 2
                ), p[1] + obj78.body.position[1] + -1 * (h / 2)
            _hy_anon_var_9 = None
        except:
            _hy_anon_var_9 = print('Exception')
        try:
            obj79.body.position = p[0] + obj79.body.position[0] + -1 * (w / 2
                ), p[1] + obj79.body.position[1] + -1 * (h / 2)
            _hy_anon_var_10 = None
        except:
            _hy_anon_var_10 = print('Exception')
        try:
            obj80.body.position = p[0] + obj80.body.position[0] + -1 * (w / 2
                ), p[1] + obj80.body.position[1] + -1 * (h / 2)
            _hy_anon_var_11 = None
        except:
            _hy_anon_var_11 = print('Exception')
        try:
            obj81.body.position = p[0] + obj81.body.position[0] + -1 * (w / 2
                ), p[1] + obj81.body.position[1] + -1 * (h / 2)
            _hy_anon_var_12 = None
        except:
            _hy_anon_var_12 = print('Exception')
        try:
            obj83.body.position = p[0] + obj83.body.position[0] + -1 * (w / 2
                ), p[1] + obj83.body.position[1] + -1 * (h / 2)
            _hy_anon_var_13 = None
        except:
            _hy_anon_var_13 = print('Exception')
        try:
            obj84.body.position = p[0] + obj84.body.position[0] + -1 * (w / 2
                ), p[1] + obj84.body.position[1] + -1 * (h / 2)
            _hy_anon_var_14 = None
        except:
            _hy_anon_var_14 = print('Exception')
        try:
            obj85.body.position = p[0] + obj85.body.position[0] + -1 * (w / 2
                ), p[1] + obj85.body.position[1] + -1 * (h / 2)
            _hy_anon_var_15 = None
        except:
            _hy_anon_var_15 = print('Exception')
        try:
            obj86.body.position = p[0] + obj86.body.position[0] + -1 * (w / 2
                ), p[1] + obj86.body.position[1] + -1 * (h / 2)
            _hy_anon_var_16 = None
        except:
            _hy_anon_var_16 = print('Exception')
        return True
        _hy_anon_var_17 = None
    else:
        _hy_anon_var_17 = None
    return _hy_anon_var_17


add_observer(on_click_67)
obj45.mass = 10
motor(obj45, 0)
obj45.gravity = 0, -100


def on_click_45(keys):
    global obj45
    f = obj45
    p = f.body.position
    if mouse_clicked() or obj45.inside(mouse_point()):
        try:
            obj46.body.position = p[0] + obj46.body.position[0] + -1 * (w / 2
                ), p[1] + obj46.body.position[1] + -1 * (h / 2)
            _hy_anon_var_19 = None
        except:
            _hy_anon_var_19 = print('Exception')
        try:
            obj47.body.position = p[0] + obj47.body.position[0] + -1 * (w / 2
                ), p[1] + obj47.body.position[1] + -1 * (h / 2)
            _hy_anon_var_20 = None
        except:
            _hy_anon_var_20 = print('Exception')
        try:
            obj48.body.position = p[0] + obj48.body.position[0] + -1 * (w / 2
                ), p[1] + obj48.body.position[1] + -1 * (h / 2)
            _hy_anon_var_21 = None
        except:
            _hy_anon_var_21 = print('Exception')
        try:
            obj49.body.position = p[0] + obj49.body.position[0] + -1 * (w / 2
                ), p[1] + obj49.body.position[1] + -1 * (h / 2)
            _hy_anon_var_22 = None
        except:
            _hy_anon_var_22 = print('Exception')
        try:
            obj51.body.position = p[0] + obj51.body.position[0] + -1 * (w / 2
                ), p[1] + obj51.body.position[1] + -1 * (h / 2)
            _hy_anon_var_23 = None
        except:
            _hy_anon_var_23 = print('Exception')
        try:
            obj52.body.position = p[0] + obj52.body.position[0] + -1 * (w / 2
                ), p[1] + obj52.body.position[1] + -1 * (h / 2)
            _hy_anon_var_24 = None
        except:
            _hy_anon_var_24 = print('Exception')
        try:
            obj53.body.position = p[0] + obj53.body.position[0] + -1 * (w / 2
                ), p[1] + obj53.body.position[1] + -1 * (h / 2)
            _hy_anon_var_25 = None
        except:
            _hy_anon_var_25 = print('Exception')
        try:
            obj54.body.position = p[0] + obj54.body.position[0] + -1 * (w / 2
                ), p[1] + obj54.body.position[1] + -1 * (h / 2)
            _hy_anon_var_26 = None
        except:
            _hy_anon_var_26 = print('Exception')
        try:
            obj56.body.position = p[0] + obj56.body.position[0] + -1 * (w / 2
                ), p[1] + obj56.body.position[1] + -1 * (h / 2)
            _hy_anon_var_27 = None
        except:
            _hy_anon_var_27 = print('Exception')
        try:
            obj57.body.position = p[0] + obj57.body.position[0] + -1 * (w / 2
                ), p[1] + obj57.body.position[1] + -1 * (h / 2)
            _hy_anon_var_28 = None
        except:
            _hy_anon_var_28 = print('Exception')
        try:
            obj58.body.position = p[0] + obj58.body.position[0] + -1 * (w / 2
                ), p[1] + obj58.body.position[1] + -1 * (h / 2)
            _hy_anon_var_29 = None
        except:
            _hy_anon_var_29 = print('Exception')
        try:
            obj59.body.position = p[0] + obj59.body.position[0] + -1 * (w / 2
                ), p[1] + obj59.body.position[1] + -1 * (h / 2)
            _hy_anon_var_30 = None
        except:
            _hy_anon_var_30 = print('Exception')
        try:
            obj61.body.position = p[0] + obj61.body.position[0] + -1 * (w / 2
                ), p[1] + obj61.body.position[1] + -1 * (h / 2)
            _hy_anon_var_31 = None
        except:
            _hy_anon_var_31 = print('Exception')
        try:
            obj62.body.position = p[0] + obj62.body.position[0] + -1 * (w / 2
                ), p[1] + obj62.body.position[1] + -1 * (h / 2)
            _hy_anon_var_32 = None
        except:
            _hy_anon_var_32 = print('Exception')
        try:
            obj63.body.position = p[0] + obj63.body.position[0] + -1 * (w / 2
                ), p[1] + obj63.body.position[1] + -1 * (h / 2)
            _hy_anon_var_33 = None
        except:
            _hy_anon_var_33 = print('Exception')
        try:
            obj64.body.position = p[0] + obj64.body.position[0] + -1 * (w / 2
                ), p[1] + obj64.body.position[1] + -1 * (h / 2)
            _hy_anon_var_34 = None
        except:
            _hy_anon_var_34 = print('Exception')
        return True
        _hy_anon_var_35 = None
    else:
        _hy_anon_var_35 = None
    return _hy_anon_var_35


add_observer(on_click_45)
obj23.mass = 10
motor(obj23, 0)
obj23.gravity = 0, -100


def on_click_23(keys):
    global obj23
    f = obj23
    p = f.body.position
    if mouse_clicked() or obj23.inside(mouse_point()):
        try:
            obj24.body.position = p[0] + obj24.body.position[0] + -1 * (w / 2
                ), p[1] + obj24.body.position[1] + -1 * (h / 2)
            _hy_anon_var_37 = None
        except:
            _hy_anon_var_37 = print('Exception')
        try:
            obj25.body.position = p[0] + obj25.body.position[0] + -1 * (w / 2
                ), p[1] + obj25.body.position[1] + -1 * (h / 2)
            _hy_anon_var_38 = None
        except:
            _hy_anon_var_38 = print('Exception')
        try:
            obj26.body.position = p[0] + obj26.body.position[0] + -1 * (w / 2
                ), p[1] + obj26.body.position[1] + -1 * (h / 2)
            _hy_anon_var_39 = None
        except:
            _hy_anon_var_39 = print('Exception')
        try:
            obj27.body.position = p[0] + obj27.body.position[0] + -1 * (w / 2
                ), p[1] + obj27.body.position[1] + -1 * (h / 2)
            _hy_anon_var_40 = None
        except:
            _hy_anon_var_40 = print('Exception')
        try:
            obj29.body.position = p[0] + obj29.body.position[0] + -1 * (w / 2
                ), p[1] + obj29.body.position[1] + -1 * (h / 2)
            _hy_anon_var_41 = None
        except:
            _hy_anon_var_41 = print('Exception')
        try:
            obj30.body.position = p[0] + obj30.body.position[0] + -1 * (w / 2
                ), p[1] + obj30.body.position[1] + -1 * (h / 2)
            _hy_anon_var_42 = None
        except:
            _hy_anon_var_42 = print('Exception')
        try:
            obj31.body.position = p[0] + obj31.body.position[0] + -1 * (w / 2
                ), p[1] + obj31.body.position[1] + -1 * (h / 2)
            _hy_anon_var_43 = None
        except:
            _hy_anon_var_43 = print('Exception')
        try:
            obj32.body.position = p[0] + obj32.body.position[0] + -1 * (w / 2
                ), p[1] + obj32.body.position[1] + -1 * (h / 2)
            _hy_anon_var_44 = None
        except:
            _hy_anon_var_44 = print('Exception')
        try:
            obj34.body.position = p[0] + obj34.body.position[0] + -1 * (w / 2
                ), p[1] + obj34.body.position[1] + -1 * (h / 2)
            _hy_anon_var_45 = None
        except:
            _hy_anon_var_45 = print('Exception')
        try:
            obj35.body.position = p[0] + obj35.body.position[0] + -1 * (w / 2
                ), p[1] + obj35.body.position[1] + -1 * (h / 2)
            _hy_anon_var_46 = None
        except:
            _hy_anon_var_46 = print('Exception')
        try:
            obj36.body.position = p[0] + obj36.body.position[0] + -1 * (w / 2
                ), p[1] + obj36.body.position[1] + -1 * (h / 2)
            _hy_anon_var_47 = None
        except:
            _hy_anon_var_47 = print('Exception')
        try:
            obj37.body.position = p[0] + obj37.body.position[0] + -1 * (w / 2
                ), p[1] + obj37.body.position[1] + -1 * (h / 2)
            _hy_anon_var_48 = None
        except:
            _hy_anon_var_48 = print('Exception')
        try:
            obj39.body.position = p[0] + obj39.body.position[0] + -1 * (w / 2
                ), p[1] + obj39.body.position[1] + -1 * (h / 2)
            _hy_anon_var_49 = None
        except:
            _hy_anon_var_49 = print('Exception')
        try:
            obj40.body.position = p[0] + obj40.body.position[0] + -1 * (w / 2
                ), p[1] + obj40.body.position[1] + -1 * (h / 2)
            _hy_anon_var_50 = None
        except:
            _hy_anon_var_50 = print('Exception')
        try:
            obj41.body.position = p[0] + obj41.body.position[0] + -1 * (w / 2
                ), p[1] + obj41.body.position[1] + -1 * (h / 2)
            _hy_anon_var_51 = None
        except:
            _hy_anon_var_51 = print('Exception')
        try:
            obj42.body.position = p[0] + obj42.body.position[0] + -1 * (w / 2
                ), p[1] + obj42.body.position[1] + -1 * (h / 2)
            _hy_anon_var_52 = None
        except:
            _hy_anon_var_52 = print('Exception')
        return True
        _hy_anon_var_53 = None
    else:
        _hy_anon_var_53 = None
    return _hy_anon_var_53


add_observer(on_click_23)
obj1.mass = 10
motor(obj1, 0)
obj1.gravity = 0, -100


def on_click_1(keys):
    global obj1
    f = obj1
    p = f.body.position
    if mouse_clicked() or obj1.inside(mouse_point()):
        try:
            obj2.body.position = p[0] + obj2.body.position[0] + -1 * (w / 2
                ), p[1] + obj2.body.position[1] + -1 * (h / 2)
            _hy_anon_var_55 = None
        except:
            _hy_anon_var_55 = print('Exception')
        try:
            obj3.body.position = p[0] + obj3.body.position[0] + -1 * (w / 2
                ), p[1] + obj3.body.position[1] + -1 * (h / 2)
            _hy_anon_var_56 = None
        except:
            _hy_anon_var_56 = print('Exception')
        try:
            obj4.body.position = p[0] + obj4.body.position[0] + -1 * (w / 2
                ), p[1] + obj4.body.position[1] + -1 * (h / 2)
            _hy_anon_var_57 = None
        except:
            _hy_anon_var_57 = print('Exception')
        try:
            obj5.body.position = p[0] + obj5.body.position[0] + -1 * (w / 2
                ), p[1] + obj5.body.position[1] + -1 * (h / 2)
            _hy_anon_var_58 = None
        except:
            _hy_anon_var_58 = print('Exception')
        try:
            obj7.body.position = p[0] + obj7.body.position[0] + -1 * (w / 2
                ), p[1] + obj7.body.position[1] + -1 * (h / 2)
            _hy_anon_var_59 = None
        except:
            _hy_anon_var_59 = print('Exception')
        try:
            obj8.body.position = p[0] + obj8.body.position[0] + -1 * (w / 2
                ), p[1] + obj8.body.position[1] + -1 * (h / 2)
            _hy_anon_var_60 = None
        except:
            _hy_anon_var_60 = print('Exception')
        try:
            obj9.body.position = p[0] + obj9.body.position[0] + -1 * (w / 2
                ), p[1] + obj9.body.position[1] + -1 * (h / 2)
            _hy_anon_var_61 = None
        except:
            _hy_anon_var_61 = print('Exception')
        try:
            obj10.body.position = p[0] + obj10.body.position[0] + -1 * (w / 2
                ), p[1] + obj10.body.position[1] + -1 * (h / 2)
            _hy_anon_var_62 = None
        except:
            _hy_anon_var_62 = print('Exception')
        try:
            obj12.body.position = p[0] + obj12.body.position[0] + -1 * (w / 2
                ), p[1] + obj12.body.position[1] + -1 * (h / 2)
            _hy_anon_var_63 = None
        except:
            _hy_anon_var_63 = print('Exception')
        try:
            obj13.body.position = p[0] + obj13.body.position[0] + -1 * (w / 2
                ), p[1] + obj13.body.position[1] + -1 * (h / 2)
            _hy_anon_var_64 = None
        except:
            _hy_anon_var_64 = print('Exception')
        try:
            obj14.body.position = p[0] + obj14.body.position[0] + -1 * (w / 2
                ), p[1] + obj14.body.position[1] + -1 * (h / 2)
            _hy_anon_var_65 = None
        except:
            _hy_anon_var_65 = print('Exception')
        try:
            obj15.body.position = p[0] + obj15.body.position[0] + -1 * (w / 2
                ), p[1] + obj15.body.position[1] + -1 * (h / 2)
            _hy_anon_var_66 = None
        except:
            _hy_anon_var_66 = print('Exception')
        try:
            obj17.body.position = p[0] + obj17.body.position[0] + -1 * (w / 2
                ), p[1] + obj17.body.position[1] + -1 * (h / 2)
            _hy_anon_var_67 = None
        except:
            _hy_anon_var_67 = print('Exception')
        try:
            obj18.body.position = p[0] + obj18.body.position[0] + -1 * (w / 2
                ), p[1] + obj18.body.position[1] + -1 * (h / 2)
            _hy_anon_var_68 = None
        except:
            _hy_anon_var_68 = print('Exception')
        try:
            obj19.body.position = p[0] + obj19.body.position[0] + -1 * (w / 2
                ), p[1] + obj19.body.position[1] + -1 * (h / 2)
            _hy_anon_var_69 = None
        except:
            _hy_anon_var_69 = print('Exception')
        try:
            obj20.body.position = p[0] + obj20.body.position[0] + -1 * (w / 2
                ), p[1] + obj20.body.position[1] + -1 * (h / 2)
            _hy_anon_var_70 = None
        except:
            _hy_anon_var_70 = print('Exception')
        return True
        _hy_anon_var_71 = None
    else:
        _hy_anon_var_71 = None
    return _hy_anon_var_71


add_observer(on_click_1)


def image_for(s):
    global image_bindings
    for b in image_bindings:
        if b[0] == s:
            return b[1]
            _hy_anon_var_73 = None
        else:
            _hy_anon_var_73 = None
    return False


def draw_images(cosmetic):

    def f(keys):
        global user_shapes
        for s in user_shapes:
            if not image_for(s):
                continue
                _hy_anon_var_75 = None
            else:
                _hy_anon_var_75 = None
            if not cosmetic == s._cosmetic:
                continue
                _hy_anon_var_76 = None
            else:
                _hy_anon_var_76 = None
            if not s.active:
                continue
                _hy_anon_var_77 = None
            else:
                _hy_anon_var_77 = None
            if s.body:
                p = Vec2d(s.body.position.x, s.body.position.y)
                _hy_anon_var_78 = None
            else:
                p = Vec2d(s._x, s._y)
                _hy_anon_var_78 = None
            angle = 0
            if s.body:
                angle = s.body.angle
                _hy_anon_var_79 = None
            else:
                _hy_anon_var_79 = None
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
            _hy_anon_var_83 = None
        else:
            _hy_anon_var_83 = None
        screen = pygame.display.get_surface()
        pygame.draw.line(screen, Color('black'), start, end)


add_observer(draw_images(True))
add_observer(draw_pivot_lines)
add_observer(draw_connection_lines)
add_observer(draw_images(False))
run()

