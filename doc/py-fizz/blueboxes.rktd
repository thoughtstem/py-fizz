33
((3) 0 () 0 () () (h ! (equal)))
procedure
(wooden-level object) -> composite?
  object : (or/c static? dynamic? cosmetic? composite?)
procedure
(bowling-ball) -> dynamic?
procedure
(crate) -> dynamic?
procedure
(wheel) -> dynamic?
procedure
(balloon) -> dynamic?
procedure
(breakable-balloon) -> dynamic?
procedure
(friend) -> dynamic?
procedure
(enemy) -> dynamic?
procedure
(motor color speed) -> dynamic?
  color : string?
  speed : number?
procedure
(pinned-motor color speed) -> dynamic?
  color : string?
  speed : number?
procedure
(catpult object) -> composite?
  object : (or/c static? dynamic? cosmetic? composite?)
procedure
(car [speed object] join-object) -> composite?
  speed : number? = 1
  object : (or/c static? dynamic? composite?) = (crate)
  join-object : (or/c static? dynamic? composite?)
procedure
(pipe width height) -> dynamic?
  width : number?
  height : number?
procedure
(balloons-pulling num object [string-length]) -> composite?
  num : number?
  object : (or/c dynamic? static?)
  string-length : number? = 100
procedure
(conveyor-belt num [speed]) -> composite?
  num : number?
  speed : number? = 10
procedure
(v-space num) -> cosmetic?
  num : number?
procedure
(h-space num) -> cosmetic?
  num : number?
procedure
(fragments  object              
            resolution          
           [energy              
            destroy-after]) -> composite?
  object : (or/c dynamic? static? cosmetic? composite?)
  resolution : number?
  energy : number? = 100000
  destroy-after : number? = 50
procedure
(fragments object [energy angle]) -> static?
  object : (or/c dynamic? static? cosmetic? composite?)
  energy : number? = 10000
  angle : number? = 0
procedure
(builder object [destroy-self?]) -> static?
  object : (or/c dynamic? static? cosmetic? composite?)
  destroy-self? : boolean? = #t
procedure
(preview object) -> image?
  object : (or/c dynamic? static? cosmetic? composite?)
procedure
(simulate object) -> void?
  object : (or/c dynamic? static? cosmetic? composite?)
procedure
(make-static object [#:collider collider]) -> static?
  object : (or/c h:image? cosmetic? layout? physical?)
  collider : collider? = circle-collider
procedure
(make-dynamic object [#:collider collider]) -> dynamic?
  object : (or/c h:image? cosmetic? layout? physical?)
  collider : collider? = circle-collider
procedure
(make-cosmetic object) -> cosmetic?
  object : (or/c h:image? cosmetic? layout?)
procedure
(make-pivot object) -> pivot?
  object : (or/c h:image? cosmetic?)
procedure
(circle radius fill-mode color) -> cosmetic?
  radius : number?
  fill-mode : mode?
  color : color?
procedure
(rectangle width height fill-mode color) -> cosmetic?
  width : number?
  height : number?
  fill-mode : mode?
  color : color?
procedure
(square size fill-mode color) -> cosmetic?
  size : number?
  fill-mode : mode?
  color : color?
procedure
(motorize speed object) -> dynamic?
  speed : number?
  object : dynamic?
procedure
(gravity direction object) -> dynamic?
  direction : (list/c number? number?)
  object : dynamic?
procedure
(elasticity amount object) -> dynamic?
  amount : number?
  object : dynamic?
procedure
(angle amount object) -> dynamic?
  amount : number?
  object : (or/c dynamic? static?)
procedure
(friction object [energy angle]) -> static?
  object : (or/c dynamic? static?)
  energy : number? = 10000
  angle : number? = 0
procedure
(ttl time object) -> dynamic?
  time : number?
  object : (or/c dynamic? static? cosmetic?)
procedure
(mass amount object) -> dynamic?
  amount : number?
  object : dynamic?
procedure
(initial-velocity direction object) -> dynamic?
  direction : (list/c number? number?)
  object : dynamic?
procedure
(toggle-static object) -> (or/c dynamic? static?)
  object : (or/c dynamic? static?)
procedure
(width object) -> number?
  object : (or/c dynamic? static? cosmetic? composite?)
procedure
(height object) -> number?
  object : (or/c dynamic? static? cosmetic? composite?)
procedure
(above object ...) -> composite?
  object : (or/c dynamic? static? cosmetic? composite?)
procedure
(beside object ...) -> composite?
  object : (or/c dynamic? static? cosmetic? composite?)
procedure
(overlay object ...) -> composite?
  object : (or/c dynamic? static? cosmetic? composite?)
procedure
(gear object1 object2) -> dynamic?
  object1 : dynamic?
  object2 : dynamic?
procedure
(connect-pivot pivot object) -> pivot?
  pivot : pivot?
  object : (or/c dynamic? static?)
procedure
(pin object1 object2) -> dynamic?
  object1 : (or/c dynamic? static?)
  object2 : (or/c dynamic? static?)
procedure
(spring object1 object2 distance) -> dynamic?
  object1 : (or/c dynamic? static?)
  object2 : (or/c dynamic? static?)
  distance : number?
procedure
(angle-spring  object1       
               object2       
              [angle         
               stiffness     
               damping]) -> dynamic?
  object1 : (or/c dynamic? static?)
  object2 : (or/c dynamic? static?)
  angle : number? = 0
  stiffness : number? = 0
  damping : number? = 0
procedure
(on-collide object                            
            callback                          
            #:friction friction-thresh        
            #:energy-loss energy-loss-thresh) 
 -> (or/c dynamic? static? cosmetic? composite?)
  object : (or/c dynamic? static? cosmetic? composite?)
  callback : callback?
  friction-thresh : 0
  energy-loss-thresh : 0
procedure
(on-click object callback)
 -> (or/c dynamic? static? cosmetic? composite?)
  object : (or/c dynamic? static? cosmetic? composite?)
  callback : callback?
procedure
(spawn object [destroy-self?]) -> callback?
  object : (or/c dynamic? static? cosmetic? composite?)
  destroy-self? : boolean? = #f
procedure
(must-survive object) -> (or/c dynamic? static?)
  object : (or/c dynamic? static?)
procedure
(must-die object) -> (or/c dynamic? static?)
  object : (or/c dynamic? static?)
procedure
(set-package-path! path) -> void?
  path : string?
