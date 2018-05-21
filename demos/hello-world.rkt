#lang racket-bricks

(require py-fizz/py-fizz) 
 
(define ball
  (make-dynamic
   (circle 40 "solid" "red")))

(define floor
  (make-static #:collider box-collider
   (rectangle 200 10 "solid" "black")))

(simulate
 ball)

#;(simulate
 (above
  ball
  (v-space 100)))

#;(simulate
 (above
  (beside (h-space 50) ball (h-space 50))
  (v-space 100)
  floor))

#;(simulate
 (wooden-level
  (bowling-ball)))