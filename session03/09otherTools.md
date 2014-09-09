---
title: Other Tools
---

Test Servers
------------

Goal 

:   1. run tests nightly
    1. run tests after each commit to github (or other)
    1. run tests on different platforms

![Soon at a UCL near you!](assets/jenkins.png)


Memory and Profiling
--------------------

* Checking for memory leaks with [valgrind](http://valgrind.org/):
  `valgrind --leak-check=full program`
* Checking cache hits and cache misses with
  [cachegrind](http://valgrind.org/docs/manual/cg-manual.html)
  `valgrind --tool=cachegrind program`
* Profiling the code with [callgrind](http://valgrind.org/docs/manual/cl-manual.html)
  `valgrind --tool=callgrind program`

    ![](assets/callgrind.png)
 
 
    <div align="left">
    * Python: [profile](http://docs.python.org/2/library/profile.html)
    * R: [Rprof](http://stat.ethz.ch/R-manual/R-devel/library/utils/html/Rprof.html)
    </div>


