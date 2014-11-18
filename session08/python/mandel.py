### "TrivialMandel"

def trivial_mandel(position,limit=50):
    value=position
    while abs(value)<2:
        limit-=1
        value=value**2+position
        if limit<0:
            return 0
    return limit

### "ResolutionDefine"

xmin=-1.5
ymin=-1.0
xmax=0.5
ymax=1.0
resolution=300
xstep=(xmax-xmin)/resolution
ystep=(ymax-ymin)/resolution
xs=[(xmin+(xmax-xmin)*i/resolution) for i in range(resolution)]
ys=[(ymin+(ymax-ymin)*i/resolution) for i in range(resolution)]

### "Imports"

import matplotlib.pyplot as plt
import numpy as np
from nose.tools import assert_raises
import time
### "GenerateTrivial"

trivial_data=[[
    trivial_mandel(complex(x,y))
    for x in xs] 
    for y in ys]

### "PlotTrivial"

plt.imshow(trivial_data,interpolation='none')

### "SaveTrivial"

plt.savefig('mandel.png')
plt.figure()

### "NumpyMandel"

def numpy_mandel(position,limit=50):
    value=position
    diverged_at_count=np.zeros(position.shape)
    while limit>0:
        limit-=1
        value=value**2+position
        diverging=value*np.conj(value)>4
        first_diverged_this_time=np.logical_and(diverging,
                diverged_at_count==0)
        diverged_at_count[first_diverged_this_time]=limit
        value[diverging]=2
    return diverged_at_count

### "NumpyGrid"

ymatrix,xmatrix=np.mgrid[ymin:ymax:ystep,xmin:xmax:xstep]
values=xmatrix+1j*ymatrix

### "GenerateNumpy"

numpy_data=numpy_mandel(values)

### "PlotNumpy"

plt.imshow(numpy_data,interpolation='none')

### "NumpyResidual"

sum(sum(abs(numpy_data-trivial_data)))

### "AppendMandel"

append_data=[]
for y in ys:
    row=[]
    for x in xs:
        row.append(trivial_mandel(complex(x,y)))
    append_data.append(row)

### "PreAllocMandel"

pre_alloc_data=[[0 for i in range(resolution)] 
        for j in range(resolution)]
for j,y in enumerate(ys):
    for i,x in enumerate(xs):
        pre_alloc_data[j][i]=trivial_mandel(complex(x,y))

### "FuncMandel"

func_data=[]
for y in ys:
    bind_mandel=lambda x: trivial_mandel(complex(x,y))
    func_data.append(map(bind_mandel,xs))

### "Zeros"

np.zeros([3,4,2])
### "NDArray"
np.ndarray([2,2,2],dtype='int')
### "FromList"
x=np.array(xrange(5))
print x
### "SingleType"
np.array([1,1.0,'one'])
### "Elementwise"
x*2
### "ElementwiseMultiply"
x*x
### "VectorizedFunction"
np.sqrt(x)
### "Linspace"
np.linspace(0,10,21)
### "Arange"
np.arange(0,10,0.5)
### "Mgrid"
ymatrix,xmatrix=np.mgrid[ymin:ymax:ystep,xmin:xmax:xstep]
print xmatrix
print ymatrix
### "ComplexCoordinate"
values=xmatrix+1j*ymatrix
print values
### "ArraywiseAlgorithms"
z0=values
z1=z0*z0+values
z2=z1*z1+values
z3=z2*z2+values
print z3
### "ArraywiseBranching"
with assert_raises(ValueError):
    trivial_mandel(values)
### "VectorizeMetafunction"
vectorized_mandel=np.vectorize(trivial_mandel)
### "GenerateVectorized"
vectorized_data=vectorized_mandel(values)
### "Exploding"
def exploding_mandel(position,limit=50):
    value=position
    while limit>0:
        limit-=1
        value=value**2+position
        diverging=abs(value)>2
    return abs(value)<2
### "GenerateExploding"
exploding_data=exploding_mandel(values)
### "Flat"
def flat_mandel(position,limit=50):
    value=position
    while limit>0:
        limit-=1
        value=value**2+position
        diverging=abs(value)>2
        # Avoid overflow
        value[diverging]=2
    return abs(value)<2
### "GenerateFlat"
flat_data=flat_mandel(values)
### "LogicalArray"
diverging=abs(z3)>2
print diverging[30]
### "ArraywiseCompare"
x=np.arange(10)
y=np.ones([10])*5
z=x>y
print z
### "LogicalIndexing"
x[z]
### "ArraywiseBooleanOperators"
x[np.logical_not(z)]
### "LogicalAssignment"
x[z]=5
print x
### "Broadcasting"
print x>5
### "BroadcastOuterProduct"
row=np.array([[1,2,3]])
column=np.array([[0],[2],[4]])
print row.shape
print column.shape
print row*column
### "Residual"
sum(sum(abs(vectorized_data-numpy_data)))
### "ResidualList"
with assert_raises(TypeError):
    trivial_data-append_data

sum(sum(abs(np.array(trivial_data)-np.array(append_data))**2))
### "NumpyTesting"
x = [1e-5, 1e-3, 1e-1]
y = np.arccos(np.cos(x))
np.testing.assert_allclose(x, y, rtol=1e-5, atol=0)
### "VectorisedResidual"
np.testing.assert_allclose(vectorized_data, numpy_data)
### "Mask"
def mask_mandel(position,limit=50):
    value=np.zeros(position.shape)+position
    calculating=np.ones(position.shape,dtype='bool')
    diverged_at_count=np.zeros(position.shape)
    while limit>0:
        limit-=1
        value[calculating]=value[calculating
                ]**2+position[calculating]
        diverging_now=np.zeros(position.shape,dtype='bool')
        diverging_now[calculating]=value[calculating
                ]*np.conj(value[calculating])>4
        calculating=np.logical_and(calculating,
                np.logical_not(diverging_now))
        diverged_at_count[diverging_now]=limit
    return diverged_at_count
### "GenerateMask"
mask_data=mask_mandel(values)
### "Reshape"
x=np.arange(64)
y=x.reshape([8,8])
print y
### "ArrayIndexing"
y[[0,2]]
### "ArrayIndexing2"
y[[0,2],[1,2]]
### "ColonIndexing"
y[:,[0,2]]
### "Reshape2"
z=x.reshape([4,4,4])
print z
### "MixedIndexing"
z[:,[1,3],0:3]
### "Newaxis"
z[:,np.newaxis,[1,3],0].shape
### "View"
a=z[:,1:3,2]
a[0,0]=-100
print z
### "Ellipsis"
z[...,1]
### "Filter"
def filter_mandel(position,limit=50):
    positions=np.zeros(position.shape)+position
    value=np.zeros(position.shape)+position
    indices=np.mgrid[0:values.shape[0],0:values.shape[1]]
    diverged_at_count=np.zeros(position.shape)
    while limit>0:
        limit-=1
        value=value**2+positions
        diverging_now=value*np.conj(value)>4
        diverging_now_indices=indices[:,diverging_now]
        carry_on=np.logical_not(diverging_now)
        value=value[carry_on]
        indices=indices[:,carry_on]
        positions=positions[carry_on]
        diverged_at_count[diverging_now_indices[0,:],
                diverging_now_indices[1,:]]=limit
    return diverged_at_count
### "GenerateFilter"
filter_data=filter_mandel(values)
