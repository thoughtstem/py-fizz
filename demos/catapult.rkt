#lang racket

(require py-fizz)

(set-package-path! "/Users/thoughtstem/Dev/Python/py-fizz")



(define b (stick-figure))
(define b2 (gravity '(0 0) (wheel)))

(define to-spawn (fragments
                   b
                   4))

(define b-with-behaviour
  (on-collide b 
              (spawn to-spawn #t)))
(simulate
 (wooden-level
  (catapult
    (above
     
     (balloons-pulling 3 b-with-behaviour)
     (v-space 100)
     b2))))
