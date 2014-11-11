---
title: Exercise
---
## Exercise
### Exercise
Numbers have units. $5\mathrm{m}^2$ is not $5\mathrm{J}$. $6\mathrm{J}$ is the
same as $6\mathrm{kg}\mathrm{m}^2\mathrm{s}^{2}$ which is the same as
$2\mathrm{N} \cdot 3\mathrm{m}$

Write a python library to implement handling quantities with units, and
converting between units, with a github repostiory and a setup.py file, and
some unit tests.

You should define operators for multiply, equality, and add for your class.

Your unit tests should include things like:
``` raw
assert(5*meters == 0.005*kilometers)
assert((60*seconds).to(minutes).value==1)
assert((60*seconds).to(minutes).unit==minutes)
with assert_raises(IncompatibleUnitsError):
    5*meters+2*seconds
```
You don't have to implement every unit! You might want to load your unit definitions from a yaml config file.

