#lang racket-bricks

(require "../compiler.rkt")
(require "../toys/toys.rkt")
(require (prefix-in h: 2htdp/image))

;TODO:
;  Broken demo.  I want to make the car switch directions.  But...
;    Collisions with composite objects are broken.  Revisit when working.

;  Also wonky... swapping to fragments makes the code gigantic!!

;  It's disgusting that you have to overlay the hidden object and activate it...
;    Better to just spawn a new one...


(define temp '())

(define (breakable-balloon)
  (define b (balloon))
  (define b2 (fragments b 4)
    #;(hidden (fragments b 4)))

  (define b-with-behaviour
    (on-click b (do-many
                 (swap-to b2))))

  (set! temp (cons b2 temp))
  
  b-with-behaviour)



(simulate
 (wooden-level
  (apply overlay
         (cons
          (above
           (beside
            (breakable-balloon)
            (breakable-balloon)
            (breakable-balloon)
            (breakable-balloon))
           (car))
          temp))))



#|
(simulate
 (wooden-level
  (above (ball)
         (ball))))

|#
