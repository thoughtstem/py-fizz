#lang racket

(require py-fizz)

;(set-package-path! "/Users/thoughtstem/Dev/Python/py-fizz")
 


(define c
  (balloons-pulling 5
                    (bowling-ball)
                    100))

(simulate
 (wooden-level
  (above
   c
   (v-space 50)
   (beside (cannon 
            (cannon 
             (cannon 
              (breakable-balloon)
              1000 120)
             0 120)
            0 120)
           (h-space 100)
           (cannon (bowling-ball) 10000 45)))))



