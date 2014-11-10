## Introduction

### "variables"

bananas=0
apples=0
oranges=0
bananas+=1
apples+=1
oranges+=1

### "constant"

initial_fruit_count=0
bananas=initial_fruit_count
apples=initial_fruit_count
oranges=initial_fruit_count

### "toclass"

class Basket:
    def __init__(self):
        self.count=0
    def buy(self):
        self.count+=1

bananas=Basket()
apples=Basket()
oranges=Basket()
bananas.buy()
apples.buy()
oranges.buy()

### "loop"

baskets=[bananas, apples, oranges]
for basket in baskets: basket.buy()

### "newerror"
from nose.tools import assert_raises
with assert_raises(NameError):
    baskets=[bananas, apples, oranges, kiwis]



### "names"
basket_names=['bananas', 'apples', 'oranges', 'kiwis']

globals()['apples']



### "globals"

for name in basket_names:
    globals()[name]=Basket()


print kiwis.count

### "dictionary"

baskets={}
for name in basket_names:
    baskets[name]=Basket()
print baskets['kiwis'].count

### "comprehension"

baskets={name:Basket() for name in baskets}
print baskets['kiwis'].count

## Functional Programming

### "add"

def add(a,b):
    return a+b

add(5,6)


### "addfive"

def add_five(a):
    return a+5
add_five(6)

### "funcgen"

def generate_five_adder():
    def _add_five(a):
        return a+5
    return _add_five

coolfunction = generate_five_adder()
coolfunction(7)

### "thirty"

def thirty_function():
    def times_three(a):
        return a*3
    def add_seven(a):
        return a+7
    return times_three(add_seven(3))

thirty_function()

### "scope"
with assert_raises(NameError):
    add_seven



### "call"

print thirty_function
x=[thirty_function, add_five, add]

for fun in x:
    print fun

### "deferred"

def deferred_greeting():
    def greet():
        print "Hello"
    return greet
friendlyfunction=deferred_greeting()

# Do something else
print "Just passing the time..."

# OK, Go!
friendlyfunction()



### "curry"

def define_adder(increment):
    def adder(a):
        return a+increment
    return adder

add_3=define_adder(3)

add_3(9)

### "rename"

add = define_adder

### "currying"

add(8)(5)

### "closure"

name = "James"
def greet():
    print "Hello, ", name

greet()

### "late"

name="Matt"

greet()

### "comprehension"

numbers=range(10)

[add_five(i) for i in numbers]

### "map"

map(add_five, numbers)

### "accumulate"

def mean(data):
    sum=0.0
    for x in data:
        sum+=x
    return sum/len(data)

mean(range(10))

import sys
def my_max(data):
    # Start with the smallest possible number
    highest=sys.float_info.min
    for x in data:
        if x>highest:
            highest=x
    return highest

my_max([2,5,10,-11,-5])

### "accum_generalise"

def accumulate(initial, operation, data):
    accumulator=initial
    for x in data:
        accumulator=operation(accumulator, x)
    return accumulator


def my_sum(data):
    def _add(a,b):
        return a+b
    return accumulate(0, _add, data)

print my_sum(range(5))

def bigger(a,b):
    if b>a:
        return b
    return a

def my_max(data):
    return accumulate(sys.float_info.min, bigger, data)

print my_max([2,5,10,-11,-5])

### "reduce"

from functools import reduce

def my_max(data):
    return reduce(bigger,data,sys.float_info.min)

my_max([2,5,10,-11,-5])

### "lambda"

def most_Cs_in_any_sequence(sequences):
    def count_Cs(sequence):
        return sequence.count('C')
    counts=map(count_Cs, sequences)
    return max(counts)

def most_Gs_in_any_sequence(sequences):
    return max(map(lambda sequence: sequence.count('G'),sequences))

data=[
    "CGTA",
    "CGGGTAAACG",
    "GATTACA"
]
most_Gs_in_any_sequence(data)



