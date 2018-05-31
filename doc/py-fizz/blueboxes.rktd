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
