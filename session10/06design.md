---
title: Design
---

## Design

### Design

Deliberate design can help us to complete complex software projects, repeatably and reliably. We looked at: 

* design in object oriented programming
* Unified Modelling Language for communicating design
* design patterns
* processes, such as Agile, in the context of design

### An eagle in the boids

We applied our new knowledge to refactor our (now-good!) boids code with elements of object orientation.

We are looking for:

* Readable code and sensible tests (always!)
* Object-orientated code
* Polymorphism and/or inheritance
* Use of design pattern/s
* Unified Modelling Language for visualisation of classes

### Separation of concerns

We'll begin by separating the model from the animation:

``` python
+ view_boids.py

+ from boids import Boids
+ from matplotlib import pyplot as plt
+ from matplotlib import animation
...
+ def animate(frame):
+    boids.update()
+    scatter.set_offsets(zip(boids.xs,boids.ys))
+    anim = animation.FuncAnimation(figure, animate,
+        frames=50, interval=50)
```

### Refactor with inheritance

We can move towards object orientation by creating separate subclasses for our different species of bird:

``` python
# Create super class
class Boid(object):
    def __init__(self,x,y,xv,yv,owner):
        self.position=array([x,y])
        self.velocity=array([xv,yv])
        self.owner=owner

class Starling(Boid):
    def __init__(self,x,y,xv,yv,owner):
        super(Starling, self).__init__(x,y,xv,yv,owner)
    ...

class Eagle(Boid):
    def __init__(self,x,y,xv,yv,owner):
        super(Eagle, self).__init__(x,y,xv,yv,owner)
    ...
```

### Counting boids

We'll also add a class member, just because we can, to keep track of the total number of boids:

``` python 
class Boid(object):
    number_created=0
    def __init__(self,x,y,xv,yv,owner):
        Boid.number_created+=1
        self.position=array([x,y])
        self.velocity=array([xv,yv])
        self.owner=owner
    @classmethod
    def howMany(cls):
        return cls.number_created

print Boid.howMany()
'50'
```

<!--
### Design patterns

Comment:

``` python

```
!-->

<!--
### Unified Modelling Language

Comment:

``` python

```
!-->

<!--
### Title

Comment:

``` python

```
!-->

### Sample solution

A sample solution is available at: 
[https://github.com/tompollard/bad-boids/commits/eagle](https://github.com/tompollard/bad-boids/commits/eagle)

