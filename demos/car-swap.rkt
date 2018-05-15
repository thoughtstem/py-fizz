#lang racket-bricks

(require "../compiler.rkt")
(require "../toys/toys.rkt")
(require (prefix-in h: 2htdp/image))

;TODO:
;  Broken demo.  I want to make the car switch directions.  But...
;    Collisions with composite objects are broken.  Revisit when working.

(define b (bowling-ball))
(define c (car))
(define c2 (hidden (car)))

(define c-with-behaviour
  (on-collide c b (do-many
                    (swap-to c2))))

(simulate
 (wooden-level
  (overlay
   c2
   (above b
          (v-space 100)
          c-with-behaviour))))



 