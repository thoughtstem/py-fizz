#lang racket

(require 2htdp/image)

(define base
  (rectangle 300
             300
             "solid"
             (make-color 0 0 0 100)))

(define msg
  (text/font "Game Over" 40 "red"
             "Gill Sans" 'swiss 'normal 'bold #f))

(define dude
  (bitmap "/Users/thoughtstem/Dev/Python/py-fizz/toys/imgs/stick-figure.png"))


(define lose-screen
  (overlay (above msg
                (circle 40 "solid" "transparent")
                (beside dude
                        (text "(Don't let people die!)" 16 "red")))
         base))

lose-screen

(save-image lose-screen "../images/lose-screen.png")


(define msg2
  (text/font "You win!" 40 "green"
             "Gill Sans" 'swiss 'normal 'bold #f))

(define dude2
  (bitmap "/Users/thoughtstem/Dev/Python/py-fizz/toys/imgs/ghost.png"))


(define win-screen
  (overlay (above msg2
                (circle 40 "solid" "transparent")
                (beside dude
                        (text "(You got them all!)" 16 "green")))
         base))

win-screen

(save-image win-screen "../images/win-screen.png")


