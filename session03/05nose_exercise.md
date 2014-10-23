---
title: Classroom Exercise
---

##Classroom Exercise: Energy Calculation

###Diffusion Model in 1D

<div align="left">

Description: simplistic 1-dimensional diffusion model

:   * Particles are on a 1d axis
    * Particles do not want to be where there are other particles

Implementation:

:   * Given a vector $n$ of positive integers, and of arbitrary length
    * Compute the energy,

        $E(n) = \frac{D}{2} \sum_i n_i(n_i - 1),$

        where $D$ is a scalar coefficient.

</div>

{% raw %}
<svg id="model" width="500" height="150" class="boundary"></svg>
<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
<script src="http://lab.hakim.se/reveal-js//lib/js/head.min.js" ></script>
<script src="http://lab.hakim.se/reveal-js//js/reveal.min.js" ></script>
<style>
.axis path, .axis line {
  fill: none;
  stroke: white;
  shape-rendering: crispEdges;
}
.axis text {
  fill: white
}
</style>
<script>
  function externalDimensions(id) {
    var svgElement = document.getElementById("model");
    var externalWidth = parseInt(svgElement.getAttribute("width"));
    var externalHeight = parseInt(svgElement.getAttribute("height"));
    return {width: externalWidth, height:externalHeight}
  }
  function model() {
    var margin = {top: 20, right: 10, bottom: 35, left: 10};
    var width=100, height=100
    var externalDims = externalDimensions("model");
    externalDims.height -= margin.top + margin.bottom
    externalDims.width -= margin.left + margin.right
    var svg = d3.select("#model").append("g")
                .attr("transform", "translate(" + margin.left + ", " + margin.top + ")");
    var numbers = Array.apply(null, Array(10)).map(function (_, i) {return i;});

    var yscale = d3.scale.linear().domain([0, height]).range([0, externalDims.height]);
    var xscale = d3.scale.ordinal().domain(numbers).rangePoints([0, externalDims.width])
    var xAxis = d3.svg.axis().orient("bottom").scale(xscale);

    // svg.append("rect").attr("x", -margin.left).attr("y", -margin.top)
    //         .attr("height", externalDims.height + margin.bottom + margin.top)
    //         .attr("width", externalDims.width + margin.right + margin.right)
    //         .style("fill", "rgb(100, 100, 100)")

    var margingroup = svg.append("g") .attr("transform", "translate(0, " + externalDims.height + ")");
    var axisgroup = margingroup.append("g").attr("class", "x axis").call(xAxis);

    var nbrects = [0, 0, 3, 5, 8, 4, 2, 1]
    var rectangles = []
    for(var j = 0; j < nbrects.length; ++j) {
      for(var i = 0; i < nbrects[j]; ++i) rectangles.push([j, i])
    }

    function xPos(i) { return xscale(i) - 10; }
    function yPos(i) { return -yscale(i * 14 + 15); }
    var rectgroup = margingroup.append("g")
    rectgroup.selectAll("rect").data(rectangles, function(d, i) {return i;}).enter()
            .append("rect")
            .attr("x", function(d) { return xPos(d[0]); })
            .attr("y", function(d) { return yPos(d[1]); })
            .attr("id", function(d, i) { return "rect" + i; })
            .attr("width", 20).attr("height", yscale(12)).style("fill", "blue").style("stroke-width", "1px");
    return {x: xPos, y: yPos, group: rectgroup}
  }
  particle_position = model();
  particle_movements = [
    [7, 2, 1],
    [14, 5, 3],
    [1, 1, 0],
    [19, 6, 3],
    [7, 3, 4],
    [2, 0, 0],
    [7, 2, 2],
    [15, 6, 2],
    [15, 5, 4],
    [2, 1, 0]
  ];
  function update_particles() {
     if(particle_movements.length == 0) { clearInterval(); return; }
     newPosition = particle_movements.pop();
     particle_position.group.select("#rect" + newPosition[0])
       .transition()
       .duration(750)
       .attr("x", particle_position.x(newPosition[1]))
       .attr("y", particle_position.y(newPosition[2]));
  }
  Reveal.addEventListener( 'slidechanged', function( event ) {
      if(event.currentSlide.getAttribute("id") != "diffusion") {
        clearInterval();
      } else { setInterval(update_particles, 1500); }
      // event.previousSlide, event.currentSlide, event.indexh, event.indexv
  } );
</script>
{% endraw %}

###Starting Point

<div align="left">
In a directory, create two files:

* Implementation file: diffusion_model.py

``` python
def energy(density, coeff=1.0):
  """ Energy associated with the diffusion model

      Parameters
      ----------

      density: array of positive integers
          Number of particles at each position i in the array
      coeff: float
          Diffusion coefficient.
  """
  # implementation goes here
```

* Testing file: test_diffusion_model.py

``` python
from diffusion_model import energy
def test_energy():
  """ Optional description for nose reporting """
  # Test something
```

</div>

###Solution

Don't look till after class!

Here is one solution:
   * Function: https://github.com/UCL/rsd-engineeringcourse/blob/staging/session03/solutions/diffusion_model.py
   * Test: https://github.com/UCL/rsd-engineeringcourse/blob/staging/session03/solutions/test_diffusion_model.py

###Coverage


1. Comment out from exception tests in solution
1. in solution directory, run
    ``` bash
    nosetests --with-coverage --cover-package=diffusion_model -v --cover-html
    ```
1. Open ``cover/index.html`` for coverage information


![](session03/figures/coverage.png)
