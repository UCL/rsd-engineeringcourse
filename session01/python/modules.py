### 'FileImport'

import pretty

pretty.arrowify(james="RITS", matt="CMIC")

### 'ModuleVariable'

pretty.arrow="=>"
pretty.arrowify(beauty=True, cause="consequence")

### 'ImportFrom'

import math
math.sin(math.pi)

from math import sin
sin(math.pi)

from math import *
sin(pi)

### 'ImportAlias'

import math as m
m.cos(0)

mypi=3
from math import pi as realpi
sin(mypi)
sin(realpi)

### 'FolderModules'

import module1
module1.hello

import module1.module2
module1.module2.hello

### 'RelativeImport'
import module1.module3
module1.module3.hello
