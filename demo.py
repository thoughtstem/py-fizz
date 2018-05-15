import math

import pymunk

from pyphysicssandbox import *
import pygame
from pymunk import Vec2d

w=505
h=373
window('Most Awesome Thing Ever', w, h)

user_shapes = []
image_bindings = []
pivots = []
connected_shapes = []

obj300 = static_box((int(0), int(363)), 505, 10)
obj300.color = Color("white")
obj300.group = 300
obj300_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj300.png")
image_bindings.append([obj300, obj300_image])
user_shapes.append(obj300)
obj302 = static_box((int(495), int(10)), 10, 353)
obj302.color = Color("white")
obj302.group = 302
obj302_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj302.png")
image_bindings.append([obj302, obj302_image])
user_shapes.append(obj302)
obj298 = cosmetic_ball((int(505/2), int(373/2)), 485/2)
obj298.color = Color("white")
obj298.group = 298
obj298_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj298.png")
image_bindings.append([obj298, obj298_image])
user_shapes.append(obj298)
obj287 = static_ball((int(505/2), int(639/2)), 1)
obj287.color = Color("white")
obj287.group = 287
obj287_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj287.png")
image_bindings.append([obj287, obj287_image])
user_shapes.append(obj287)
obj284 = box((int(152), int(605/2)), 201, 11)
obj284.color = Color("white")
obj284.group = 284
obj284_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj284.png")
image_bindings.append([obj284, obj284_image])
user_shapes.append(obj284)
obj280 = cosmetic_ball((int(505/2), int(308)), 21/2)
obj280.color = Color("white")
obj280.group = 280
obj280_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj280.png")
image_bindings.append([obj280, obj280_image])
user_shapes.append(obj280)
obj1 = box((int(595/2), int(475/2)), 60, 60)
obj1.color = Color("white")
obj1.group = 1
obj1_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj1.png")
image_bindings.append([obj1, obj1_image])
user_shapes.append(obj1)
obj278 = cosmetic_ball((int(655/2), int(425/2)), 25)
obj278.color = Color("white")
obj278.group = 278
obj278_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj278.png")
image_bindings.append([obj278, obj278_image])
user_shapes.append(obj278)
obj2 = ball((int(655/2), int(335/2)), 20)
obj2.color = Color("white")
obj2.group = 2
obj2_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj2.png")
image_bindings.append([obj2, obj2_image])
user_shapes.append(obj2)
obj293 = cosmetic_ball((int(445/2), int(445/2)), 75)
obj293.color = Color("white")
obj293.group = 293
obj293_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj293.png")
image_bindings.append([obj293, obj293_image])
user_shapes.append(obj293)
obj292 = cosmetic_ball((int(505/2), int(245/2)), 25)
obj292.color = Color("white")
obj292.group = 292
obj292_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj292.png")
image_bindings.append([obj292, obj292_image])
user_shapes.append(obj292)
obj290 = cosmetic_ball((int(275), int(75)), 75)
obj290.color = Color("white")
obj290.group = 290
obj290_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj290.png")
image_bindings.append([obj290, obj290_image])
user_shapes.append(obj290)
obj285 = ball((int(355/2), int(75)), 45/2)
obj285.color = Color("white")
obj285.group = 285
obj285_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj285.png")
image_bindings.append([obj285, obj285_image])
user_shapes.append(obj285)
obj274 = box((int(561/2), int(429/2)), 4, 4)
obj274.color = Color("white")
obj274.group = 274
obj274_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj274.png")
image_bindings.append([obj274, obj274_image])
user_shapes.append(obj274)
obj273 = box((int(561/2), int(421/2)), 4, 4)
obj273.color = Color("white")
obj273.group = 273
obj273_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj273.png")
image_bindings.append([obj273, obj273_image])
user_shapes.append(obj273)
obj272 = box((int(561/2), int(413/2)), 4, 4)
obj272.color = Color("white")
obj272.group = 272
obj272_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj272.png")
image_bindings.append([obj272, obj272_image])
user_shapes.append(obj272)
obj271 = box((int(561/2), int(405/2)), 4, 4)
obj271.color = Color("white")
obj271.group = 271
obj271_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj271.png")
image_bindings.append([obj271, obj271_image])
user_shapes.append(obj271)
obj270 = box((int(561/2), int(397/2)), 4, 4)
obj270.color = Color("white")
obj270.group = 270
obj270_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj270.png")
image_bindings.append([obj270, obj270_image])
user_shapes.append(obj270)
obj269 = box((int(561/2), int(389/2)), 4, 4)
obj269.color = Color("white")
obj269.group = 269
obj269_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj269.png")
image_bindings.append([obj269, obj269_image])
user_shapes.append(obj269)
obj268 = box((int(561/2), int(381/2)), 4, 4)
obj268.color = Color("white")
obj268.group = 268
obj268_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj268.png")
image_bindings.append([obj268, obj268_image])
user_shapes.append(obj268)
obj267 = box((int(561/2), int(373/2)), 4, 4)
obj267.color = Color("white")
obj267.group = 267
obj267_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj267.png")
image_bindings.append([obj267, obj267_image])
user_shapes.append(obj267)
obj266 = box((int(561/2), int(365/2)), 4, 4)
obj266.color = Color("white")
obj266.group = 266
obj266_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj266.png")
image_bindings.append([obj266, obj266_image])
user_shapes.append(obj266)
obj265 = box((int(561/2), int(357/2)), 4, 4)
obj265.color = Color("white")
obj265.group = 265
obj265_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj265.png")
image_bindings.append([obj265, obj265_image])
user_shapes.append(obj265)
obj264 = box((int(561/2), int(349/2)), 4, 4)
obj264.color = Color("white")
obj264.group = 264
obj264_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj264.png")
image_bindings.append([obj264, obj264_image])
user_shapes.append(obj264)
obj263 = box((int(561/2), int(341/2)), 4, 4)
obj263.color = Color("white")
obj263.group = 263
obj263_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj263.png")
image_bindings.append([obj263, obj263_image])
user_shapes.append(obj263)
obj262 = box((int(561/2), int(333/2)), 4, 4)
obj262.color = Color("white")
obj262.group = 262
obj262_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj262.png")
image_bindings.append([obj262, obj262_image])
user_shapes.append(obj262)
obj261 = box((int(561/2), int(325/2)), 4, 4)
obj261.color = Color("white")
obj261.group = 261
obj261_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj261.png")
image_bindings.append([obj261, obj261_image])
user_shapes.append(obj261)
obj260 = box((int(561/2), int(317/2)), 4, 4)
obj260.color = Color("white")
obj260.group = 260
obj260_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj260.png")
image_bindings.append([obj260, obj260_image])
user_shapes.append(obj260)
obj259 = box((int(561/2), int(309/2)), 4, 4)
obj259.color = Color("white")
obj259.group = 259
obj259_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj259.png")
image_bindings.append([obj259, obj259_image])
user_shapes.append(obj259)
obj257 = box((int(553/2), int(429/2)), 4, 4)
obj257.color = Color("white")
obj257.group = 257
obj257_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj257.png")
image_bindings.append([obj257, obj257_image])
user_shapes.append(obj257)
obj256 = box((int(553/2), int(421/2)), 4, 4)
obj256.color = Color("white")
obj256.group = 256
obj256_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj256.png")
image_bindings.append([obj256, obj256_image])
user_shapes.append(obj256)
obj255 = box((int(553/2), int(413/2)), 4, 4)
obj255.color = Color("white")
obj255.group = 255
obj255_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj255.png")
image_bindings.append([obj255, obj255_image])
user_shapes.append(obj255)
obj254 = box((int(553/2), int(405/2)), 4, 4)
obj254.color = Color("white")
obj254.group = 254
obj254_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj254.png")
image_bindings.append([obj254, obj254_image])
user_shapes.append(obj254)
obj253 = box((int(553/2), int(397/2)), 4, 4)
obj253.color = Color("white")
obj253.group = 253
obj253_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj253.png")
image_bindings.append([obj253, obj253_image])
user_shapes.append(obj253)
obj252 = box((int(553/2), int(389/2)), 4, 4)
obj252.color = Color("white")
obj252.group = 252
obj252_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj252.png")
image_bindings.append([obj252, obj252_image])
user_shapes.append(obj252)
obj251 = box((int(553/2), int(381/2)), 4, 4)
obj251.color = Color("white")
obj251.group = 251
obj251_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj251.png")
image_bindings.append([obj251, obj251_image])
user_shapes.append(obj251)
obj250 = box((int(553/2), int(373/2)), 4, 4)
obj250.color = Color("white")
obj250.group = 250
obj250_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj250.png")
image_bindings.append([obj250, obj250_image])
user_shapes.append(obj250)
obj249 = box((int(553/2), int(365/2)), 4, 4)
obj249.color = Color("white")
obj249.group = 249
obj249_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj249.png")
image_bindings.append([obj249, obj249_image])
user_shapes.append(obj249)
obj248 = box((int(553/2), int(357/2)), 4, 4)
obj248.color = Color("white")
obj248.group = 248
obj248_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj248.png")
image_bindings.append([obj248, obj248_image])
user_shapes.append(obj248)
obj247 = box((int(553/2), int(349/2)), 4, 4)
obj247.color = Color("white")
obj247.group = 247
obj247_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj247.png")
image_bindings.append([obj247, obj247_image])
user_shapes.append(obj247)
obj246 = box((int(553/2), int(341/2)), 4, 4)
obj246.color = Color("white")
obj246.group = 246
obj246_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj246.png")
image_bindings.append([obj246, obj246_image])
user_shapes.append(obj246)
obj245 = box((int(553/2), int(333/2)), 4, 4)
obj245.color = Color("white")
obj245.group = 245
obj245_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj245.png")
image_bindings.append([obj245, obj245_image])
user_shapes.append(obj245)
obj244 = box((int(553/2), int(325/2)), 4, 4)
obj244.color = Color("white")
obj244.group = 244
obj244_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj244.png")
image_bindings.append([obj244, obj244_image])
user_shapes.append(obj244)
obj243 = box((int(553/2), int(317/2)), 4, 4)
obj243.color = Color("white")
obj243.group = 243
obj243_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj243.png")
image_bindings.append([obj243, obj243_image])
user_shapes.append(obj243)
obj242 = box((int(553/2), int(309/2)), 4, 4)
obj242.color = Color("white")
obj242.group = 242
obj242_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj242.png")
image_bindings.append([obj242, obj242_image])
user_shapes.append(obj242)
obj240 = box((int(545/2), int(429/2)), 4, 4)
obj240.color = Color("white")
obj240.group = 240
obj240_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj240.png")
image_bindings.append([obj240, obj240_image])
user_shapes.append(obj240)
obj239 = box((int(545/2), int(421/2)), 4, 4)
obj239.color = Color("white")
obj239.group = 239
obj239_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj239.png")
image_bindings.append([obj239, obj239_image])
user_shapes.append(obj239)
obj238 = box((int(545/2), int(413/2)), 4, 4)
obj238.color = Color("white")
obj238.group = 238
obj238_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj238.png")
image_bindings.append([obj238, obj238_image])
user_shapes.append(obj238)
obj237 = box((int(545/2), int(405/2)), 4, 4)
obj237.color = Color("white")
obj237.group = 237
obj237_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj237.png")
image_bindings.append([obj237, obj237_image])
user_shapes.append(obj237)
obj236 = box((int(545/2), int(397/2)), 4, 4)
obj236.color = Color("white")
obj236.group = 236
obj236_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj236.png")
image_bindings.append([obj236, obj236_image])
user_shapes.append(obj236)
obj235 = box((int(545/2), int(389/2)), 4, 4)
obj235.color = Color("white")
obj235.group = 235
obj235_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj235.png")
image_bindings.append([obj235, obj235_image])
user_shapes.append(obj235)
obj234 = box((int(545/2), int(381/2)), 4, 4)
obj234.color = Color("white")
obj234.group = 234
obj234_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj234.png")
image_bindings.append([obj234, obj234_image])
user_shapes.append(obj234)
obj233 = box((int(545/2), int(373/2)), 4, 4)
obj233.color = Color("white")
obj233.group = 233
obj233_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj233.png")
image_bindings.append([obj233, obj233_image])
user_shapes.append(obj233)
obj232 = box((int(545/2), int(365/2)), 4, 4)
obj232.color = Color("white")
obj232.group = 232
obj232_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj232.png")
image_bindings.append([obj232, obj232_image])
user_shapes.append(obj232)
obj231 = box((int(545/2), int(357/2)), 4, 4)
obj231.color = Color("white")
obj231.group = 231
obj231_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj231.png")
image_bindings.append([obj231, obj231_image])
user_shapes.append(obj231)
obj230 = box((int(545/2), int(349/2)), 4, 4)
obj230.color = Color("white")
obj230.group = 230
obj230_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj230.png")
image_bindings.append([obj230, obj230_image])
user_shapes.append(obj230)
obj229 = box((int(545/2), int(341/2)), 4, 4)
obj229.color = Color("white")
obj229.group = 229
obj229_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj229.png")
image_bindings.append([obj229, obj229_image])
user_shapes.append(obj229)
obj228 = box((int(545/2), int(333/2)), 4, 4)
obj228.color = Color("white")
obj228.group = 228
obj228_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj228.png")
image_bindings.append([obj228, obj228_image])
user_shapes.append(obj228)
obj227 = box((int(545/2), int(325/2)), 4, 4)
obj227.color = Color("white")
obj227.group = 227
obj227_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj227.png")
image_bindings.append([obj227, obj227_image])
user_shapes.append(obj227)
obj226 = box((int(545/2), int(317/2)), 4, 4)
obj226.color = Color("white")
obj226.group = 226
obj226_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj226.png")
image_bindings.append([obj226, obj226_image])
user_shapes.append(obj226)
obj225 = box((int(545/2), int(309/2)), 4, 4)
obj225.color = Color("white")
obj225.group = 225
obj225_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj225.png")
image_bindings.append([obj225, obj225_image])
user_shapes.append(obj225)
obj223 = box((int(537/2), int(429/2)), 4, 4)
obj223.color = Color("white")
obj223.group = 223
obj223_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj223.png")
image_bindings.append([obj223, obj223_image])
user_shapes.append(obj223)
obj222 = box((int(537/2), int(421/2)), 4, 4)
obj222.color = Color("white")
obj222.group = 222
obj222_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj222.png")
image_bindings.append([obj222, obj222_image])
user_shapes.append(obj222)
obj221 = box((int(537/2), int(413/2)), 4, 4)
obj221.color = Color("white")
obj221.group = 221
obj221_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj221.png")
image_bindings.append([obj221, obj221_image])
user_shapes.append(obj221)
obj220 = box((int(537/2), int(405/2)), 4, 4)
obj220.color = Color("white")
obj220.group = 220
obj220_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj220.png")
image_bindings.append([obj220, obj220_image])
user_shapes.append(obj220)
obj219 = box((int(537/2), int(397/2)), 4, 4)
obj219.color = Color("white")
obj219.group = 219
obj219_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj219.png")
image_bindings.append([obj219, obj219_image])
user_shapes.append(obj219)
obj218 = box((int(537/2), int(389/2)), 4, 4)
obj218.color = Color("white")
obj218.group = 218
obj218_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj218.png")
image_bindings.append([obj218, obj218_image])
user_shapes.append(obj218)
obj217 = box((int(537/2), int(381/2)), 4, 4)
obj217.color = Color("white")
obj217.group = 217
obj217_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj217.png")
image_bindings.append([obj217, obj217_image])
user_shapes.append(obj217)
obj216 = box((int(537/2), int(373/2)), 4, 4)
obj216.color = Color("white")
obj216.group = 216
obj216_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj216.png")
image_bindings.append([obj216, obj216_image])
user_shapes.append(obj216)
obj215 = box((int(537/2), int(365/2)), 4, 4)
obj215.color = Color("white")
obj215.group = 215
obj215_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj215.png")
image_bindings.append([obj215, obj215_image])
user_shapes.append(obj215)
obj214 = box((int(537/2), int(357/2)), 4, 4)
obj214.color = Color("white")
obj214.group = 214
obj214_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj214.png")
image_bindings.append([obj214, obj214_image])
user_shapes.append(obj214)
obj213 = box((int(537/2), int(349/2)), 4, 4)
obj213.color = Color("white")
obj213.group = 213
obj213_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj213.png")
image_bindings.append([obj213, obj213_image])
user_shapes.append(obj213)
obj212 = box((int(537/2), int(341/2)), 4, 4)
obj212.color = Color("white")
obj212.group = 212
obj212_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj212.png")
image_bindings.append([obj212, obj212_image])
user_shapes.append(obj212)
obj211 = box((int(537/2), int(333/2)), 4, 4)
obj211.color = Color("white")
obj211.group = 211
obj211_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj211.png")
image_bindings.append([obj211, obj211_image])
user_shapes.append(obj211)
obj210 = box((int(537/2), int(325/2)), 4, 4)
obj210.color = Color("white")
obj210.group = 210
obj210_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj210.png")
image_bindings.append([obj210, obj210_image])
user_shapes.append(obj210)
obj209 = box((int(537/2), int(317/2)), 4, 4)
obj209.color = Color("white")
obj209.group = 209
obj209_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj209.png")
image_bindings.append([obj209, obj209_image])
user_shapes.append(obj209)
obj208 = box((int(537/2), int(309/2)), 4, 4)
obj208.color = Color("white")
obj208.group = 208
obj208_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj208.png")
image_bindings.append([obj208, obj208_image])
user_shapes.append(obj208)
obj206 = box((int(529/2), int(429/2)), 4, 4)
obj206.color = Color("white")
obj206.group = 206
obj206_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj206.png")
image_bindings.append([obj206, obj206_image])
user_shapes.append(obj206)
obj205 = box((int(529/2), int(421/2)), 4, 4)
obj205.color = Color("white")
obj205.group = 205
obj205_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj205.png")
image_bindings.append([obj205, obj205_image])
user_shapes.append(obj205)
obj204 = box((int(529/2), int(413/2)), 4, 4)
obj204.color = Color("white")
obj204.group = 204
obj204_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj204.png")
image_bindings.append([obj204, obj204_image])
user_shapes.append(obj204)
obj203 = box((int(529/2), int(405/2)), 4, 4)
obj203.color = Color("white")
obj203.group = 203
obj203_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj203.png")
image_bindings.append([obj203, obj203_image])
user_shapes.append(obj203)
obj202 = box((int(529/2), int(397/2)), 4, 4)
obj202.color = Color("white")
obj202.group = 202
obj202_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj202.png")
image_bindings.append([obj202, obj202_image])
user_shapes.append(obj202)
obj201 = box((int(529/2), int(389/2)), 4, 4)
obj201.color = Color("white")
obj201.group = 201
obj201_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj201.png")
image_bindings.append([obj201, obj201_image])
user_shapes.append(obj201)
obj200 = box((int(529/2), int(381/2)), 4, 4)
obj200.color = Color("white")
obj200.group = 200
obj200_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj200.png")
image_bindings.append([obj200, obj200_image])
user_shapes.append(obj200)
obj199 = box((int(529/2), int(373/2)), 4, 4)
obj199.color = Color("white")
obj199.group = 199
obj199_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj199.png")
image_bindings.append([obj199, obj199_image])
user_shapes.append(obj199)
obj198 = box((int(529/2), int(365/2)), 4, 4)
obj198.color = Color("white")
obj198.group = 198
obj198_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj198.png")
image_bindings.append([obj198, obj198_image])
user_shapes.append(obj198)
obj197 = box((int(529/2), int(357/2)), 4, 4)
obj197.color = Color("white")
obj197.group = 197
obj197_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj197.png")
image_bindings.append([obj197, obj197_image])
user_shapes.append(obj197)
obj196 = box((int(529/2), int(349/2)), 4, 4)
obj196.color = Color("white")
obj196.group = 196
obj196_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj196.png")
image_bindings.append([obj196, obj196_image])
user_shapes.append(obj196)
obj195 = box((int(529/2), int(341/2)), 4, 4)
obj195.color = Color("white")
obj195.group = 195
obj195_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj195.png")
image_bindings.append([obj195, obj195_image])
user_shapes.append(obj195)
obj194 = box((int(529/2), int(333/2)), 4, 4)
obj194.color = Color("white")
obj194.group = 194
obj194_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj194.png")
image_bindings.append([obj194, obj194_image])
user_shapes.append(obj194)
obj193 = box((int(529/2), int(325/2)), 4, 4)
obj193.color = Color("white")
obj193.group = 193
obj193_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj193.png")
image_bindings.append([obj193, obj193_image])
user_shapes.append(obj193)
obj192 = box((int(529/2), int(317/2)), 4, 4)
obj192.color = Color("white")
obj192.group = 192
obj192_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj192.png")
image_bindings.append([obj192, obj192_image])
user_shapes.append(obj192)
obj191 = box((int(529/2), int(309/2)), 4, 4)
obj191.color = Color("white")
obj191.group = 191
obj191_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj191.png")
image_bindings.append([obj191, obj191_image])
user_shapes.append(obj191)
obj189 = box((int(521/2), int(429/2)), 4, 4)
obj189.color = Color("white")
obj189.group = 189
obj189_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj189.png")
image_bindings.append([obj189, obj189_image])
user_shapes.append(obj189)
obj188 = box((int(521/2), int(421/2)), 4, 4)
obj188.color = Color("white")
obj188.group = 188
obj188_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj188.png")
image_bindings.append([obj188, obj188_image])
user_shapes.append(obj188)
obj187 = box((int(521/2), int(413/2)), 4, 4)
obj187.color = Color("white")
obj187.group = 187
obj187_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj187.png")
image_bindings.append([obj187, obj187_image])
user_shapes.append(obj187)
obj186 = box((int(521/2), int(405/2)), 4, 4)
obj186.color = Color("white")
obj186.group = 186
obj186_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj186.png")
image_bindings.append([obj186, obj186_image])
user_shapes.append(obj186)
obj185 = box((int(521/2), int(397/2)), 4, 4)
obj185.color = Color("white")
obj185.group = 185
obj185_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj185.png")
image_bindings.append([obj185, obj185_image])
user_shapes.append(obj185)
obj184 = box((int(521/2), int(389/2)), 4, 4)
obj184.color = Color("white")
obj184.group = 184
obj184_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj184.png")
image_bindings.append([obj184, obj184_image])
user_shapes.append(obj184)
obj183 = box((int(521/2), int(381/2)), 4, 4)
obj183.color = Color("white")
obj183.group = 183
obj183_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj183.png")
image_bindings.append([obj183, obj183_image])
user_shapes.append(obj183)
obj182 = box((int(521/2), int(373/2)), 4, 4)
obj182.color = Color("white")
obj182.group = 182
obj182_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj182.png")
image_bindings.append([obj182, obj182_image])
user_shapes.append(obj182)
obj181 = box((int(521/2), int(365/2)), 4, 4)
obj181.color = Color("white")
obj181.group = 181
obj181_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj181.png")
image_bindings.append([obj181, obj181_image])
user_shapes.append(obj181)
obj180 = box((int(521/2), int(357/2)), 4, 4)
obj180.color = Color("white")
obj180.group = 180
obj180_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj180.png")
image_bindings.append([obj180, obj180_image])
user_shapes.append(obj180)
obj179 = box((int(521/2), int(349/2)), 4, 4)
obj179.color = Color("white")
obj179.group = 179
obj179_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj179.png")
image_bindings.append([obj179, obj179_image])
user_shapes.append(obj179)
obj178 = box((int(521/2), int(341/2)), 4, 4)
obj178.color = Color("white")
obj178.group = 178
obj178_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj178.png")
image_bindings.append([obj178, obj178_image])
user_shapes.append(obj178)
obj177 = box((int(521/2), int(333/2)), 4, 4)
obj177.color = Color("white")
obj177.group = 177
obj177_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj177.png")
image_bindings.append([obj177, obj177_image])
user_shapes.append(obj177)
obj176 = box((int(521/2), int(325/2)), 4, 4)
obj176.color = Color("white")
obj176.group = 176
obj176_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj176.png")
image_bindings.append([obj176, obj176_image])
user_shapes.append(obj176)
obj175 = box((int(521/2), int(317/2)), 4, 4)
obj175.color = Color("white")
obj175.group = 175
obj175_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj175.png")
image_bindings.append([obj175, obj175_image])
user_shapes.append(obj175)
obj174 = box((int(521/2), int(309/2)), 4, 4)
obj174.color = Color("white")
obj174.group = 174
obj174_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj174.png")
image_bindings.append([obj174, obj174_image])
user_shapes.append(obj174)
obj172 = box((int(513/2), int(429/2)), 4, 4)
obj172.color = Color("white")
obj172.group = 172
obj172_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj172.png")
image_bindings.append([obj172, obj172_image])
user_shapes.append(obj172)
obj171 = box((int(513/2), int(421/2)), 4, 4)
obj171.color = Color("white")
obj171.group = 171
obj171_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj171.png")
image_bindings.append([obj171, obj171_image])
user_shapes.append(obj171)
obj170 = box((int(513/2), int(413/2)), 4, 4)
obj170.color = Color("white")
obj170.group = 170
obj170_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj170.png")
image_bindings.append([obj170, obj170_image])
user_shapes.append(obj170)
obj169 = box((int(513/2), int(405/2)), 4, 4)
obj169.color = Color("white")
obj169.group = 169
obj169_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj169.png")
image_bindings.append([obj169, obj169_image])
user_shapes.append(obj169)
obj168 = box((int(513/2), int(397/2)), 4, 4)
obj168.color = Color("white")
obj168.group = 168
obj168_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj168.png")
image_bindings.append([obj168, obj168_image])
user_shapes.append(obj168)
obj167 = box((int(513/2), int(389/2)), 4, 4)
obj167.color = Color("white")
obj167.group = 167
obj167_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj167.png")
image_bindings.append([obj167, obj167_image])
user_shapes.append(obj167)
obj166 = box((int(513/2), int(381/2)), 4, 4)
obj166.color = Color("white")
obj166.group = 166
obj166_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj166.png")
image_bindings.append([obj166, obj166_image])
user_shapes.append(obj166)
obj165 = box((int(513/2), int(373/2)), 4, 4)
obj165.color = Color("white")
obj165.group = 165
obj165_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj165.png")
image_bindings.append([obj165, obj165_image])
user_shapes.append(obj165)
obj164 = box((int(513/2), int(365/2)), 4, 4)
obj164.color = Color("white")
obj164.group = 164
obj164_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj164.png")
image_bindings.append([obj164, obj164_image])
user_shapes.append(obj164)
obj163 = box((int(513/2), int(357/2)), 4, 4)
obj163.color = Color("white")
obj163.group = 163
obj163_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj163.png")
image_bindings.append([obj163, obj163_image])
user_shapes.append(obj163)
obj162 = box((int(513/2), int(349/2)), 4, 4)
obj162.color = Color("white")
obj162.group = 162
obj162_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj162.png")
image_bindings.append([obj162, obj162_image])
user_shapes.append(obj162)
obj161 = box((int(513/2), int(341/2)), 4, 4)
obj161.color = Color("white")
obj161.group = 161
obj161_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj161.png")
image_bindings.append([obj161, obj161_image])
user_shapes.append(obj161)
obj160 = box((int(513/2), int(333/2)), 4, 4)
obj160.color = Color("white")
obj160.group = 160
obj160_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj160.png")
image_bindings.append([obj160, obj160_image])
user_shapes.append(obj160)
obj159 = box((int(513/2), int(325/2)), 4, 4)
obj159.color = Color("white")
obj159.group = 159
obj159_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj159.png")
image_bindings.append([obj159, obj159_image])
user_shapes.append(obj159)
obj158 = box((int(513/2), int(317/2)), 4, 4)
obj158.color = Color("white")
obj158.group = 158
obj158_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj158.png")
image_bindings.append([obj158, obj158_image])
user_shapes.append(obj158)
obj157 = box((int(513/2), int(309/2)), 4, 4)
obj157.color = Color("white")
obj157.group = 157
obj157_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj157.png")
image_bindings.append([obj157, obj157_image])
user_shapes.append(obj157)
obj155 = box((int(505/2), int(429/2)), 4, 4)
obj155.color = Color("white")
obj155.group = 155
obj155_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj155.png")
image_bindings.append([obj155, obj155_image])
user_shapes.append(obj155)
obj154 = box((int(505/2), int(421/2)), 4, 4)
obj154.color = Color("white")
obj154.group = 154
obj154_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj154.png")
image_bindings.append([obj154, obj154_image])
user_shapes.append(obj154)
obj153 = box((int(505/2), int(413/2)), 4, 4)
obj153.color = Color("white")
obj153.group = 153
obj153_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj153.png")
image_bindings.append([obj153, obj153_image])
user_shapes.append(obj153)
obj152 = box((int(505/2), int(405/2)), 4, 4)
obj152.color = Color("white")
obj152.group = 152
obj152_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj152.png")
image_bindings.append([obj152, obj152_image])
user_shapes.append(obj152)
obj151 = box((int(505/2), int(397/2)), 4, 4)
obj151.color = Color("white")
obj151.group = 151
obj151_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj151.png")
image_bindings.append([obj151, obj151_image])
user_shapes.append(obj151)
obj150 = box((int(505/2), int(389/2)), 4, 4)
obj150.color = Color("white")
obj150.group = 150
obj150_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj150.png")
image_bindings.append([obj150, obj150_image])
user_shapes.append(obj150)
obj149 = box((int(505/2), int(381/2)), 4, 4)
obj149.color = Color("white")
obj149.group = 149
obj149_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj149.png")
image_bindings.append([obj149, obj149_image])
user_shapes.append(obj149)
obj148 = box((int(505/2), int(373/2)), 4, 4)
obj148.color = Color("white")
obj148.group = 148
obj148_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj148.png")
image_bindings.append([obj148, obj148_image])
user_shapes.append(obj148)
obj147 = box((int(505/2), int(365/2)), 4, 4)
obj147.color = Color("white")
obj147.group = 147
obj147_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj147.png")
image_bindings.append([obj147, obj147_image])
user_shapes.append(obj147)
obj146 = box((int(505/2), int(357/2)), 4, 4)
obj146.color = Color("white")
obj146.group = 146
obj146_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj146.png")
image_bindings.append([obj146, obj146_image])
user_shapes.append(obj146)
obj145 = box((int(505/2), int(349/2)), 4, 4)
obj145.color = Color("white")
obj145.group = 145
obj145_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj145.png")
image_bindings.append([obj145, obj145_image])
user_shapes.append(obj145)
obj144 = box((int(505/2), int(341/2)), 4, 4)
obj144.color = Color("white")
obj144.group = 144
obj144_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj144.png")
image_bindings.append([obj144, obj144_image])
user_shapes.append(obj144)
obj143 = box((int(505/2), int(333/2)), 4, 4)
obj143.color = Color("white")
obj143.group = 143
obj143_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj143.png")
image_bindings.append([obj143, obj143_image])
user_shapes.append(obj143)
obj142 = box((int(505/2), int(325/2)), 4, 4)
obj142.color = Color("white")
obj142.group = 142
obj142_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj142.png")
image_bindings.append([obj142, obj142_image])
user_shapes.append(obj142)
obj141 = box((int(505/2), int(317/2)), 4, 4)
obj141.color = Color("white")
obj141.group = 141
obj141_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj141.png")
image_bindings.append([obj141, obj141_image])
user_shapes.append(obj141)
obj140 = box((int(505/2), int(309/2)), 4, 4)
obj140.color = Color("white")
obj140.group = 140
obj140_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj140.png")
image_bindings.append([obj140, obj140_image])
user_shapes.append(obj140)
obj138 = box((int(497/2), int(429/2)), 4, 4)
obj138.color = Color("white")
obj138.group = 138
obj138_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj138.png")
image_bindings.append([obj138, obj138_image])
user_shapes.append(obj138)
obj137 = box((int(497/2), int(421/2)), 4, 4)
obj137.color = Color("white")
obj137.group = 137
obj137_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj137.png")
image_bindings.append([obj137, obj137_image])
user_shapes.append(obj137)
obj136 = box((int(497/2), int(413/2)), 4, 4)
obj136.color = Color("white")
obj136.group = 136
obj136_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj136.png")
image_bindings.append([obj136, obj136_image])
user_shapes.append(obj136)
obj135 = box((int(497/2), int(405/2)), 4, 4)
obj135.color = Color("white")
obj135.group = 135
obj135_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj135.png")
image_bindings.append([obj135, obj135_image])
user_shapes.append(obj135)
obj134 = box((int(497/2), int(397/2)), 4, 4)
obj134.color = Color("white")
obj134.group = 134
obj134_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj134.png")
image_bindings.append([obj134, obj134_image])
user_shapes.append(obj134)
obj133 = box((int(497/2), int(389/2)), 4, 4)
obj133.color = Color("white")
obj133.group = 133
obj133_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj133.png")
image_bindings.append([obj133, obj133_image])
user_shapes.append(obj133)
obj132 = box((int(497/2), int(381/2)), 4, 4)
obj132.color = Color("white")
obj132.group = 132
obj132_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj132.png")
image_bindings.append([obj132, obj132_image])
user_shapes.append(obj132)
obj131 = box((int(497/2), int(373/2)), 4, 4)
obj131.color = Color("white")
obj131.group = 131
obj131_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj131.png")
image_bindings.append([obj131, obj131_image])
user_shapes.append(obj131)
obj130 = box((int(497/2), int(365/2)), 4, 4)
obj130.color = Color("white")
obj130.group = 130
obj130_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj130.png")
image_bindings.append([obj130, obj130_image])
user_shapes.append(obj130)
obj129 = box((int(497/2), int(357/2)), 4, 4)
obj129.color = Color("white")
obj129.group = 129
obj129_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj129.png")
image_bindings.append([obj129, obj129_image])
user_shapes.append(obj129)
obj128 = box((int(497/2), int(349/2)), 4, 4)
obj128.color = Color("white")
obj128.group = 128
obj128_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj128.png")
image_bindings.append([obj128, obj128_image])
user_shapes.append(obj128)
obj127 = box((int(497/2), int(341/2)), 4, 4)
obj127.color = Color("white")
obj127.group = 127
obj127_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj127.png")
image_bindings.append([obj127, obj127_image])
user_shapes.append(obj127)
obj126 = box((int(497/2), int(333/2)), 4, 4)
obj126.color = Color("white")
obj126.group = 126
obj126_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj126.png")
image_bindings.append([obj126, obj126_image])
user_shapes.append(obj126)
obj125 = box((int(497/2), int(325/2)), 4, 4)
obj125.color = Color("white")
obj125.group = 125
obj125_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj125.png")
image_bindings.append([obj125, obj125_image])
user_shapes.append(obj125)
obj124 = box((int(497/2), int(317/2)), 4, 4)
obj124.color = Color("white")
obj124.group = 124
obj124_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj124.png")
image_bindings.append([obj124, obj124_image])
user_shapes.append(obj124)
obj123 = box((int(497/2), int(309/2)), 4, 4)
obj123.color = Color("white")
obj123.group = 123
obj123_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj123.png")
image_bindings.append([obj123, obj123_image])
user_shapes.append(obj123)
obj121 = box((int(489/2), int(429/2)), 4, 4)
obj121.color = Color("white")
obj121.group = 121
obj121_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj121.png")
image_bindings.append([obj121, obj121_image])
user_shapes.append(obj121)
obj120 = box((int(489/2), int(421/2)), 4, 4)
obj120.color = Color("white")
obj120.group = 120
obj120_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj120.png")
image_bindings.append([obj120, obj120_image])
user_shapes.append(obj120)
obj119 = box((int(489/2), int(413/2)), 4, 4)
obj119.color = Color("white")
obj119.group = 119
obj119_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj119.png")
image_bindings.append([obj119, obj119_image])
user_shapes.append(obj119)
obj118 = box((int(489/2), int(405/2)), 4, 4)
obj118.color = Color("white")
obj118.group = 118
obj118_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj118.png")
image_bindings.append([obj118, obj118_image])
user_shapes.append(obj118)
obj117 = box((int(489/2), int(397/2)), 4, 4)
obj117.color = Color("white")
obj117.group = 117
obj117_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj117.png")
image_bindings.append([obj117, obj117_image])
user_shapes.append(obj117)
obj116 = box((int(489/2), int(389/2)), 4, 4)
obj116.color = Color("white")
obj116.group = 116
obj116_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj116.png")
image_bindings.append([obj116, obj116_image])
user_shapes.append(obj116)
obj115 = box((int(489/2), int(381/2)), 4, 4)
obj115.color = Color("white")
obj115.group = 115
obj115_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj115.png")
image_bindings.append([obj115, obj115_image])
user_shapes.append(obj115)
obj114 = box((int(489/2), int(373/2)), 4, 4)
obj114.color = Color("white")
obj114.group = 114
obj114_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj114.png")
image_bindings.append([obj114, obj114_image])
user_shapes.append(obj114)
obj113 = box((int(489/2), int(365/2)), 4, 4)
obj113.color = Color("white")
obj113.group = 113
obj113_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj113.png")
image_bindings.append([obj113, obj113_image])
user_shapes.append(obj113)
obj112 = box((int(489/2), int(357/2)), 4, 4)
obj112.color = Color("white")
obj112.group = 112
obj112_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj112.png")
image_bindings.append([obj112, obj112_image])
user_shapes.append(obj112)
obj111 = box((int(489/2), int(349/2)), 4, 4)
obj111.color = Color("white")
obj111.group = 111
obj111_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj111.png")
image_bindings.append([obj111, obj111_image])
user_shapes.append(obj111)
obj110 = box((int(489/2), int(341/2)), 4, 4)
obj110.color = Color("white")
obj110.group = 110
obj110_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj110.png")
image_bindings.append([obj110, obj110_image])
user_shapes.append(obj110)
obj109 = box((int(489/2), int(333/2)), 4, 4)
obj109.color = Color("white")
obj109.group = 109
obj109_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj109.png")
image_bindings.append([obj109, obj109_image])
user_shapes.append(obj109)
obj108 = box((int(489/2), int(325/2)), 4, 4)
obj108.color = Color("white")
obj108.group = 108
obj108_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj108.png")
image_bindings.append([obj108, obj108_image])
user_shapes.append(obj108)
obj107 = box((int(489/2), int(317/2)), 4, 4)
obj107.color = Color("white")
obj107.group = 107
obj107_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj107.png")
image_bindings.append([obj107, obj107_image])
user_shapes.append(obj107)
obj106 = box((int(489/2), int(309/2)), 4, 4)
obj106.color = Color("white")
obj106.group = 106
obj106_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj106.png")
image_bindings.append([obj106, obj106_image])
user_shapes.append(obj106)
obj104 = box((int(481/2), int(429/2)), 4, 4)
obj104.color = Color("white")
obj104.group = 104
obj104_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj104.png")
image_bindings.append([obj104, obj104_image])
user_shapes.append(obj104)
obj103 = box((int(481/2), int(421/2)), 4, 4)
obj103.color = Color("white")
obj103.group = 103
obj103_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj103.png")
image_bindings.append([obj103, obj103_image])
user_shapes.append(obj103)
obj102 = box((int(481/2), int(413/2)), 4, 4)
obj102.color = Color("white")
obj102.group = 102
obj102_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj102.png")
image_bindings.append([obj102, obj102_image])
user_shapes.append(obj102)
obj101 = box((int(481/2), int(405/2)), 4, 4)
obj101.color = Color("white")
obj101.group = 101
obj101_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj101.png")
image_bindings.append([obj101, obj101_image])
user_shapes.append(obj101)
obj100 = box((int(481/2), int(397/2)), 4, 4)
obj100.color = Color("white")
obj100.group = 100
obj100_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj100.png")
image_bindings.append([obj100, obj100_image])
user_shapes.append(obj100)
obj99 = box((int(481/2), int(389/2)), 4, 4)
obj99.color = Color("white")
obj99.group = 99
obj99_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj99.png")
image_bindings.append([obj99, obj99_image])
user_shapes.append(obj99)
obj98 = box((int(481/2), int(381/2)), 4, 4)
obj98.color = Color("white")
obj98.group = 98
obj98_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj98.png")
image_bindings.append([obj98, obj98_image])
user_shapes.append(obj98)
obj97 = box((int(481/2), int(373/2)), 4, 4)
obj97.color = Color("white")
obj97.group = 97
obj97_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj97.png")
image_bindings.append([obj97, obj97_image])
user_shapes.append(obj97)
obj96 = box((int(481/2), int(365/2)), 4, 4)
obj96.color = Color("white")
obj96.group = 96
obj96_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj96.png")
image_bindings.append([obj96, obj96_image])
user_shapes.append(obj96)
obj95 = box((int(481/2), int(357/2)), 4, 4)
obj95.color = Color("white")
obj95.group = 95
obj95_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj95.png")
image_bindings.append([obj95, obj95_image])
user_shapes.append(obj95)
obj94 = box((int(481/2), int(349/2)), 4, 4)
obj94.color = Color("white")
obj94.group = 94
obj94_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj94.png")
image_bindings.append([obj94, obj94_image])
user_shapes.append(obj94)
obj93 = box((int(481/2), int(341/2)), 4, 4)
obj93.color = Color("white")
obj93.group = 93
obj93_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj93.png")
image_bindings.append([obj93, obj93_image])
user_shapes.append(obj93)
obj92 = box((int(481/2), int(333/2)), 4, 4)
obj92.color = Color("white")
obj92.group = 92
obj92_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj92.png")
image_bindings.append([obj92, obj92_image])
user_shapes.append(obj92)
obj91 = box((int(481/2), int(325/2)), 4, 4)
obj91.color = Color("white")
obj91.group = 91
obj91_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj91.png")
image_bindings.append([obj91, obj91_image])
user_shapes.append(obj91)
obj90 = box((int(481/2), int(317/2)), 4, 4)
obj90.color = Color("white")
obj90.group = 90
obj90_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj90.png")
image_bindings.append([obj90, obj90_image])
user_shapes.append(obj90)
obj89 = box((int(481/2), int(309/2)), 4, 4)
obj89.color = Color("white")
obj89.group = 89
obj89_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj89.png")
image_bindings.append([obj89, obj89_image])
user_shapes.append(obj89)
obj87 = box((int(473/2), int(429/2)), 4, 4)
obj87.color = Color("white")
obj87.group = 87
obj87_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj87.png")
image_bindings.append([obj87, obj87_image])
user_shapes.append(obj87)
obj86 = box((int(473/2), int(421/2)), 4, 4)
obj86.color = Color("white")
obj86.group = 86
obj86_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj86.png")
image_bindings.append([obj86, obj86_image])
user_shapes.append(obj86)
obj85 = box((int(473/2), int(413/2)), 4, 4)
obj85.color = Color("white")
obj85.group = 85
obj85_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj85.png")
image_bindings.append([obj85, obj85_image])
user_shapes.append(obj85)
obj84 = box((int(473/2), int(405/2)), 4, 4)
obj84.color = Color("white")
obj84.group = 84
obj84_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj84.png")
image_bindings.append([obj84, obj84_image])
user_shapes.append(obj84)
obj83 = box((int(473/2), int(397/2)), 4, 4)
obj83.color = Color("white")
obj83.group = 83
obj83_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj83.png")
image_bindings.append([obj83, obj83_image])
user_shapes.append(obj83)
obj82 = box((int(473/2), int(389/2)), 4, 4)
obj82.color = Color("white")
obj82.group = 82
obj82_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj82.png")
image_bindings.append([obj82, obj82_image])
user_shapes.append(obj82)
obj81 = box((int(473/2), int(381/2)), 4, 4)
obj81.color = Color("white")
obj81.group = 81
obj81_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj81.png")
image_bindings.append([obj81, obj81_image])
user_shapes.append(obj81)
obj80 = box((int(473/2), int(373/2)), 4, 4)
obj80.color = Color("white")
obj80.group = 80
obj80_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj80.png")
image_bindings.append([obj80, obj80_image])
user_shapes.append(obj80)
obj79 = box((int(473/2), int(365/2)), 4, 4)
obj79.color = Color("white")
obj79.group = 79
obj79_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj79.png")
image_bindings.append([obj79, obj79_image])
user_shapes.append(obj79)
obj78 = box((int(473/2), int(357/2)), 4, 4)
obj78.color = Color("white")
obj78.group = 78
obj78_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj78.png")
image_bindings.append([obj78, obj78_image])
user_shapes.append(obj78)
obj77 = box((int(473/2), int(349/2)), 4, 4)
obj77.color = Color("white")
obj77.group = 77
obj77_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj77.png")
image_bindings.append([obj77, obj77_image])
user_shapes.append(obj77)
obj76 = box((int(473/2), int(341/2)), 4, 4)
obj76.color = Color("white")
obj76.group = 76
obj76_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj76.png")
image_bindings.append([obj76, obj76_image])
user_shapes.append(obj76)
obj75 = box((int(473/2), int(333/2)), 4, 4)
obj75.color = Color("white")
obj75.group = 75
obj75_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj75.png")
image_bindings.append([obj75, obj75_image])
user_shapes.append(obj75)
obj74 = box((int(473/2), int(325/2)), 4, 4)
obj74.color = Color("white")
obj74.group = 74
obj74_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj74.png")
image_bindings.append([obj74, obj74_image])
user_shapes.append(obj74)
obj73 = box((int(473/2), int(317/2)), 4, 4)
obj73.color = Color("white")
obj73.group = 73
obj73_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj73.png")
image_bindings.append([obj73, obj73_image])
user_shapes.append(obj73)
obj72 = box((int(473/2), int(309/2)), 4, 4)
obj72.color = Color("white")
obj72.group = 72
obj72_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj72.png")
image_bindings.append([obj72, obj72_image])
user_shapes.append(obj72)
obj70 = box((int(465/2), int(429/2)), 4, 4)
obj70.color = Color("white")
obj70.group = 70
obj70_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj70.png")
image_bindings.append([obj70, obj70_image])
user_shapes.append(obj70)
obj69 = box((int(465/2), int(421/2)), 4, 4)
obj69.color = Color("white")
obj69.group = 69
obj69_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj69.png")
image_bindings.append([obj69, obj69_image])
user_shapes.append(obj69)
obj68 = box((int(465/2), int(413/2)), 4, 4)
obj68.color = Color("white")
obj68.group = 68
obj68_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj68.png")
image_bindings.append([obj68, obj68_image])
user_shapes.append(obj68)
obj67 = box((int(465/2), int(405/2)), 4, 4)
obj67.color = Color("white")
obj67.group = 67
obj67_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj67.png")
image_bindings.append([obj67, obj67_image])
user_shapes.append(obj67)
obj66 = box((int(465/2), int(397/2)), 4, 4)
obj66.color = Color("white")
obj66.group = 66
obj66_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj66.png")
image_bindings.append([obj66, obj66_image])
user_shapes.append(obj66)
obj65 = box((int(465/2), int(389/2)), 4, 4)
obj65.color = Color("white")
obj65.group = 65
obj65_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj65.png")
image_bindings.append([obj65, obj65_image])
user_shapes.append(obj65)
obj64 = box((int(465/2), int(381/2)), 4, 4)
obj64.color = Color("white")
obj64.group = 64
obj64_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj64.png")
image_bindings.append([obj64, obj64_image])
user_shapes.append(obj64)
obj63 = box((int(465/2), int(373/2)), 4, 4)
obj63.color = Color("white")
obj63.group = 63
obj63_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj63.png")
image_bindings.append([obj63, obj63_image])
user_shapes.append(obj63)
obj62 = box((int(465/2), int(365/2)), 4, 4)
obj62.color = Color("white")
obj62.group = 62
obj62_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj62.png")
image_bindings.append([obj62, obj62_image])
user_shapes.append(obj62)
obj61 = box((int(465/2), int(357/2)), 4, 4)
obj61.color = Color("white")
obj61.group = 61
obj61_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj61.png")
image_bindings.append([obj61, obj61_image])
user_shapes.append(obj61)
obj60 = box((int(465/2), int(349/2)), 4, 4)
obj60.color = Color("white")
obj60.group = 60
obj60_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj60.png")
image_bindings.append([obj60, obj60_image])
user_shapes.append(obj60)
obj59 = box((int(465/2), int(341/2)), 4, 4)
obj59.color = Color("white")
obj59.group = 59
obj59_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj59.png")
image_bindings.append([obj59, obj59_image])
user_shapes.append(obj59)
obj58 = box((int(465/2), int(333/2)), 4, 4)
obj58.color = Color("white")
obj58.group = 58
obj58_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj58.png")
image_bindings.append([obj58, obj58_image])
user_shapes.append(obj58)
obj57 = box((int(465/2), int(325/2)), 4, 4)
obj57.color = Color("white")
obj57.group = 57
obj57_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj57.png")
image_bindings.append([obj57, obj57_image])
user_shapes.append(obj57)
obj56 = box((int(465/2), int(317/2)), 4, 4)
obj56.color = Color("white")
obj56.group = 56
obj56_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj56.png")
image_bindings.append([obj56, obj56_image])
user_shapes.append(obj56)
obj55 = box((int(465/2), int(309/2)), 4, 4)
obj55.color = Color("white")
obj55.group = 55
obj55_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj55.png")
image_bindings.append([obj55, obj55_image])
user_shapes.append(obj55)
obj53 = box((int(457/2), int(429/2)), 4, 4)
obj53.color = Color("white")
obj53.group = 53
obj53_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj53.png")
image_bindings.append([obj53, obj53_image])
user_shapes.append(obj53)
obj52 = box((int(457/2), int(421/2)), 4, 4)
obj52.color = Color("white")
obj52.group = 52
obj52_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj52.png")
image_bindings.append([obj52, obj52_image])
user_shapes.append(obj52)
obj51 = box((int(457/2), int(413/2)), 4, 4)
obj51.color = Color("white")
obj51.group = 51
obj51_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj51.png")
image_bindings.append([obj51, obj51_image])
user_shapes.append(obj51)
obj50 = box((int(457/2), int(405/2)), 4, 4)
obj50.color = Color("white")
obj50.group = 50
obj50_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj50.png")
image_bindings.append([obj50, obj50_image])
user_shapes.append(obj50)
obj49 = box((int(457/2), int(397/2)), 4, 4)
obj49.color = Color("white")
obj49.group = 49
obj49_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj49.png")
image_bindings.append([obj49, obj49_image])
user_shapes.append(obj49)
obj48 = box((int(457/2), int(389/2)), 4, 4)
obj48.color = Color("white")
obj48.group = 48
obj48_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj48.png")
image_bindings.append([obj48, obj48_image])
user_shapes.append(obj48)
obj47 = box((int(457/2), int(381/2)), 4, 4)
obj47.color = Color("white")
obj47.group = 47
obj47_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj47.png")
image_bindings.append([obj47, obj47_image])
user_shapes.append(obj47)
obj46 = box((int(457/2), int(373/2)), 4, 4)
obj46.color = Color("white")
obj46.group = 46
obj46_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj46.png")
image_bindings.append([obj46, obj46_image])
user_shapes.append(obj46)
obj45 = box((int(457/2), int(365/2)), 4, 4)
obj45.color = Color("white")
obj45.group = 45
obj45_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj45.png")
image_bindings.append([obj45, obj45_image])
user_shapes.append(obj45)
obj44 = box((int(457/2), int(357/2)), 4, 4)
obj44.color = Color("white")
obj44.group = 44
obj44_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj44.png")
image_bindings.append([obj44, obj44_image])
user_shapes.append(obj44)
obj43 = box((int(457/2), int(349/2)), 4, 4)
obj43.color = Color("white")
obj43.group = 43
obj43_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj43.png")
image_bindings.append([obj43, obj43_image])
user_shapes.append(obj43)
obj42 = box((int(457/2), int(341/2)), 4, 4)
obj42.color = Color("white")
obj42.group = 42
obj42_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj42.png")
image_bindings.append([obj42, obj42_image])
user_shapes.append(obj42)
obj41 = box((int(457/2), int(333/2)), 4, 4)
obj41.color = Color("white")
obj41.group = 41
obj41_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj41.png")
image_bindings.append([obj41, obj41_image])
user_shapes.append(obj41)
obj40 = box((int(457/2), int(325/2)), 4, 4)
obj40.color = Color("white")
obj40.group = 40
obj40_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj40.png")
image_bindings.append([obj40, obj40_image])
user_shapes.append(obj40)
obj39 = box((int(457/2), int(317/2)), 4, 4)
obj39.color = Color("white")
obj39.group = 39
obj39_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj39.png")
image_bindings.append([obj39, obj39_image])
user_shapes.append(obj39)
obj38 = box((int(457/2), int(309/2)), 4, 4)
obj38.color = Color("white")
obj38.group = 38
obj38_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj38.png")
image_bindings.append([obj38, obj38_image])
user_shapes.append(obj38)
obj36 = box((int(449/2), int(429/2)), 4, 4)
obj36.color = Color("white")
obj36.group = 36
obj36_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj36.png")
image_bindings.append([obj36, obj36_image])
user_shapes.append(obj36)
obj35 = box((int(449/2), int(421/2)), 4, 4)
obj35.color = Color("white")
obj35.group = 35
obj35_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj35.png")
image_bindings.append([obj35, obj35_image])
user_shapes.append(obj35)
obj34 = box((int(449/2), int(413/2)), 4, 4)
obj34.color = Color("white")
obj34.group = 34
obj34_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj34.png")
image_bindings.append([obj34, obj34_image])
user_shapes.append(obj34)
obj33 = box((int(449/2), int(405/2)), 4, 4)
obj33.color = Color("white")
obj33.group = 33
obj33_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj33.png")
image_bindings.append([obj33, obj33_image])
user_shapes.append(obj33)
obj32 = box((int(449/2), int(397/2)), 4, 4)
obj32.color = Color("white")
obj32.group = 32
obj32_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj32.png")
image_bindings.append([obj32, obj32_image])
user_shapes.append(obj32)
obj31 = box((int(449/2), int(389/2)), 4, 4)
obj31.color = Color("white")
obj31.group = 31
obj31_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj31.png")
image_bindings.append([obj31, obj31_image])
user_shapes.append(obj31)
obj30 = box((int(449/2), int(381/2)), 4, 4)
obj30.color = Color("white")
obj30.group = 30
obj30_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj30.png")
image_bindings.append([obj30, obj30_image])
user_shapes.append(obj30)
obj29 = box((int(449/2), int(373/2)), 4, 4)
obj29.color = Color("white")
obj29.group = 29
obj29_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj29.png")
image_bindings.append([obj29, obj29_image])
user_shapes.append(obj29)
obj28 = box((int(449/2), int(365/2)), 4, 4)
obj28.color = Color("white")
obj28.group = 28
obj28_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj28.png")
image_bindings.append([obj28, obj28_image])
user_shapes.append(obj28)
obj27 = box((int(449/2), int(357/2)), 4, 4)
obj27.color = Color("white")
obj27.group = 27
obj27_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj27.png")
image_bindings.append([obj27, obj27_image])
user_shapes.append(obj27)
obj26 = box((int(449/2), int(349/2)), 4, 4)
obj26.color = Color("white")
obj26.group = 26
obj26_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj26.png")
image_bindings.append([obj26, obj26_image])
user_shapes.append(obj26)
obj25 = box((int(449/2), int(341/2)), 4, 4)
obj25.color = Color("white")
obj25.group = 25
obj25_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj25.png")
image_bindings.append([obj25, obj25_image])
user_shapes.append(obj25)
obj24 = box((int(449/2), int(333/2)), 4, 4)
obj24.color = Color("white")
obj24.group = 24
obj24_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj24.png")
image_bindings.append([obj24, obj24_image])
user_shapes.append(obj24)
obj23 = box((int(449/2), int(325/2)), 4, 4)
obj23.color = Color("white")
obj23.group = 23
obj23_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj23.png")
image_bindings.append([obj23, obj23_image])
user_shapes.append(obj23)
obj22 = box((int(449/2), int(317/2)), 4, 4)
obj22.color = Color("white")
obj22.group = 22
obj22_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj22.png")
image_bindings.append([obj22, obj22_image])
user_shapes.append(obj22)
obj21 = box((int(449/2), int(309/2)), 4, 4)
obj21.color = Color("white")
obj21.group = 21
obj21_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj21.png")
image_bindings.append([obj21, obj21_image])
user_shapes.append(obj21)
obj19 = box((int(441/2), int(429/2)), 4, 4)
obj19.color = Color("white")
obj19.group = 19
obj19_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj19.png")
image_bindings.append([obj19, obj19_image])
user_shapes.append(obj19)
obj18 = box((int(441/2), int(421/2)), 4, 4)
obj18.color = Color("white")
obj18.group = 18
obj18_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj18.png")
image_bindings.append([obj18, obj18_image])
user_shapes.append(obj18)
obj17 = box((int(441/2), int(413/2)), 4, 4)
obj17.color = Color("white")
obj17.group = 17
obj17_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj17.png")
image_bindings.append([obj17, obj17_image])
user_shapes.append(obj17)
obj16 = box((int(441/2), int(405/2)), 4, 4)
obj16.color = Color("white")
obj16.group = 16
obj16_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj16.png")
image_bindings.append([obj16, obj16_image])
user_shapes.append(obj16)
obj15 = box((int(441/2), int(397/2)), 4, 4)
obj15.color = Color("white")
obj15.group = 15
obj15_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj15.png")
image_bindings.append([obj15, obj15_image])
user_shapes.append(obj15)
obj14 = box((int(441/2), int(389/2)), 4, 4)
obj14.color = Color("white")
obj14.group = 14
obj14_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj14.png")
image_bindings.append([obj14, obj14_image])
user_shapes.append(obj14)
obj13 = box((int(441/2), int(381/2)), 4, 4)
obj13.color = Color("white")
obj13.group = 13
obj13_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj13.png")
image_bindings.append([obj13, obj13_image])
user_shapes.append(obj13)
obj12 = box((int(441/2), int(373/2)), 4, 4)
obj12.color = Color("white")
obj12.group = 12
obj12_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj12.png")
image_bindings.append([obj12, obj12_image])
user_shapes.append(obj12)
obj11 = box((int(441/2), int(365/2)), 4, 4)
obj11.color = Color("white")
obj11.group = 11
obj11_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj11.png")
image_bindings.append([obj11, obj11_image])
user_shapes.append(obj11)
obj10 = box((int(441/2), int(357/2)), 4, 4)
obj10.color = Color("white")
obj10.group = 10
obj10_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj10.png")
image_bindings.append([obj10, obj10_image])
user_shapes.append(obj10)
obj9 = box((int(441/2), int(349/2)), 4, 4)
obj9.color = Color("white")
obj9.group = 9
obj9_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj9.png")
image_bindings.append([obj9, obj9_image])
user_shapes.append(obj9)
obj8 = box((int(441/2), int(341/2)), 4, 4)
obj8.color = Color("white")
obj8.group = 8
obj8_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj8.png")
image_bindings.append([obj8, obj8_image])
user_shapes.append(obj8)
obj7 = box((int(441/2), int(333/2)), 4, 4)
obj7.color = Color("white")
obj7.group = 7
obj7_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj7.png")
image_bindings.append([obj7, obj7_image])
user_shapes.append(obj7)
obj6 = box((int(441/2), int(325/2)), 4, 4)
obj6.color = Color("white")
obj6.group = 6
obj6_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj6.png")
image_bindings.append([obj6, obj6_image])
user_shapes.append(obj6)
obj5 = box((int(441/2), int(317/2)), 4, 4)
obj5.color = Color("white")
obj5.group = 5
obj5_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj5.png")
image_bindings.append([obj5, obj5_image])
user_shapes.append(obj5)
obj4 = box((int(441/2), int(309/2)), 4, 4)
obj4.color = Color("white")
obj4.group = 4
obj4_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj4.png")
image_bindings.append([obj4, obj4_image])
user_shapes.append(obj4)
obj302 = static_box((int(0), int(10)), 10, 353)
obj302.color = Color("white")
obj302.group = 302
obj302_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj302.png")
image_bindings.append([obj302, obj302_image])
user_shapes.append(obj302)
obj300 = static_box((int(0), int(0)), 505, 10)
obj300.color = Color("white")
obj300.group = 300
obj300_image = pygame.image.load("/Users/thoughtstem/Dev/Python/py-fizzery/obj300.png")
image_bindings.append([obj300, obj300_image])
user_shapes.append(obj300)



