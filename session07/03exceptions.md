---
title: Exceptions
---

## Exceptions

When we learned about testing, we saw that Python complains when things go wrong by raising an "Exception" naming a type of error:

{{pyfrag('07','all','divzero', check_errors=False)}}
Exceptions are objects, forming a class hierarchy. We just raised an instance
of the ZeroDivisionError class, making the program crash.

{{pyfrag('07','all','hierarchy')}}
So we can see that a zero division error is a particular kind of Arithmetic Error.

{{pyfrag('07','all','typerror')}}

When we were looking at testing, we saw that it is important for code to crash with a meaningful exception type when something is wrong.
We raise an Exception with `raise`. Often, we can look for an appropriate exception from the standard set to raise. 

However, we may want to define our own exceptions. Doing this is as simple as inheriting from Exception:

{{pyfrag('07','all','custom')}}
You can add custom data to your exception:

{{pyfrag('07','all','customdata')}}
The real power of exceptions comes, however, not in letting them crash the program, but in letting your program handle them. We say that an exception has been "thrown" and then "caught".

{{pyfrag('07','all','handling')}}
Note that we specify only the error we expect to happen and want to handle. Sometimes you see code that catches everything:

{{pyfrag('07','all','omnicatch')}}
There was a mistyped function name there, but we did not notice the error, as the generic except caught it. 
Therefore, we should catch only the error we want.

{{pyfrag('07','all','threereads')}}

This last code has a flaw: the file was successfully opened, the missing key was noticed, but not explicitly closed. It's normally OK, as python will close the file as soon as it notices there are no longer any references to datasource in memory, after the function exits. But this is not good practice, you should keep a file handle for as short a time as possible.

{{pyfrag('07','all','finally')}}

The `finally` clause is executed whether or not an exception occurs.

The last optional clause of a `try` statement, an `else` clause is called only if an exception is NOT raised. It can be a better place than the `try` clause to put code other than that which you expect to raise the error, and which you do not want to be executed if the error is raised. It is executed in the same circumstances as code put in the end of the `try` block, the only difference is that errors raised during the `else` clause are not caught. Don't worry if this seems useless to you; most languages implementations of try/except don't support such a clause.

{{pyfrag('07','all','tryelse')}}
Exceptions do not have to be caught close to the part of the program calling
them. They can be caught anywhere "above" the calling point in
the call stack: control can jump arbitrarily far in the program: up to the `except` clause of the "highest" containing try statement.

{{pyfrag('07','all','stackexample')}}

## Design with Exceptions

Now we know how exceptions work, we need to think about the design implications... How best to use them.

Traditional software design theory will tell you that they should only be used
to describe and recover from **exceptional** conditions: things going wrong.
Normal program flow shouldn't use them.

Python's designers take a different view: use of exceptions in normal flow is
considered OK. For example, all iterators raise a `StopIteration` exception to
indicate the iteration is complete.

A commonly recommended python design pattern is to use exceptions to determine
whether an object implments a protocol (concept/interface), rather than testing
on type.

For example, we might want a function which can be supplied *either* a data
series *or* a path to a location on disk where data can be found. We can
examine the type of the supplied content:

{{pyfrag('07','all','typecheck')}}

However, we can also use the try-it-and-handle-exceptions approach to this. 

{{pyfrag('07','all','duckexception')}}

This approach is more extensible, and **behaves properly if we give it some
other data-source which responds like a dictionary or string.**

{{pyfrag('07','all','duckextension')}}

Sometimes we want to catch an error, partially handle it, perhaps add some
extra data to the exception, and then re-raise to be caught again further up
the call stack. 

The keyword "`raise`" with no argument in an `except:` clause will cause the
caught error to be re-thrown. Doing this is the only circumstance where it is
safe to do except: without catching a specfic type of error.

{{pyfrag('07','all','rethrow')}}
It can be useful to catch and re-throw an error as you go up the chain, doing any clean-up needed for each layer of a program.

The error will finally be caught and not re-thrown only at a higher program
layer that knows how to recover. This is known as the "throw low catch high"
principle.

