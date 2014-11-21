---
title: Numerics
---


###Structure of Arrays

Numerical code is sometimes faster with raw structures of arrays:

```cpp
class Model(object):
    def __init__(self,count):
       self.positions=[[random.random(),random.random()] for x in range(count)]
       self.velocities=[[0,0]]*count
    def simulate(self, step):
       for i in range(len(positions)):
           self.positions[i][0]+=self.velocities[i][0]
           self.positions[i][1]+=self.velocities[i][1]

%timeit Model(100).simulate()
```

###Array of structures can be slow

Object oriented programming gives clearest answers using *Arrays Of Structures*:

```python
class Particle(object):
    def __init__(self):
      self.pos=[random.random(),random.random()]
      self.vel=[0,0]
    def move(self):
      self.pos[0]+=self.vel[0]
      self.pos[1]+=self.vel[1]

class Model(object):
    def __init__(self, count):
        self.particles=[Particle() for x in range(100)]
    def simulate():
        for particle in self.particles:
            particle.move()

%timeit Model(100).simulate()
```

This can be slow, due to memory layout issues.

How can we do object oriented programming, and still get maximum HPC performance?

###HandleBody Pattern

``` python

class Particle(object):
    index=0
    data=[]

    def __init__(self):
        Particle.data.append([random.random(),random.random(),0,0])
        self.index=Particle.index
        Particle.index+=1

    def move(self, step):
        # Called repeatedly, but now, more cache efficient
        Particle.data[self.index][0]+=Particle.data[self.index][2]
        Particle.data[self.index][1]+=Particle.data[self.index][3]

%timeit Model(100).simulate()
```

With this approach, code can often make use of memory locality, while still writing
object-oriented looking client code.

This would be even faster with NumPy arrays, see later lectures.

