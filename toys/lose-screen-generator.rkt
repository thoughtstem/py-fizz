#lang racket

(require 2htdp/image)

(define base
  (rectangle 300
             300
             "solid"
             (make-color 0 0 0 100)))

(define msg
  (text/font "Game Over" 40 "orange"
             "Gill Sans" 'swiss 'normal 'bold #f))

(define dude
  (overlay
   (bitmap "/Users/thoughtstem/Dev/Python/py-fizz/toys/imgs/stick-figure.png")
   (circle 40 "solid" "orange")))


(define lose-screen
  (overlay (above msg
                (circle 40 "solid" "transparent")
                (beside dude
                        (circle 10 "solid" "transparent")
                        (text "(Don't let people die!)" 16 "orange")))
         base))

lose-screen

(save-image lose-screen "../images/lose-screen.png")


(define msg2
  (text/font "You win!" 40 "green"
             "Gill Sans" 'swiss 'normal 'bold #f))

(define dude2
  (overlay
   (bitmap "/Users/thoughtstem/Dev/Python/py-fizz/toys/imgs/ghost.png")
   (circle 40 "solid" "green")))


(define win-screen
  (overlay (above msg2
                (circle 40 "solid" "transparent")
                (beside dude2
                        (circle 10 "solid" "transparent")
                        (text "(You got them all!)" 16 "green")))
         base))

win-screen

(save-image win-screen "../images/win-screen.png")


