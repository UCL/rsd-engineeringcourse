Nose Exercise
=============


Description {#diffusion}
-----------

<div align="left">

Goal:

:   implement simple and unphysical 1-dimensional diffusion model

Description:

:   * Particles are on a 1d axis
    * Particles do not want to be where there are other particles

Implementation:

:   * Given a vector $n$ of positive integers, and of arbitray length 
    * Compute the energy,

        $E(n) = \frac{D}{2} \sum_i n_i(n_i - 1),$
        
        where $D$ is a scalar coefficient.

</div>

Starting Point
--------------

<div align="left">
In a directory, create two files:

* Implementation file: diffusion_model.py

    ~~~~~~~~~~~~~~~~~~{.python}
    def energy(density):
      """ Energy associated with the diffusion model

          :Parameters:
            density: array of positive integers
               Number of particles at each position i 
               in the array
      """
      # implementation goes here
    ~~~~~~~~~~~~~~~~~~

* Testing file: test_diffusion_model.py

    ~~~~~~~~~~~~~~~~~~~~{.python}
    from diffusion_model import energy
    def test_energy():
      """ Optional description for nose reporting """
      # Test something
    ~~~~~~~~~~~~~~~~~~~~
</div>

Coverage
--------

<div align="left">

1. Comment out from exception tests in solution 
1. in solution directory, run

    ~~~~~~~~~~~~~~{.bash}
    nosetests --with-coverage --cover-package=diffusion_model -v --cover-html
    ~~~~~~~~~~~~~~

1. Open ``cover/index.html`` for coverage information

</div>
![](assets/coverage.png)
