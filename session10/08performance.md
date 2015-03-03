---
title: Performance computing
---

## Performance computing

### Performance computing

Profiling allows us to spot and address performance issues with our code. The session on performance programming explored: 

* faster, array-wise operations using NumPy
* implications of data type on performance
* the Big O notation
* speed benefits of Cython

### Optimising the boids

Returning to the Boids code for our exercise, we sought to reimplement the model with NumPy and Cython to make it run as fast as possible. We are looking for:

* Readable code and sensible tests <div class="fragment grow">(always!)</div>
* Profiling to assess performance
* Attempts to optimise, for example with:
    - Appropriate use of data types
    - Cython and/or NumPy
    - Vectorisation of loops
    - Arraywise operations

### Create a new working branch

As suggested in the exercise, we'll begin our work by creating a new branch in our repository, based on the original bad-boids:

``` bash
git clone git@github.com:USERNAME/bad-boids.git
git checkout -b perform
```

### A little tidying...

We'll begin with a little housekeeping, first by putting the step that initialises the boids into a function, taking us from:

``` python
boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
```

to:

``` python
def initialise_boids(number_of_boids):
    boid_rng = range(number_of_boids)
    boids_x=[random.uniform(-450,50.0) for boid in boid_rng]
    boids_y=[random.uniform(300.0,600.0) for boid in boid_rng]
    boid_x_velocities=[random.uniform(0,10.0) for boid in boid_rng]
    boid_y_velocities=[random.uniform(-20.0,20.0) for boid in boid_rng]
    boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
    return boids
```

<!--
Reminder about the importance of tests, which most people completing the exercise neglected. Also, if refactoring, keep the original functionality. Still need to plot. Still need to be able to run.
-->

### Write tests

Before thinking about performance, we'll update our tests. Our boids should exhibit the following behaviour:

* fly towards the centre of a flock
* fly away from nearby boids
* attempt to match speed with nearby boids
* move according to velocity

``` python 
def test_only_one_boid_shows_no_flocking_behaviour():
    x_pos,y_pos,x_vel,y_vel = [1.0],[1.0],[2.0],[7.0]
    boid = (x_pos, y_pos, x_vel, y_vel)
    initial_boid = copy.deepcopy(boid)
    bd.update_boids(boid)
    # new positions equal initial position + velocity
    assert_equal(boid[0],initial_boid[0][0]+initial_boid[2][0])
    assert_equal(boid[1],initial_boid[1][0]+initial_boid[3][0])
```

### Consistent syntax

There are tools that can save us time in cleaning up syntax:

``` bash
# check output using autopep8, without making changes
autopep8 boids.py

# if happy, change in place
autopep8 -i boids.py
```

### Making a start

We'll first add an empty function to contain our soon-to-be-faster code:

``` python
def update_boids_faster(boids):
    ''' This is where our faster boids will live '''
    pass
```

### Two competing functions

We now have two functions, which, eventually, should do the same thing at different speeds:

* ```update_boids()```
* ```update_boids_faster()```

### Updating our tests
  
We will also add the new function to our test framework, using the nose_parameterized decorator. We're expecting it to fail the tests to begin with:

``` python
# nose_parameterized lets us use the @parameterized decorator
# to pass a list of functions through each test
from nose_parameterized import parameterized

# for example:
@parameterized([[bd.update_boids],[bd.update_boids_faster]])
def test_only_one_boid_shows_no_flocking_behaviour(update_function):
    ...
    update_function(boid)
```

### Refactor a loop

Our current ```update_boids()``` function uses a loop to update the position of boids based on their velocities:

``` python
# Move according to velocities
for i in range(len(xs)):
    xs[i] = xs[i] + xvs[i]
    ys[i] = ys[i] + yvs[i]
```
  
We'll replace this loop with a vectorised version:

``` python
# Move according to velocities
# for i in range(len(xs)):
#   xs[i]=xs[i]+xvs[i]
#   ys[i]=ys[i]+yvs[i]
xs = xs + xvs
ys = ys + yvs
```

### More loops
  
We'll also replace the nested loops used to compute velocity towards the middle of the flock with a vectorised approach:

``` python
# Fly towards the middle
newxs = (xs - np.sum(xs)/float(boid_num)) * 0.01
xvs = xvs - newxs
newys = (ys - np.sum(ys)/float(boid_num)) * 0.01
yvs = yvs - newys
```

### More refactoring

We can optimise further to perform the operations on the boids array in-place, instead of copying and unpacking to the xs, ys, xvs, and yvs.

``` python
# Fly towards the middle
boids[2:,:]-= 0.01*(boids[0:2,:]- \
    np.sum(boids[0:2,:,np.newaxis],1)/boid_num)
```

### Timing it

After our changes:

``` python
# initialise with 100 boids
%%timeit
update_boids(boids)
'Best of 3: 365 ms per loop'

%%timeit
update_boids_faster(boids)
'Best of 3: 945 µs per loop'
```

### Sample solution

A sample solution with clean commit history is available at: 
[https://github.com/tompollard/bad-boids/commits/perform](https://github.com/tompollard/bad-boids/commits/perform)



