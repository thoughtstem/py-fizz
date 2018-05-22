#lang racket

(require 2htdp/image)

(define base
  (rectangle 300
             300
             "solid"
             (make-color 100 100 100 100)))

(define msg
  (text "Game Over" 40 "red"))

(define dude
  (bitmap "/Users/thoughtstem/Dev/Python/py-fizz/toys/imgs/stick-figure.png"))


(overlay (above msg
                (circle 40 "solid" "transparent")
                (beside dude
                        (text "(Don't let people die!)" 16 "red")))
         base
         )