### "lambda_same"

func_name=lambda a,b,c : a+b+c

def func_name(a,b,c):
    a+b+c



### "lambda_closure"

def most_of_given_base_in_any_sequence(sequences, base):
    return max(map(lambda sequence: sequence.count(base), sequences))

most_of_given_base_in_any_sequence(data,'A')


### "pretty_max"

def my_max(data): return reduce(lambda a,b: a if a>b else b, data, sys.float_info.min)

my_max([2,5,10,-11,-5])




### "funcalgo"

from scipy.optimize import newton
from numpy import linspace, zeros
from matplotlib import pyplot as plt
solve_me=lambda x: x**2-x

print newton(solve_me, 2), newton(solve_me,0.2)

xs=linspace(-1,2,50)
plt.plot(xs,map(solve_me,xs),xs,zeros(50))

### derivative

def derivative(func, eps):
    def _func_derived(x):
        return (func(x+eps)-func(x))/eps
    return _func_derived

plt.plot(xs,map(solve_me,xs),xs,map(derivative(solve_me,0.01),xs))

newton(derivative(solve_me,0.01),0)

### "stdlib"

import scipy.misc

def derivative(func):
    def _func_derived(x):
        return scipy.misc.derivative(solve_me,x)
    return _func_derived

newton(derivative(solve_me),0)

## Iterators


### "iterable"

for key in baskets:
    print key.upper()

### "range"

print range(10)

total=0
for x in range(int(1e6)): total+= x
print total



### "xrange"

print xrange(3)

a=iter(xrange(3))

print a

print a.next()

print a.next()

print a.next()
with assert_raises(StopIteration):
    print a.next()

total=0
for x in xrange(int(1e6)): total+= x
print total

### "iteritems"

print baskets.items()

print baskets.iteritems()

### "iterator_protocol "

class fib_iterator(object):
    def __init__(self, limit, seed1=1, seed2=1):
        self.limit=limit
        self.previous=seed1
        self.current=seed2
    def __iter__(self):
        return self
    def next(self):
        self.previous, self.current=self.current, self.previous+self.current
        self.limit -=1
        if self.limit<0: raise StopIteration() # This will be explained in a few slides!
        return self.current

x=fib_iterator(5)

x.next()

x.next()

x.next()

x.next()

for x in fib_iterator(5):
    print x

sum(fib_iterator(5))

### "iterable_protocol"

from numpy import array
class MyImage(object):
    def __init__(self, pixels):
        self.pixels=array(pixels,dtype='uint8')
        self.channels=self.pixels.shape[2]
    def __iter__(self):
        # return an iterator over the pixels
        # See future NumPy lecture for using reshape
        return iter(self.pixels.reshape(-1,self.channels))
    def show(self):
        plt.imshow(self.pixels, interpolation="None")

x=[[[255,255,0],[0,255,0]],[[0,0,255],[255,255,255]]]
image=MyImage(x)

image.show()

print image.channels

from webcolors import rgb_to_name
for pixel in image:
    print rgb_to_name(pixel)

## Generators


### "generator"

def my_generator():
    yield 5
    yield 10

x=my_generator()
print x.next()
print x.next()
with assert_raises(StopIteration):
    print x.next()

### "fib_generator"

def yield_fibs(limit, seed1=1,seed2=1):
    current=seed1
    previous=seed2
    while limit>0:
        limit-=1
        current, previous = current+previous, current
        yield current
print sum(yield_fibs(5))

plt.plot(list(yield_fibs(20)))

## Exceptions


### "divzero"
with assert_raises(ZeroDivisionError):
    1/0

### "hierarchy"

import inspect
inspect.getmro(ZeroDivisionError)

### "typerror"
x=1
with assert_raises(TypeError):
    for y in x: print y

inspect.getmro(TypeError)

### "custom"

class MyCustomErrorType(Exception):
    pass

with assert_raises(MyCustomErrorType):
    raise(MyCustomErrorType("Problem"))

