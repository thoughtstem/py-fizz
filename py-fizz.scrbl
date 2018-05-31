#lang scribble/manual

@require[py-fizz]

@title{py-fizz}

Fun with fizzics!

@image[#:scale 1]{./doc-images/BalloonCannon2.gif}

Py-fizz is a language for creating physics simulations and games.
Compiles to Python and runs in the context of Pygame and Pymunk.
But Racket is the compile-time language, and provides a purely functional
API for doing awesome physics stuff.

Py-fizz is divided into two languages.
The first is a higher-level one, used for creating levels and simulations out of pre-built
gadgets: e.g. Bowling balls, balloons, motors, etc.  Eg.:

@racketblock[(simulate 
                (wooden-level
                  (bowling-ball)))]

@preview[(wooden-level
          (bowling-ball))]

There is also a lower-level language for defining your own such gadgets. For example, the bowling-ball gadget might be defined as:

@racketblock[
(define (bowling-ball)
  (mass 100000
        (make-dynamic (h:bitmap "./imgs/bowling-ball.png"))))
]

These docs describe both the high and low level languages.

@section{Basic vocabulary}

Before we start, there are a few basic concepts.

First of all, everything in py-fizz is some kind of physical object.
There are three basic kinds: cosmetic, dynamic, and static.

Cosmetic objects do not collide with anything.  They are just for show.

Dynamic objects do collide.  Also, they can move around.

Static objects also collide, but they do not move around.

There is one other kind of object, which is a "composite" object.
This just means that the object is composed of more basic objects.

For example, the car object is composed of three wheels and a crate.
The wheels and crate are all dynamic objects.  The car is a composite object.

@racketblock[(simulate 
                (wooden-level
                  (car)))]

@preview[(wooden-level
          (car))]

One last critical concept!  Objects can be parameterized.  For example, the
car is a function that takes a speed and/or ANOTHER OBJECT.

@racketblock[(simulate 
                (wooden-level
                  (car 1 (bowling-ball))))]

@preview[(wooden-level
                  (car 1 (bowling-ball)))]

Or...

@racketblock[(simulate 
                (wooden-level
                  (car 1 (balloon))))]

@preview[(wooden-level
                  (car 1 (balloon)))]


Or...

@racketblock[(simulate 
                (wooden-level
                  (car 1 (enemy))))]

@preview[(wooden-level
                  (car 1 (enemy)))]

And so on.  You can pass in any basic object to the car function, and you'll get
a new composite object back.  You could then pass this new car into any other
function that takes a composite object.

For example, maybe you want to be able to shoot a balloon-car out of a cannon...

@racketblock[(simulate 
                (wooden-level
                  (cannon (car 1 (balloon)))))]

@preview[(wooden-level
                  (cannon (car 1 (balloon))))]

The image above probably doesn't communicate exactly how cool this is.  Let's
check out a gif...

@image[#:scale 1]{./doc-images/BalloonCannon.gif}

So that's the basic idea.  You create objects.  You make those into composite
objects.  And you can combine composite objects to get even cooler composite objects.

And so on.

Exercise: Can you figure out how to make a car with a cannon on top that shoots out other cars?

@image[#:scale 1]{./doc-images/BalloonCannon2.gif}

@section{py-fizz High Level}

The High Level library consists of various gadgets (composite and basic) that
all tend to have a consistent look and feel, as well as physical properties that
work well together.  Many of the gadgets are parameterized, so you can make your
own new gadgets with them (like that balloon car shooter seen above).

This part of the documentation lists the provided gadgets and shows you how to
compose them to make new ones.

@subsection{Basic Gadgets}


@defproc[(wooden-level [object (or/c static? dynamic? cosmetic? composite?)])
         composite?]{

  @preview[(wooden-level (balloon))]

  This is just a pretty-looking space for running simulations.  There are static walls on
  all sides, and a cosmetic (wooden) background in the middle.  It will dynamically resize
  if what's inside doesn't fit in the default 600x600 space.
}


@defproc[(bowling-ball)
         dynamic?]{

  @preview[(bowling-ball)]

  Simple bowling ball.  High mass.

  No parameters on this one.
  But you can alter its properties with functions like toggle-static, mass, initial-velocity,
  etc.  
}

@defproc[(crate)
         dynamic?]{

  @preview[(crate)]

  Dynamic crate.  Falls by default.  If you want to use it as a platform, call toggle-static
  on it to convert it to a static object.
}

@defproc[(wheel)
         dynamic?]{

  @preview[(wheel)]

  Low mass, circular object.
}

@defproc[(balloon)
         dynamic?]{

  @preview[(balloon)]

  Floats.  (Obeys opposite gravity.)

  If it is attached to other objects, it will pull them upward.
}

@defproc[(breakable-balloon)
         dynamic?]{

  @preview[(breakable-balloon)]

  Like a regular balloon, but it can be destroyed by clicking on it.

  It can also be destroyed if it collides strongly with other objects.
}


@defproc[(friend)
         dynamic?]{

  @preview[(friend)]

  A dynamic object that causes you to lose the game if any of them are destroyed.
  Useful when building puzzles.
}

@defproc[(enemy)
         dynamic?]{

  @preview[(enemy)]

  A dynamic object that causes you to win the game if all of them are destroyed.
  Useful when building puzzles.
}


@defproc[(motor [color        string?]
                [speed        number?]
                )
         dynamic?]{
                   
 @racketblock[(motor "red" 1)]
 @preview[(motor "red" 1)]
 @racketblock[(motor "green" 1)]
 @preview[(motor "green" 1)]
 @racketblock[(motor "blue" 1)]
 @preview[(motor "blue" 1)]
  
 A dynamic object that rotates continually.  Good for vehicles.

 Use negative numbers to make it rotate the other direction.
}

@defproc[(pinned-motor
          [color        string?]
          [speed        number?]
          )
         dynamic?]{
                   
 @racketblock[(pinned-motor "red" 1)]
 @preview[(pinned-motor "red" 1)]
 @racketblock[(pinned-motor "green" 1)]
 @preview[(pinned-motor "green" 1)]
 @racketblock[(pinned-motor "blue" 1)]
 @preview[(pinned-motor "blue" 1)]
  
 A dynamic object that rotates continually.  It's pinned to one spot.
 Good for conveyor belts.

 Use negative numbers to make it rotate the other direction.
}


@defproc[(catpult
          [object (or/c static? dynamic? cosmetic? composite?)]
          )
         composite?]{

 @racketblock[(catapult (crate))]
 @preview[(catapult (crate))]
 
 @racketblock[(catapult (car))]
 @preview[(catapult (car))]

 @racketblock[(catapult (above (bowling-ball) (bowling-ball)))]
 @preview[(catapult (above (bowling-ball) (bowling-ball)))]
                   
 Makes a see-saw contraption, on one side is a bowling ball with a strong downward
 starting velocity.  On the other side is whatever object you supply.

 Note that although this function accepts static, dynamic, cosmetic, or composite objects,
 it is most exciting when you pass in a dynamic object (or a composite object that contains
 dynamic objects).
}

@defproc[(car
          [speed  number? 1] 
          [object (or/c static? dynamic? composite?) (crate)]
          [join-object (or/c static? dynamic? composite?)]
          )
         composite?]{

 @racketblock[(car)]
 @preview[(car)]
                     
 Makes a car.  You can control speed and direction with the speed parameter (negative numbers
 go counter clockwise).

 The second parameter controls what object is on top of the car.  Passing in a dynamic object
 is the simplest thing.
 
 @racketblock[(car 1 (bowling-ball))]
 @preview[(car 1 (bowling-ball))]

 If you pass in a static object, the car will be stuck in the air, "pinned"
 by the static object.  Usually not what you want.  (Use toggle-static to switch your
 static object to a dynamic one before passing it into the car function.)

 @racketblock[(car 1 (toggle-static (cannon)))]
 @preview[(car 1 (toggle-static (cannon)))]

 ADVANCED USAGE: If you pass in a composite object, you pust also pass in a join-object as the third parameter.
 This determines which part of the composite object to connect the wheels to.

 @racketblock[
 (let ([c (crate)])
   (car 1
        (balloons-pulling 10 c)
        c))]
 @preview[
 (let ([c (crate)])
   (car 1 (balloons-pulling 10 c) c))] 

 @racketblock[
 (let ([c (crate)])
   (car 1
        (car 1 c)
        c))]
 @preview[
 (let ([c (crate)])
   (car 1
        (car 1 c)
        c))] 

 Let's take a moment to see how cool it is to be able to make flying cars...

 @image[#:scale 1]{./doc-images/WeirdCars.gif}           
}

@defproc[(pipe
          [width number?]
          [height number?]
          )
         dynamic?]{

 @racketblock[(pipe 100 10)]
 @preview[(pipe 100 10)]

 Makes a dynamic rectangle that looks like a pipe.  Good for platforms, walls,
 falling pipes, etc.
}

@defproc[(balloons-pulling
          [num number?]
          [object (or/c dynamic? static?)]
          [string-length number? 100]
          )
         composite?]{
                     
 @racketblock[(balloons-pulling 4
                                (pipe 100 10)
                                50)]
 @preview[(balloons-pulling 4
                            (pipe 100 10)
                            50)]
                    
 Attaches the given number of balloons to the given object.  The length of the
 balloon string can also be configured.
}

@defproc[(conveyor-belt
          [num number?]
          [speed number? 10]
          )
         composite?]{
                     
 @racketblock[(conveyor-belt 5 -10)]
 @preview[(conveyor-belt 5 -10)]

 @racketblock[(conveyor-belt 5 10)]
 @preview[(conveyor-belt 5 10)]
                    
 Creates the given number of motors in a horizontal row.  The speed
 determines three things: the speed (obviously), the direction (negative is
 counter-clockwise), and the color (blue for counter-clockwise, red for clockwise).
}

@defproc[(v-space
          [num number?]
          )
         cosmetic?]{

 Creates transparent vertical space.  Good for positioning things.

 @racketblock[(above (bowling-ball)
                     (v-space 10)
                     (bowling-ball))]
 @preview[(above (bowling-ball)
                 (v-space 10)
                 (bowling-ball))]
}

@defproc[(h-space
          [num number?]
          )
         cosmetic?]{

 Creates transparent vertical space.  Good for positioning things.

 @racketblock[(beside (bowling-ball)
                      (h-space 10)
                      (bowling-ball))]
 @preview[(beside (bowling-ball)
                  (h-space 10)
                  (bowling-ball))]
}

@defproc[(fragments
          [object (or/c dynamic? static? cosmetic? composite?)]
          [resolution number?]
          [energy number? 100000]
          [destroy-after number? 50])
         composite?]{

 @racketblock[(fragments (car) 4)]
 @preview[(fragments (car) 4)]

 Takes the object and returns a composite object that looks like the original,
 but is really a bunch of dynamic objects constructed from a sliced up image
 of the original.

 This is how breakable-balloons explode when destroyed.

 Note that fragments are computationally expensive.  Keep the resolution and
 the destroy-after parameters low.
}

@defproc[(fragments
          [object (or/c dynamic? static? cosmetic? composite?)]
          [energy number? 10000]
          [angle  number? 0])
         static?]{

 @racketblock[(cannon (car))]
 @preview[(cannon (car))]

 Returns a static cannon that shoots the provided object when clicked.

 The angle and the power of the shot can be adjusted.
}

@defproc[(builder
          [object (or/c dynamic? static? cosmetic? composite?)]
          [destroy-self? boolean? #t])
         static?]{

 @racketblock[(builder (car))]
 @preview[(builder (car))]

 Returns a static treasure chest that turns into the provided object when
 clicked.  Good for puzzles.

 An icon of the provided object is displayed above the chest, so the user
 knows what to anticipate.
}


@section{py-fizz Low Level}

@subsection{Top Level}

@defproc[(preview
          [object (or/c dynamic? static? cosmetic? composite?)])
         image?]{

  Any object or composite you make can be passed into the preview function
  to get an image of what it will look like.
}

@defproc[(simulate
          [object (or/c dynamic? static? cosmetic? composite?)])
         void?]{

  This triggers the actual compilation to Python and runs the game/simulation.
}


@subsection{Basic Constructors}

@defproc[(make-static
          [object (or/c h:image? cosmetic? layout? physical?)]
          [#:collider collider collider? circle-collider])
         static?]{


}

@defproc[(make-dynamic
          [object (or/c h:image? cosmetic? layout? physical?)]
          [#:collider collider collider? circle-collider])
         dynamic?]{


}

@defproc[(make-cosmetic
          [object (or/c h:image? cosmetic? layout?)])
         cosmetic?]{

}

@defproc[(make-pivot
          [object (or/c h:image? cosmetic?)])
         pivot?]{

}

        
@defproc[(circle
          [radius number?]
          [fill-mode mode?]
          [color color?])
         cosmetic?]{

  A lifted version of the 2htdp/image function (see those docs for details).
  Returns a cosmetic.
}

@defproc[(rectangle
          [width number?]
          [height number?]
          [fill-mode mode?]
          [color color?])
         cosmetic?]{

  A lifted version of the 2htdp/image function (see those docs for details).
  Returns a cosmetic.
}

@defproc[(square
          [size number?]
          [fill-mode mode?]
          [color color?])
         cosmetic?]{

  A lifted version of the 2htdp/image function (see those docs for details).
  Returns a cosmetic.
}


@subsection{Setting Physical Properties of Objects}



@defproc[(motorize
          [speed number?]
          [object dynamic?])
         dynamic?]{


}


@defproc[(gravity
          [direction (list/c number? number?)]
          [object dynamic?])
         dynamic?]{


}

@defproc[(elasticity
          [amount number?]
          [object dynamic?])
         dynamic?]{


}

@defproc[(angle
          [amount number?]
          [object (or/c dynamic? static?)])
         dynamic?]{


}
         
@defproc[(friction
          [object (or/c dynamic? static?)]
          [energy number? 10000]
          [angle  number? 0])
         static?]{


}



@defproc[(ttl
          [time number?]
          [object (or/c dynamic? static? cosmetic?)])
         dynamic?]{


}


@defproc[(mass
          [amount number?]
          [object dynamic?])
         dynamic?]{


}  
 

@defproc[(initial-velocity
          [direction (list/c number? number?)]
          [object dynamic?])
         dynamic?]{

  
}

@defproc[(toggle-static
          [object (or/c dynamic? static?)])
         (or/c dynamic? static?)]{


}
 
@defproc[(width
          [object (or/c dynamic? static? cosmetic? composite?)])
         number?]{


}
         
@defproc[(height
          [object (or/c dynamic? static? cosmetic? composite?)])
         number?]{


}

@subsection{Making composite objects}

The easiest way to make a composite object is to use a spatial layout function:
above, beside, or overlay.

These place two objects in a spatial relation to each other.

Additionally, objects can be associated with physical properties: e.g.
they might have a joint connecting them.  If this is the case, you'll
create the composite object with a two-step process --
1) establish the physical relation
ship (e.g. with the spring-joint function), and then place the two objects
into a spatial relationship (e.g. with the above function).

@racketblock[(let* ([b1 (bowling-ball)]
                    [b2 (bowling-ball)]
                    [b1-with-connection
                     (pin b1 b2)])
               (simulate
                (above b1-with-connection b2)))]

Note that the pin function takes b1 and returns a new version of b1
that has a pin joint relationship to b2.  But you still need to place
both b1-with-connection and b2 into a relation with each other.

(You'll get a runtime error if you don't.)

@subsubsection{Spatial Relations for Composite Objects}

Spatial relations may be established between any two objects.  They
do not need to be related to each other physically.

@defproc[(above
          [object (or/c dynamic? static? cosmetic? composite?)]
          ...)
         composite?]{


}

@defproc[(beside
          [object (or/c dynamic? static? cosmetic? composite?)]
          ...)
         composite?]{


}

@defproc[(overlay
          [object (or/c dynamic? static? cosmetic? composite?)]
          ...)
         composite?]{


}

@subsubsection{Physical Relations for Composite Objects}

As stated above, spatial relations may be established between any two objects.  They
do not need to be related to each other physically.

The opposite, however, is not true.  If you create a physical relationship between
two objects, you must ALSO relate them spatially.

Think of it this way: If you say that two objects are physically related (e.g.
they have a connecting joint), you also need to say where those objects are in
the universe.  The only way to place things into the universe is to relate them
spatially to each other.

Keep that in mind with all of the functions in this subsection.

@defproc[(gear
          [object1 dynamic?]
          [object2 dynamic?])
         dynamic?]{

  The two objects will rotate together.

  Returns a new version of the first object.
}


@defproc[(connect-pivot
          [pivot pivot?]
          [object (or/c dynamic? static?)])
         pivot?]{

  Causes the object to swing around the pivot point.

  Returns a new version of the pivot.
}

@defproc[(pin
          [object1 (or/c dynamic? static?)]
          [object2 (or/c dynamic? static?)])
         dynamic?]{

  Establishes a rigid "rod" between the two objects.

  Returns a new version of the first object.
}

         
@defproc[(spring
          [object1 (or/c dynamic? static?)]
          [object2 (or/c dynamic? static?)]
          [distance number?])
         dynamic?]{

  Establishes a springy connection between two objects.  (Used for balloon strings.)

  Returns a new version of the first object.
}          


@defproc[(angle-spring
          [object1 (or/c dynamic? static?)]
          [object2 (or/c dynamic? static?)]
          [angle       number? 0]
          [stiffness   number? 0]
          [damping     number? 0])
         dynamic?]{

  The two objects will prefer to be at the same angle.  They will spring back
  to that angle if forces do not prevent it.
}

@subsection{Runtime Behaviours}
         
@defproc[(on-collide
          [object (or/c dynamic? static? cosmetic? composite?)]
          [callback callback?]
          [#:friction  friction-thresh 0]
          [#:energy-loss energy-loss-thresh 0])
         (or/c dynamic? static? cosmetic? composite?)]{

  If the object suffers a collision, the callback is triggered.

  Collisions can be filtered out based on friction and kinetic energy loss.
}

@defproc[(on-click
          [object (or/c dynamic? static? cosmetic? composite?)]
          [callback callback?])
         (or/c dynamic? static? cosmetic? composite?)]{

  If the object is clicked, the callback is triggered.
}
                
@defproc[(spawn
          [object (or/c dynamic? static? cosmetic? composite?)]
          [destroy-self? boolean? #f])
         callback?]{

  Spawns a new object.  Only useful in the context of on-click or on-collide.
}

@defproc[(must-survive
          [object (or/c dynamic? static?)])
         (or/c dynamic? static?)]{

  The given object triggers a lose screen if it
  is destroyed.
}

@defproc[(must-die
          [object (or/c dynamic? static?)])
         (or/c dynamic? static?)]{

  The given object triggers a win screen if all such
  objects are destroyed.
}



@subsection{Misc}
         
@defproc[(set-package-path!
          [path string?])
         void?]{
  If you have the py-fizz package installed in a weird place
  (like I do when I'm developing it).
}
         




