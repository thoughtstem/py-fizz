#lang racket

(require (prefix-in h: 2htdp/image))
(require racket-to-python/python-module)

(provide compile
         make-static
         make-dynamic
         make-cosmetic
         make-pivot
         connect-pivot
         motorize
         pin
         gear
         gravity
         spring
         angle-spring
         
         box-collider
         circle-collider

         initial-velocity

         circle
         rectangle
         square

         width
         height

         above
         beside
         overlay

         add-after-compile
         on-collide
         on-click
         id

         hidden

         ;Callbacks for collisions...
         do-many
         spawn
         swap-to

         preview
         preview2
         simulate)


(define (map-with-i f l)
  (for/list ([i (range (length l))])
    (f (list-ref l i)
       i)))

(define (make-safe f)
  (lambda (x . xs)
    (if (empty? xs)
        x
        (apply f (cons x xs)))))

(define (half i)
  (/ i 2))

(define (format-s s . insertions)
  (string->symbol (apply (curry format s) insertions)))


(struct layout   (id x y w h name preview-f children)           #:transparent)
(struct physical (id x y after-compile collider image dynamic?) #:transparent)
(struct cosmetic (id x y after-compile image)                   #:transparent)
  
(define (is-cosmetic? phys)
  (cosmetic? phys))

(define (is-dynamic? phys)
  (and (physical? phys)
       (physical-dynamic? phys)))

(define (is-static? phys)
  (and (physical? phys)
       (not (physical-dynamic? phys))))

(define/contract (get-image x)
  (-> (or/c physical? cosmetic?) h:image?)
  (if (physical? x)
      (physical-image x)
      (cosmetic-image x)))

(define/contract (add-after-compile thing f)
  (-> (or/c physical? cosmetic? layout?) any/c (or/c physical? cosmetic? layout?))
  (cond [(layout? thing)  (struct-copy layout
                                       thing
                                       [children (map (curryr add-after-compile f) (layout-children thing))])]
        [(physical? thing)  (struct-copy physical
                                         thing
                                         [after-compile (append (physical-after-compile thing) (list f))])]
        [(cosmetic? thing)  (struct-copy cosmetic
                                         thing
                                         [after-compile (append (cosmetic-after-compile thing) (list f))])]))

(struct collider ())
(struct circle-collider collider (r))
(struct box-collider collider (w h))



(define current-id 0)
(define (next-id)
  (set! current-id (add1 current-id))
  current-id)

(define/contract (id thing)
  (-> (or/c cosmetic? physical? layout?) number?)
  (cond [(layout? thing)  (layout-id thing)]
        [(physical? thing) (physical-id thing)]
        [(cosmetic? thing)  (cosmetic-id thing)]))

(define (obj-name me)
  (format-s "obj~a" (id me)))

(define/contract (width thing)
  (-> (or/c h:image? cosmetic? physical? layout?) number?)
  (cond [(layout? thing)  (layout-w thing)]
        [(h:image? thing) (h:image-width thing)]
        [(physical? thing) (h:image-width (physical-image thing))]
        [(cosmetic? thing)  (h:image-width (cosmetic-image thing))]))

(define/contract (height thing)
  (-> (or/c h:image? cosmetic? physical? layout?) number?)
  (cond [(layout? thing)  (layout-h thing)]
        [(h:image? thing) (h:image-height thing)]
        [(physical? thing) (h:image-height (physical-image thing))]
        [(cosmetic? thing)  (h:image-height (cosmetic-image thing))]))

(define/contract (x thing)
  (-> (or/c cosmetic? physical? layout?) number?)
  (cond [(layout? thing)    (layout-x thing)]
        [(physical? thing)  (physical-x thing)]
        [(cosmetic? thing)  (cosmetic-x thing)]))

(define/contract (y thing)
  (-> (or/c cosmetic? physical? layout?) number?)
  (cond [(layout? thing)    (layout-y thing)]
        [(physical? thing)  (physical-y thing)]
        [(cosmetic? thing)  (cosmetic-y thing)]))

(define/contract (set-x thing new-x)
  (-> (or/c cosmetic? physical? layout?)
      number?
      (or/c cosmetic? physical? layout?))

  (cond [(layout? thing)    (struct-copy layout   thing  [x new-x])]
        [(physical? thing)  (struct-copy physical thing  [x new-x])]
        [(cosmetic? thing)  (struct-copy cosmetic thing  [x new-x])]))

(define/contract (set-y thing new-y)
  (-> (or/c cosmetic? physical? layout?)
      number?
      (or/c cosmetic? physical? layout?))

  (cond [(layout? thing)    (struct-copy layout   thing  [y new-y])]
        [(physical? thing)  (struct-copy physical thing  [y new-y])]
        [(cosmetic? thing)  (struct-copy cosmetic thing  [y new-y])]))

(define (set-xy thing new-x new-y)
  (set-y (set-x thing new-x) new-y))

(define (half-width t)
  (half (width t)))

(define (half-height t)
  (half (height t)))


(define (wrap-images i)
  (if (h:image? i)
      (make-cosmetic i)
      i))

;Takes in a list of things
;  they are either images or physical objects
(define/contract (overlay . things)
  (->* () #:rest (listof (or/c h:image? cosmetic? physical? layout?)) layout?)

  (define w (apply max (map width things)))
  (define h (apply max (map height things)))
  
  (define (fix-xy thing i)
    (define younger-siblings (take things i))


    (define y-adj (if (layout? thing)
                      (/ (- h (height thing)) 2)
                      (/ h 2)))

    (define x-adj
      (if (layout? thing)
          (/ (- w (width thing)) 2)
          (/ w 2)))

    (set-xy thing x-adj y-adj))

  (layout (next-id)
          0 0
          w h
          'overlay
          h:overlay
          (map-with-i fix-xy
                      (map wrap-images things))))


(define/contract (above . things)
  (->* () #:rest (listof (or/c h:image? cosmetic? physical? layout?)) layout?)

  (define w (apply max (map width things)))
  (define h (apply + (map height things)))
  
  (define (fix-xy thing i)
    (define younger-siblings (take things i))
    (define y-adj (+ (y thing)
                     (apply + (map height younger-siblings))))

    (define x-adj
      (if (layout? thing)
          (/ (- w (width thing)) 2)
          (/ w 2)))

    (set-xy thing x-adj y-adj))
  
  (layout (next-id)
          0 0
          w h
          'above
          h:above
          ;(map wrap-images things)
          (map-with-i fix-xy
                      (map wrap-images things))))


(define/contract (beside . things)
  (->* () #:rest (listof (or/c h:image? cosmetic? physical? layout?)) layout?)

  (define w (apply + (map width things)))
  (define h (apply max (map height things)))
  
  (define (fix-xy thing i)
    (define younger-siblings (take things i))
    (define y-adj (if (layout? thing)
                      (/ (- h (height thing)) 2)
                      (/ h 2)))

    (define x-adj (+ (x thing)
                     (apply + (map width younger-siblings))))

    (set-xy thing x-adj y-adj))

  (layout (next-id)
          0 0
          w h
          'beside
          h:beside
          (map-with-i fix-xy
                      (map wrap-images things))))

(define/contract (preview thing)
  (-> (or/c h:image? cosmetic? physical? layout?) h:image?)

  (cond [(h:image? thing) thing]
        [(cosmetic? thing) (cosmetic-image thing)]
        [(physical? thing) (physical-image thing)]
        [(layout? thing) (apply (make-safe (layout-preview-f thing))
                                (map preview (layout-children thing)))]))



(define/contract (collider-for i collider-type)
  (-> h:image? any/c collider?)
  (if (eq? collider-type circle-collider)
      (circle-collider (max (h:image-width i)
                            (h:image-height i)))

      (box-collider (h:image-width i)
                    (h:image-height i))))

(define/contract (make-dynamic i
                               #:collider (type circle-collider)
                               #:mass (mass 10)
                               )
  (->* ((or/c h:image? cosmetic? layout?)) (#:collider any/c #:mass number?) physical?)

  (define img (preview i))
  (define obj
    (physical (next-id)
            (half-width img) (half-height img)
            '()
            (collider-for img type)
            img
            #t))

  (add-after-compile obj
                     (λ(me py-obj)
                       (py-begin
                        (py-set `(hy-DOT ,(obj-name me) mass) mass))
                       #;(compile-py (py-set `(hy-DOT ,(obj-name me) mass) mass)) ;(id me) "obj~a.mass = ~a"
                               
                               )))

(define/contract (make-static i #:collider (type circle-collider))
  (->* ((or/c h:image? cosmetic? layout?)) (#:collider any/c) physical?)
  (define img (preview i))
  (physical (next-id) 
            (half-width img) (half-height img)
            '() ;After compile
            (collider-for img type)
            img
            #f))

(define/contract (make-cosmetic i)
  (-> (or/c h:image? cosmetic? layout?) cosmetic?)
  (define img (preview i))
  (cosmetic (next-id)
            (half-width img) (half-height img)
            '()
            img))

(define/contract (make-pivot i)
  (-> (or/c h:image? cosmetic?) cosmetic?)
  (define base (make-cosmetic i))
  (add-after-compile base
                     (λ(me py-obj)
                       (define piv-name (format-s "pivot~a" (id me)))
                       (py-begin
                        (py-set piv-name
                               `(pivot (,(pymunk-obj-x py-obj) ,(pymunk-obj-y py-obj)))))
                       `(pivots.append ,piv-name))))


(define/contract (connect-pivot p other)
  (-> cosmetic? physical? cosmetic?)
  (add-after-compile p
                     (λ(me py-obj)
                       (define piv-connect (format-s "pivot~a.connect" (id me)))
                       (py-begin `(,piv-connect ,(obj-name other))))))



(define/contract (gear f s)
  (-> physical? physical? physical?)
  (add-after-compile f
                     (λ(me py-obj)
                       (py-begin
                        `(gear ,(obj-name f) ,(obj-name s))))))


(define/contract (pin f s)
  (-> physical? physical? physical?)
  (add-after-compile f
                     (λ(me py-obj)
                       (define f.body.position (format-s "obj~a.body.position" (id f)))
                       (define s.body.position (format-s "obj~a.body.position" (id s)))
                       (py-begin `(pin ,f.body.position ,(obj-name f) ,s.body.position ,(obj-name s))
                                 `(connected_shapes.append ,(py-list (obj-name f)
                                                                     (obj-name s)))))))


(define/contract (initial-velocity dir p)
  (-> (listof number?) physical? physical?)
  (add-after-compile p
                     (λ(me py-obj)
                       (define me.hit      (format-s "obj~a.hit" (id me)))
                       (define me.position (format-s "obj~a.position" (id me)))
                       (py-begin
                        `(,me.hit ,(py-list (first dir) (second dir))
                                 ,me.position)))))


(define/contract (motorize speed p)
  (-> number? physical? physical?)
  (add-after-compile p
                     (λ(me py-obj)
                       `(motor ,(obj-name me) ,speed))))


;I don't love that dist is a param.  Better to set based on initial object positions
(define/contract (spring f s dist) 
  (-> physical? physical? number? physical?)
  (add-after-compile f
                     (λ(me py-obj)
                       (define f.body.position (py-dot (obj-name f) 'body 'position))
                       (define s.body.position (py-dot (obj-name s) 'body 'position))
                       (py-begin `(spring ,f.body.position ,(obj-name f) ,s.body.position ,(obj-name s) 20000 1000)
                                 `(connected-shapes.append ,(py-list (obj-name f)
                                                                     (obj-name s)))))))

(define/contract (angle-spring f s
                               (angle 0)
                               (stiffness 0)
                               (damping 0)
                               ) 
  (->* (physical? physical?) (number? number? number?) physical?)
  (add-after-compile f
                     (λ(me py-obj)
                       (py-begin
                        `(rotary_spring ,(obj-name f)
                                       ,(obj-name s)
                                       ,angle
                                       ,stiffness
                                       ,damping)))))


(define/contract (gravity dir p)
  (-> (list/c number? number?) physical? physical?)
  (add-after-compile p
                     (λ(me py-obj)
                       (define me.gravity (format-s "obj~a.gravity" (id me)))
                       
                       (py-begin
                        (py-set me.gravity (py-tuple (first dir)
                                                     (second dir)))))))


(define/contract (on-collide f s py-code)
  (-> (or/c physical? layout?) (or/c physical? layout?) list? (or/c physical? layout?))
  (define collision-f (format-s "on_collide_~a_~a"
                                (id f)
                                (id s)))
  
  (add-after-compile f
                     (λ(me py-obj)
                       (py-begin (py-define (collision-f f s p)
                                            py-code)
                                 (py-if `(in ,(symbol->string (obj-name me))
                                             (vars))
                                        `(add-collision ,(obj-name s)
                                                        ,(obj-name me)
                                                        ,collision-f))))))

(define (hidden o)
  (add-after-compile o
                     (λ(me py-obj)
                       (py-begin
                        (py-if `(in ,(symbol->string (obj-name me))
                                    (vars))
                               `(deactivate ,(obj-name me)))))))

(define (spawn o)
  (define o.body.position (format-s "obj~a.body.position" (id o)))
  (if (layout? o)
      (apply do-many (map spawn (layout-children o)))
      (py-begin (py-set o.body.position 'p)
                `(reactivate ,(obj-name o)))))




(define (swap-to o)
  (define o.body.position (format-s "obj~a.body.position" (id o)))
  (if (layout? o)
      (apply do-many (map swap-to (layout-children o)))
      (py-begin
       `(try
         ,(py-set o.body.position
                  (py-tuple (py-add (py-dot 'p (py-list 0))
                                    (py-dot o.body.position (py-list 0))
                                    '(* -1 (/ w 2)))
                            (py-add (py-dot 'p (py-list 1))
                                    (py-dot o.body.position (py-list 1))
                                   '(* -1 (/ h 2)))))
         (except ,(py-list)
                 (print "Exception"))))))



(define/contract (on-click f py-code)
  (-> (or/c physical? layout?) list? (or/c physical? layout?))

  
  (add-after-compile f
                     (λ(me py-obj)
                       (define click-f (format-s "on_click_~a"
                                                 (id me)))
                       (define me.inside (format-s "obj~a.inside" (id me)))
                       (py-begin (py-define (,click-f keys)
                                            `(global ,(obj-name me))
                                            (py-set 'f (obj-name me))
                                            (py-set 'p 'f.body.position)
                                            (py-if (py-and '(mouse-clicked)
                                                           `(,me.inside (mouse-point)))
                                                   (py-begin
                                                    py-code
                                                    (py-return #t))))
                                 `(add-observer ,click-f)))))



(define (do-many . things)
  `(do ,@things))



(struct pymunk-obj (dynamic x y) #:transparent)
(define (pymunk-obj-name o)
  (format "obj~a" (id (pymunk-obj-dynamic o))))






;Should interpret the layout structure into
;  a list of colliders with absolute locations and appropriately bound images

(define/contract (pymunk-obj-list current (root-x 0) (root-y 0))
  (->* ((or/c physical? cosmetic? layout?))
       (integer? integer?)
       (listof pymunk-obj?))


  (cond [(not (layout? current)) (list (pymunk-obj current
                                               (+ root-x (x current))
                                               (+ root-y (y current))))]
        [(layout? current) (apply append
                             (map-with-i (λ(c i)
                                           (pymunk-obj-list c
                                                            (+ root-x (x current))
                                                            (+ root-y (y current))))
                                         (layout-children current)))]))





(define (obj->after-compiles x i)
  (define phys (pymunk-obj-dynamic x))

  (define after-compiles (if (cosmetic? phys)
                             (cosmetic-after-compile phys)
                             (physical-after-compile phys)))
  
  (map (λ(f) (f phys x)) after-compiles))


(define (obj->python x i)
  (define phys (pymunk-obj-dynamic x))

  (define w (width  (pymunk-obj-dynamic x)))
  (define h (height (pymunk-obj-dynamic x)))

  (define after-compiles (if (cosmetic? phys)
                             (cosmetic-after-compile phys)
                             (physical-after-compile phys)))

  (define collider (and
                    (not (is-cosmetic? phys))
                    (physical-collider phys)))

  
  (define collider-type (cond 
                          [(circle-collider? collider) "ball"]
                          [(box-collider? collider)    "box"]
                          [else "ball"]))

  
  (define fun-name (format-s
                    (cond [(is-cosmetic? phys) "cosmetic_~a"]
                          [(is-dynamic? phys) "~a"]
                          [(is-static? phys) "static_~a"])
                    collider-type))

  (define name
    (format-s (pymunk-obj-name x)))
  
  (define first-line
    (if (box-collider? collider)
        (py-set name
                `(,fun-name ,(py-list
                              `(int (- ,(pymunk-obj-x x) ,(half w)))
                              `(int (- ,(pymunk-obj-y x) ,(half h))))
                            ,w
                            ,h))
        (py-set name
                `(,fun-name ,(py-list
                              `(int ,(pymunk-obj-x x))
                              `(int ,(pymunk-obj-y x)))
                            ,(/ (max w h) 2)))))

  (define second-line
    (py-set (format-s "~a.color" name)
            '(Color "white")))

  (define third-line
    (py-set (format-s "~a.group" name)
            (id (pymunk-obj-dynamic x))))

  ;Should be able to write out the embedded image here.  It's inside the dynamic/cosmetic object...
  (define path
    (format "/Users/thoughtstem/Dev/Python/py-fizzery/~a" (format "~a.png"
                                                                  (pymunk-obj-name x))))

  (h:save-image (get-image phys) path)
  
  (define fourth-line
    (py-set (format-s "~a_image" name)
            `(pygame.image.load ,path)))

  (define fifth-line
    `(image-bindings.append ,(py-list name
                                      (format-s "~a_image" name))))

  (define sixth-line
    `(user_shapes.append ,name))

  (define construction-lines
    (py-begin first-line second-line third-line fourth-line fifth-line sixth-line))

  construction-lines)

(define (simulate thing)
  (define objs (reverse (pymunk-obj-list thing)))

  (define pre (preview thing))
  
  (compile (apply append-py*
                  (append (map-with-i obj->python objs)
                          (filter (not/c empty?)
                                  (map-with-i obj->after-compiles objs))))
           "demo.py"
           (h:image-width pre)
           (h:image-height pre)))

(define (preview2 thing)
  (define objs (pymunk-obj-list thing))

  (define pre (preview thing))
  
  (define bg (h:rectangle (h:image-width pre)
                          (h:image-height pre)
                          "solid"
                          "transparent"))

  (apply (make-safe h:overlay)
         (map (λ(i) (h:place-image
                     (get-image (pymunk-obj-dynamic i))
                     (pymunk-obj-x i)
                     (pymunk-obj-y i)
                     bg)) objs)))


(define circle    (compose make-cosmetic h:circle))
(define square    (compose make-cosmetic h:square))
(define rectangle (compose make-cosmetic h:rectangle))



(define (compile p file-name w h)
  (define final (boiler w h p))
  (displayln final)
  (with-output-to-file file-name #:exists 'replace
    (lambda () (printf final)))
  (system (string-append "PYTHONPATH=/Users/thoughtstem/Dev/Python/py-fizzery/pygame/pyphysicssandbox /usr/local/bin/python3 " file-name)))



(define imports
  (py-begin '(import math)
            '(import pymunk)
            '(import [hy-SQUARE pyphysicssandbox [hy-SQUARE *]])
            '(import pygame)
            '(import [hy-SQUARE pyphysicssandbox [hy-SQUARE Vec2d]])))



(define (setup-code w h)
  (py-begin (py-set 'w w)
        (py-set 'h h)
        (py-set 'user_shapes '[hy-SQUARE])
        (py-set 'image_bindings '[hy-SQUARE])
        (py-set 'pivots '[hy-SQUARE])
        (py-set 'connected_shapes '[hy-SQUARE])
        `(window "Most Awesome Thing Ever" ,w ,h)))


(define (boiler w h user-hy-codes)
  (define full-hy
    (append-py*
     imports
     (setup-code w h)

     ;User code
     user-hy-codes

     ;Python crap below

    
     (py-begin
      ;image-for
      (py-define (image-for s)
                 (py-global 'image-bindings)
                 (py-for-in (b 'image-bindings)
                            (py-if (py-eq (py-dot b (py-list 0))
                                          s)
                                   (py-return (py-dot b (py-list 1)))))
                 (py-return #f))

      ;draw-images
      (py-define (draw-images cosmetic)
                 (py-define (f keys)
                            (py-global 'user-shapes)
                            (py-for-in (s 'user-shapes)
                                       (py-if (py-not '(image-for s)) ;Have to literalize image-for, but would be cool if we could build up a better scoping...
                                              py-continue)          ;Pass in context?


                                       (py-if (py-not (py-eq cosmetic (py-dot s '_cosmetic)))
                                              py-continue)

                                       (py-if (py-not (py-dot s 'active))
                                              py-continue)


                                       (py-if (py-dot s 'body)
                                              (py-set 'p `(Vec2d ,(py-dot s 'body 'position 'x)
                                                                 ,(py-dot s 'body 'position 'y)))
                                              (py-set 'p `(Vec2d ,(py-dot s '_x)
                                                                 ,(py-dot s '_y))))


                                       (py-set 'angle 0)

                                       (py-if (py-dot s 'body)
                                              (py-set 'angle (py-dot s 'body 'angle)))


                                       (py-set 'angle_degrees `(math.degrees angle))


                                       (py-set 'rotated_logo_img `(pygame.transform.rotate (image-for s) (* -1 angle-degrees)))

                                       (py-set 'offset (py-div '(Vec2d (rotated_logo_img.get_size)) 2))

                                       (py-set 'p (py-sub 'p 'offset))

                                       (py-set 'screen '(pygame.display.get-surface))

                                       '(screen.blit rotated_logo_img p)))
                 (py-return 'f))

      ;draw-pivot-lines
      (py-define (draw_pivot_lines keys)
                 (py-global 'pivots)
                 (py-for-in (p 'pivots)
                            (py-set 'start (py-dot p 'body 'position))
                            (py-for-in (j (py-dot p 'shape))
                                       (py-set 'other (py-dot j 'a))
                                       (py-set 'end   (py-dot 'other 'position))
                                       (py-set 'screen '(pygame.display.get_surface))
                                       '(pygame.draw.line screen (Color "black") start end)
                          
                                       )
                            ))

      ;draw-connection-lines
      (py-define (draw_connection_lines keys)
                 (py-global 'pivots)
                 (py-for-in (c 'connected_shapes)
                            (py-set 'start (py-dot c (py-list 0) 'body 'position))
                            (py-set 'end   (py-dot c (py-list 1) 'body 'position))

                            (py-if (py-or (py-not (py-dot c (py-list 0) 'active))
                                          (py-not (py-dot c (py-list 0) 'active)))
                                   py-continue)

                            (py-set 'screen '(pygame.display.get_surface))
                            '(pygame.draw.line screen (Color "black") start end)
                            ))

    
      '(add-observer (draw-images #t))
      '(add-observer draw_pivot_lines)
      '(add-observer draw_connection_lines)
      '(add-observer (draw-images #f))
      '(run))))

  (pretty-print full-hy)
  
  (compile-py
   full-hy)
  )



