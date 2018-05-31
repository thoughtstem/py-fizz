#lang racket

(require py-fizz)

(set-package-path! "/Users/thoughtstem/Dev/Python/py-fizz")
 

(define thing
  (make-static (pipe 20 20)))

(define d 50)
(define nothing (circle 1 "solid" "transparent"))

(define (my-builder-right n another (end nothing))
  (my-builder 1 0 n another end))

(define (my-builder-left n another (end nothing))
  (my-builder -1 0 n another end))

(define (my-builder-up n another (end nothing))
  (my-builder 0 -1 n another end))

(define (my-builder-down n another (end nothing))
  (my-builder 0 1 n another end))


(define (my-builder x y n another (end nothing))
  (overlay thing
           (builder #:left-right x
                    #:up-down    y
                    (if (= 1 n)
                        end
                        (overlay another
                                 (my-builder x y (- n 1) another end))))))

(simulate
 (wooden-level
  (above
   ;(breakable-balloon)
   (beside
    (my-builder-left 5
                     (my-builder-down 5 nothing (balloon)))
    (my-builder-right 5
                     (my-builder-down 5 nothing (balloon))))
   (v-space 50)
   (car)
   (v-space 50)
   (beside
    (my-builder-left 5
                     (my-builder-up 5 nothing (balloon)))
    (my-builder-right 5
                     (my-builder-up 5 nothing (balloon)))))))