### "customdata"

class MyCustomErrorType(Exception):
    def __init__(self, category=None):
        self.category=category
    def __str__(self):
        return "Error, cateory " + str(self. category)

with assert_raises(MyCustomErrorType):
    raise(MyCustomErrorType(404))

### "handling"

import yaml
try:
    config=yaml.load(open("datasource.yaml"))
    user=config["userid"]
    password=config["password"]
except IOError:
    user="anonymous"
    password=None
print user

### "omnicatch"

try:
    config=yaml.lod(open("datasource.yaml"))
    user=config["userid"]
    password=config["password"]
except:
    user="anonymous"
    password=None
print user

### "threereads"
with open('datasource2.yaml','w') as outfile:
    outfile.write('userid: jamespjh\n')
    outfile.write('password: secret\n')

with open('datasource3.yaml','w') as outfile:
    outfile.write('user: jamespjh\n')
    outfile.write('password: secret\n')

def read_credentials(source):
    try:
       datasource=open(source)
       config=yaml.load(datasource)
       user=config["userid"]
       password=config["password"]
       datasource.close()
    except IOError:
       user="anonymous"
       password=None
    return user, password

print read_credentials('datasource2.yaml')

print read_credentials('datasource.yaml')

with assert_raises(KeyError):
    print read_credentials('datasource3.yaml')

### "finally"

def read_credentials(source):
    try:
       datasource=open(source)
       config=yaml.load(datasource)
       user=config["userid"]
       password=config["password"]
    except IOError:
       user="anonymous"
       password=None
    finally:
        datasource.close()
    return user, password


### "tryelse"

def read_credentials(source):
    try:
       datasource=open(source)
    except IOError:
       user="anonymous"
       password=None
    else:
       config=yaml.load(datasource)
       user=config["userid"]
       password=config["password"]
    finally:
        datasource.close()
    return user, password



### "stackexample"

def f4(x):
    if x==0:
        return
    if x==1:
        raise ArithmeticError()
    if x==2:
        raise SyntaxError()
    if x==3:
        raise TypeError()

def f3(x):
    try:
        print "F3Before"
        f4(x)
        print "F3After"
    except ArithmeticError:
        print "F3Except"

def f2(x):
    try:
        print "F2Before"
        f3(x)
        print "F2After"
    except SyntaxError:
        print "F2Except"

def f1(x):
    try:
        print "F1Before"
        f2(x)
        print "F1After"
    except TypeError:
        print "F1Except"

print "Example 0"
f1(0)

print "Example 1"
f1(1)

print "Example 2"
f1(2)

print "Example 3"
f1(3)

### "typecheck"

import yaml
def analysis(source):
    if type(source)==dict:
        name=source['modelname']
    else:
        content=open(source)
        source=yaml.load(content)
        name=source['modelname']
    print name

analysis({'modelname':'Super'})

with open('example.yaml','w') as outfile:
    outfile.write('modelname: brilliant\n')

analysis('example.yaml')

### "duckexception"

def analysis(source):
    try:
      name=source['modelname']
    except TypeError:
      content=open(source)
      source=yaml.load(content)
      name=source['modelname']
    print name

analysis('example.yaml')

### "duckextension"

def analysis(source):
    try:
      name=source['modelname']
    except TypeError:
      # Source was not a dictionary-like object
      # Maybe it is a file path
      try:
        content=open(source)
        source=yaml.load(content)
        name=source['modelname']
      except IOError:
        # Maybe it was already raw YAML content
        source=yaml.load(source)
        name=source['modelname']
    print name

analysis("modelname: Amazing")

### "rethrow"

try:
    # Something
    pass
except:
    # Do this code here if anything goes wrong
    raise

## Context managers


### "context"

with open('example.yaml') as foo:
    print yaml.load(foo)

### "context_protocol"

class verbose_context():
    def __init__(self, name):
        self.name=name
    def __enter__(self):
        print "Get ready, ", self.name
    def __exit__(self, exc_type, exc_value, traceback):
        print "OK, done"