rotary_spring(obj287, obj284, 0, 100000000, 0)
obj284.mass = 10
pivot280 = pivot((505/2,308))
pivots.append(pivot280)
pivot280.connect(obj284)
obj1.mass = 10
def on_collide_1_2(f,s,p):
  try:
    obj4.body.position=(p[0]+obj4.body.position[0]-w/2, p[1]+obj4.body.position[1]-h/2)
    print('HERE')
    reactivate(obj4)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj5.body.position=(p[0]+obj5.body.position[0]-w/2, p[1]+obj5.body.position[1]-h/2)
    print('HERE')
    reactivate(obj5)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj6.body.position=(p[0]+obj6.body.position[0]-w/2, p[1]+obj6.body.position[1]-h/2)
    print('HERE')
    reactivate(obj6)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj7.body.position=(p[0]+obj7.body.position[0]-w/2, p[1]+obj7.body.position[1]-h/2)
    print('HERE')
    reactivate(obj7)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj8.body.position=(p[0]+obj8.body.position[0]-w/2, p[1]+obj8.body.position[1]-h/2)
    print('HERE')
    reactivate(obj8)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj9.body.position=(p[0]+obj9.body.position[0]-w/2, p[1]+obj9.body.position[1]-h/2)
    print('HERE')
    reactivate(obj9)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj10.body.position=(p[0]+obj10.body.position[0]-w/2, p[1]+obj10.body.position[1]-h/2)
    print('HERE')
    reactivate(obj10)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj11.body.position=(p[0]+obj11.body.position[0]-w/2, p[1]+obj11.body.position[1]-h/2)
    print('HERE')
    reactivate(obj11)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj12.body.position=(p[0]+obj12.body.position[0]-w/2, p[1]+obj12.body.position[1]-h/2)
    print('HERE')
    reactivate(obj12)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj13.body.position=(p[0]+obj13.body.position[0]-w/2, p[1]+obj13.body.position[1]-h/2)
    print('HERE')
    reactivate(obj13)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj14.body.position=(p[0]+obj14.body.position[0]-w/2, p[1]+obj14.body.position[1]-h/2)
    print('HERE')
    reactivate(obj14)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj15.body.position=(p[0]+obj15.body.position[0]-w/2, p[1]+obj15.body.position[1]-h/2)
    print('HERE')
    reactivate(obj15)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj16.body.position=(p[0]+obj16.body.position[0]-w/2, p[1]+obj16.body.position[1]-h/2)
    print('HERE')
    reactivate(obj16)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj17.body.position=(p[0]+obj17.body.position[0]-w/2, p[1]+obj17.body.position[1]-h/2)
    print('HERE')
    reactivate(obj17)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj18.body.position=(p[0]+obj18.body.position[0]-w/2, p[1]+obj18.body.position[1]-h/2)
    print('HERE')
    reactivate(obj18)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj19.body.position=(p[0]+obj19.body.position[0]-w/2, p[1]+obj19.body.position[1]-h/2)
    print('HERE')
    reactivate(obj19)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj21.body.position=(p[0]+obj21.body.position[0]-w/2, p[1]+obj21.body.position[1]-h/2)
    print('HERE')
    reactivate(obj21)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj22.body.position=(p[0]+obj22.body.position[0]-w/2, p[1]+obj22.body.position[1]-h/2)
    print('HERE')
    reactivate(obj22)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj23.body.position=(p[0]+obj23.body.position[0]-w/2, p[1]+obj23.body.position[1]-h/2)
    print('HERE')
    reactivate(obj23)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj24.body.position=(p[0]+obj24.body.position[0]-w/2, p[1]+obj24.body.position[1]-h/2)
    print('HERE')
    reactivate(obj24)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj25.body.position=(p[0]+obj25.body.position[0]-w/2, p[1]+obj25.body.position[1]-h/2)
    print('HERE')
    reactivate(obj25)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj26.body.position=(p[0]+obj26.body.position[0]-w/2, p[1]+obj26.body.position[1]-h/2)
    print('HERE')
    reactivate(obj26)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj27.body.position=(p[0]+obj27.body.position[0]-w/2, p[1]+obj27.body.position[1]-h/2)
    print('HERE')
    reactivate(obj27)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj28.body.position=(p[0]+obj28.body.position[0]-w/2, p[1]+obj28.body.position[1]-h/2)
    print('HERE')
    reactivate(obj28)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj29.body.position=(p[0]+obj29.body.position[0]-w/2, p[1]+obj29.body.position[1]-h/2)
    print('HERE')
    reactivate(obj29)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj30.body.position=(p[0]+obj30.body.position[0]-w/2, p[1]+obj30.body.position[1]-h/2)
    print('HERE')
    reactivate(obj30)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj31.body.position=(p[0]+obj31.body.position[0]-w/2, p[1]+obj31.body.position[1]-h/2)
    print('HERE')
    reactivate(obj31)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj32.body.position=(p[0]+obj32.body.position[0]-w/2, p[1]+obj32.body.position[1]-h/2)
    print('HERE')
    reactivate(obj32)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj33.body.position=(p[0]+obj33.body.position[0]-w/2, p[1]+obj33.body.position[1]-h/2)
    print('HERE')
    reactivate(obj33)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj34.body.position=(p[0]+obj34.body.position[0]-w/2, p[1]+obj34.body.position[1]-h/2)
    print('HERE')
    reactivate(obj34)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj35.body.position=(p[0]+obj35.body.position[0]-w/2, p[1]+obj35.body.position[1]-h/2)
    print('HERE')
    reactivate(obj35)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj36.body.position=(p[0]+obj36.body.position[0]-w/2, p[1]+obj36.body.position[1]-h/2)
    print('HERE')
    reactivate(obj36)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj38.body.position=(p[0]+obj38.body.position[0]-w/2, p[1]+obj38.body.position[1]-h/2)
    print('HERE')
    reactivate(obj38)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj39.body.position=(p[0]+obj39.body.position[0]-w/2, p[1]+obj39.body.position[1]-h/2)
    print('HERE')
    reactivate(obj39)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj40.body.position=(p[0]+obj40.body.position[0]-w/2, p[1]+obj40.body.position[1]-h/2)
    print('HERE')
    reactivate(obj40)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj41.body.position=(p[0]+obj41.body.position[0]-w/2, p[1]+obj41.body.position[1]-h/2)
    print('HERE')
    reactivate(obj41)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj42.body.position=(p[0]+obj42.body.position[0]-w/2, p[1]+obj42.body.position[1]-h/2)
    print('HERE')
    reactivate(obj42)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj43.body.position=(p[0]+obj43.body.position[0]-w/2, p[1]+obj43.body.position[1]-h/2)
    print('HERE')
    reactivate(obj43)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj44.body.position=(p[0]+obj44.body.position[0]-w/2, p[1]+obj44.body.position[1]-h/2)
    print('HERE')
    reactivate(obj44)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj45.body.position=(p[0]+obj45.body.position[0]-w/2, p[1]+obj45.body.position[1]-h/2)
    print('HERE')
    reactivate(obj45)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj46.body.position=(p[0]+obj46.body.position[0]-w/2, p[1]+obj46.body.position[1]-h/2)
    print('HERE')
    reactivate(obj46)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj47.body.position=(p[0]+obj47.body.position[0]-w/2, p[1]+obj47.body.position[1]-h/2)
    print('HERE')
    reactivate(obj47)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj48.body.position=(p[0]+obj48.body.position[0]-w/2, p[1]+obj48.body.position[1]-h/2)
    print('HERE')
    reactivate(obj48)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj49.body.position=(p[0]+obj49.body.position[0]-w/2, p[1]+obj49.body.position[1]-h/2)
    print('HERE')
    reactivate(obj49)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj50.body.position=(p[0]+obj50.body.position[0]-w/2, p[1]+obj50.body.position[1]-h/2)
    print('HERE')
    reactivate(obj50)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj51.body.position=(p[0]+obj51.body.position[0]-w/2, p[1]+obj51.body.position[1]-h/2)
    print('HERE')
    reactivate(obj51)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj52.body.position=(p[0]+obj52.body.position[0]-w/2, p[1]+obj52.body.position[1]-h/2)
    print('HERE')
    reactivate(obj52)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj53.body.position=(p[0]+obj53.body.position[0]-w/2, p[1]+obj53.body.position[1]-h/2)
    print('HERE')
    reactivate(obj53)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj55.body.position=(p[0]+obj55.body.position[0]-w/2, p[1]+obj55.body.position[1]-h/2)
    print('HERE')
    reactivate(obj55)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj56.body.position=(p[0]+obj56.body.position[0]-w/2, p[1]+obj56.body.position[1]-h/2)
    print('HERE')
    reactivate(obj56)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj57.body.position=(p[0]+obj57.body.position[0]-w/2, p[1]+obj57.body.position[1]-h/2)
    print('HERE')
    reactivate(obj57)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj58.body.position=(p[0]+obj58.body.position[0]-w/2, p[1]+obj58.body.position[1]-h/2)
    print('HERE')
    reactivate(obj58)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj59.body.position=(p[0]+obj59.body.position[0]-w/2, p[1]+obj59.body.position[1]-h/2)
    print('HERE')
    reactivate(obj59)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj60.body.position=(p[0]+obj60.body.position[0]-w/2, p[1]+obj60.body.position[1]-h/2)
    print('HERE')
    reactivate(obj60)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj61.body.position=(p[0]+obj61.body.position[0]-w/2, p[1]+obj61.body.position[1]-h/2)
    print('HERE')
    reactivate(obj61)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj62.body.position=(p[0]+obj62.body.position[0]-w/2, p[1]+obj62.body.position[1]-h/2)
    print('HERE')
    reactivate(obj62)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj63.body.position=(p[0]+obj63.body.position[0]-w/2, p[1]+obj63.body.position[1]-h/2)
    print('HERE')
    reactivate(obj63)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj64.body.position=(p[0]+obj64.body.position[0]-w/2, p[1]+obj64.body.position[1]-h/2)
    print('HERE')
    reactivate(obj64)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj65.body.position=(p[0]+obj65.body.position[0]-w/2, p[1]+obj65.body.position[1]-h/2)
    print('HERE')
    reactivate(obj65)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj66.body.position=(p[0]+obj66.body.position[0]-w/2, p[1]+obj66.body.position[1]-h/2)
    print('HERE')
    reactivate(obj66)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj67.body.position=(p[0]+obj67.body.position[0]-w/2, p[1]+obj67.body.position[1]-h/2)
    print('HERE')
    reactivate(obj67)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj68.body.position=(p[0]+obj68.body.position[0]-w/2, p[1]+obj68.body.position[1]-h/2)
    print('HERE')
    reactivate(obj68)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj69.body.position=(p[0]+obj69.body.position[0]-w/2, p[1]+obj69.body.position[1]-h/2)
    print('HERE')
    reactivate(obj69)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj70.body.position=(p[0]+obj70.body.position[0]-w/2, p[1]+obj70.body.position[1]-h/2)
    print('HERE')
    reactivate(obj70)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj72.body.position=(p[0]+obj72.body.position[0]-w/2, p[1]+obj72.body.position[1]-h/2)
    print('HERE')
    reactivate(obj72)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj73.body.position=(p[0]+obj73.body.position[0]-w/2, p[1]+obj73.body.position[1]-h/2)
    print('HERE')
    reactivate(obj73)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj74.body.position=(p[0]+obj74.body.position[0]-w/2, p[1]+obj74.body.position[1]-h/2)
    print('HERE')
    reactivate(obj74)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj75.body.position=(p[0]+obj75.body.position[0]-w/2, p[1]+obj75.body.position[1]-h/2)
    print('HERE')
    reactivate(obj75)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj76.body.position=(p[0]+obj76.body.position[0]-w/2, p[1]+obj76.body.position[1]-h/2)
    print('HERE')
    reactivate(obj76)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj77.body.position=(p[0]+obj77.body.position[0]-w/2, p[1]+obj77.body.position[1]-h/2)
    print('HERE')
    reactivate(obj77)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj78.body.position=(p[0]+obj78.body.position[0]-w/2, p[1]+obj78.body.position[1]-h/2)
    print('HERE')
    reactivate(obj78)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj79.body.position=(p[0]+obj79.body.position[0]-w/2, p[1]+obj79.body.position[1]-h/2)
    print('HERE')
    reactivate(obj79)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj80.body.position=(p[0]+obj80.body.position[0]-w/2, p[1]+obj80.body.position[1]-h/2)
    print('HERE')
    reactivate(obj80)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj81.body.position=(p[0]+obj81.body.position[0]-w/2, p[1]+obj81.body.position[1]-h/2)
    print('HERE')
    reactivate(obj81)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj82.body.position=(p[0]+obj82.body.position[0]-w/2, p[1]+obj82.body.position[1]-h/2)
    print('HERE')
    reactivate(obj82)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj83.body.position=(p[0]+obj83.body.position[0]-w/2, p[1]+obj83.body.position[1]-h/2)
    print('HERE')
    reactivate(obj83)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj84.body.position=(p[0]+obj84.body.position[0]-w/2, p[1]+obj84.body.position[1]-h/2)
    print('HERE')
    reactivate(obj84)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj85.body.position=(p[0]+obj85.body.position[0]-w/2, p[1]+obj85.body.position[1]-h/2)
    print('HERE')
    reactivate(obj85)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj86.body.position=(p[0]+obj86.body.position[0]-w/2, p[1]+obj86.body.position[1]-h/2)
    print('HERE')
    reactivate(obj86)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj87.body.position=(p[0]+obj87.body.position[0]-w/2, p[1]+obj87.body.position[1]-h/2)
    print('HERE')
    reactivate(obj87)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj89.body.position=(p[0]+obj89.body.position[0]-w/2, p[1]+obj89.body.position[1]-h/2)
    print('HERE')
    reactivate(obj89)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj90.body.position=(p[0]+obj90.body.position[0]-w/2, p[1]+obj90.body.position[1]-h/2)
    print('HERE')
    reactivate(obj90)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj91.body.position=(p[0]+obj91.body.position[0]-w/2, p[1]+obj91.body.position[1]-h/2)
    print('HERE')
    reactivate(obj91)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj92.body.position=(p[0]+obj92.body.position[0]-w/2, p[1]+obj92.body.position[1]-h/2)
    print('HERE')
    reactivate(obj92)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj93.body.position=(p[0]+obj93.body.position[0]-w/2, p[1]+obj93.body.position[1]-h/2)
    print('HERE')
    reactivate(obj93)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj94.body.position=(p[0]+obj94.body.position[0]-w/2, p[1]+obj94.body.position[1]-h/2)
    print('HERE')
    reactivate(obj94)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj95.body.position=(p[0]+obj95.body.position[0]-w/2, p[1]+obj95.body.position[1]-h/2)
    print('HERE')
    reactivate(obj95)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj96.body.position=(p[0]+obj96.body.position[0]-w/2, p[1]+obj96.body.position[1]-h/2)
    print('HERE')
    reactivate(obj96)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj97.body.position=(p[0]+obj97.body.position[0]-w/2, p[1]+obj97.body.position[1]-h/2)
    print('HERE')
    reactivate(obj97)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj98.body.position=(p[0]+obj98.body.position[0]-w/2, p[1]+obj98.body.position[1]-h/2)
    print('HERE')
    reactivate(obj98)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj99.body.position=(p[0]+obj99.body.position[0]-w/2, p[1]+obj99.body.position[1]-h/2)
    print('HERE')
    reactivate(obj99)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj100.body.position=(p[0]+obj100.body.position[0]-w/2, p[1]+obj100.body.position[1]-h/2)
    print('HERE')
    reactivate(obj100)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj101.body.position=(p[0]+obj101.body.position[0]-w/2, p[1]+obj101.body.position[1]-h/2)
    print('HERE')
    reactivate(obj101)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj102.body.position=(p[0]+obj102.body.position[0]-w/2, p[1]+obj102.body.position[1]-h/2)
    print('HERE')
    reactivate(obj102)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj103.body.position=(p[0]+obj103.body.position[0]-w/2, p[1]+obj103.body.position[1]-h/2)
    print('HERE')
    reactivate(obj103)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj104.body.position=(p[0]+obj104.body.position[0]-w/2, p[1]+obj104.body.position[1]-h/2)
    print('HERE')
    reactivate(obj104)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj106.body.position=(p[0]+obj106.body.position[0]-w/2, p[1]+obj106.body.position[1]-h/2)
    print('HERE')
    reactivate(obj106)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj107.body.position=(p[0]+obj107.body.position[0]-w/2, p[1]+obj107.body.position[1]-h/2)
    print('HERE')
    reactivate(obj107)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj108.body.position=(p[0]+obj108.body.position[0]-w/2, p[1]+obj108.body.position[1]-h/2)
    print('HERE')
    reactivate(obj108)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj109.body.position=(p[0]+obj109.body.position[0]-w/2, p[1]+obj109.body.position[1]-h/2)
    print('HERE')
    reactivate(obj109)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj110.body.position=(p[0]+obj110.body.position[0]-w/2, p[1]+obj110.body.position[1]-h/2)
    print('HERE')
    reactivate(obj110)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj111.body.position=(p[0]+obj111.body.position[0]-w/2, p[1]+obj111.body.position[1]-h/2)
    print('HERE')
    reactivate(obj111)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj112.body.position=(p[0]+obj112.body.position[0]-w/2, p[1]+obj112.body.position[1]-h/2)
    print('HERE')
    reactivate(obj112)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj113.body.position=(p[0]+obj113.body.position[0]-w/2, p[1]+obj113.body.position[1]-h/2)
    print('HERE')
    reactivate(obj113)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj114.body.position=(p[0]+obj114.body.position[0]-w/2, p[1]+obj114.body.position[1]-h/2)
    print('HERE')
    reactivate(obj114)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj115.body.position=(p[0]+obj115.body.position[0]-w/2, p[1]+obj115.body.position[1]-h/2)
    print('HERE')
    reactivate(obj115)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj116.body.position=(p[0]+obj116.body.position[0]-w/2, p[1]+obj116.body.position[1]-h/2)
    print('HERE')
    reactivate(obj116)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj117.body.position=(p[0]+obj117.body.position[0]-w/2, p[1]+obj117.body.position[1]-h/2)
    print('HERE')
    reactivate(obj117)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj118.body.position=(p[0]+obj118.body.position[0]-w/2, p[1]+obj118.body.position[1]-h/2)
    print('HERE')
    reactivate(obj118)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj119.body.position=(p[0]+obj119.body.position[0]-w/2, p[1]+obj119.body.position[1]-h/2)
    print('HERE')
    reactivate(obj119)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj120.body.position=(p[0]+obj120.body.position[0]-w/2, p[1]+obj120.body.position[1]-h/2)
    print('HERE')
    reactivate(obj120)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj121.body.position=(p[0]+obj121.body.position[0]-w/2, p[1]+obj121.body.position[1]-h/2)
    print('HERE')
    reactivate(obj121)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj123.body.position=(p[0]+obj123.body.position[0]-w/2, p[1]+obj123.body.position[1]-h/2)
    print('HERE')
    reactivate(obj123)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj124.body.position=(p[0]+obj124.body.position[0]-w/2, p[1]+obj124.body.position[1]-h/2)
    print('HERE')
    reactivate(obj124)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj125.body.position=(p[0]+obj125.body.position[0]-w/2, p[1]+obj125.body.position[1]-h/2)
    print('HERE')
    reactivate(obj125)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj126.body.position=(p[0]+obj126.body.position[0]-w/2, p[1]+obj126.body.position[1]-h/2)
    print('HERE')
    reactivate(obj126)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj127.body.position=(p[0]+obj127.body.position[0]-w/2, p[1]+obj127.body.position[1]-h/2)
    print('HERE')
    reactivate(obj127)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj128.body.position=(p[0]+obj128.body.position[0]-w/2, p[1]+obj128.body.position[1]-h/2)
    print('HERE')
    reactivate(obj128)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj129.body.position=(p[0]+obj129.body.position[0]-w/2, p[1]+obj129.body.position[1]-h/2)
    print('HERE')
    reactivate(obj129)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj130.body.position=(p[0]+obj130.body.position[0]-w/2, p[1]+obj130.body.position[1]-h/2)
    print('HERE')
    reactivate(obj130)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj131.body.position=(p[0]+obj131.body.position[0]-w/2, p[1]+obj131.body.position[1]-h/2)
    print('HERE')
    reactivate(obj131)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj132.body.position=(p[0]+obj132.body.position[0]-w/2, p[1]+obj132.body.position[1]-h/2)
    print('HERE')
    reactivate(obj132)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj133.body.position=(p[0]+obj133.body.position[0]-w/2, p[1]+obj133.body.position[1]-h/2)
    print('HERE')
    reactivate(obj133)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj134.body.position=(p[0]+obj134.body.position[0]-w/2, p[1]+obj134.body.position[1]-h/2)
    print('HERE')
    reactivate(obj134)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj135.body.position=(p[0]+obj135.body.position[0]-w/2, p[1]+obj135.body.position[1]-h/2)
    print('HERE')
    reactivate(obj135)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj136.body.position=(p[0]+obj136.body.position[0]-w/2, p[1]+obj136.body.position[1]-h/2)
    print('HERE')
    reactivate(obj136)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj137.body.position=(p[0]+obj137.body.position[0]-w/2, p[1]+obj137.body.position[1]-h/2)
    print('HERE')
    reactivate(obj137)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj138.body.position=(p[0]+obj138.body.position[0]-w/2, p[1]+obj138.body.position[1]-h/2)
    print('HERE')
    reactivate(obj138)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj140.body.position=(p[0]+obj140.body.position[0]-w/2, p[1]+obj140.body.position[1]-h/2)
    print('HERE')
    reactivate(obj140)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj141.body.position=(p[0]+obj141.body.position[0]-w/2, p[1]+obj141.body.position[1]-h/2)
    print('HERE')
    reactivate(obj141)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj142.body.position=(p[0]+obj142.body.position[0]-w/2, p[1]+obj142.body.position[1]-h/2)
    print('HERE')
    reactivate(obj142)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj143.body.position=(p[0]+obj143.body.position[0]-w/2, p[1]+obj143.body.position[1]-h/2)
    print('HERE')
    reactivate(obj143)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj144.body.position=(p[0]+obj144.body.position[0]-w/2, p[1]+obj144.body.position[1]-h/2)
    print('HERE')
    reactivate(obj144)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj145.body.position=(p[0]+obj145.body.position[0]-w/2, p[1]+obj145.body.position[1]-h/2)
    print('HERE')
    reactivate(obj145)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj146.body.position=(p[0]+obj146.body.position[0]-w/2, p[1]+obj146.body.position[1]-h/2)
    print('HERE')
    reactivate(obj146)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj147.body.position=(p[0]+obj147.body.position[0]-w/2, p[1]+obj147.body.position[1]-h/2)
    print('HERE')
    reactivate(obj147)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj148.body.position=(p[0]+obj148.body.position[0]-w/2, p[1]+obj148.body.position[1]-h/2)
    print('HERE')
    reactivate(obj148)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj149.body.position=(p[0]+obj149.body.position[0]-w/2, p[1]+obj149.body.position[1]-h/2)
    print('HERE')
    reactivate(obj149)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj150.body.position=(p[0]+obj150.body.position[0]-w/2, p[1]+obj150.body.position[1]-h/2)
    print('HERE')
    reactivate(obj150)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj151.body.position=(p[0]+obj151.body.position[0]-w/2, p[1]+obj151.body.position[1]-h/2)
    print('HERE')
    reactivate(obj151)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj152.body.position=(p[0]+obj152.body.position[0]-w/2, p[1]+obj152.body.position[1]-h/2)
    print('HERE')
    reactivate(obj152)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj153.body.position=(p[0]+obj153.body.position[0]-w/2, p[1]+obj153.body.position[1]-h/2)
    print('HERE')
    reactivate(obj153)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj154.body.position=(p[0]+obj154.body.position[0]-w/2, p[1]+obj154.body.position[1]-h/2)
    print('HERE')
    reactivate(obj154)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj155.body.position=(p[0]+obj155.body.position[0]-w/2, p[1]+obj155.body.position[1]-h/2)
    print('HERE')
    reactivate(obj155)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj157.body.position=(p[0]+obj157.body.position[0]-w/2, p[1]+obj157.body.position[1]-h/2)
    print('HERE')
    reactivate(obj157)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj158.body.position=(p[0]+obj158.body.position[0]-w/2, p[1]+obj158.body.position[1]-h/2)
    print('HERE')
    reactivate(obj158)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj159.body.position=(p[0]+obj159.body.position[0]-w/2, p[1]+obj159.body.position[1]-h/2)
    print('HERE')
    reactivate(obj159)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj160.body.position=(p[0]+obj160.body.position[0]-w/2, p[1]+obj160.body.position[1]-h/2)
    print('HERE')
    reactivate(obj160)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj161.body.position=(p[0]+obj161.body.position[0]-w/2, p[1]+obj161.body.position[1]-h/2)
    print('HERE')
    reactivate(obj161)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj162.body.position=(p[0]+obj162.body.position[0]-w/2, p[1]+obj162.body.position[1]-h/2)
    print('HERE')
    reactivate(obj162)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj163.body.position=(p[0]+obj163.body.position[0]-w/2, p[1]+obj163.body.position[1]-h/2)
    print('HERE')
    reactivate(obj163)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj164.body.position=(p[0]+obj164.body.position[0]-w/2, p[1]+obj164.body.position[1]-h/2)
    print('HERE')
    reactivate(obj164)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj165.body.position=(p[0]+obj165.body.position[0]-w/2, p[1]+obj165.body.position[1]-h/2)
    print('HERE')
    reactivate(obj165)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj166.body.position=(p[0]+obj166.body.position[0]-w/2, p[1]+obj166.body.position[1]-h/2)
    print('HERE')
    reactivate(obj166)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj167.body.position=(p[0]+obj167.body.position[0]-w/2, p[1]+obj167.body.position[1]-h/2)
    print('HERE')
    reactivate(obj167)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj168.body.position=(p[0]+obj168.body.position[0]-w/2, p[1]+obj168.body.position[1]-h/2)
    print('HERE')
    reactivate(obj168)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj169.body.position=(p[0]+obj169.body.position[0]-w/2, p[1]+obj169.body.position[1]-h/2)
    print('HERE')
    reactivate(obj169)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj170.body.position=(p[0]+obj170.body.position[0]-w/2, p[1]+obj170.body.position[1]-h/2)
    print('HERE')
    reactivate(obj170)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj171.body.position=(p[0]+obj171.body.position[0]-w/2, p[1]+obj171.body.position[1]-h/2)
    print('HERE')
    reactivate(obj171)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj172.body.position=(p[0]+obj172.body.position[0]-w/2, p[1]+obj172.body.position[1]-h/2)
    print('HERE')
    reactivate(obj172)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj174.body.position=(p[0]+obj174.body.position[0]-w/2, p[1]+obj174.body.position[1]-h/2)
    print('HERE')
    reactivate(obj174)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj175.body.position=(p[0]+obj175.body.position[0]-w/2, p[1]+obj175.body.position[1]-h/2)
    print('HERE')
    reactivate(obj175)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj176.body.position=(p[0]+obj176.body.position[0]-w/2, p[1]+obj176.body.position[1]-h/2)
    print('HERE')
    reactivate(obj176)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj177.body.position=(p[0]+obj177.body.position[0]-w/2, p[1]+obj177.body.position[1]-h/2)
    print('HERE')
    reactivate(obj177)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj178.body.position=(p[0]+obj178.body.position[0]-w/2, p[1]+obj178.body.position[1]-h/2)
    print('HERE')
    reactivate(obj178)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj179.body.position=(p[0]+obj179.body.position[0]-w/2, p[1]+obj179.body.position[1]-h/2)
    print('HERE')
    reactivate(obj179)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj180.body.position=(p[0]+obj180.body.position[0]-w/2, p[1]+obj180.body.position[1]-h/2)
    print('HERE')
    reactivate(obj180)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj181.body.position=(p[0]+obj181.body.position[0]-w/2, p[1]+obj181.body.position[1]-h/2)
    print('HERE')
    reactivate(obj181)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj182.body.position=(p[0]+obj182.body.position[0]-w/2, p[1]+obj182.body.position[1]-h/2)
    print('HERE')
    reactivate(obj182)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj183.body.position=(p[0]+obj183.body.position[0]-w/2, p[1]+obj183.body.position[1]-h/2)
    print('HERE')
    reactivate(obj183)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj184.body.position=(p[0]+obj184.body.position[0]-w/2, p[1]+obj184.body.position[1]-h/2)
    print('HERE')
    reactivate(obj184)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj185.body.position=(p[0]+obj185.body.position[0]-w/2, p[1]+obj185.body.position[1]-h/2)
    print('HERE')
    reactivate(obj185)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj186.body.position=(p[0]+obj186.body.position[0]-w/2, p[1]+obj186.body.position[1]-h/2)
    print('HERE')
    reactivate(obj186)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj187.body.position=(p[0]+obj187.body.position[0]-w/2, p[1]+obj187.body.position[1]-h/2)
    print('HERE')
    reactivate(obj187)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj188.body.position=(p[0]+obj188.body.position[0]-w/2, p[1]+obj188.body.position[1]-h/2)
    print('HERE')
    reactivate(obj188)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj189.body.position=(p[0]+obj189.body.position[0]-w/2, p[1]+obj189.body.position[1]-h/2)
    print('HERE')
    reactivate(obj189)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj191.body.position=(p[0]+obj191.body.position[0]-w/2, p[1]+obj191.body.position[1]-h/2)
    print('HERE')
    reactivate(obj191)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj192.body.position=(p[0]+obj192.body.position[0]-w/2, p[1]+obj192.body.position[1]-h/2)
    print('HERE')
    reactivate(obj192)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj193.body.position=(p[0]+obj193.body.position[0]-w/2, p[1]+obj193.body.position[1]-h/2)
    print('HERE')
    reactivate(obj193)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj194.body.position=(p[0]+obj194.body.position[0]-w/2, p[1]+obj194.body.position[1]-h/2)
    print('HERE')
    reactivate(obj194)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj195.body.position=(p[0]+obj195.body.position[0]-w/2, p[1]+obj195.body.position[1]-h/2)
    print('HERE')
    reactivate(obj195)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj196.body.position=(p[0]+obj196.body.position[0]-w/2, p[1]+obj196.body.position[1]-h/2)
    print('HERE')
    reactivate(obj196)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj197.body.position=(p[0]+obj197.body.position[0]-w/2, p[1]+obj197.body.position[1]-h/2)
    print('HERE')
    reactivate(obj197)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj198.body.position=(p[0]+obj198.body.position[0]-w/2, p[1]+obj198.body.position[1]-h/2)
    print('HERE')
    reactivate(obj198)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj199.body.position=(p[0]+obj199.body.position[0]-w/2, p[1]+obj199.body.position[1]-h/2)
    print('HERE')
    reactivate(obj199)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj200.body.position=(p[0]+obj200.body.position[0]-w/2, p[1]+obj200.body.position[1]-h/2)
    print('HERE')
    reactivate(obj200)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj201.body.position=(p[0]+obj201.body.position[0]-w/2, p[1]+obj201.body.position[1]-h/2)
    print('HERE')
    reactivate(obj201)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj202.body.position=(p[0]+obj202.body.position[0]-w/2, p[1]+obj202.body.position[1]-h/2)
    print('HERE')
    reactivate(obj202)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj203.body.position=(p[0]+obj203.body.position[0]-w/2, p[1]+obj203.body.position[1]-h/2)
    print('HERE')
    reactivate(obj203)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj204.body.position=(p[0]+obj204.body.position[0]-w/2, p[1]+obj204.body.position[1]-h/2)
    print('HERE')
    reactivate(obj204)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj205.body.position=(p[0]+obj205.body.position[0]-w/2, p[1]+obj205.body.position[1]-h/2)
    print('HERE')
    reactivate(obj205)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj206.body.position=(p[0]+obj206.body.position[0]-w/2, p[1]+obj206.body.position[1]-h/2)
    print('HERE')
    reactivate(obj206)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj208.body.position=(p[0]+obj208.body.position[0]-w/2, p[1]+obj208.body.position[1]-h/2)
    print('HERE')
    reactivate(obj208)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj209.body.position=(p[0]+obj209.body.position[0]-w/2, p[1]+obj209.body.position[1]-h/2)
    print('HERE')
    reactivate(obj209)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj210.body.position=(p[0]+obj210.body.position[0]-w/2, p[1]+obj210.body.position[1]-h/2)
    print('HERE')
    reactivate(obj210)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj211.body.position=(p[0]+obj211.body.position[0]-w/2, p[1]+obj211.body.position[1]-h/2)
    print('HERE')
    reactivate(obj211)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj212.body.position=(p[0]+obj212.body.position[0]-w/2, p[1]+obj212.body.position[1]-h/2)
    print('HERE')
    reactivate(obj212)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj213.body.position=(p[0]+obj213.body.position[0]-w/2, p[1]+obj213.body.position[1]-h/2)
    print('HERE')
    reactivate(obj213)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj214.body.position=(p[0]+obj214.body.position[0]-w/2, p[1]+obj214.body.position[1]-h/2)
    print('HERE')
    reactivate(obj214)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj215.body.position=(p[0]+obj215.body.position[0]-w/2, p[1]+obj215.body.position[1]-h/2)
    print('HERE')
    reactivate(obj215)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj216.body.position=(p[0]+obj216.body.position[0]-w/2, p[1]+obj216.body.position[1]-h/2)
    print('HERE')
    reactivate(obj216)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj217.body.position=(p[0]+obj217.body.position[0]-w/2, p[1]+obj217.body.position[1]-h/2)
    print('HERE')
    reactivate(obj217)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj218.body.position=(p[0]+obj218.body.position[0]-w/2, p[1]+obj218.body.position[1]-h/2)
    print('HERE')
    reactivate(obj218)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj219.body.position=(p[0]+obj219.body.position[0]-w/2, p[1]+obj219.body.position[1]-h/2)
    print('HERE')
    reactivate(obj219)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj220.body.position=(p[0]+obj220.body.position[0]-w/2, p[1]+obj220.body.position[1]-h/2)
    print('HERE')
    reactivate(obj220)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj221.body.position=(p[0]+obj221.body.position[0]-w/2, p[1]+obj221.body.position[1]-h/2)
    print('HERE')
    reactivate(obj221)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj222.body.position=(p[0]+obj222.body.position[0]-w/2, p[1]+obj222.body.position[1]-h/2)
    print('HERE')
    reactivate(obj222)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj223.body.position=(p[0]+obj223.body.position[0]-w/2, p[1]+obj223.body.position[1]-h/2)
    print('HERE')
    reactivate(obj223)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj225.body.position=(p[0]+obj225.body.position[0]-w/2, p[1]+obj225.body.position[1]-h/2)
    print('HERE')
    reactivate(obj225)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj226.body.position=(p[0]+obj226.body.position[0]-w/2, p[1]+obj226.body.position[1]-h/2)
    print('HERE')
    reactivate(obj226)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj227.body.position=(p[0]+obj227.body.position[0]-w/2, p[1]+obj227.body.position[1]-h/2)
    print('HERE')
    reactivate(obj227)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj228.body.position=(p[0]+obj228.body.position[0]-w/2, p[1]+obj228.body.position[1]-h/2)
    print('HERE')
    reactivate(obj228)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj229.body.position=(p[0]+obj229.body.position[0]-w/2, p[1]+obj229.body.position[1]-h/2)
    print('HERE')
    reactivate(obj229)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj230.body.position=(p[0]+obj230.body.position[0]-w/2, p[1]+obj230.body.position[1]-h/2)
    print('HERE')
    reactivate(obj230)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj231.body.position=(p[0]+obj231.body.position[0]-w/2, p[1]+obj231.body.position[1]-h/2)
    print('HERE')
    reactivate(obj231)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj232.body.position=(p[0]+obj232.body.position[0]-w/2, p[1]+obj232.body.position[1]-h/2)
    print('HERE')
    reactivate(obj232)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj233.body.position=(p[0]+obj233.body.position[0]-w/2, p[1]+obj233.body.position[1]-h/2)
    print('HERE')
    reactivate(obj233)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj234.body.position=(p[0]+obj234.body.position[0]-w/2, p[1]+obj234.body.position[1]-h/2)
    print('HERE')
    reactivate(obj234)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj235.body.position=(p[0]+obj235.body.position[0]-w/2, p[1]+obj235.body.position[1]-h/2)
    print('HERE')
    reactivate(obj235)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj236.body.position=(p[0]+obj236.body.position[0]-w/2, p[1]+obj236.body.position[1]-h/2)
    print('HERE')
    reactivate(obj236)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj237.body.position=(p[0]+obj237.body.position[0]-w/2, p[1]+obj237.body.position[1]-h/2)
    print('HERE')
    reactivate(obj237)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj238.body.position=(p[0]+obj238.body.position[0]-w/2, p[1]+obj238.body.position[1]-h/2)
    print('HERE')
    reactivate(obj238)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj239.body.position=(p[0]+obj239.body.position[0]-w/2, p[1]+obj239.body.position[1]-h/2)
    print('HERE')
    reactivate(obj239)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj240.body.position=(p[0]+obj240.body.position[0]-w/2, p[1]+obj240.body.position[1]-h/2)
    print('HERE')
    reactivate(obj240)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj242.body.position=(p[0]+obj242.body.position[0]-w/2, p[1]+obj242.body.position[1]-h/2)
    print('HERE')
    reactivate(obj242)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj243.body.position=(p[0]+obj243.body.position[0]-w/2, p[1]+obj243.body.position[1]-h/2)
    print('HERE')
    reactivate(obj243)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj244.body.position=(p[0]+obj244.body.position[0]-w/2, p[1]+obj244.body.position[1]-h/2)
    print('HERE')
    reactivate(obj244)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj245.body.position=(p[0]+obj245.body.position[0]-w/2, p[1]+obj245.body.position[1]-h/2)
    print('HERE')
    reactivate(obj245)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj246.body.position=(p[0]+obj246.body.position[0]-w/2, p[1]+obj246.body.position[1]-h/2)
    print('HERE')
    reactivate(obj246)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj247.body.position=(p[0]+obj247.body.position[0]-w/2, p[1]+obj247.body.position[1]-h/2)
    print('HERE')
    reactivate(obj247)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj248.body.position=(p[0]+obj248.body.position[0]-w/2, p[1]+obj248.body.position[1]-h/2)
    print('HERE')
    reactivate(obj248)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj249.body.position=(p[0]+obj249.body.position[0]-w/2, p[1]+obj249.body.position[1]-h/2)
    print('HERE')
    reactivate(obj249)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj250.body.position=(p[0]+obj250.body.position[0]-w/2, p[1]+obj250.body.position[1]-h/2)
    print('HERE')
    reactivate(obj250)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj251.body.position=(p[0]+obj251.body.position[0]-w/2, p[1]+obj251.body.position[1]-h/2)
    print('HERE')
    reactivate(obj251)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj252.body.position=(p[0]+obj252.body.position[0]-w/2, p[1]+obj252.body.position[1]-h/2)
    print('HERE')
    reactivate(obj252)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj253.body.position=(p[0]+obj253.body.position[0]-w/2, p[1]+obj253.body.position[1]-h/2)
    print('HERE')
    reactivate(obj253)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj254.body.position=(p[0]+obj254.body.position[0]-w/2, p[1]+obj254.body.position[1]-h/2)
    print('HERE')
    reactivate(obj254)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj255.body.position=(p[0]+obj255.body.position[0]-w/2, p[1]+obj255.body.position[1]-h/2)
    print('HERE')
    reactivate(obj255)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj256.body.position=(p[0]+obj256.body.position[0]-w/2, p[1]+obj256.body.position[1]-h/2)
    print('HERE')
    reactivate(obj256)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj257.body.position=(p[0]+obj257.body.position[0]-w/2, p[1]+obj257.body.position[1]-h/2)
    print('HERE')
    reactivate(obj257)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj259.body.position=(p[0]+obj259.body.position[0]-w/2, p[1]+obj259.body.position[1]-h/2)
    print('HERE')
    reactivate(obj259)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj260.body.position=(p[0]+obj260.body.position[0]-w/2, p[1]+obj260.body.position[1]-h/2)
    print('HERE')
    reactivate(obj260)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj261.body.position=(p[0]+obj261.body.position[0]-w/2, p[1]+obj261.body.position[1]-h/2)
    print('HERE')
    reactivate(obj261)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj262.body.position=(p[0]+obj262.body.position[0]-w/2, p[1]+obj262.body.position[1]-h/2)
    print('HERE')
    reactivate(obj262)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj263.body.position=(p[0]+obj263.body.position[0]-w/2, p[1]+obj263.body.position[1]-h/2)
    print('HERE')
    reactivate(obj263)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj264.body.position=(p[0]+obj264.body.position[0]-w/2, p[1]+obj264.body.position[1]-h/2)
    print('HERE')
    reactivate(obj264)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj265.body.position=(p[0]+obj265.body.position[0]-w/2, p[1]+obj265.body.position[1]-h/2)
    print('HERE')
    reactivate(obj265)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj266.body.position=(p[0]+obj266.body.position[0]-w/2, p[1]+obj266.body.position[1]-h/2)
    print('HERE')
    reactivate(obj266)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj267.body.position=(p[0]+obj267.body.position[0]-w/2, p[1]+obj267.body.position[1]-h/2)
    print('HERE')
    reactivate(obj267)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj268.body.position=(p[0]+obj268.body.position[0]-w/2, p[1]+obj268.body.position[1]-h/2)
    print('HERE')
    reactivate(obj268)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj269.body.position=(p[0]+obj269.body.position[0]-w/2, p[1]+obj269.body.position[1]-h/2)
    print('HERE')
    reactivate(obj269)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj270.body.position=(p[0]+obj270.body.position[0]-w/2, p[1]+obj270.body.position[1]-h/2)
    print('HERE')
    reactivate(obj270)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj271.body.position=(p[0]+obj271.body.position[0]-w/2, p[1]+obj271.body.position[1]-h/2)
    print('HERE')
    reactivate(obj271)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj272.body.position=(p[0]+obj272.body.position[0]-w/2, p[1]+obj272.body.position[1]-h/2)
    print('HERE')
    reactivate(obj272)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj273.body.position=(p[0]+obj273.body.position[0]-w/2, p[1]+obj273.body.position[1]-h/2)
    print('HERE')
    reactivate(obj273)
    deactivate(f)
  except:
    print('Exception')

  try:
    obj274.body.position=(p[0]+obj274.body.position[0]-w/2, p[1]+obj274.body.position[1]-h/2)
    print('HERE')
    reactivate(obj274)
    deactivate(f)
  except:
    print('Exception')

  return True
