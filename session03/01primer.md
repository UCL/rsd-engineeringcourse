---
title: Primer
---

##Testing Primer

###Tests at different scales

-----------------------     ---------------------------------------------------------
**Unit testing**            smallest logical block of work (often < 10 lines of code)

**Component testing**       several logical blocks of work together

**Integration testing**     all components together / whole program
-----------------------     ---------------------------------------------------------

<br>
<div class="fragment fade-in">
Always start at the smallest scale! 

<div class="fragment grow">
If unit test is too complicated, go smaller.
</div>
</div>


###Testing vocabulary

* **fixture** input data
* **action** function that is being tested
* **expected result** the ouput that should be obtained
* **actual result** the ouput that is obtained

* **coverage** Proportion of all possible paths in the code that the tests take

    ~~~~~~~~~~~~~~~~~~~~~~~~{.fortran}
    if(energy > 0) then
       ! Do this 
    else 
       ! Do that
    endif
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Is there a test for `energy > 0` and `energy <= 0`?