with verbose_context("James"):
    print "Doing it!"

### "context_generator"

from contextlib import contextmanager

@contextmanager
def verbose_context(name):
    print "Get ready for action, ", name
    yield name.upper()
    print "You did it"

with verbose_context("James") as shouty:
    print "Doing it, ",  shouty

## Decorators

### "repeater"

def repeater(func, count):
    def _repeated(x):
        counter=count
        while counter>0:
            counter-=1
            x=func(x)
        return x
    return _repeated

from math import sqrt

fiftyroots=repeater(sqrt,50)

print fiftyroots(100)

### "resetrequired"

def reset_required(func):
    def _with_data_save(self, *args):
        func(self,*args)
        self.stored_data.append(self.data)
    return _with_data_save

class SomeClass(object):
    def __init__(self):
        self.data=[]
        self.stored_data=[]

    def _step1(self, ins):
        self.data=[x*2 for x in ins]

    step1=reset_required(_step1)

x=SomeClass()

x.step1("Hello")
print x.data

x.step1("World")
print x.data

print x.stored_data

### "resetdecorator"

def reset_required(func):
    def _with_data_save(self, *args):
        func(self,*args)
        self.stored_data.append(self.data)
    return _with_data_save

class SomeClass(object):
    def __init__(self):
        self.data=[]
        self.stored_data=[]
        
    @reset_required
    def step1(self, ins):
        self.data=[x*2 for x in ins]

x=SomeClass()
x.step1("Hello")
x.step1("World")
print x.stored_data

## Testing and functional programming.


### "test_generator"

def assert_examplar(**fixture):
    answer=fixture.pop('answer')
    assert_equal(greet(**fixture), answer)

def test_greeter():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','samples.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        for fixture in fixtures:
            yield assert_exemplar(**fixture)

### "assertraises"

@contextmanager
def my_assert_raises(exception):
    try:
        yield
    except exception:
        pass
    else:
        raise Exception("Expected,", exception, " to be raised, nothing was.")

### "decorate_raises"

from nose.tools import raises

@raises(TypeError, ValueError)
def test_raises_type_error():
    raise TypeError("This test passes")

@raises(Exception)
def test_that_fails_by_passing():
    pass

test_raises_type_error()

with assert_raises(AssertionError):
    test_that_fails_by_passing()

### "my_decorate_raises"

def my_raises(func, exception):
    def _output(*args):
        with assert_raises(exception):
            func(*args)
    return _output


## Metaprogramming class attributes



### "setattr"

class Boring(object): pass

x=Boring()

x.name="James"

print x.name

print x.__dict__

print getattr(x,'name')

setattr(x,'age',38)

print x.age

### "metamember"

setattr(Boring, 'describe', lambda self: self.name+ " is "+str(self.age))


print x.describe(), x.describe, Boring.describe

### "modclass"

y=Boring()
with assert_raises(AttributeError):
    y.describe()

### "newclassmethod"

def broken_birth_year(self):
    import datetime
    current=datetime.datetime.now().year
    return current-self.age

Boring.birth_year=broken_birth_year

print x.birth_year()

print x.birth_year

print broken_birth_year.__name__

### "locals"

class Person(object):
    def __init__(self, name, age, job, children_count):
        for name,value in locals().iteritems():
            if name=='self': continue
            print "Setting self.", name, " to ", value 
            setattr(self, name, value)

me=Person("James", 38, "Scientific Programmer", 0)

print me.name

### "dontMP"

class Person(object):
    def __init__(self, name, age, job, children_count):
       self.name=name
       self.age=age
       self.job=job
       self.children_count=children_count





## Operator overloading


### "algebra1"

class Term(object):
    def __init__(self, symbols=[], powers=[], coefficient=1):
        self.coefficient=coefficient
        self.data={symbol: exponent for symbol,exponent in zip(symbols, powers)}

