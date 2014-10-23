---
title: Comments
---

##Comments

###Bad Comments

"I write good code, you can tell by the number of comments."

This is wrong.

###Comments which are obvious

``` cpp
i += 1 ; // Add one to i
j += 1 ; // Increment the index variable
```

``` python
for element in array: # Loop over elements
```

###Comments which could be replaced by better style

```cpp
for (int i=0;i<agent_count;i++){ // for each agent
agt[i].theta+=ws[i]; // Increment the angle of each agent by its angular velocity
agt[i].x+=r*sin(agt[i].theta); // Move the agent by the step-size r in the direction indicated
agt[i].y+=r*cos(agt[i].theta);
}
```

compared to:

``` cpp
for (Agent& agent: agents){ // C++11 range-based for loop
  agent.turn();
  agent.move();
}

Agent::turn(){
   direction+=angular_velocity;
}
Agent::move(){
   // Angle is measured clockwise from +ve y-axis
   x+=step_length*sin(direction);
   y+=step_length*cos(direction);
}
```

###Comments which could be replaced by better style


“The proper use of comments is to compensate for our failure to express yourself in code. 
Note that I used the word failure. I meant it. Comments are always failures.”

-- Robert Martin, [Clean Code](http://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882).

###Comments which belong in an issue tracker

``` cpp
delete x; // Code crashes here sometimes
```

``` cpp
class Agent {
   // TODO: Implement pretty-printer method
}
```

``` cpp
typedef const struct direct direct_t; // Doesn't compile on OSX
```

BUT 

``` cpp
if (x->safe()){ // Guard added as temporary fix to #32
   delete x;
}
```

is OK.

###Comments which only make sense to the author today

``` cpp
agent.turn(); // Turtle Power!
agent.move();
delete *agent; // Shredder!
```

###Comments which are unpublishable

``` cpp
// Stupid supervisor made me write this code
// So I did it while very very drunk.
```

##Good comments

###Pedagogical comments

Code that *is* good style, but you're not familiar with, or 
that colleagues might not be familiar with

``` cpp
for (auto agent : agents) { \\ C++11 range based for loop 
```

``` python

# This is how you define a decorator in python
def double(decorated_function):
   # Here, the result function forms a closure over the decorated function
   def result_function(input):
     return decorated_function(decorated_function(input))
   # The returned result is a function
   return result_function

@double
def try_me_twice():
   pass
```

###Documentation as comments

``` cpp
//! \brief Creates parameter structure from HDF5 input.
//! \param[in] _filename File to read data from
//! \param[in] _flags when opening file
//! \tparam DIMS number of dimensions. Should be 2 or 3, and the content of the file should
//! correspond.
//! \tparam T_SCALAR type of scalar to use in calculations. Should be float, double, or long
//! double.
template<t_dimensionality DIMS, class T_SCALAR KWAVE_MACRO>
  ElastikParameters<DIMS, T_SCALAR> parameters_from_hdf5( std::string const &_filename,
                                                          unsigned int _flags = H5F_ACC_RDONLY ) {
    return parameters_from_hdf5<DIMS, t_real>(HDF5_File(_filename, _flags));
  }
```
###Documentation as comments

``` python
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    ... #content    
```

``` 
>>> help(complex)
 |  complex(real[, imag]) -> complex number
 |
 |  Create a complex number from a real part and an optional imaginary part.
 |  This is equivalent to (real + imag*1j) where imag defaults to 0.
```


###Other good comments

``` cpp
double angle; // clockwise from +ve y-axis
vector<int> nonzero_indices; // Use sparse model as memory constrained
// Populate the collision count arrays.
for (unsigned collisionType = 0; collisionType < COLLISION_TYPES; collisionType++)
{
   midDomainProcCollisions[collisionType] = midDomainBlockNumbers[collisionType].size();
   domainEdgeProcCollisions[collisionType] = domainEdgeBlockNumbers[collisionType].size();
}
```
