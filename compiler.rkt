#lang racket

(require (prefix-in h: 2htdp/image))

(provide compile
         make-static
         make-dynamic
         make-cosmetic
         make-pivot
         connect-pivot
         motorize
         pin
         gear
         gravity
         spring
         angle-spring
         
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

         add-after-compile
         on-collide
         on-click
         id

         hidden

         ;Callbacks for collisions...
         do-many
         spawn
         swap-to

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
  (-> (or/c physical? cosmetic? layout?) any/c (or/c physical? cosmetic? layout?))
  (cond [(layout? thing)  (struct-copy layout
                                       thing
                                       [children (map (curryr add-after-compile f) (layout-children thing))])]
        [(physical? thing)  (struct-copy physical
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

(define/contract (make-dynamic i
                               #:collider (type circle-collider)
                               #:mass (mass 10)
                               )
  (->* ((or/c h:image? cosmetic? layout?)) (#:collider any/c #:mass number?) physical?)

  (define img (preview i))
  (define obj
    (physical (next-id)
            (half-width img) (half-height img)
            '()
            (collider-for img type)
            img
            #t))

  (add-after-compile obj
                     (λ(me py-obj)
                       (format "obj~a.mass = ~a"
                               (id me)
                               mass))))

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



(define/contract (gear f s)
  (-> physical? physical? physical?)
  (add-after-compile f
                     (λ(me py-obj)
                       (format "gear(obj~a,obj~a)"
                               (id f)
                               (id s)))))


(define/contract (pin f s)
  (-> physical? physical? physical?)
  (add-after-compile f
                     (λ(me py-obj)
                       (format "pin(obj~a.body.position,obj~a,obj~a.body.position,obj~a)\nconnected_shapes.append([obj~a, obj~a])"
                               (id f)
                               (id f)
                               (id s)
                               (id s)
                               (id f)
                               (id s)))))


(define/contract (initial-velocity dir p)
  (-> (listof number?) physical? physical?)
  (add-after-compile p
                     (λ(me py-obj)
                       (format "obj~a.hit((~a, ~a), obj~a.position)"
                               (id me)
                               (first dir) (second dir)
                               (id me)
                               ))))

(define/contract (motorize speed p)
  (-> number? physical? physical?)
  (add-after-compile p
                     (λ(me py-obj)
                       (format "motor(obj~a, ~a)"
                               (id me)
                               speed
                               ))))

;I don't love that dist is a param.  Better to set based on initial object positions
(define/contract (spring f s dist) 
  (-> physical? physical? number? physical?)
  (add-after-compile f
                     (λ(me py-obj)
                       (format "spring(obj~a.body.position, obj~a, obj~a.body.position, obj~a, ~a, 20000, 1000)\nconnected_shapes.append([obj~a, obj~a])"
                               (id f)
                               (id f)
                               (id s)
                               (id s)
                               dist
                               (id f)
                               (id s)))))

(define/contract (angle-spring f s
                               (angle 0)
                               (stiffness 0)
                               (damping 0)
                               ) 
  (->* (physical? physical?) (number? number? number?) physical?)
  (add-after-compile f
                     (λ(me py-obj)
                       (format "rotary_spring(obj~a, obj~a, ~a, ~a, ~a)"
                               (id f)
                               (id s)
                               angle
                               stiffness
                               damping))))


(define/contract (gravity dir p)
  (-> (list/c number? number?) physical? physical?)
  (add-after-compile p
                     (λ(me py-obj)
                       (format "obj~a.gravity = (~a,~a)"
                               (id me)
                               (first dir) (second dir)))))


(define/contract (on-collide f s py-code)
  (-> (or/c physical? layout?) (or/c physical? layout?) string? (or/c physical? layout?))
  (define collision-f (format "on_collide_~a_~a"
                              (id f)
                              (id s)
                              ))
  
  (add-after-compile f
                     (λ(me py-obj)
                       (format "def ~a(f,s,p):\n~a\n  return True\nadd_collision(obj~a, obj~a, ~a) if 'obj~a' in vars() else None"
                               collision-f
                               py-code
                               (id me)
                               (id s)
                               collision-f
                               (id me)))))

(define (hidden o)
  (add-after-compile o
                     (λ(me py-obj)
                       (format "deactivate(obj~a) if 'obj~a' in vars() else None" (id me) (id me)))))

(define (spawn o)
  (if (layout? o)
      (apply do-many (map spawn (layout-children o)))
      (format "  obj~a.body.position=p\n  reactivate(obj~a)"
              (id o) (id o))))

(define (swap-to o)
  (if (layout? o)
      (apply do-many (map swap-to (layout-children o)))
      (string-append
       (regexp-replace* #rx"OBJ" "  try:\n    OBJ.body.position=(p[0]+OBJ.body.position[0]-w/2, p[1]+OBJ.body.position[1]-h/2)\n"
                        (format "obj~a" (id o)))
       (format "    reactivate(obj~a)\n    deactivate(f)\n" (id o))
       "  except:\n    print('Exception')\n")))



(define/contract (on-click f py-code)
  (-> (or/c physical? layout?) string? (or/c physical? layout?))

  
  (add-after-compile f
                     (λ(me py-obj)
                       (define click-f (format "on_click_~a"
                                               (id me)))
                       (format "def ~a(keys):\n  global obj~a\n  f = obj~a\n  p=f.body.position\n  if(mouse_clicked() and obj~a.inside(mouse_point())):\n~a\n  return True\nadd_observer(~a)\n"
                               
                               click-f
                               (id me)
                               (id me)
                               (id me)
                               (regexp-replace* #rx"  " py-code "    ") ;OMG this is disgusting.  Use hy please!!!
                               click-f
                               ))))



(define (do-many . things)
  (string-join things "\n"))



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

w=~a
h=~a
window('Most Awesome Thing Ever', w, h)

user_shapes = []
image_bindings = []
pivots = []
connected_shapes = []

~a


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
      pygame.draw.line(screen, Color(\"black\"), start, end)

      #screen.blit(rotated_logo_img, p)

def draw_connection_lines(keys):
  global pivots
  for c in connected_shapes:
    start = c[0].body.position
    end   = c[1].body.position

    if(not(c[0].active) or not(c[1].active)):
      continue
   
    screen = pygame.display.get_surface()
    pygame.draw.line(screen, Color(\"black\"), start, end)

 

add_observer(draw_images(True))
add_observer(draw_pivot_lines)
add_observer(draw_connection_lines)
add_observer(draw_images(False))

run()")

