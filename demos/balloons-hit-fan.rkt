#lang racket

(require py-fizz)

;(set-package-path! "/Users/thoughtstem/Dev/Python/py-fizz")
 


(define c
  (balloons-pulling 5
                    (bowling-ball);(motorize 5 (block))
                    100))

(define (m) (pinned-motor "orange" 100))

(simulate
 (wooden-level
  
  (above
   (crate)
   (beside (m) (m) (m))
   (v-space 30)
   c)))
