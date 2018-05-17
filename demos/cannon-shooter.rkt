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
   (beside (gun (balloon))
           (h-space 20)
           (gun (bowling-ball))
           (h-space 200)))))
