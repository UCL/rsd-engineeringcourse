---
title: Construction
---

## Construction

### Construction

Construction is about we use letters and symbols to build readable, meaningful software. Our session covered: 

* conventions of layout and syntax
* how to write comments and documentation
* progressive improvement of code with refactoring
* refactoring code with classes

Our exercise put this knowledge into practice by refactoring 'Bad Boids', some intentionally-bad code that mimicked the motion of a flock of birds.

### Refactoring bad-boids

We are looking for:

* Readable code and sensible tests (always!)
* Appropriate refactoring
    - cleaning up syntax (whitespace; repetition; unnecessary code)
    - named variables replacing hardcoded values
    - relevant use of functions and/or classes

### Tidier code (spacing, variable names):

Before:

``` python
def update_boids(boids):
        xs,ys,xvs,yvs=boids
        # Fly towards the middle
        for i in range(len(xs)):
                for j in range(len(xs)):
                          xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
```

After:

``` python
class Boid(object):
    ...
    def interaction(self,other):
        delta_v=array([0.0,0.0])
        separation=other.position-self.position
        separation_sq=separation.dot(separation)

         # Fly towards the middle
        delta_v+=separation*self.owner.flock_attraction
```

### Use of functions and/or classes:

Before:

``` python
boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
```

After:

``` python
class Boid(object):
    def initialise_random(self,count):
        self.boids=[Boid(random.uniform(-450,50.0),
        random.uniform(300.0,600.0),
        random.uniform(0,10.0), ... )]
```

### Tests, written alongside code:

For example, use of fixtures:

``` python
    def test_bad_boids_regression():
    boids=bd.Boids(0.01/50,10,100,0.125/50)
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),
        'fixture.yml'))) ... 
```

... and expected behaviour:

``` python
def test_boid_interaction_avoidance():
    boids=bd.Boids(3.0,10.0,10,0) # Define flocking behaviour
    first=bd.Boid(0,0,1,0,boids) 
    second=bd.Boid(0,5,0,0,boids)
    # Test expected interaction of first and second boid
    assert_array_equal(first.interaction(second),[0.0,10.0])
```

### Sample solution

A sample solution, with full commit history, is available at: 
https://github.com/jamespjh/bad-boids/commits/better_boids

