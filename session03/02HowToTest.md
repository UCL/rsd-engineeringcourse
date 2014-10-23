---
title: How to Test
---

##How to Test

###Equivalence partitioning

Think hard about the different cases the code will run under: this is science, not coding!

{% raw %}
----------------------  ------------------------------------------------------------------------
Research Project        Evolution of agricultural fields in Saskatchewan from aerial photography

In silico translation   Compute overlap of two rectangles
----------------------  ------------------------------------------------------------------------

<div class="fragment"
     x="[5, width * 0.75-5]"
     y="[20, 30]"
     widths ="[width/3, width/4]"
     text="non-overlapping"> </div>

<div class="fragment"
     x="[width*0.25, width * 0.5]"
     y="[20, 50]"
     widths ="[width/3, width/4]"
     text="overlapping one way"> </div>

<div class="fragment"
     x="[width*0.25, width * 0.5]"
     y="[20, 30]"
     widths ="[width/3, width/4]"
     text="overlapping another way"> </div>

<div class="fragment"
     x="[width*(0.5 - 1/6), width * (0.5 - 1/8)]"
     y="[20, 30]"
     widths ="[width/3, width/4]"
     text="contained one inside the other"> </div>

<div class="fragment"
     x="[width*(0.5 - 1/8), width * (0.5 - 1/8)]"
     y="[20, 30]"
     widths ="[width/4, width/4]"
     text="same width"> </div>

<div class="fragment"
     x="[width*(0.5 - 1/6), width * (0.5 + 1/6)]"
     y="[20, 30]"
     widths ="[width/3, width/4]"
     text="edge sharing"> </div>

<div class="fragment"
     x="[width*(0.5 - 1/6), width * (0.5 + 1/6)]"
     y="[20, 20 + height * 0.65]"
     widths ="[width/3, width/4]"
     text="corner sharing"> </div>

<style>
  .boundary rect {
    stroke:rgb(255, 255, 255);
    stroke-width:4;
    fill-opacity:0.5;
  }
  .boundary text {
    fill:#eeeeee;
    font-family: "Open Sans", sans-serif;
    font-size: 30px;
    font-weight: 200;
    letter-spacing: -0.02em;
    color: #eeeeee; }
  }
</style>
<svg id="boundary" width="500" height="300" class="boundary"> </svg>

<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
<script src="http://lab.hakim.se/reveal-js//lib/js/head.min.js" ></script>
<script src="http://lab.hakim.se/reveal-js//js/reveal.min.js" ></script>
<script>
  var svgElement = document.getElementById("boundary");
  var externalWidth = parseInt(svgElement.getAttribute("width"));
  var externalHeight = parseInt(svgElement.getAttribute("height"));
  var width=100, height=100
  var xscale = d3.scale.linear().domain([0, width]).range([0, externalWidth])
  var yscale = d3.scale.linear().domain([0, height]).range([0, externalHeight]);

  var rectangles = [
    { "x": 5, "y": 20, "width": width /3, "height": height * 0.65, "fill": "(0, 0, 255)" },
    { "x": width * 0.75-5, "y": 30, "width": width / 4, "height": height * 0.45, "fill": "(0, 125, 0)" }
  ];


  var svg = d3.select("#boundary")

  svg.selectAll("rect").data(rectangles, function(d, i) { return i; }).enter().append("rect")
        .attr("x", function(d) { return xscale(d.x); })
        .attr("y", function(d) { return yscale(d.y); })
        .attr("width", function(d) { return xscale(d.width); })
        .attr("height", function(d) { return yscale(d.height); })
        .style("fill", function(d) { return "rgb" + d.fill})

  svg.append("text")
     .text("")
     .attr("x", 0)
     .attr("y", "1em")

  function update(fragment) {
    if(!fragment) return;
    if(!fragment.hasAttribute("text")) return;
    console.log("update: " + fragment.getAttribute("text") + fragment.getAttribute("x"))
    var xPositions = eval(fragment.getAttribute("x"));
    var yPositions = eval(fragment.getAttribute("y"));
    var widths = eval(fragment.getAttribute("widths"));
    svg.selectAll("rect").data(rectangles, function(d, i) { return i; })
            .transition()
            .duration(750)
            .attr("x", function(d, i) { return xscale(xPositions[i]); })
            .attr("y", function(d, i) { return yscale(yPositions[i]); })
            .attr("width", function(d, i) { return xscale(widths[i]); })
    svg.selectAll("text").text("Case: " + fragment.getAttribute("text"))
  }
  function back(fragment) {
    update(fragment.previousElementSibling)
  }

  Reveal.addEventListener( 'fragmentshown', function( event ) { update(event.fragment); });
  Reveal.addEventListener( 'fragmenthidden', function( event ) { back(event.fragment); });

</script>

{% endraw %}

###Boundary cases

* Limit between two equivalence classes: edge and corner sharing fields
* Where-ever indices appear, check values at ``0``, ``N``, ``N+1``
* Empty arrays:

``` python
    atoms = [read_input_atom(input_atom) for input_atom in input_file]
    energy = force_field(atoms)
```

    What happens if ``atoms`` is an empty list?

* What happens when a matrix/data-frame reaches one row, or one column?


###Positive *and* Negative tests

* **Positive tests**: program/component/unit in normal situations

* **Negative tests**: program/component/unit in pathological functionning mode

<div align="left">
Bad input should be expected and should fail early and explicitely.

<div class="fragment roll-in">
Testing should ensure that explicit failures do indeed happen.

``` python
def I_only_accept_positive_numbers(number):
    # Check input
    if number < 0: raise ValueError("Input ({0}) is negative".format(number))

    # Do something
```

An in test file:

``` python
def test_I_only_accept_positive_numbers(number):
    from mymodule import I_only_accept_positive_numbers

    try:  I_only_accept_positive_numbers(0)
    except: pass
    else: raise AssertionError("zero did not raise an error")
```
</div>
</div>

###Legacy Code Hardening

* Very difficult to create unit-tests for existing code
* Easier to run program as a black box:

```
      setup input
      run program
      read output
      check output against expected result
```

<div class="fragment fade-in">
* Does not test correctness of code
* Checks code is a similarly wrong on day N as day 0
</div>
