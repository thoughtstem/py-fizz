#lang racket

(require py-fizz)

;(set-package-path! "/Users/thoughtstem/Dev/Python/py-fizz")

(simulate
 (wooden-level
  (above
   (beside
    (breakable-balloon)
    (breakable-balloon)
    (breakable-balloon)
    (breakable-balloon))
   (beside (car 5)
           (h-space 200)))))
