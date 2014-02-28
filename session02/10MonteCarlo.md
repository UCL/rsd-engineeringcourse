Exercise: Monte-Carlo
=====================


Description
-----------

Goal

:    Perform Monte-Carlo over diffusion model


Description

:    Given an input function (energy) and starting point (density) and a temperature $T$

     1. Compute energy at current density
     1. Move randomly chosen particle left or right 
     1. Compute second energy
     1. Compare the two energies:
         
         1. If second energy is lower, accept move
         1. Otherwise compute $P_0=e^{-\frac{E_1 - E_0}{T}}$ and $P_1$ a random number,
            accept move only if $P_0 > P_1$

     1. Repeat


Caveats

:    * should work for (m)any energy function(s)
     * separate tests for separate steps! What constitute a step?
     * test should not depend on other parts of code


Bonus

:    * Use debugger to stop code at each iteration
     * Use [matplotlib](http://matplotlib.org/) to plot density at each iteration