add_collision(obj1, obj2, on_collide_1_2)

obj2.mass = 10
obj2.gravity = (0,0)



obj285.mass = 10000
obj285.hit((0, 1500000), obj285.position)
obj274.mass = 10
deactivate(obj274) if 'obj274' in vars() else None
obj273.mass = 10
deactivate(obj273) if 'obj273' in vars() else None
obj272.mass = 10
deactivate(obj272) if 'obj272' in vars() else None
obj271.mass = 10
deactivate(obj271) if 'obj271' in vars() else None
obj270.mass = 10
deactivate(obj270) if 'obj270' in vars() else None
obj269.mass = 10
deactivate(obj269) if 'obj269' in vars() else None
obj268.mass = 10
deactivate(obj268) if 'obj268' in vars() else None
obj267.mass = 10
deactivate(obj267) if 'obj267' in vars() else None
obj266.mass = 10
deactivate(obj266) if 'obj266' in vars() else None
obj265.mass = 10
deactivate(obj265) if 'obj265' in vars() else None
obj264.mass = 10
deactivate(obj264) if 'obj264' in vars() else None
obj263.mass = 10
deactivate(obj263) if 'obj263' in vars() else None
obj262.mass = 10
deactivate(obj262) if 'obj262' in vars() else None
obj261.mass = 10
deactivate(obj261) if 'obj261' in vars() else None
obj260.mass = 10
deactivate(obj260) if 'obj260' in vars() else None
obj259.mass = 10
deactivate(obj259) if 'obj259' in vars() else None
obj257.mass = 10
deactivate(obj257) if 'obj257' in vars() else None
obj256.mass = 10
deactivate(obj256) if 'obj256' in vars() else None
obj255.mass = 10
deactivate(obj255) if 'obj255' in vars() else None
obj254.mass = 10
deactivate(obj254) if 'obj254' in vars() else None
obj253.mass = 10
deactivate(obj253) if 'obj253' in vars() else None
obj252.mass = 10
deactivate(obj252) if 'obj252' in vars() else None
obj251.mass = 10
deactivate(obj251) if 'obj251' in vars() else None
obj250.mass = 10
deactivate(obj250) if 'obj250' in vars() else None
obj249.mass = 10
deactivate(obj249) if 'obj249' in vars() else None
obj248.mass = 10
deactivate(obj248) if 'obj248' in vars() else None
obj247.mass = 10
deactivate(obj247) if 'obj247' in vars() else None
obj246.mass = 10
deactivate(obj246) if 'obj246' in vars() else None
obj245.mass = 10
deactivate(obj245) if 'obj245' in vars() else None
obj244.mass = 10
deactivate(obj244) if 'obj244' in vars() else None
obj243.mass = 10
deactivate(obj243) if 'obj243' in vars() else None
obj242.mass = 10
deactivate(obj242) if 'obj242' in vars() else None
obj240.mass = 10
deactivate(obj240) if 'obj240' in vars() else None
obj239.mass = 10
deactivate(obj239) if 'obj239' in vars() else None
obj238.mass = 10
deactivate(obj238) if 'obj238' in vars() else None
obj237.mass = 10
deactivate(obj237) if 'obj237' in vars() else None
obj236.mass = 10
deactivate(obj236) if 'obj236' in vars() else None
obj235.mass = 10
deactivate(obj235) if 'obj235' in vars() else None
obj234.mass = 10
deactivate(obj234) if 'obj234' in vars() else None
obj233.mass = 10
deactivate(obj233) if 'obj233' in vars() else None
obj232.mass = 10
deactivate(obj232) if 'obj232' in vars() else None
obj231.mass = 10
deactivate(obj231) if 'obj231' in vars() else None
obj230.mass = 10
deactivate(obj230) if 'obj230' in vars() else None
obj229.mass = 10
deactivate(obj229) if 'obj229' in vars() else None
obj228.mass = 10
deactivate(obj228) if 'obj228' in vars() else None
obj227.mass = 10
deactivate(obj227) if 'obj227' in vars() else None
obj226.mass = 10
deactivate(obj226) if 'obj226' in vars() else None
obj225.mass = 10
deactivate(obj225) if 'obj225' in vars() else None
obj223.mass = 10
deactivate(obj223) if 'obj223' in vars() else None
obj222.mass = 10
deactivate(obj222) if 'obj222' in vars() else None
obj221.mass = 10
deactivate(obj221) if 'obj221' in vars() else None
obj220.mass = 10
deactivate(obj220) if 'obj220' in vars() else None
obj219.mass = 10
deactivate(obj219) if 'obj219' in vars() else None
obj218.mass = 10
deactivate(obj218) if 'obj218' in vars() else None
obj217.mass = 10
deactivate(obj217) if 'obj217' in vars() else None
obj216.mass = 10
deactivate(obj216) if 'obj216' in vars() else None
obj215.mass = 10
deactivate(obj215) if 'obj215' in vars() else None
obj214.mass = 10
deactivate(obj214) if 'obj214' in vars() else None
obj213.mass = 10
deactivate(obj213) if 'obj213' in vars() else None
obj212.mass = 10
deactivate(obj212) if 'obj212' in vars() else None
obj211.mass = 10
deactivate(obj211) if 'obj211' in vars() else None
obj210.mass = 10
deactivate(obj210) if 'obj210' in vars() else None
obj209.mass = 10
deactivate(obj209) if 'obj209' in vars() else None
obj208.mass = 10
deactivate(obj208) if 'obj208' in vars() else None
obj206.mass = 10
deactivate(obj206) if 'obj206' in vars() else None
obj205.mass = 10
deactivate(obj205) if 'obj205' in vars() else None
obj204.mass = 10
deactivate(obj204) if 'obj204' in vars() else None
obj203.mass = 10
deactivate(obj203) if 'obj203' in vars() else None
obj202.mass = 10
deactivate(obj202) if 'obj202' in vars() else None
obj201.mass = 10
deactivate(obj201) if 'obj201' in vars() else None
obj200.mass = 10
deactivate(obj200) if 'obj200' in vars() else None
obj199.mass = 10
deactivate(obj199) if 'obj199' in vars() else None
obj198.mass = 10
deactivate(obj198) if 'obj198' in vars() else None
obj197.mass = 10
deactivate(obj197) if 'obj197' in vars() else None
obj196.mass = 10
deactivate(obj196) if 'obj196' in vars() else None
obj195.mass = 10
deactivate(obj195) if 'obj195' in vars() else None
obj194.mass = 10
deactivate(obj194) if 'obj194' in vars() else None
obj193.mass = 10
deactivate(obj193) if 'obj193' in vars() else None
obj192.mass = 10
deactivate(obj192) if 'obj192' in vars() else None
obj191.mass = 10
deactivate(obj191) if 'obj191' in vars() else None
obj189.mass = 10
deactivate(obj189) if 'obj189' in vars() else None
obj188.mass = 10
deactivate(obj188) if 'obj188' in vars() else None
obj187.mass = 10
deactivate(obj187) if 'obj187' in vars() else None
obj186.mass = 10
deactivate(obj186) if 'obj186' in vars() else None
obj185.mass = 10
deactivate(obj185) if 'obj185' in vars() else None
obj184.mass = 10
deactivate(obj184) if 'obj184' in vars() else None
obj183.mass = 10
deactivate(obj183) if 'obj183' in vars() else None
obj182.mass = 10
deactivate(obj182) if 'obj182' in vars() else None
obj181.mass = 10
deactivate(obj181) if 'obj181' in vars() else None
obj180.mass = 10
deactivate(obj180) if 'obj180' in vars() else None
obj179.mass = 10
deactivate(obj179) if 'obj179' in vars() else None
obj178.mass = 10
deactivate(obj178) if 'obj178' in vars() else None
obj177.mass = 10
deactivate(obj177) if 'obj177' in vars() else None
obj176.mass = 10
deactivate(obj176) if 'obj176' in vars() else None
obj175.mass = 10
deactivate(obj175) if 'obj175' in vars() else None
obj174.mass = 10
deactivate(obj174) if 'obj174' in vars() else None
obj172.mass = 10
deactivate(obj172) if 'obj172' in vars() else None
obj171.mass = 10
deactivate(obj171) if 'obj171' in vars() else None
obj170.mass = 10
deactivate(obj170) if 'obj170' in vars() else None
obj169.mass = 10
deactivate(obj169) if 'obj169' in vars() else None
obj168.mass = 10
deactivate(obj168) if 'obj168' in vars() else None
obj167.mass = 10
deactivate(obj167) if 'obj167' in vars() else None
obj166.mass = 10
deactivate(obj166) if 'obj166' in vars() else None
obj165.mass = 10
deactivate(obj165) if 'obj165' in vars() else None
obj164.mass = 10
deactivate(obj164) if 'obj164' in vars() else None
obj163.mass = 10
deactivate(obj163) if 'obj163' in vars() else None
obj162.mass = 10
deactivate(obj162) if 'obj162' in vars() else None
obj161.mass = 10
deactivate(obj161) if 'obj161' in vars() else None
obj160.mass = 10
deactivate(obj160) if 'obj160' in vars() else None
obj159.mass = 10
deactivate(obj159) if 'obj159' in vars() else None
obj158.mass = 10
deactivate(obj158) if 'obj158' in vars() else None
obj157.mass = 10
deactivate(obj157) if 'obj157' in vars() else None
obj155.mass = 10
deactivate(obj155) if 'obj155' in vars() else None
obj154.mass = 10
deactivate(obj154) if 'obj154' in vars() else None
obj153.mass = 10
deactivate(obj153) if 'obj153' in vars() else None
obj152.mass = 10
deactivate(obj152) if 'obj152' in vars() else None
obj151.mass = 10
deactivate(obj151) if 'obj151' in vars() else None
obj150.mass = 10
deactivate(obj150) if 'obj150' in vars() else None
obj149.mass = 10
deactivate(obj149) if 'obj149' in vars() else None
obj148.mass = 10
deactivate(obj148) if 'obj148' in vars() else None
obj147.mass = 10
deactivate(obj147) if 'obj147' in vars() else None
obj146.mass = 10
deactivate(obj146) if 'obj146' in vars() else None
obj145.mass = 10
deactivate(obj145) if 'obj145' in vars() else None
obj144.mass = 10
deactivate(obj144) if 'obj144' in vars() else None
obj143.mass = 10
deactivate(obj143) if 'obj143' in vars() else None
obj142.mass = 10
deactivate(obj142) if 'obj142' in vars() else None
obj141.mass = 10
deactivate(obj141) if 'obj141' in vars() else None
obj140.mass = 10
deactivate(obj140) if 'obj140' in vars() else None
obj138.mass = 10
deactivate(obj138) if 'obj138' in vars() else None
obj137.mass = 10
deactivate(obj137) if 'obj137' in vars() else None
obj136.mass = 10
deactivate(obj136) if 'obj136' in vars() else None
obj135.mass = 10
deactivate(obj135) if 'obj135' in vars() else None
obj134.mass = 10
deactivate(obj134) if 'obj134' in vars() else None
obj133.mass = 10
deactivate(obj133) if 'obj133' in vars() else None
obj132.mass = 10
deactivate(obj132) if 'obj132' in vars() else None
obj131.mass = 10
deactivate(obj131) if 'obj131' in vars() else None
obj130.mass = 10
deactivate(obj130) if 'obj130' in vars() else None
obj129.mass = 10
deactivate(obj129) if 'obj129' in vars() else None
obj128.mass = 10
deactivate(obj128) if 'obj128' in vars() else None
obj127.mass = 10
deactivate(obj127) if 'obj127' in vars() else None
obj126.mass = 10
deactivate(obj126) if 'obj126' in vars() else None
obj125.mass = 10
deactivate(obj125) if 'obj125' in vars() else None
obj124.mass = 10
deactivate(obj124) if 'obj124' in vars() else None
obj123.mass = 10
deactivate(obj123) if 'obj123' in vars() else None
obj121.mass = 10
deactivate(obj121) if 'obj121' in vars() else None
obj120.mass = 10
deactivate(obj120) if 'obj120' in vars() else None
obj119.mass = 10
deactivate(obj119) if 'obj119' in vars() else None
obj118.mass = 10
deactivate(obj118) if 'obj118' in vars() else None
obj117.mass = 10
deactivate(obj117) if 'obj117' in vars() else None
obj116.mass = 10
deactivate(obj116) if 'obj116' in vars() else None
obj115.mass = 10
deactivate(obj115) if 'obj115' in vars() else None
obj114.mass = 10
deactivate(obj114) if 'obj114' in vars() else None
obj113.mass = 10
deactivate(obj113) if 'obj113' in vars() else None
obj112.mass = 10
deactivate(obj112) if 'obj112' in vars() else None
obj111.mass = 10
deactivate(obj111) if 'obj111' in vars() else None
obj110.mass = 10
deactivate(obj110) if 'obj110' in vars() else None
obj109.mass = 10
deactivate(obj109) if 'obj109' in vars() else None
obj108.mass = 10
deactivate(obj108) if 'obj108' in vars() else None
obj107.mass = 10
deactivate(obj107) if 'obj107' in vars() else None
obj106.mass = 10
deactivate(obj106) if 'obj106' in vars() else None
obj104.mass = 10
deactivate(obj104) if 'obj104' in vars() else None
obj103.mass = 10
deactivate(obj103) if 'obj103' in vars() else None
obj102.mass = 10
deactivate(obj102) if 'obj102' in vars() else None
obj101.mass = 10
deactivate(obj101) if 'obj101' in vars() else None
obj100.mass = 10
deactivate(obj100) if 'obj100' in vars() else None
obj99.mass = 10
deactivate(obj99) if 'obj99' in vars() else None
obj98.mass = 10
deactivate(obj98) if 'obj98' in vars() else None
obj97.mass = 10
deactivate(obj97) if 'obj97' in vars() else None
obj96.mass = 10
deactivate(obj96) if 'obj96' in vars() else None
obj95.mass = 10
deactivate(obj95) if 'obj95' in vars() else None
obj94.mass = 10
deactivate(obj94) if 'obj94' in vars() else None
obj93.mass = 10
deactivate(obj93) if 'obj93' in vars() else None
obj92.mass = 10
deactivate(obj92) if 'obj92' in vars() else None
obj91.mass = 10
deactivate(obj91) if 'obj91' in vars() else None
obj90.mass = 10
deactivate(obj90) if 'obj90' in vars() else None
obj89.mass = 10
deactivate(obj89) if 'obj89' in vars() else None
obj87.mass = 10
deactivate(obj87) if 'obj87' in vars() else None
obj86.mass = 10
deactivate(obj86) if 'obj86' in vars() else None
obj85.mass = 10
deactivate(obj85) if 'obj85' in vars() else None
obj84.mass = 10
deactivate(obj84) if 'obj84' in vars() else None
obj83.mass = 10
deactivate(obj83) if 'obj83' in vars() else None
obj82.mass = 10
deactivate(obj82) if 'obj82' in vars() else None
obj81.mass = 10
deactivate(obj81) if 'obj81' in vars() else None
obj80.mass = 10
deactivate(obj80) if 'obj80' in vars() else None
obj79.mass = 10
deactivate(obj79) if 'obj79' in vars() else None
obj78.mass = 10
deactivate(obj78) if 'obj78' in vars() else None
obj77.mass = 10
deactivate(obj77) if 'obj77' in vars() else None
obj76.mass = 10
deactivate(obj76) if 'obj76' in vars() else None
obj75.mass = 10
deactivate(obj75) if 'obj75' in vars() else None
obj74.mass = 10
deactivate(obj74) if 'obj74' in vars() else None
obj73.mass = 10
deactivate(obj73) if 'obj73' in vars() else None
obj72.mass = 10
deactivate(obj72) if 'obj72' in vars() else None
obj70.mass = 10
deactivate(obj70) if 'obj70' in vars() else None
obj69.mass = 10
deactivate(obj69) if 'obj69' in vars() else None
obj68.mass = 10
deactivate(obj68) if 'obj68' in vars() else None
obj67.mass = 10
deactivate(obj67) if 'obj67' in vars() else None
obj66.mass = 10
deactivate(obj66) if 'obj66' in vars() else None
obj65.mass = 10
deactivate(obj65) if 'obj65' in vars() else None
obj64.mass = 10
deactivate(obj64) if 'obj64' in vars() else None
obj63.mass = 10
deactivate(obj63) if 'obj63' in vars() else None
obj62.mass = 10
deactivate(obj62) if 'obj62' in vars() else None
obj61.mass = 10
deactivate(obj61) if 'obj61' in vars() else None
obj60.mass = 10
deactivate(obj60) if 'obj60' in vars() else None
obj59.mass = 10
deactivate(obj59) if 'obj59' in vars() else None
obj58.mass = 10
deactivate(obj58) if 'obj58' in vars() else None
obj57.mass = 10
deactivate(obj57) if 'obj57' in vars() else None
obj56.mass = 10
deactivate(obj56) if 'obj56' in vars() else None
obj55.mass = 10
deactivate(obj55) if 'obj55' in vars() else None
obj53.mass = 10
deactivate(obj53) if 'obj53' in vars() else None
obj52.mass = 10
deactivate(obj52) if 'obj52' in vars() else None
obj51.mass = 10
deactivate(obj51) if 'obj51' in vars() else None
obj50.mass = 10
deactivate(obj50) if 'obj50' in vars() else None
obj49.mass = 10
deactivate(obj49) if 'obj49' in vars() else None
obj48.mass = 10
deactivate(obj48) if 'obj48' in vars() else None
obj47.mass = 10
deactivate(obj47) if 'obj47' in vars() else None
obj46.mass = 10
deactivate(obj46) if 'obj46' in vars() else None
obj45.mass = 10
deactivate(obj45) if 'obj45' in vars() else None
obj44.mass = 10
deactivate(obj44) if 'obj44' in vars() else None
obj43.mass = 10
deactivate(obj43) if 'obj43' in vars() else None
obj42.mass = 10
deactivate(obj42) if 'obj42' in vars() else None
obj41.mass = 10
deactivate(obj41) if 'obj41' in vars() else None
obj40.mass = 10
deactivate(obj40) if 'obj40' in vars() else None
obj39.mass = 10
deactivate(obj39) if 'obj39' in vars() else None
obj38.mass = 10
deactivate(obj38) if 'obj38' in vars() else None
obj36.mass = 10
deactivate(obj36) if 'obj36' in vars() else None
obj35.mass = 10
deactivate(obj35) if 'obj35' in vars() else None
obj34.mass = 10
deactivate(obj34) if 'obj34' in vars() else None
obj33.mass = 10
deactivate(obj33) if 'obj33' in vars() else None
obj32.mass = 10
deactivate(obj32) if 'obj32' in vars() else None
obj31.mass = 10
deactivate(obj31) if 'obj31' in vars() else None
obj30.mass = 10
deactivate(obj30) if 'obj30' in vars() else None
obj29.mass = 10
deactivate(obj29) if 'obj29' in vars() else None
obj28.mass = 10
deactivate(obj28) if 'obj28' in vars() else None
obj27.mass = 10
deactivate(obj27) if 'obj27' in vars() else None
obj26.mass = 10
deactivate(obj26) if 'obj26' in vars() else None
obj25.mass = 10
deactivate(obj25) if 'obj25' in vars() else None
obj24.mass = 10
deactivate(obj24) if 'obj24' in vars() else None
obj23.mass = 10
deactivate(obj23) if 'obj23' in vars() else None
obj22.mass = 10
deactivate(obj22) if 'obj22' in vars() else None
obj21.mass = 10
deactivate(obj21) if 'obj21' in vars() else None
obj19.mass = 10
deactivate(obj19) if 'obj19' in vars() else None
obj18.mass = 10
deactivate(obj18) if 'obj18' in vars() else None
obj17.mass = 10
deactivate(obj17) if 'obj17' in vars() else None
obj16.mass = 10
deactivate(obj16) if 'obj16' in vars() else None
obj15.mass = 10
deactivate(obj15) if 'obj15' in vars() else None
obj14.mass = 10
deactivate(obj14) if 'obj14' in vars() else None
obj13.mass = 10
deactivate(obj13) if 'obj13' in vars() else None
obj12.mass = 10
deactivate(obj12) if 'obj12' in vars() else None
obj11.mass = 10
deactivate(obj11) if 'obj11' in vars() else None
obj10.mass = 10
deactivate(obj10) if 'obj10' in vars() else None
obj9.mass = 10
deactivate(obj9) if 'obj9' in vars() else None
obj8.mass = 10
deactivate(obj8) if 'obj8' in vars() else None
obj7.mass = 10
deactivate(obj7) if 'obj7' in vars() else None
obj6.mass = 10
deactivate(obj6) if 'obj6' in vars() else None
obj5.mass = 10
deactivate(obj5) if 'obj5' in vars() else None
obj4.mass = 10
deactivate(obj4) if 'obj4' in vars() else None




