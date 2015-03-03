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

We'll begin by separating out the code used to model our boids from the code used for animation.

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

<!--
### Polymorphism and inheritance

Comment:

``` python

```
!-->

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

A sample solution, with full commit history, is available at: 
[https://github.com/jamespjh/bad-boids/commits/eagle](https://github.com/jamespjh/bad-boids/commits/eagle)

