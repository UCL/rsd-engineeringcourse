---
title: Recap and Worked Answers
---

## Recap

### Python

Our first session looked at the basics of programming in Python, covering data types, control and flow, functions, and modules. We also set up our tools for future work, including Python, IPython Notebook, Git, and Github.

### Collaboration

Our second session reviewed the elements of collaborative programming, looking at version control with Git, the importance of clear licensing, and approaches to managing software issues. Together we identified and fixed errors in a repository on GitHub.

### Testing

Tests save time, improve code quality, and give peace of mind. In the testing session, we learnt how to incorporate tests using frameworks like Nose, reviewed mocking and debugging, and discussed test-driven development. Our exercise was to apply this new knowledge to a Monte-Carlo algorithm.

### Libraries

Libraries make us powerful. In this session we demonstrated how existing libraries could help us to find and download a map from the web and measure the density of green space. Our exercise focused on packaging code to make it easy to share and reuse.

### Construction

Construction is about we use letters and symbols to build readable, meaningful software. Our session covered: 

* conventions of layout and syntax
* how to write comments and documentation
* progressive improvement of code with refactoring
* refactoring code with classes

Our exercise put this knowledge into practice by refactoring 'Bad Boids', some intentionally-bad code that mimicked the motion of a flock of birds

### Design

Deliberate design can help us to complete complex software projects, repeatably and reliably. We looked at: 

* design in object oriented programming
* Unified Modelling Language for communicating design
* design patterns
* processes, such as Agile, in the context of design

We applied the newly-gained knowledge to refactor our (now Good!) Boids code with elements of inheritance, polymorphism, and pattern design. The new code was then visualised in Unified Modelling Language.

### DRY programming tricks

Unnecessary code is a home for unnecessary mistakes, so **d**on't **r**epeat **y**ourself. This session explored techniques for refactoring away repetitive code, and introduced the concepts of functional programming, exception handling, decorators, and operator overloading. Our exercise was to write a library to handle quantities with units, creating an opportunity to apply some of these concepts.

### Performance programming

Profiling allows us to spot and address performance issues with our code. The session on performance programming showed: 

* how the NumPy library can be used to carry out faster array-wise operations
* looked at the implications of data type on performance
* introduced the Big O notation
* demonstrated the speed benefits of Cython

Returning to the Boids code for our exercise, we sought to reimplement the model with NumPy and Cython to make it run as fast as possible.

### Further Git

Mastering Git opens up a powerful set of tools for collaborative programming. In this session we took a more in depth look at Git, reviewing features such as branching and tagging, looking at the process of merging code in more detail, and showing how Git can be used to publish a website.