class Expression(object):
    def __init__(self, terms):
        self.terms=terms



### "algebra2"

first=Term(['x','y'],[2,1],5)
second=Term(['x'],[1],7)
third=Term([],[],2)
result=Expression([first, second, third])


### "Polyconstruct"

class Term(object):
    def __init__(self, *args):
        lead=args[0]
        if type(lead)==type(self):
            # Copy constructor
            self.data=dict(lead.data)
            self.coefficient=lead.coefficient
        elif type(lead)==int:
            self.from_constant(lead)
        elif type(lead)==str:
            self.from_symbol(*args)
        elif type(lead)==dict:
            self.from_dictionary(*args)
        else:
            self.from_lists(*args)
    def from_constant(self, constant):
        self.coefficient=constant
        self.data={}
    def from_symbol(self, symbol, coefficient=1, power=1):
        self.coefficient=coefficient
        self.data={symbol:power}
    def from_dictionary(self, data, coefficient=1):
        self.data=data
        self.coefficient=coefficient
    def from_lists(self, symbols=[], powers=[], coefficient=1):
        self.coefficient=coefficient
        self.data={symbol: exponent for symbol,exponent in zip(symbols, powers)}
### "OperatorFunctions"
    def add(self, *others):
        return Expression((self,)+others)
    def multiply(self, *others):
        result_data=dict(self.data)
        result_coeff=self.coefficient
        # Convert arguments to Terms first if they are constants or integers
        others=map(Term,others)
        for another in others:
            for symbol, exponent in another.data.iteritems():
                if symbol in result_data:
                    result_data[symbol]+=another.data[symbol]
                else:
                    result_data[symbol]=another.data[symbol]
            result_coeff*=another.coefficient
        return Term(result_data,result_coeff)
### Overloads    
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.multiply(other)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __radd__(self, other):
        return self.__add__(other)
### StringOverload    
    def __str__(self):
        def symbol_string(symbol, power):
            if power==1:
                return symbol
            else:
                return symbol+'^'+str(power)
        symbol_strings=[symbol_string(symbol, power) for symbol, power in self.data.iteritems()]
        prod='*'.join(symbol_strings)
        if not prod:
            return str(self.coefficient)
        if self.coefficient==1:
            return prod
        else:
            return str(self.coefficient)+'*'+prod

### ExpressionConstruct

class Expression(object):
    def __init__(self, terms=[]):
        self.terms=list(terms)
### ExpressionFunctions
    def add(self, *others):
        result=Expression(self.terms)
        for another in others:
            if type(another)==Term:
                result.terms.append(another)
            else:
                result.terms+=another.terms
        return result
### ExpressionOverloads
    def multiply(self, another):
        # Distributive law left as exercise
        pass
    def __add__(self, other):
        return self.add(other)
    def __radd__(self, other):
        return self.__add__(other)
### ExpressionStringOverload
    def __str__(self):
        return '+'.join(map(str,self.terms))



### "withfunc"

x=Term('x')
y=Term('y')

first=Term(5).multiply(Term('x'),Term('x'),Term('y'))
second=Term(7).multiply(Term('x'))
third=Term(2)
expr=first.add(second,third)

### "withop"

x_plus_y=Term('x')+'y'
print x_plus_y.terms[0].data

five_x_ysq=Term('x')*5*'y'*'y'
print five_x_ysq.data, five_x_ysq.coefficient

### "RightUse"

print 5*Term('x')

### "HardTest"

fivex=5*Term('x')
print fivex.data, fivex.coefficient

### "UseString"

first=Term(5)*'x'*'x'*'y'
second=Term(7)*'x'
third=Term(2)
expr=first+second+third
print expr

### "Callable"

class MyCallable(object):
    def __call__(self, name):
        print "Hello, ", name

x=MyCallable()

x("James")

### "591"

from IPython.display import YouTubeVideo
YouTubeVideo('2Op3QLzMgSY')

