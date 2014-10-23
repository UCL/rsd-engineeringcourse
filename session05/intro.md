---
title: Construction
---

##Coding Conventions

###One code, many layouts:

Consider the following fragment of C++

``` cpp
reactor::Species & reactor::ReactionSystem::NewSpecies(const std::string &name){
	species.push_back(new Species(name));
	return *species.back();
}
```

This could also have been written:

``` cpp
using namespace std;

namespace reactor
{

 species & reactionsystem::new_species(const string& a_Name)
 {

  species.push_back( new species( name ));
  return *(species.back());

 }
}
```

###So many choices

* Layout
* Naming
* Syntax choices

###Layout

```cpp
declaration {
   contents
}
```

vs

```cpp
declaration
{
	contents
}
```

###Layout choices

* Brace style
* Line length
* Indentation
* Whitespace/Tabs

###Nameing Conventions

``` cpp
ClassName
methodName
variable_name
```

vs

```cpp
ClassName
method_name
l_local_variable
m_instance_variable
s_class_variable
```

###Hungarian Notation

Prefix denotes *type*:

``` c
lAnInteger
lpAPointer
szAString
rwAMatrixRow
```

###Newlines

* Newlines make code easier to read
* Newlines make less code fit on a screen

Use newlines to describe your code's *rhythm*

###Syntax Choices

``` cpp
if ((variable==anothervariable++)&&flag1||flag2) do_something;
```

vs

``` cpp
anothervariable++;
bool const variable_equality = variable == anothervariable;
if ((variable_equality && flag1) || flag2) {
   do_something;
}
```

###Syntax choices

* Compound statements
* Explicit operator precedence
* Compound controlled statements
* Namespace choices

###Coding Conventions

You should try to have an agreed policy for your team for these matters.

If your language sponsor has a standard policy, use that.

E.g. [Python PEP8](http://legacy.python.org/dev/peps/pep-0008/)

E.g. [Google's guide for R](https://google-styleguide.googlecode.com/svn/trunk/Rguide.xml)

E.g. [Google's style guide for C++](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml)

###Lint

There are automated tools which enforce coding conventions and check for common mistakes.

These are called *linters*

E.g. [pep8](https://pypi.python.org/pypi/pep8)

``` bash
easy_install pep8
$ pep8 --first optparse.py
optparse.py:69:11: E401 multiple imports on one line
optparse.py:77:1: E302 expected 2 blank lines, found 1
optparse.py:88:5: E301 expected 1 blank line, found 0
optparse.py:222:34: W602 deprecated form of raising exception
optparse.py:347:31: E211 whitespace before '('
optparse.py:357:17: E201 whitespace after '{'
optparse.py:472:29: E221 multiple spaces before operator
optparse.py:544:21: W601 .has_key() is deprecated, use 'in'
```