def image_for(s):
  global image_bindings
  for b in image_bindings:
    if b[0] == s:
      return b[1]
  return False

def draw_images(cosmetic):
  def f(keys):
    global user_shapes
    for s in user_shapes:
      if(not image_for(s)):
        continue

      if(not (s._cosmetic == cosmetic)):
        continue

      if(not (s.active)):
        continue

      if(s.body):
        p = Vec2d(s.body.position.x, s.body.position.y)
      else:
        p = Vec2d(s._x, s._y)

      angle = 0
      if(s.body):
        angle = s.body.angle

      angle_degrees    = math.degrees(angle) 
      rotated_logo_img = pygame.transform.rotate(image_for(s), -angle_degrees)
    
      offset = Vec2d(rotated_logo_img.get_size()) / 2.
      p      = p - offset
     
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
      pygame.draw.line(screen, Color("black"), start, end)

      #screen.blit(rotated_logo_img, p)

def draw_connection_lines(keys):
  global pivots
  for c in connected_shapes:
    start = c[0].body.position
    end   = c[1].body.position

    #if(not(c[0].active) or not(c[1].active)):
    #  continue
   
    screen = pygame.display.get_surface()
    pygame.draw.line(screen, Color("black"), start, end)

 

add_observer(draw_images(True))
add_observer(draw_pivot_lines)
add_observer(draw_connection_lines)
add_observer(draw_images(False))

run()