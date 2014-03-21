Building
========

Building
--------

Usually, the code you type in is not the code that runs.

The most usual example of this is converting source code to object files, and thence to executables:

``` bash
gcc hello_world.c
./a.out
```

``` bash
/usr/bin/c++
-I/Users/jamespjh/devel/rsdt/training/rsd-cppcourse-example/reactor/src
-I/usr/local/include
-I/Users/jamespjh/devel/rsdt/training/rsd-cppcourse-example/reactor/build/external/src/googletest/include
-o CMakeFiles/test_SolverTest.dir/SolverTest.cpp.o
-c /Users/jamespjh/devel/rsdt/training/rsd-cppcourse-example/reactor/test/SolverTest.cpp
...
/usr/bin/c++
-Wl,-search_paths_first
-Wl,-headerpad_max_install_names
CMakeFiles/test_SpeciesTest.dir/SpeciesTest.cpp.o  
-o test_SpeciesTest  
../external/src/googletest-build/libgtest.a
../src/libreactor_library.a
```

Analysis pipelines as a build process
-------------------------------------

However, we often do lots of other things which are conceptually like a build process:

```
wget updated_dataset.csv
python clean_data.py < updated_dataset.csv > cleaned.csv
sort cleaned.csv | uniq | sorted.csv
gnuplot make_plots.gnu
```

Publishing and reporting as a build process
-------------------------------------------

``` bash
python make_figures.py
latex mypaper.tex
bibtex
latex mypaper.tex
dvips mypaper.dvi
```

Metaprogramming
---------------

Another source of a build process is _Metaprogramming_:
writing a program which writes other programs.

#TODO: Write an example using mako.

Packaging, configuration and deployment
------------------------

Other activities which are similar to build processes,
in that they require management of a number of steps in a pipeline leading
to a final product, are:

* Packaging: Wrapping up your code into something easy for others to use
* Configuration: Setting up a server or development environment
* Deployment: Delivering your code to a server from where it will be used, run, or downloaded

We'll look at specialist tools for these particular pipelines later.

Build Tool History
==================

Build tools
-----------

Build tools define pipelines, specifying how each step leads on to the next.
When the tool is invoked, the whole pipeline is *not* rerun.
Instead, only the steps which are needed are carried out.
For example, if only one input file has changed, only steps whose results
depend on that file are rerun.

Tasks and prerequisites
-----------------------

We define a build process as a series of tasks, each of which has zero or more
prerequisites. Tasks are run only if the prerequisites are out of date.

Make
----

Make is the original build tool. It defines its own language for
tasks and prerequisites. You'll almost certainly encounter some Makefiles.
Make's system for determining which tasks are out of date and need to occur
is powerful and robust. However, the Make language is pretty horrible, and we
recommend against adopting it as a primary tool for new projects.

Tool-specific tasks
-------------------

The main disadvantage of `make` is that it is unaware of the specific semantics
of standard common build steps. For example, it is unable to guess that
a set of `.cpp` files are likely C++ source code. Each build step must be
explicitly given in terms of shell commands in every makefile.

Later build tools have support for common patterns of dependencies in many
languages, and do not need steps to be defined in terms of shell commands.

Cross-platform make files
-------------------------

Another big drawback of `make` is that makefiles written for it usually work only
on the machine of the person who wrote it. Locations, versions, and configuration options
for compilers, libraries and tools vary greatly between machines.
Some modern version control tools allow the investigation of machines, trying to
automatically determine the appropriate local configuration and react accordingly.

Make-file generators
--------------------

If you've ever installed anything on Linux, you've almost certainly used
`automake`, which interrogates the local environment, and generates an appropriate
makefile which should work for the local tools.

``` bash
./configure
make
make install
```

However, it is really quite hard to work with.

CMake
-----

CMake, one of the two leading modern research build tools,
builds on this concept to allow cross-platform builds, spitting out, for example,
make files for building on Linux, XCode files on mac, and Visual studio
project files on Windows.

The CMake DSL
-------------

CMake defines a language of it's own to describe build processes:

``` cmake
include_directories(src) # This location "src" is added to the list of locations
                         # which are searched when resolving #include statements
                         # in C/C++
add_subdirectory(src) # Look in the CMakeLists.txt file for explanation on how
                      # to build our library code
add_executable(reactor reactor.cpp) # The executable to make is
        # called "reactor" and depends on the listed source files and libraries
target_link_libraries(reactor reactor_library)
```

which looks fine enough... but...

Why CMake Why?
--------------

