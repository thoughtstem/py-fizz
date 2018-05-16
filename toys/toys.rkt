#lang racket

(provide wooden-level
         pipe
         catapult
         car
         balloon
         ball
         block
         balloons-pulling
         balloon-pulling
         conveyor-belt
         pendulum
         my-motor
         pinned-motor
         my-pivot

         bowling-ball

         v-space
         h-space

         fragments
         stick-figure
         )

(require "../compiler.rkt")
(require (prefix-in h: 2htdp/image))

(define (boxify thing)
  (make-dynamic #:collider box-collider thing))


(define (stick-figure)
  (make-dynamic #:collider box-collider
   (h:bitmap "./imgs/stick-figure.png")))


(define (fragments thing res)
  (define i (preview thing))
  

  (define (fragment x y d)
    (boxify 
     (h:crop (* x (/ (h:image-width i) d))
             (* y (/ (h:image-height i) d))
                           
             (/ (h:image-width i) d)
             (/ (h:image-height i) d)
             i)))

  (define cols
    (for/list ([x (range res)])
      (apply above (for/list ([y (range res)])
                     (fragment x y res)))))
  
  (apply beside cols))


(define (pipe w h)
  (define texture (scale-to w h (h:bitmap "./imgs/brushed-metal.png")))
  (define main (h:rectangle w h "solid" "black"))
  (make-dynamic #:collider box-collider
                (stroke (h:place-image texture (/ w 2) (/ h 2) main))))


(define (catapult launch)
  (define piv (my-pivot))
  (define rod (pipe 200 10))

  (define launcher (initial-velocity '(0 1500000) (bowling-ball)))

  (define connected-piv
    (connect-pivot
      piv
      rod))

  (define base (make-static (circle 1 "solid" "black")))
  
  (define spring-pivot
    (angle-spring base
                  rod
                  0
                  100000000))

  (define seesaw
    (above
     (overlay connected-piv
              rod)
     spring-pivot))


  (above (beside launcher (h-space 150))
         (v-space 50)
         (beside (h-space 150) launch)
         seesaw))





(module+ test


  (define (catapult-test)

    (define example1
      (wooden-level
       (catapult (ball))))

    (simulate example1))

  
  

  

  (define (balloon-test)

    (define example1

      (wooden-level
       (above
        (car)
        (v-space 20)
        (balloons-pulling 4 (motorize 0 (block)) 100))
       ))

      

    (displayln (list
                (preview example1)
                (preview2 example1)))

    (simulate example1))

  


  (define (pin-test)

    (define example1

      (wooden-level

       (above (car)
              (v-space 100)
              (car) )
       ))

      

    (displayln (list
                (preview example1)
                (preview2 example1)))

    (simulate example1))



  
  (define (belt-test)

    (define example1

      (wooden-level
       (above

        (beside
         (block)
         (block)
         (block)
         (block)
         (block)
         (h-space 100))
        (v-space 20)
        (conveyor-belt 8 5)
        (v-space 100)
        (conveyor-belt 10 -5)
        )))

    

    (displayln (list
                (preview example1)
                (preview2 example1)))

    (simulate example1))


  )






;Correlate strength of balloon and its size
(define (balloon)
  (gravity '(0 -100) (motorize 0
                               (make-dynamic #:collider box-collider
                                   (h:bitmap "./imgs/balloon.png")))))


(define (balloon-pulling obj rope-dist)
  (define b (balloon))

  (define p-obj (spring obj b rope-dist))
 
  (above b
         (v-space rope-dist)
         p-obj))


(define (balloons-pulling n obj rope-dist)
  (define bs (map (thunk* (balloon)) (range n)))

  (define p-obj (foldl (λ(n res)
                         (spring res n rope-dist))
                       obj
                       bs))
 
  (above (apply beside bs)
         (v-space rope-dist)
         p-obj))




(define (conveyor-belt num (s 10))
  (define num-list (range num))
  (define pinned-motor-list (map (thunk* (pinned-motor (if (positive? s) "red" "blue") s)) num-list))
  (apply beside
   pinned-motor-list))



(define (car (speed 1))
  (define b1 (ball))

  (define b2 (ball))

  (define b3 (ball))

  (define top (motorize 0 (block)))

  (define p-b1 (pin
                (pin b1 b2)
                top))

  (define p-b2 (pin (pin b2 b3) top))

  (define p-b3 (pin b3 top))

  (above top
         (v-space 5)
         (beside (motorize speed p-b1)
                 (h-space 5)
                 (motorize speed p-b2)
                 (h-space 5)
                 (motorize speed p-b3))))
























(define (scale-to x y i)
  (h:scale/xy (/ x (h:image-width i)) (/ y (h:image-height i)) i))

(define (borders i)
  (define h-line (make-static #:collider box-collider
                              (rectangle (+ 20 (width i)) 10 "solid" "black")))
  
  (define v-line (make-static #:collider box-collider
                              (rectangle 10 (height i) "solid" "black")))

  (above
   h-line
   (beside v-line
           i
           v-line)
   h-line))

(define (stroke i)
  (define w (add1 (h:image-width i)))
  (define h (add1 (h:image-height i)))
  (overlay i
           (rectangle w h "solid" "black")))

(define (my-pivot)
  (make-pivot
   (h:bitmap "./imgs/screw.png")))


(define (bowling-ball)
  (make-dynamic #:mass 10000 (h:bitmap "./imgs/bowling-ball.png")))

(define (ball (size 40))
  (make-dynamic
   (scale-to size size (h:bitmap "./imgs/wheel.png"))))

(define (block (force-dir '(0 0)) (size 40))
  (initial-velocity
   force-dir
   (make-dynamic #:collider box-collider
   (stroke (scale-to size size (h:bitmap
                                "./imgs/crate.png") )))))

(define (v-space size)
  (rectangle 1 size "solid" "transparent"))

(define (h-space size)
  (rectangle size 1 "solid" "transparent"))

(define (pendulum (force-dir '(0 0)))
  (define piv (my-pivot))
  (define b1 (ball force-dir))

  (define connected-piv
    (connect-pivot
     piv
     b1))

  (above connected-piv
         (v-space 50)
         b1))




(define (my-motor c (s 10))
  (motorize s (make-dynamic
                    (overlay
                     (ball 40)
                     (circle 20 "solid" c)))))


(define (pinned-motor c (s 10))
  (define piv (my-pivot))
  (define m1 (my-motor c s))

    
  (define c-piv
    (connect-pivot
     piv
     m1))
    
  (overlay c-piv m1))

(define (wooden-level i)
  (borders
   (overlay
    i
    (h:bitmap "./imgs/wooden-bg.png"))))


;Can refactor most of these tests. DRY
#;(module+ test






  
  (define (gear-test)

  
    (define internal
      
      (above
       (ball)
       (v-space 20)
       (pinned-motor "blue")))

    (define example1
      (wooden-level internal))

    (simulate example1))

  (define (motor-test)

    (define m1 (my-motor "red"))
    (define m2 (my-motor "green"))
    (define m3 (my-motor "blue"))

    (define internal
      (beside
        m1 m2 m3))

    (define example1
      (wooden-level internal))

    (simulate example1))


  (define (piv-test)
    (define internal
      (above
       ;(ball)
      ; (space 20)
       (beside
        (pendulum)
        (pendulum)
        (pendulum)
        (pendulum)
        (pendulum '(500000 0))
        (pendulum '(500000 0)))))

    (define example1
      (wooden-level internal))

    (simulate example1))



  
  
  

  (define (cool-test)
    
    (define internal
      (above
       (apply beside
              (map ball (range 3)))
       (make-dynamic (circle 50 "solid" "blue"))))

    (define example1
      (borders
       (overlay
        internal
        (square 300 "solid" "white"))))

    (simulate example1))

  )











