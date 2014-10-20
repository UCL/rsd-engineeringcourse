### "Function"

def double(x):
  return x*2

print double(5), double([5]), double('five')

### "SideEffect"

def double_inplace(vec):
    vec[:]=[element*2 for element in vec]

z=range(4)
double_inplace(z)
print z

### "EarlyReturn"

def extend(to,vec,pad):
    if len(vec)>=to:
        return
    else:
        vec[:]=vec+[pad]*(to-len(vec))

x=range(3)
extend(6,x,'a')
print x

### "UnpackingArguments"

def arrow(before, after):
    return str(before)+" -> "+str(after)

x=[1,-1]
print arrow(*x)

### "UnpackingPower"

charges={"neutron": 0, "proton": 1, "electron": -1}
for particle in charges.items():
    print arrow(*particle)

### "SequenceArguments"

def doubler(*sequence):
    return [x*2 for x in sequence]

print doubler(1,2,3)

### "KeywordArguments"

def arrowify(**args):
    for key, value in args.items():
        print key+"->"+value

arrowify(neutron="n",proton="p",electron="e")


