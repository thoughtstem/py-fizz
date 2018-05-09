#lang racket

(require (prefix-in h: 2htdp/image))
(require "./compiler.rkt")

;Do we really need to be caching w and h?  We can calc from f and args...
(struct wrapper (sym f w h args) #:transparent)

;This is a stub that only works for circles at the moment...
(define (wrapper-color w)
  (third (wrapper-args w)))

(define (above . is)
  (wrapper 'above
           h:above
           (apply max (map wrapper-w is))
           (apply + (map wrapper-h is))
           is))

(define (beside . is)
  (wrapper 'beside
           h:beside
           (apply +
                  (map wrapper-w is))
           (apply max (map wrapper-h is))
           is))

(define (circle r k c)
  (wrapper 'circle
           h:circle (* r 2) (* r 2) (list r k c)))

(define (leaf? w)
  (not (findf wrapper? (wrapper-args w))))

(define (preview w)
  (if (leaf? w)
      (apply (wrapper-f w) (wrapper-args w))
      (apply (wrapper-f w) (map preview (wrapper-args w)))))



(define (flatten-shape-tree w
                            (root-x (/ WIDTH 2))
                            (root-y (/ HEIGHT 2)))
 
  
  (define name (wrapper-sym w))

  (define args ((if (eq? 'above name)
                    reverse
                    identity)
                (wrapper-args w)))

  ;Customized for circle for now.  Refactor when we need to branch
  (define (leaf->flat)
    `(,name ,root-x ,root-y ,(/ (wrapper-w w) 2) ,(wrapper-color w)))

  (define (sum-of-prior f i)
    (apply + (map f (take args i))))
  
  (define (do-recursion i thing)
    (define main-width (wrapper-w w))
    (define main-height (wrapper-h w))
    (define sub-width (wrapper-w thing))
    (define sub-height (wrapper-h thing))
    (match name
      ('beside (flatten-shape-tree thing
                                   (+ root-x (sum-of-prior wrapper-w i))
                                   (+ root-y (/ (- main-height sub-height) 2))))
      ('above  (flatten-shape-tree thing
                                   (+ root-x (/ (- main-width sub-width) 2))
                                   (+ root-y (sum-of-prior wrapper-h i))))))
  
  (if (leaf? w)
      (list (leaf->flat))
      (apply append (for/list ([i (range (length args))])
                      (do-recursion i
                                    (list-ref args i))))))

(define (shape->pymunk-obj-list w)
  (define shapes
    (flatten-shape-tree w))
  
  (string-join
   (map (λ(x) (format "~a(~a,~a,~a,~s)"
                      (first x)
                      (second x)
                      (third x)
                      (fourth x)
                      (fifth x))) shapes)
   "\n")

  ; "circle(random.randint(115,350), 400, \"green\")"
  )

(define (simulate w)
  (compile (shape->pymunk-obj-list w)
           "demo.py"))



(module+ test
  (require rackunit)

  (define ref-shape
    (h:above
     (h:circle 16 "solid" "red")
     (h:circle 16 "solid" "red")))
  
  (define my-shape
    (above
     (circle 16 "solid" "red")
     (circle 16 "solid" "red")))
  
  (check-equal? ref-shape
                (preview my-shape))


  (check-equal? (flatten-shape-tree my-shape)
                '((circle 300 300 16 "red")
                  (circle 300 332 16 "red")))







(define thingy2
  (beside
   (above
    (circle 10 "solid" "yellow")
    (circle 20 "solid" "orange"))
   (above
    (circle 40 "solid" "red")
    (circle 28 "solid" "blue"))))

(simulate (map (thunk* thingy2) (range 3)))



  










  
  )

(define WIDTH 600)
(define HEIGHT 600)
