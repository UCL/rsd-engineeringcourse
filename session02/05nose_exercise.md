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

<svg id="model" width="500" height="300" class="boundary"></svg>
<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
<script src="http://lab.hakim.se/reveal-js//lib/js/head.min.js" ></script>
<script src="http://lab.hakim.se/reveal-js//js/reveal.min.js" ></script>
<style>
.axis path, .axis line {
  fill: none;
  stroke: white;
  shape-rendering: crispEdges;
}
</style>
<script>
  var width=100, height=100
  var svg = d3.select("#model")
  var svgElement = document.getElementById("boundary");
  var externalWidth = parseInt(svgElement.getAttribute("width"));
  var externalHeight = parseInt(svgElement.getAttribute("height"));
  var numbers = Array.apply(null, Array(10)).map(function (_, i) {return i;});

  var yscale = d3.scale.linear().domain([0, height]).range([0, externalHeight]);
  var xscale = d3.scale.ordinal().domain(numbers).rangePoints([0, externalWidth-20])
  var xAxis = d3.svg.axis().orient("bottom").scale(xscale);
  var margingroup = svg.append("g")
                       .attr("transform", "translate(10, " + (externalHeight - 50) + ")");
  var axisgroup = margingroup.append("g").attr("class", "x axis").call(xAxis);

  var nbrects = [0, 0, 3, 5, 8, 4, 2, 1]
  var rectangles = []
  for(var j = 0; j < nbrects.length; ++j) {
    for(var i = 0; i < nbrects[j]; ++i) rectangles.push([j, i])
  }

  var rectgroup = margingroup.append("g")
  rectgroup.selectAll("rect").data(rectangles, function(d, i) {return i;}).enter()
           .append("rect")
           .attr("x", function(d) { return xscale(d[0]) - 10; })
           .attr("y", function(d) { return -yscale(d[1] * 8 + 7); })
           .attr("id", function(d, i) { return "rect" + i; })
           .attr("width", 20).attr("height", yscale(6)).style("fill", "blue").style("stroke-width", "1px");

  changes = [
    [2, 1, 0],
    [15, 5, 4],
    [15, 6, 2]
  ];
  ncalls = 0;
  function update() {
     console.log(changes.length)
     if(ncalls == changes.length) {
       clearInterval();
       return;
     }
     rectgroup.select("#rect" + changes[ncalls][0])
       .transition()
       .duration(750)
       .attr("x", xscale(changes[ncalls][1]) - 10)
       .attr("y", -yscale(changes[ncalls][2] * 8 + 7));
     ncalls += 1
  }
  setInterval(update, 1500);

</script>

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
