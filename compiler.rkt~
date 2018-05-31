#lang racket

(require (prefix-in h: 2htdp/image))
(require racket-to-python/python-module
         setup/dirs)

(provide compile
         
         shape->list
         make-static
         make-dynamic
         make-cosmetic
         make-pivot
         connect-pivot
         motorize
         pin
         gear
         gravity
         elasticity
         angle
         friction
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
         layout?


         on-collide
         on-click
         id

         hidden

         ;Callbacks for collisions...
         do-many
         spawn

         shape-map

         preview
         preview2
         simulate

         toggle-static
         set-package-path!

         must-survive
         must-die)


(define (default-package-path)
  (string-append
   (path->string (find-user-pkgs-dir))
   "/py-fizz/"))

(define package-path   (default-package-path))

(define (set-package-path! s)   (set! package-path s))


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


(struct layout   (id x y w h name preview-f children)                #:transparent)
(struct physical (id x y after-construct relational-after-construct collider image dynamic?)      #:transparent)
(struct cosmetic (id x y after-construct relational-after-construct image)                        #:transparent)
  
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

(define/contract (add-after-construct thing f)
  (-> (or/c physical? cosmetic? layout?) any/c (or/c physical? cosmetic? layout?))
  (cond [(layout? thing)  (struct-copy layout
                                       thing
                                       [children (map (curryr add-after-construct f) (layout-children thing))])]
        [(physical? thing)  (struct-copy physical
                                         thing
                                         [after-construct (append (physical-after-construct thing) (list f))])]
        [(cosmetic? thing)  (struct-copy cosmetic
                                         thing
                                         [after-construct (append (cosmetic-after-construct thing) (list f))])]))

(define/contract (add-relational-after-construct thing f)
  (-> (or/c physical? cosmetic? layout?) any/c (or/c physical? cosmetic? layout?))
  (cond [(layout? thing)  (struct-copy layout
                                       thing
                                       [children (map (curryr add-relational-after-construct f) (layout-children thing))])]
        [(physical? thing)  (struct-copy physical
                                         thing
                                         [relational-after-construct (append (physical-relational-after-construct thing) (list f))])]
        [(cosmetic? thing)  (struct-copy cosmetic
                                         thing
                                         [relational-after-construct (append (cosmetic-relational-after-construct thing) (list f))])]))



(struct collider ())
(struct circle-collider collider (r))
(struct box-collider collider (w h))



(define current-id 0)
(define (next-id)
  (set! current-id (add1 current-id))
  current-id)

(define/contract (id thing)
  (-> (or/c cosmetic? physical? layout?) number?)
  (cond [(layout? thing)    (layout-id thing)]
        [(physical? thing)  (physical-id thing)]
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

(define/contract (toggle-static i)
  (-> physical? physical?)
  (struct-copy physical i
               [dynamic? (not (physical-dynamic? i))]))

(define/contract (make-dynamic i
                               #:collider (type circle-collider)
                               #:mass (mass 10)
                               )
  (->* ((or/c h:image? cosmetic? layout? physical?)) (#:collider any/c #:mass number?) physical?)

  (define img (preview i))
  (define obj
    (physical (next-id)
              (half-width img) (half-height img)
              '()
              '()
              (collider-for img type)
              img
              #t))

  (add-after-construct obj
                     (λ(me py-obj)
                       (py-begin
                        (py-set `(hy-DOT ,(obj-name me) mass) mass)))))

(define/contract (make-static i #:collider (type circle-collider))
  (->* ((or/c h:image? cosmetic? layout? physical?)) (#:collider any/c) physical?)
  (define img (preview i))
  (if (physical? i)
      (struct-copy physical i
                   [dynamic? #f])
      (physical (next-id) 
                (half-width img) (half-height img)
                '()
                '() 
                (collider-for img type)
                img
                #f)))

(define/contract (make-cosmetic i)
  (-> (or/c h:image? cosmetic? layout?) cosmetic?)
  (define img (preview i))
  (cosmetic (next-id)
            (half-width img) (half-height img)
            '()
            '() 
            img))

(define/contract (make-pivot i)
  (-> (or/c h:image? cosmetic?) cosmetic?)
  (define base (make-cosmetic i))
  (add-after-construct base
                     (λ(me py-obj)
                       (define piv-name (format-s "pivot~a" (id me)))
                      (py-begin
                       `(global ,piv-name)
                        (py-set piv-name
                               `(pivot ,(py-tuple (pymunk-obj-x py-obj) (pymunk-obj-y py-obj))))
                       `(pivots.append ,piv-name)))))


(define/contract (connect-pivot p other)
  (-> cosmetic? physical? cosmetic?)
  (add-relational-after-construct p
                                  (λ(me py-obj)
                                    (define piv-connect (format-s "pivot~a.connect" (id me)))
                                    (py-begin `(,piv-connect ,(obj-name other))))))



(define/contract (gear f s)
  (-> physical? physical? physical?)
  (add-relational-after-construct f
                                  (λ(me py-obj)
                                    (py-begin
                                     `(gear ,(obj-name f) ,(obj-name s))))))


(define/contract (pin f s)
  (-> physical? physical? physical?)
  (add-relational-after-construct f
                     (λ(me py-obj)
                       (define f.body.position (format-s "obj~a.body.position" (id f)))
                       (define s.body.position (format-s "obj~a.body.position" (id s)))
                       (py-begin (py-set 'p
                                         `(pin ,f.body.position ,(obj-name f) ,s.body.position ,(obj-name s)))
                                 `(connected_shapes.append ,(py-list (obj-name f)
                                                                     (obj-name s)
                                                                     'p))))))


(define/contract (initial-velocity dir p)
  (-> (listof number?) physical? physical?)
  (add-after-construct p
                     (λ(me py-obj)
                       (define me.hit      (format-s "obj~a.hit" (id me)))
                       (define me.position (format-s "obj~a.position" (id me)))
                       (py-begin
                        #;'(print "YO DOG")
                        `(,me.hit ,(py-list (first dir) (second dir))
                                  ,me.position)))))



(define/contract (motorize speed p)
  (-> number? physical? physical?)
  (add-after-construct p
                     (λ(me py-obj)
                       (py-begin
                        `(motor ,(obj-name me) ,speed)))))


;I don't love that dist is a param.  Better to set based on initial object positions
(define/contract (spring f s dist) 
  (-> physical? physical? number? physical?)
  (add-relational-after-construct f
                                  (λ(me py-obj)
                                    (define f.body.position (py-dot (obj-name f) 'body 'position))
                                    (define s.body.position (py-dot (obj-name s) 'body 'position))
                                    (py-begin (py-set 'p
                                                      `(spring ,f.body.position ,(obj-name f) ,s.body.position ,(obj-name s) ,dist 20000 1000))
                                              `(connected-shapes.append ,(py-list (obj-name f)
                                                                                  (obj-name s)
                                                                                  'p))))))

(define/contract (angle-spring f s
                               (angle 0)
                               (stiffness 0)
                               (damping 0)
                               ) 
  (->* (physical? physical?) (number? number? number?) physical?)
  (add-relational-after-construct f
                                  (λ(me py-obj)
                                    (py-begin
                                     `(rotary_spring ,(obj-name f)
                                                     ,(obj-name s)
                                                     ,angle
                                                     ,stiffness
                                                     ,damping)))))


(define/contract (gravity dir p)
  (-> (list/c number? number?) physical? physical?)
  (add-after-construct p
                     (λ(me py-obj)
                       (define me.gravity (format-s "obj~a.gravity" (id me)))
                       
                       (py-begin
                        (py-set me.gravity (py-tuple (first dir)
                                                     (second dir)))))))

(define/contract (elasticity e p)
  (-> number? physical? physical?)
  (add-after-construct p
                       (λ(me py-obj)
                         (define me.elasticity (format-s "obj~a.elasticity" (id me)))
                       
                         (py-begin
                          (py-set me.elasticity `(* 1.0 ,e))))))

(define/contract (angle e p)
  (-> number? physical? physical?)
  (add-after-construct p
                       (λ(me py-obj)
                         (define me.angle (format-s "obj~a.angle" (id me)))
                       
                         (py-begin
                          (py-set me.angle `(* 1.0 ,e))))))


(define/contract (friction e p)
  (-> number? physical? physical?)
  (add-after-construct p
                       (λ(me py-obj)
                         (define me.friction (format-s "obj~a.friction" (id me)))
                       
                         (py-begin
                          (py-set me.friction `(* 1.0 ,e))))))


(define/contract (must-survive p)
  (-> physical? physical?)
  (add-after-construct p
                       (λ(me py-obj)
                         (py-begin
                          `(friends.append ,(obj-name me))))))

(define/contract (must-die p)
  (-> physical? physical?)
  (add-after-construct p
                       (λ(me py-obj)
                         (py-begin
                          `(enemies.append ,(obj-name me))))))


(define (hidden o)
  (add-after-construct o
                     (λ(me py-obj)
                       (py-begin
                        (py-if `(in ,(symbol->string (obj-name me))
                                    (vars))
                               `(deactivate ,(obj-name me)))))))



(define (spawn o (destroy-self #t))
  (define o.body.position (format-s "obj~a.body.position" (id o)))
  
  (define (helper p-obj)
    (define phys (pymunk-obj-dynamic p-obj))
    (append-call (obj->python-fun (pymunk-obj phys
                                               `(+ p.x
                                                   ,(pymunk-obj-x p-obj)
                                                   ,(- (half-width o)))
                                               `(+ p.y
                                                   ,(pymunk-obj-y p-obj)
                                                   ,(- (half-height o)))))))

  (define cs (pymunk-obj-list o))

  (define insert (apply append-py* (map helper cs)))

  (define actual-insert
    (if (= 1 (length cs))
                 (list (first insert))
                 insert))

  (define afters (apply append-py*
                        (map obj->relational-after-constructs cs)))

  (if destroy-self
      `(do ,@actual-insert (deactivate f) ,@afters)
      `(do ,@actual-insert ,@afters)))



(define/contract (on-collide f py-code
                             #:friction    (friction-thresh 0)
                             #:energy-loss (energy-loss-thresh 0))
  (->* ((or/c physical? layout?) list?)
       (#:friction number?
        #:energy-loss number?)
       (or/c physical? layout?))
  (define collision-f (format-s "on_collide_~a"
                                (id f)))

  (define f.collision-type (format-s "obj~a.collision_type"
                                     (id f)))
  
  (add-after-construct f
                     (λ(me py-obj)
                       (py-begin (py-define (,collision-f arbiter space data)
                                            ;`(print (+ "F: " (string ,(py-dot 'arbiter 'shapes (py-list 0) 'collision_type))))
                                            ;`(print (+ "S: " (string ,(py-dot 'arbiter 'shapes (py-list 1) 'collision_type))))

                                            (py-set 'f (obj-name f))
                                            (py-set 'p 'f.body.position)

                                            (py-set 'friction    (py-dot 'arbiter 'friction))
                                            (py-set 'restitution (py-dot 'arbiter 'restitution))

                                            (py-set 'total_impulse (py-dot 'arbiter 'total_impulse))

                                            (py-set 'energy_loss (py-dot 'arbiter 'total_ke))

                                            #;`(print (+ ;"Friction    " (string friction) "\n"
                                                       ;"Restitution " (string restitution) "\n"
                                                       ;"Impulse     " (string total_impulse) "\n"
                                                       "Energy loss " (string energy_loss)))

                                           
                                            
                                            (py-if (py-and
                                                    (py-gt 'friction    friction-thresh)
                                                    (py-gt 'energy-loss energy-loss-thresh))
                                                   py-code)
                                            )
                                 (py-set 'space
                                         (py-dot (obj-name f) 'body 'space))

                                 (py-set 'ch `(space.add-wildcard-collision-handler ,f.collision-type))

                                 (py-set 'ch.post_solve collision-f)
                                 ))))

(define/contract (on-click f py-code)
  (-> (or/c physical? layout?) list? (or/c physical? layout?))

  
  (add-after-construct f
                     (λ(me py-obj)
                       (define click-f (format-s "on_click_~a"
                                                 (id me)))
                       (define me.inside (format-s "obj~a.inside" (id me)))
                       (py-begin (py-define (,click-f keys)
                                           ; `(global ,(obj-name me))
                                            `(global click-handled)
                                            (py-set 'f (obj-name me))
                                            (py-if (py-or (py-not 'f)
                                                          (py-not 'f.body))
                                                   (py-return #f))
                                            (py-set 'p 'f.body.position)
                                            (py-if (py-and '(mouse-clicked)
                                                           `(,me.inside (mouse-point))
                                                           (py-dot (obj-name me) 'active)
                                                           (py-eq 'click-handled 0))
                                                   (py-begin
                                                    py-code
                                                    (py-set 'click-handled 2)
                                                    (py-return #t))))
                                 `(add-observer ,click-f)))))



(define (do-many . things)
  `(do ,@things))



(struct pymunk-obj (dynamic x y) #:transparent)
(define (pymunk-obj-name o)
  (format "obj~a" (id (pymunk-obj-dynamic o))))



(define (shape-map f obj)
  (cond [(cosmetic? obj) obj]
        [(not (layout? obj)) (f obj)]
        [(layout? obj) (struct-copy layout
                                    obj
                                    [children (map (curry shape-map f) (layout-children obj))])]))



(define (shape->list obj)
  (map pymunk-obj-dynamic (pymunk-obj-list obj)))


(define/contract (pymunk-obj-list current
                                  (root-x 0)
                                  (root-y 0))
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





(define (obj->after-constructs x)
  (define phys (pymunk-obj-dynamic x))

  (define after-constructs (if (cosmetic? phys)
                             (cosmetic-after-construct phys)
                             (physical-after-construct phys)))
  
  (map (λ(f) (f phys x)) after-constructs))


(define (obj->relational-after-constructs x)
  (define phys (pymunk-obj-dynamic x))

  (define after-constructs (if (cosmetic? phys)
                             (cosmetic-relational-after-construct phys)
                             (physical-relational-after-construct phys)))
  
  (map (λ(f) (f phys x)) after-constructs))



(define (obj->python x)
  (define phys (pymunk-obj-dynamic x))

  (define w (width  (pymunk-obj-dynamic x)))
  (define h (height (pymunk-obj-dynamic x)))

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
                               (py-add
                                `(int (- ,(pymunk-obj-x x) ,(half w)))
                                '(int off-x))
                               (py-add
                                `(int (- ,(pymunk-obj-y x) ,(half h)))
                                '(int off-y))
                               )
                            ,w
                            ,h))
        (py-set name
                `(,fun-name ,(py-list
                              (py-add
                               `(int ,(pymunk-obj-x x))
                               '(int off-x))
                              (py-add
                               `(int ,(pymunk-obj-y x)))
                              '(int off-y))
                            ,(/ (max w h) 2)))))

  (define second-line
    (py-set (format-s "~a.color" name)
            '(Color "white")))

  (define third-line
    (py-set (format-s "~a.group" name)
            (id (pymunk-obj-dynamic x))))

  
  (make-directory* "./py-fizz-images")
  (define path
    (format "./py-fizz-images/~a" (format "~a.png"
                                          (pymunk-obj-name x))))

  (h:save-image (get-image phys) path)
  
  (define fourth-line
    (py-set (format-s "~a_image" name)
            `(pygame.image.load ,path)))

  (define fifth-line
    `(image-bindings.append ,(py-list name
                                      (format-s "~a_image" name))))

  (define sixth-line
    `(user-shapes.append ,name))

  (define return-line
    name)

  (define construction-lines
    (list first-line second-line third-line fourth-line fifth-line sixth-line))

  (define afters (obj->after-constructs x))

  `(do ,@(append construction-lines afters (list return-line))))

(define (obj->python-fun x)
  (define inner (obj->python x))

  (define phys (pymunk-obj-dynamic x))
  
  (define f-name (format-s "make_obj~a" (id phys)))

  (py-define (,f-name off-x off-y #;debug)
             #;`(if debug (print (+ "Making "
                                    ,(~a f-name)
                                    "\n"
                                    ,(~a phys))))
             inner))


(define (append-call f-def)
  (define f-name (second f-def))

  (define obj-name (string->symbol (regexp-replace #rx"make_" (symbol->string f-name) "")))
  
  (py-begin
     f-def
     (py-set obj-name `(,f-name 0 0 #;#f))))

(define (simulate thing)
  (define objs (reverse (pymunk-obj-list thing)))

  (define pre (preview thing))


  
  
  (compile (apply append-py*
                  (append (map append-call (map obj->python-fun objs))
                          (filter (not/c empty?)
                                  (map obj->relational-after-constructs objs))))
           "py-fizz.py"
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
  ;(displayln final)
  (with-output-to-file file-name #:exists 'replace
    (lambda () (printf final)))
  (system (string-append "PYTHONPATH=" package-path "/pygame/pyphysicssandbox PATH=$PATH:/usr/local/bin/ python3 " file-name)))



(define imports
  (py-begin '(import sys)
            '(import math)
            '(import pymunk)
            '(import [hy-SQUARE pyphysicssandbox [hy-SQUARE *]])
            '(import pygame)
            '(import [hy-SQUARE pyphysicssandbox [hy-SQUARE Vec2d]])))



(define (setup-code w h)
  (py-begin (py-set 'w w)

      
            (py-set 'h h)
            (py-set 'user_shapes '[hy-SQUARE])
            (py-set 'image_bindings '[hy-SQUARE])
            (py-set 'friends '[hy-SQUARE])
            (py-set 'enemies '[hy-SQUARE])
            (py-set 'pivots '[hy-SQUARE])
            (py-set 'connected_shapes '[hy-SQUARE])
            (py-set 'click-handled 2)
        
            (py-set 'the-window `(window "Most Awesome Thing Ever" w h))
            (py-set 'game-already-over #f)

                    
            (py-define (create-end-screen won?)
                       (py-begin
                        '(global image-bindings)
                        '(global user-shapes)
                        (py-set 'end-screen-img
                                `(pygame.image.load
                                   (if won?
                                       ,(string-append package-path
                                                  "/images/win-screen.png")
                                       ,(string-append package-path
                                                  "/images/lose-screen.png")))) ;Make this
                  
                        (py-set 'end-screen `(static_box ,(py-tuple `(/ w 2)
                                                                    `(/ h 2)) 0 0))
                  
                        `(image-bindings.append ,(py-list 'end-screen
                                                          'end-screen-img))

                        `(user-shapes.append end-screen)
                        'end-screen))

            ))


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
                                       (py-if (py-not 'p.active)
                                              py-continue)
                                       (py-set 'other (py-dot j 'a))
                                       (py-set 'end   (py-dot 'other 'position))
                                       (py-set 'screen '(pygame.display.get_surface))
                                       '(pygame.draw.line screen (Color "black") start end)
                          
                                       )
                            ))

      ;draw-connection-lines
      (py-define (draw_connection_lines keys)
                 (py-for-in (c 'connected_shapes)
                            (py-set 'start (py-dot c (py-list 0) 'body 'position))
                            (py-set 'end   (py-dot c (py-list 1) 'body 'position))

                            (py-if (py-or (py-not (py-dot c (py-list 0) 'active))
                                          (py-not (py-dot c (py-list 1) 'active)))
                                   (py-begin
                                     `(deactivate ,(py-dot c (py-list 2)))
                                     py-continue))

                            (py-set 'screen '(pygame.display.get_surface))
                            '(pygame.draw.line screen (Color "black") start end)
                            ))
      
      ;Just for testing
      #;(py-define (test-ball keys)
                 (py-if '(in constants.K_b keys)
                        (py-begin
                          (obj->python (pymunk-obj (make-dynamic (circle 10 "solid" "red")) 300 300)))))

      ;For testing...
     ; '(add-observer test-ball)

      (py-define (clear-click keys)
                 (py-begin
                  `(global click-handled)
                  (py-set 'click-handled '(max 0 (- click-handled 1)))))


      (py-define (game-over won?)
                 (py-begin
                  `(global game-already-over)
                  `(print "Game over!")
                  
                  (py-for-in (f 'user-shapes)
                             (py-set 'f.damping 0.01))

                  (py-set 'game-already-over #t)

                  (py-set 'end-screen `(create-end-screen won?))))


      (py-define (check-friends-and-enemies keys)
                 (py-begin
                  `(global friends)
                  (py-for-in (f 'friends)
                             (py-if (py-and (py-not 'f.active) (py-not 'game-already-over))
                                    `(game-over #f)))

                  (py-if `(= 0 (len enemies))
                         `(return #t))
                  
                  (py-for-in (f 'enemies)
                             (py-if (py-or 'f.active 'game-already-over)
                                    `(return #t)))

                  `(game-over #t)))



      '(add-observer check-friends-and-enemies)
      '(add-observer clear-click)
      '(add-observer (draw-images #t))
      '(add-observer draw_pivot_lines)
      '(add-observer draw_connection_lines)
      '(add-observer (draw-images #f))


      
      '(run))))

 ; (pretty-print full-hy)
  
  (compile-py
   full-hy)
  )