When you try to do something complicated in CMake it gets very ugly:

``` cmake
foreach(_file ${SOURCES})
  string(REPLACE "." "_" file_tro ${_file})
  set(file_tro "${file_tro}_tro")
  add_custom_command(
    OUTPUT ${file_tro}
    COMMAND perl ${CMAKE_CURRENT_SOURCE_DIR}/trans.pl
      ${CMAKE_CURRENT_SOURCE_DIR}/${_file} -o ${file_tro}
    DEPENDS ${_file}
  )
  list(APPEND trofiles ${file_tro})
endforeach()
```

Internal vs External DSLs
-------------------------

* DSL means Domain Specific Language
* An External DSL had its own grammar and syntax
* An Internal DSL looks superfically like it's own language...
* But is actually cleverly crafted code hiding a host language

Internal DSLs are best, because you can always use language libraries and
features you know, and it's one less syntax to learn

SCons
=====

SCons is secretly Python
------------------------

``` python
Program("TestModule1")
Program("TestModule2")
Program("TestModuel3")
```

``` python
for i in range(1,4):
  Program("TestModule"+i)
```

CMake vs SCons
--------------

CMake advantages:

* More powerful library-hunting
* Better support for HPC
* Builds project files for use in IDEs like XCode and Visual Studio
* Built in support for downloading "external projects"
* Existing in build tool for many research projects

SCons advantages:

* _Much_ easier to write custom builders for data pipelines
* Easier to learn (just python)

Scons C++ build worked example
------------------------------

* [Code without a builder](https://github.com/UCL/rsd-cppcourse-example/tree/no_build_system)
* [My solution](https://github.com/UCL/rsd-cppcourse-example/compare/no_build_system...scons)

Scons pipeline worked example
-----------------------------

* [Pipeline just as a script](http://github.com/jamespjh/greengraph/fragments)
* [Pipeline as a single python program](http://github.com/jamespjh/greengraph/)
* [Pipeline with SCons](http://github.com/jamespjh/greengraph/scons)

Generated source files
----------------------

You should include the date or current revision control number in
source code.

In SCons, just create an appropriate command builder:

```python
def header_template():
  return """
  #define DATE {date}
  #define REVISION {revision}
  """.format(
    date=str(datetime.datetime.now()),
    revision=os.popen("git rev-parse HEAD").read()
  )
Command('header.h',None,header_template)
```

Generated Source (CMake)
------------------------

In CMake there's direct support for including
information from the build in source files:

``` cmake
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )
```
``` cpp
#define Tutorial_VERSION_MAJOR @Tutorial_VERSION_MAJOR@
#define Tutorial_VERSION_MINOR @Tutorial_VERSION_MINOR@
```

Installers
----------

```
env.Install('/usr/bin',program)

env.Install('/usr/local/include', Glob('src/*.h'))

my_library=SharedLibrary(reactor,Glob('src/*.cpp'))
env.Install('/usr/local/lib',my_library)
```

Command line arguments
----------------------

``` python
AddOption('--prefix',
          dest='prefix',
          type='string',
          nargs=1,
          action='store',
          metavar='DIR',
          help='installation prefix')

env = Environment(PREFIX = GetOption('prefix'))

installed = env.Install('$PREFIX/bin', myprogram)
Alias('install',installed)
```
``` bash
scons install --prefix=~ # No need to sudo
```

Platform Dependent Builds
=========================

Platform dependent code
--------------

We often want to do different things to build our code on different platforms:

```
assert( (!isnan(localTau)) ); # Wrong namespace on compile on some platforms
```

It is tempting to write:

``` cpp
#ifdef OSX # Or whatever
  assert( (!std::isnan(localTau)) );
#else
  assert( (!std::isnan(localTau)) );
#endif
```

But this will only work on platforms you've tested, and will break if things change.

Testing your compiler
---------------------

Instead, have your build tool try out a fragment of code, and define accordingly:

``` python

def check_isnan(context):
    context.Message('Checking for std::isnan... ')
    result = context.TryCompile("""
    #include <cmath>
    int main(int, char**){return std::isnan(0);}
    """, '.cpp')
    context.Result(result)
    return result

conf = Configure(env, config_h="config.h",
    custom_tests = { 'Isnan' : check_isnan })
if conf.Isnan():
    conf.Define("HAVE_STD_ISNAN")
env = conf.Finish()
```

```cpp
#ifdef HAVE_STD_ISNAN
  assert( (!std::isnan(localTau)) );
#else
  assert( (!isnan(localTau)) );
#endif
```
