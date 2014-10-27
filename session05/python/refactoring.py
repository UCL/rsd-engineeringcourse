### "setup"
from mock import Mock
Mock.__sub__=Mock()
Mock.__abs__=Mock()
chromosome=None
start_codon=None
x=None
y=None
subsequence=Mock()
transcribe=Mock()
ribe=Mock()
find=Mock()
hawk=Mock()
starling=Mock()
can_see=Mock()
my_name=""
your_name=""
flag1=False
flag2=False
start=0.0
end=1.0
step=0.1
birds=[Mock()]*2
import numpy as np
import math
import yaml
import os
### "magic_before"
data= [math.sin(x) for x in np.arange(0,3.141,3.141/100)]
result= [0]*100
for i in range(100):
    for j in range(i+1, 100):
        result[j] += data[i] * data[i-j] / 100
### "magic_after"
resolution=100
pi=3.141
data= [math.sin(x) for x in np.arange(0,pi,pi/resolution)]
result= [0]*resolution
for i in range(resolution):
    for j in range(i + 1, resolution):
        result[j] += data[i] * data[i-j] / resolution
### "function_before"
if abs(hawk.facing-starling.facing)<hawk.viewport:
    hawk.hunting()

if abs(starling.facing-hawk.facing)<starling.viewport:
    starling.flee()
### "function_after"
def can_see(source,target):
    return (source.facing-target.facing)<source.viewport

if can_see(hawk,starling):
    hawk.hunting()

if can_see(starling,hawk):
    starling.flee()

### "names_before"
z=find(x,y)
if z:
    ribe(x)

### "names_after"
gene = subsequence(chromosome, start_codon)
if gene:
    transcribe(gene)

### "temporary_before"
if ((my_name==your_name) and flag1 or flag2): do_something()
### "temporary_after"
same_names= (my_name==your_name)
flags_OK=flag1 or flag2
if same_names and flags_OK: do_something()
### "iterator_before"
sum=0
for i in range(resolution):
    sum+=data[i]	

### "iterator_after"
sum=0
for value in data:
    sum+=value

### "library_before"
xcoords=[start+i*step for i in range(int((end-start)/step))]
### "library_after"
import numpy as np
xcoords=np.arange(start,end,step)
### "arrays"
def can_see(index,source_angles,target_angles,source_viewports):
    return abs(source_angles[i]-target_angles[i])<source_viewports[i]

### "structures"
def can_see(source,target):
    return (source["facing"]-target["facing"])<source["viewport"]

### "config_before"
flight_speed=2.0 # mph
bounds=[0,0,100,100]
turning_circle=3.0 # m
bird_counts= {"hawk": 5, "starling": 500}
### "config_after"
config=yaml.load(open("config.yaml"))

### "globals"
viewport=pi/4
if hawk.can_see(starling):
    hawk.hunt(starling)

class Hawk(object):
    def can_see(self,target):
        return (self.facing-target.facing)<viewport

### "arguments"
viewport=pi/4
if hawk.can_see(starling,viewport):
    hawk.hunt(starling)

class Hawk(object):
    def can_see(self,target,viewport):
        return (self.facing-target.facing)<viewport

### "loops"
for bird in birds:
    bird.build_nest()

for bird in birds:
    bird.lay_eggs()

### "merged"
for bird in birds:
    bird.build_nest()
    bird.lay_eggs()

### "subroutine_before"
def do_calculation():
    for predator in predators:
        for prey in preys:
            if predator.can_see(prey):
                predator.hunt(prey)
            if predator.can_reach(prey):
                predator.eat(prey)

### "subroutine_after"
def do_calculation():
    for predator in predators:
        for prey in preys:
            predate(predator, prey)

def predate(predator,prey):
    if predator.can_see(prey):
        predator.hunt(prey)
    if predator.can_reach(prey):
        predator.eat(prey)

### "files_before"
class One(object):
    pass


class Two(object):
    def __init__():
        self.child=One()

### "files_after"
from anotherfile import One

class Two(object):
    def __init__():
        self.child=One()
