---
title: Testing
---

##Testing

###A few reasons not to do testing

<div class="reveal constrastTable">
  ------------------------------------      -------------------------------------
  Sensibility                               Sense
  ------------------------------------      -------------------------------------
  **It's boring**                           *Maybe*

  **Code is just a one off throwaway**      *As with most research codes*

  **No time for it**                        *A bit more code, a lot less debugging*

  **Tests can be buggy too**                *See above*

  **Not a professional programmer**         *See above*

  **Will do it later**                      *See above*
  ------------------------------------      -------------------------------------
</div>


###A few reasons to do testing

<div class="reveal happy">
  * **lazyness** *testing saves time*
  * **peace of mind** *tests (should) ensures code is correct*
  * **runnable specification** *best way to let others know what a function should do and
    not do*
  * **reproducible debugging** *debugging that happened and is saved for later reuse*
  * code structure / **modularity** *since the code is designed for at least two situations*
  * easier to modify *since results can be tested*
</div>


###Not a panacea

> Trying to improve the quality of software by doing more testing is like trying to lose weight by
> weighting yourself more often.

|                               - Steve McConnell

<div class="fragment roll-in">
 * Testing won't corrrect a buggy code
 * Testing will tell you were the bugs are...
 * ... if the test cases *cover* the bugs
</div>
