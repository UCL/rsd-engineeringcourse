---
title: Methodology
---

##Test Driven Development

###Test-driven development

![Developing with TDD: Write test, see it fail](session03/figures/tdd)


###Behavior Driven Development

<div align="left">
BDD

:    * Plain English description of scenario
     * Communicates behavior of code, rather than how code works
     * Simple enough for thesis director to understand
     * Translated to code internally by developer
</div>

``` ruby
Scenario: eat 5 out of 12
  Given there are 12 cucumbers
  When I eat 5 cucumbers
  Then I should have 7 cucumbers
```
