#lang racket-bricks

(require "../py-fizz.rkt")


;(simulate #|a|# (wooden-level #|with a|# (cannon #|that shoots out a|# (car))))


(define balloon-builder
  (toggle-static
                  (builder (balloon))))

(define payload (balloons-pulling 7 balloon-builder))



(simulate
 (wooden-level
  (beside
   (car 1
    (toggle-static
     (cannon balloon-builder 10000 170)))
   
   (h-space 200)
   
   (builder (car -1
                 payload
                 (last (shape->list payload))))

   (h-space 200)

   (builder (car 1
                 balloon-builder)))))



