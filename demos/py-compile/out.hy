(import sys) (import math) (import pymunk) (import [pyphysicssandbox [*]]) (import pygame) (import [pyphysicssandbox [Vec2d]]) (setv w 520) (setv h 520) (setv user_shapes []) (setv image_bindings []) (setv friends []) (setv enemies []) (setv temp-shapes []) (setv pivots []) (setv connected_shapes []) (setv click-handled 2) (setv the-window (window "Most Awesome Thing Ever" w h)) (setv game-already-over False) (defn create-end-screen [won?] (do (do (global image-bindings) (global user-shapes) (setv end-screen-img (pygame.image.load (if won? "/Users/thoughtstem/Dev/Python/py-fizz/images/win-screen.png" "/Users/thoughtstem/Dev/Python/py-fizz/images/lose-screen.png"))) (setv end-screen (static_box (, (/ w 2) (/ h 2)) 0 0)) (image-bindings.append [end-screen end-screen-img]) (user-shapes.append end-screen) end-screen))) (defn make_obj24 [off-x off-y] (do (do (setv obj24 (static_box [(+ (int (- 260 260)) (int off-x)) (+ (int (- 515 5)) (int off-y))] 520 10)) (setv obj24.color (Color "white")) (setv obj24.group 24) (setv obj24_image (pygame.image.load "./py-fizz-images/obj24.png")) (image-bindings.append [obj24 obj24_image]) (user-shapes.append obj24) obj24))) (setv obj24 (make_obj24 0 0)) (defn make_obj26 [off-x off-y] (do (do (setv obj26 (static_box [(+ (int (- 515 5)) (int off-x)) (+ (int (- 260 250)) (int off-y))] 10 500)) (setv obj26.color (Color "white")) (setv obj26.group 26) (setv obj26_image (pygame.image.load "./py-fizz-images/obj26.png")) (image-bindings.append [obj26 obj26_image]) (user-shapes.append obj26) obj26))) (setv obj26 (make_obj26 0 0)) (defn make_obj22 [off-x off-y] (do (do (setv obj22 (cosmetic_ball [(+ (int 260) (int off-x)) (+ (int 260)) (int off-y)] 250)) (setv obj22.color (Color "white")) (setv obj22.group 22) (setv obj22_image (pygame.image.load "./py-fizz-images/obj22.png")) (image-bindings.append [obj22 obj22_image]) (user-shapes.append obj22) obj22))) (setv obj22 (make_obj22 0 0)) (defn make_obj17 [off-x off-y] (do (do (setv obj17 (box [(+ (int (- 260 101/2)) (int off-x)) (+ (int (- 260 25)) (int off-y))] 101 50)) (setv obj17.color (Color "white")) (setv obj17.group 17) (setv obj17_image (pygame.image.load "./py-fizz-images/obj17.png")) (image-bindings.append [obj17 obj17_image]) (user-shapes.append obj17) (do (defn on_click_17 [keys] (do (global click-handled) (setv f obj17) (if (or (not f) (not f.body)) (return False)) (setv p f.body.position) (if (and (mouse-clicked) (obj17.inside (mouse-point)) (. obj17 active) (= click-handled 0)) (do (do (defn make_obj4 [off-x off-y] (do (do (setv obj4 (box [(+ (int (- (+ p.x 65 -331/2) 41/2)) (int off-x)) (+ (int (- (+ p.y 41/2 -43) 41/2)) (int off-y))] 41 41)) (setv obj4.color (Color "white")) (setv obj4.group 4) (setv obj4_image (pygame.image.load "./py-fizz-images/obj4.png")) (image-bindings.append [obj4 obj4_image]) (user-shapes.append obj4) (do (obj4.hit [0 0] obj4.position)) (do (obj4.hit [-2010000 0] obj4.position)) obj4))) (setv obj4 (make_obj4 0 0)) (defn make_obj8 [off-x off-y] (do (do (setv obj8 (cosmetic_ball [(+ (int (+ p.x 65 -331/2)) (int off-x)) (+ (int (+ p.y 87/2 -43))) (int off-y)] 5/2)) (setv obj8.color (Color "white")) (setv obj8.group 8) (setv obj8_image (pygame.image.load "./py-fizz-images/obj8.png")) (image-bindings.append [obj8 obj8_image]) (user-shapes.append obj8) obj8))) (setv obj8 (make_obj8 0 0)) (defn make_obj5 [off-x off-y] (do (do (setv obj5 (ball [(+ (int (+ p.x 20 -331/2)) (int off-x)) (+ (int (+ p.y 66 -43))) (int off-y)] 20)) (setv obj5.color (Color "white")) (setv obj5.group 5) (setv obj5_image (pygame.image.load "./py-fizz-images/obj5.png")) (image-bindings.append [obj5 obj5_image]) (user-shapes.append obj5) (do (setv obj5.elasticity (* 1.0 0))) (do (motor obj5 1)) (do (obj5.hit [-2010000 0] obj5.position)) obj5))) (setv obj5 (make_obj5 0 0)) (defn make_obj9 [off-x off-y] (do (do (setv obj9 (cosmetic_ball [(+ (int (+ p.x 85/2 -331/2)) (int off-x)) (+ (int (+ p.y 66 -43))) (int off-y)] 5/2)) (setv obj9.color (Color "white")) (setv obj9.group 9) (setv obj9_image (pygame.image.load "./py-fizz-images/obj9.png")) (image-bindings.append [obj9 obj9_image]) (user-shapes.append obj9) obj9))) (setv obj9 (make_obj9 0 0)) (defn make_obj6 [off-x off-y] (do (do (setv obj6 (ball [(+ (int (+ p.x 65 -331/2)) (int off-x)) (+ (int (+ p.y 66 -43))) (int off-y)] 20)) (setv obj6.color (Color "white")) (setv obj6.group 6) (setv obj6_image (pygame.image.load "./py-fizz-images/obj6.png")) (image-bindings.append [obj6 obj6_image]) (user-shapes.append obj6) (do (setv obj6.elasticity (* 1.0 0))) (do (motor obj6 1)) (do (obj6.hit [-2010000 0] obj6.position)) obj6))) (setv obj6 (make_obj6 0 0)) (defn make_obj10 [off-x off-y] (do (do (setv obj10 (cosmetic_ball [(+ (int (+ p.x 175/2 -331/2)) (int off-x)) (+ (int (+ p.y 66 -43))) (int off-y)] 5/2)) (setv obj10.color (Color "white")) (setv obj10.group 10) (setv obj10_image (pygame.image.load "./py-fizz-images/obj10.png")) (image-bindings.append [obj10 obj10_image]) (user-shapes.append obj10) obj10))) (setv obj10 (make_obj10 0 0)) (defn make_obj7 [off-x off-y] (do (do (setv obj7 (ball [(+ (int (+ p.x 110 -331/2)) (int off-x)) (+ (int (+ p.y 66 -43))) (int off-y)] 20)) (setv obj7.color (Color "white")) (setv obj7.group 7) (setv obj7_image (pygame.image.load "./py-fizz-images/obj7.png")) (image-bindings.append [obj7 obj7_image]) (user-shapes.append obj7) (do (setv obj7.elasticity (* 1.0 0))) (do (motor obj7 1)) (do (obj7.hit [-2010000 0] obj7.position)) obj7))) (setv obj7 (make_obj7 0 0)) (defn make_obj19 [off-x off-y] (do (do (setv obj19 (cosmetic_ball [(+ (int (+ p.x 461/2 -331/2)) (int off-x)) (+ (int (+ p.y 43 -43))) (int off-y)] 201/2)) (setv obj19.color (Color "white")) (setv obj19.group 19) (setv obj19_image (pygame.image.load "./py-fizz-images/obj19.png")) (image-bindings.append [obj19 obj19_image]) (user-shapes.append obj19) obj19))) (setv obj19 (make_obj19 0 0)) (do (setv p (pin obj5.body.position obj5 obj6.body.position obj6)) (connected_shapes.append [obj5 obj6 p])) (do (setv p (pin obj5.body.position obj5 obj4.body.position obj4)) (connected_shapes.append [obj5 obj4 p])) (do (setv p (pin obj6.body.position obj6 obj7.body.position obj7)) (connected_shapes.append [obj6 obj7 p])) (do (setv p (pin obj6.body.position obj6 obj4.body.position obj4)) (connected_shapes.append [obj6 obj4 p])) (do (setv p (pin obj7.body.position obj7 obj4.body.position obj4)) (connected_shapes.append [obj7 obj4 p]))) (setv click-handled 2) (return True))))) (add-observer on_click_17)) obj17))) (setv obj17 (make_obj17 0 0)) (defn make_obj26 [off-x off-y] (do (do (setv obj26 (static_box [(+ (int (- 5 5)) (int off-x)) (+ (int (- 260 250)) (int off-y))] 10 500)) (setv obj26.color (Color "white")) (setv obj26.group 26) (setv obj26_image (pygame.image.load "./py-fizz-images/obj26.png")) (image-bindings.append [obj26 obj26_image]) (user-shapes.append obj26) obj26))) (setv obj26 (make_obj26 0 0)) (defn make_obj24 [off-x off-y] (do (do (setv obj24 (static_box [(+ (int (- 260 260)) (int off-x)) (+ (int (- 5 5)) (int off-y))] 520 10)) (setv obj24.color (Color "white")) (setv obj24.group 24) (setv obj24_image (pygame.image.load "./py-fizz-images/obj24.png")) (image-bindings.append [obj24 obj24_image]) (user-shapes.append obj24) obj24))) (setv obj24 (make_obj24 0 0)) (defn image-for [s] (do (global image-bindings) (for (b image-bindings) (if (= (. b [0]) s) (return (. b [1])))) (return False))) (defn draw-images [cosmetic] (do (defn f [keys] (do (global user-shapes) (for (s user-shapes) (if (not (image-for s)) (continue)) (if (not (= cosmetic (. s _cosmetic))) (continue)) (if (not (. s active)) (continue)) (if (. s body) (setv p (Vec2d (. s body position x) (. s body position y))) (setv p (Vec2d (. s _x) (. s _y)))) (setv angle 0) (if (. s body) (setv angle (. s body angle))) (setv angle_degrees (math.degrees angle)) (setv rotated_logo_img (pygame.transform.rotate (image-for s) (* -1 angle-degrees))) (setv offset (/ (Vec2d (rotated_logo_img.get_size)) 2)) (setv p (- p offset)) (setv screen (pygame.display.get-surface)) (screen.blit rotated_logo_img p)))) (return f))) (defn draw_pivot_lines [keys] (do (global pivots) (for (p pivots) (setv start (. p body position)) (for (j (. p shape)) (if (not p.active) (continue)) (setv other (. j a)) (setv end (. other position)) (setv screen (pygame.display.get_surface)) (pygame.draw.line screen (Color "black") start end))))) (defn draw_connection_lines [keys] (do (for (c connected_shapes) (setv start (. c [0] body position)) (setv end (. c [1] body position)) (if (or (not (. c [0] active)) (not (. c [1] active))) (do (deactivate (. c [2])) (continue))) (setv screen (pygame.display.get_surface)) (pygame.draw.line screen (Color "black") start end)))) (defn clear-click [keys] (do (do (global click-handled) (setv click-handled (max 0 (- click-handled 1)))))) (defn game-over [won?] (do (do (global game-already-over) (print "Game over!") (for (f user-shapes) (setv f.damping 0.01)) (setv game-already-over True) (setv end-screen (create-end-screen won?))))) (defn check-friends-and-enemies [keys] (do (do (global friends) (for (f friends) (if (and (not f.active) (not game-already-over)) (game-over False))) (if (= 0 (len enemies)) (return True)) (for (f enemies) (if (or f.active game-already-over) (return True))) (game-over True)))) (defn tick-temp-shapes [keys] (do (do (global temp-shapes) (setv new-temp-shapes []) (for (f temp-shapes) (setv shape (. f [0])) (setv time-left (. f [1])) (setv new-time-left (- time-left 1)) (setv (. f [1]) new-time-left) (if (< time-left 0) (deactivate shape) (new-temp-shapes.append [shape new-time-left]))) (setv temp-shapes new-temp-shapes)))) (defn take-final-screenshot [keys] (do (if game-already-over (take-screenshot)))) (defn take-screenshot [] (do (setv screen (pygame.display.get-surface)) (pygame.image.save screen "screenshot.jpg"))) (add-observer tick-temp-shapes) (add-observer clear-click) (add-observer (draw-images True)) (add-observer draw_pivot_lines) (add-observer draw_connection_lines) (add-observer (draw-images False)) (add-observer check-friends-and-enemies) (add-observer take-final-screenshot) (run)