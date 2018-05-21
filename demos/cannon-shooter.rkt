#lang racket-bricks

(require "../compiler.rkt")
(require "../toys/toys.rkt")
(require (prefix-in h: 2htdp/image))


(define c
  (balloons-pulling 5
                    (bowling-ball)
                    100))

(simulate
 (wooden-level
  (above
   c
   (v-space 50)
   (beside (cannon (cannon (cannon (breakable-balloon))))
           (h-space 100)
           (cannon (bowling-ball))))))



