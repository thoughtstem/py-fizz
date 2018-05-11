#lang racket

(require (prefix-in h: 2htdp/image))

(provide compile
         make-static
         make-dynamic
         make-cosmetic
         make-pivot
         connect-pivot
         
         box-collider
         circle-collider

         initial-velocity

         circle
         rectangle
         square

         width
         height

         above
         beside
         overlay

         preview
         preview2
         simulate)


(define (map-with-i f l)
  (for/list ([i (range (length l))])
    (f (list-ref l i)
       i)))

(define (make-safe f)
  (lambda (x . xs)
    (if (empty? xs)
        x
        (apply f (cons x xs)))))

(define (half i)
  (/ i 2))


(struct layout   (id x y w h name preview-f children)           #:transparent)
(struct physical (id x y after-compile collider image dynamic?) #:transparent)
(struct cosmetic (id x y after-compile image)                   #:transparent)

(define (is-cosmetic? phys)
  (cosmetic? phys))

(define (is-dynamic? phys)
  (and (physical? phys)
       (physical-dynamic? phys)))

(define (is-static? phys)
  (and (physical? phys)
       (not (physical-dynamic? phys))))

(define/contract (get-image x)
  (-> (or/c physical? cosmetic?) h:image?)
  (if (physical? x)
      (physical-image x)
      (cosmetic-image x)))

(define/contract (add-after-compile thing f)
  (-> (or/c physical? cosmetic?) any/c (or/c physical? cosmetic?))
  (cond [(physical? thing)  (struct-copy physical
                                         thing
                                         [after-compile (append (physical-after-compile thing) (list f))])]
        [(cosmetic? thing)  (struct-copy cosmetic
                                         thing
                                         [after-compile (append (cosmetic-after-compile thing) (list f))])]))

(struct collider ())
(struct circle-collider collider (r))
(struct box-collider collider (w h))



(define current-id 0)
(define (next-id)
  (set! current-id (add1 current-id))
  current-id)

(define/contract (id thing)
  (-> (or/c cosmetic? physical? layout?) number?)
  (cond [(layout? thing)  (layout-id thing)]
        [(physical? thing) (physical-id thing)]
        [(cosmetic? thing)  (cosmetic-id thing)]))

(define/contract (width thing)
  (-> (or/c h:image? cosmetic? physical? layout?) number?)
  (cond [(layout? thing)  (layout-w thing)]
        [(h:image? thing) (h:image-width thing)]
        [(physical? thing) (h:image-width (physical-image thing))]
        [(cosmetic? thing)  (h:image-width (cosmetic-image thing))]))

(define/contract (height thing)
  (-> (or/c h:image? cosmetic? physical? layout?) number?)
  (cond [(layout? thing)  (layout-h thing)]
        [(h:image? thing) (h:image-height thing)]
        [(physical? thing) (h:image-height (physical-image thing))]
        [(cosmetic? thing)  (h:image-height (cosmetic-image thing))]))

(define/contract (x thing)
  (-> (or/c cosmetic? physical? layout?) number?)
  (cond [(layout? thing)    (layout-x thing)]
        [(physical? thing)  (physical-x thing)]
        [(cosmetic? thing)  (cosmetic-x thing)]))

(define/contract (y thing)
  (-> (or/c cosmetic? physical? layout?) number?)
  (cond [(layout? thing)    (layout-y thing)]
        [(physical? thing)  (physical-y thing)]
        [(cosmetic? thing)  (cosmetic-y thing)]))

(define/contract (set-x thing new-x)
  (-> (or/c cosmetic? physical? layout?)
      number?
      (or/c cosmetic? physical? layout?))

  (cond [(layout? thing)    (struct-copy layout   thing  [x new-x])]
        [(physical? thing)  (struct-copy physical thing  [x new-x])]
        [(cosmetic? thing)  (struct-copy cosmetic thing  [x new-x])]))

(define/contract (set-y thing new-y)
  (-> (or/c cosmetic? physical? layout?)
      number?
      (or/c cosmetic? physical? layout?))

  (cond [(layout? thing)    (struct-copy layout   thing  [y new-y])]
        [(physical? thing)  (struct-copy physical thing  [y new-y])]
        [(cosmetic? thing)  (struct-copy cosmetic thing  [y new-y])]))

(define (set-xy thing new-x new-y)
  (set-y (set-x thing new-x) new-y))

(define (half-width t)
  (half (width t)))

(define (half-height t)
  (half (height t)))


(define (wrap-images i)
  (if (h:image? i)
      (make-cosmetic i)
      i))

;Takes in a list of things
;  they are either images or physical objects
(define/contract (overlay . things)
  (->* () #:rest (listof (or/c h:image? cosmetic? physical? layout?)) layout?)

  (define w (apply max (map width things)))
  (define h (apply max (map height things)))
  
  (define (fix-xy thing i)
    (define younger-siblings (take things i))


    (define y-adj (if (layout? thing)
                      (/ (- h (height thing)) 2)
                      (/ h 2)))

    (define x-adj
      (if (layout? thing)
          (/ (- w (width thing)) 2)
          (/ w 2)))

    (set-xy thing x-adj y-adj))

  (layout (next-id)
          0 0
          w h
          'overlay
          h:overlay
          (map-with-i fix-xy
                      (map wrap-images things))))


(define/contract (above . things)
  (->* () #:rest (listof (or/c h:image? cosmetic? physical? layout?)) layout?)

  (define w (apply max (map width things)))
  (define h (apply + (map height things)))
  
  (define (fix-xy thing i)
    (define younger-siblings (take things i))
    (define y-adj (+ (y thing)
                     (apply + (map height younger-siblings))))

    (define x-adj
      (if (layout? thing)
          (/ (- w (width thing)) 2)
          (/ w 2)))

    (set-xy thing x-adj y-adj))
  
  (layout (next-id)
          0 0
          w h
          'above
          h:above
          ;(map wrap-images things)
          (map-with-i fix-xy
                      (map wrap-images things))))


(define/contract (beside . things)
  (->* () #:rest (listof (or/c h:image? cosmetic? physical? layout?)) layout?)

  (define w (apply + (map width things)))
  (define h (apply max (map height things)))
  
  (define (fix-xy thing i)
    (define younger-siblings (take things i))
    (define y-adj (if (layout? thing)
                      (/ (- h (height thing)) 2)
                      (/ h 2)))

    (define x-adj (+ (x thing)
                     (apply + (map width younger-siblings))))

    (set-xy thing x-adj y-adj))

  (layout (next-id)
          0 0
          w h
          'beside
          h:beside
          (map-with-i fix-xy
                      (map wrap-images things))))

(define/contract (preview thing)
  (-> (or/c h:image? cosmetic? physical? layout?) h:image?)

  (cond [(h:image? thing) thing]
        [(cosmetic? thing) (cosmetic-image thing)]
        [(physical? thing) (physical-image thing)]
        [(layout? thing) (apply (make-safe (layout-preview-f thing))
                                (map preview (layout-children thing)))]))



(define/contract (collider-for i collider-type)
  (-> h:image? any/c collider?)
  (if (eq? collider-type circle-collider)
      (circle-collider (max (h:image-width i)
                            (h:image-height i)))

      (box-collider (h:image-width i)
                    (h:image-height i))))

(define/contract (make-dynamic i #:collider (type circle-collider))
  (->* ((or/c h:image? cosmetic? layout?)) (#:collider any/c) physical?)

  (define img (preview i))
  (physical (next-id)
            (half-width img) (half-height img)
            '()
            (collider-for img circle-collider)
            img
            #t))

(define/contract (make-static i #:collider (type circle-collider))
  (->* ((or/c h:image? cosmetic? layout?)) (#:collider any/c) physical?)
  (define img (preview i))
  (physical (next-id) 
            (half-width img) (half-height img)
            '() ;After compile
            (collider-for img type)
            img
            #f))

(define/contract (make-cosmetic i)
  (-> (or/c h:image? cosmetic? layout?) cosmetic?)
  (define img (preview i))
  (cosmetic (next-id)
            (half-width img) (half-height img)
            '()
            img))

(define/contract (make-pivot i)
  (-> (or/c h:image? cosmetic?) cosmetic?)
  (define base (make-cosmetic i))
  (add-after-compile base
                     (λ(me py-obj)
                       (format "pivot~a = pivot((~a,~a))\npivots.append(pivot~a)"
                               (id me)
                               (pymunk-obj-x py-obj)
                               (pymunk-obj-y py-obj)
                               (id me)))))


(define/contract (connect-pivot p other)
  (-> cosmetic? physical? cosmetic?)
  (add-after-compile p
                     (λ(me py-obj)
                       (format "pivot~a.connect(obj~a)"
                               (id p)
                               (id other)))))


(define/contract (initial-velocity dir p)
  (-> (listof number?) physical? physical?)
  (add-after-compile p
                     (λ(me py-obj)
                       (format "obj~a.hit((~a, ~a), obj~a.position)"
                               (id me)
                               (first dir) (second dir)
                               (id me)
                               ))))




(struct pymunk-obj (dynamic x y) #:transparent)
(define (pymunk-obj-name o)
  (format "obj~a" (id (pymunk-obj-dynamic o))))






;Should interpret the layout structure into
;  a list of colliders with absolute locations and appropriately bound images

(define/contract (pymunk-obj-list current (root-x 0) (root-y 0))
  (->* ((or/c physical? cosmetic? layout?))
       (integer? integer?)
       (listof pymunk-obj?))


  (cond [(not (layout? current)) (list (pymunk-obj current
                                               (+ root-x (x current))
                                               (+ root-y (y current))))]
        [(layout? current) (apply append
                             (map-with-i (λ(c i)
                                           (pymunk-obj-list c
                                                            (+ root-x (x current))
                                                            (+ root-y (y current))))
                                         (layout-children current)))]))





(define (obj->after-compiles x i)
  (define phys (pymunk-obj-dynamic x))

  (define after-compiles (if (cosmetic? phys)
                             (cosmetic-after-compile phys)
                             (physical-after-compile phys)))
  
  (string-join (map (λ(f) (f phys x)) after-compiles)
               "\n"))


(define (obj->python x i)
  (define phys (pymunk-obj-dynamic x))

  (define w (width  (pymunk-obj-dynamic x)))
  (define h (height (pymunk-obj-dynamic x)))

  (define after-compiles (if (cosmetic? phys)
                             (cosmetic-after-compile phys)
                             (physical-after-compile phys)))

  (define collider (and
                    (not (is-cosmetic? phys))
                    (physical-collider phys)))

  
  (define collider-type (cond 
                          [(circle-collider? collider) "ball"]
                          [(box-collider? collider)    "box"]
                          [else "ball"]))

  
  (define fun-name (format
                    (cond [(is-cosmetic? phys) "cosmetic_~a"]
                          [(is-dynamic? phys) "~a"]
                          [(is-static? phys) "static_~a"])
                    collider-type))

  (define name
    (pymunk-obj-name x))
  
  (define first-line
    (if (box-collider? collider)
        (format "~a = ~a((int(~a), int(~a)), ~a, ~a)"
                name
                fun-name
                (- (pymunk-obj-x x) (half w))
                (- (pymunk-obj-y x) (half h))
                w
                h)
        (format "~a = ~a((int(~a), int(~a)), ~a)"
                name
                fun-name
                (pymunk-obj-x x)
                (pymunk-obj-y x)
                (/ (max w h) 2))))

  (define second-line
    (format "~a.color = Color(~s)"
            name
            "white"))

  (define third-line
    (format "~a.group = ~a"
            name
            (id (pymunk-obj-dynamic x))))

  ;Should be able to write out the embedded image here.  It's inside the dynamic/cosmetic object...
  (define path
    (format "/Users/thoughtstem/Dev/Python/py-fizzery/~a" (format "~a.png"
                                                                  (pymunk-obj-name x))))

  (h:save-image (get-image phys) path)
  
  (define fourth-line
    (format "~a_image = pygame.image.load(~s)"
            name
            path))

  (define fifth-line
    (format "image_bindings.append([~a, ~a_image])"
            name
            name))

  (define sixth-line
    (format "user_shapes.append(~a)"
            name))

  (define construction-lines
    (list first-line second-line third-line fourth-line fifth-line sixth-line))

  (define after-compile-lines
    (map force after-compiles))

  (string-join construction-lines
               "\n"))

(define (simulate thing)
  (define objs (reverse (pymunk-obj-list thing)))

  (define pre (preview thing))
  
  (compile (string-join (append (map-with-i obj->python objs)
                                (map-with-i obj->after-compiles objs)
                                ) "\n")
           "demo.py"
           (h:image-width pre)
           (h:image-height pre)))

(define (preview2 thing)
  (define objs (pymunk-obj-list thing))

  (define pre (preview thing))
  
  (define bg (h:rectangle (h:image-width pre)
                          (h:image-height pre)
                          "solid"
                          "transparent"))

  (apply (make-safe h:overlay)
         (map (λ(i) (h:place-image
                     (get-image (pymunk-obj-dynamic i))
                     (pymunk-obj-x i)
                     (pymunk-obj-y i)
                     bg)) objs)))


(define circle    (compose make-cosmetic h:circle))
(define square    (compose make-cosmetic h:square))
(define rectangle (compose make-cosmetic h:rectangle))


(define (program->string p)
  (~a p))

(define (compile p file-name w h)
  (define final (format (boiler)
                        w h
                        (program->string p)))
  (with-output-to-file file-name #:exists 'replace
    (lambda () (printf final)))
  (system (string-append "PYTHONPATH=/Users/thoughtstem/Dev/Python/py-fizzery/pygame/pyphysicssandbox /usr/local/bin/python3 " file-name)))






(define (boiler)
  "import math

import pymunk

from pyphysicssandbox import *
import pygame
from pymunk import Vec2d

def hit_ball(keys):
#    if mouse_clicked():
#        ball1.hit((0, -400000), ball1.position)

    if constants.K_RIGHT in keys:
        floor.surface_velocity = (100, 0)
    elif constants.K_LEFT in keys:
        floor.surface_velocity = (-100, 0)



window('Shape Methods & Properties', ~a, ~a)

user_shapes = []
image_bindings = []
pivots = []

~a


add_observer(hit_ball)


def flipy(y):
    return -y+600

def image_for(s):
  global image_bindings
  for b in image_bindings:
    if b[0] == s:
      return b[1]
  return False

def draw_images(keys):
  global user_shapes
  for s in user_shapes:
    if(not image_for(s)):
      continue

    if(s.body):
      p = Vec2d(s.body.position.x, s.body.position.y)
    else:
      p = Vec2d(s._x, s._y)

    angle = 0
    if(s.body):
      angle = s.body.angle

    angle_degrees    = math.degrees(angle) 
    rotated_logo_img = pygame.transform.rotate(image_for(s), angle_degrees)
    
    offset = Vec2d(rotated_logo_img.get_size()) / 2.
    p      = p - offset
    
    screen = pygame.display.get_surface()
    screen.blit(rotated_logo_img, p)

def draw_pivot_lines(keys):
  global pivots
  for p in pivots:
    start = p.body.position
    for j in p.shape:
      other = j.a
      end = other.position
      
      screen = pygame.display.get_surface()
      pygame.draw.line(screen, Color(\"black\"), start, end)

      #screen.blit(rotated_logo_img, p)


add_observer(draw_images)
add_observer(draw_pivot_lines)

run()"
  )

