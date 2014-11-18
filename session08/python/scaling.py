### "Imports"
import numpy as np
from timeit import repeat
from matplotlib import pyplot as plt
### "TimeAppendToList"
counts=np.arange(1,100000,10000)
def time_append_to_list(count):
    return repeat('before.append(0)','before=[0]*'+str(count),number=10000)
plt.plot(counts,map(time_append_to_list,counts))
plt.ylim(ymin=0)
### "SaveAppendToList"
plt.savefig('AppendToList.png')
plt.figure()
### "TimeAppendToArray"
def time_append_to_ndarray(count):
    return repeat('np.append(before,[0])','import numpy as np; before=np.ndarray('+str(count)+')',number=10000)
plt.plot(counts,map(time_append_to_ndarray,counts))
plt.ylim(ymin=0)
### "SaveAppendToArray"
plt.savefig('AppendToArray.png')
plt.figure()
### "TimeLookupInArray"
def time_lookup_middle_element_in_ndarray(count):
    before=np.ndarray(count)
    def totime():
        x=before[count/2]
    return repeat(totime,number=10000)
plt.plot(counts,map(time_lookup_middle_element_in_ndarray,counts))
plt.ylim(ymin=0)
### "SaveLookupInArray"
plt.savefig('LookupArray.png')
plt.figure()
### "TimeLookupInList"
def time_lookup_middle_element_in_list(count):
    before=[0]*count
    def totime():
        x=before[count/2]
    return repeat(totime,number=10000)
plt.plot(counts,map(time_lookup_middle_element_in_list,counts))
plt.ylim(ymin=0)
### "SaveLookupInArray"
plt.savefig('LookupList.png')
plt.figure()
### "TimeInsertToList"
def time_insert_to_list(count):
    return repeat('before[0:0]=[0]','before=[0]*'+str(count),number=10000)
plt.plot(counts,map(time_insert_to_list,counts))
plt.ylim(ymin=0)
### "SaveLookupInArray"
plt.savefig('InsertList.png')
plt.figure()
### "TimeInsertDeque"
from collections import deque
def time_insert_to_deque(count):
    return repeat('before.appendleft(0)','from collections import deque; before=deque([0]*'+str(count)+')',number=10000)
plt.plot(counts,map(time_insert_to_deque,counts))
plt.ylim(ymin=0)
### "SaveInsertDeque"
plt.savefig('InsertDeque.png')
plt.figure()
### "TimeLookupDeque"
def time_lookup_middle_element_in_deque(count):
    before=deque([0]*count)
    def totime():
        x=before[count/2]
    return repeat(totime,number=10000)
plt.plot(counts,map(time_lookup_middle_element_in_deque,counts))
plt.ylim(ymin=0)
### "SaveLookupDeque"
plt.savefig('LookupDeque.png')
plt.figure()
### "Dict"
me=[["Name","James"],["Job","Programmer"],["Home","London"]]
me_dict=dict(me)
print me_dict["Job"]
### "EvilDict"
class evildict(object):
    def __init__(self,data):
        self.data=data
    def __getitem__(self,akey):
        for key,value in self.data:
            if key==akey:
                return value
        raise KeyError()
me_evil=evildict(me)
print me_evil["Job"]
### "SortedDict"
class sorteddict(object):
    def __init__(self,data):
        self.data=sorted(data,key=lambda x:x[0])
        self.keys=map(lambda x:x[0],self.data)
    def __getitem__(self,akey):
        from bisect import bisect_left
        loc=bisect_left(self.keys,akey)
        if loc!=len(self.data):
            return self.data[loc][1]
        raise KeyError()
me_sorted=sorteddict(me)
print me_sorted["Job"]
### "SetupTimeDicts"
def time_dict_generic(ttype,count,number=10000):
    from random import randrange
    keys=range(count)
    values=[0]*count
    data=ttype(zip(keys,values))
    def totime():
        x=data[keys[count/2]]
    return repeat(totime,number=10000)
time_dict=lambda count: time_dict_generic(dict,count)
time_sorted=lambda count: time_dict_generic(sorteddict,count)
time_evil=lambda count: time_dict_generic(evildict,count)
counts=np.arange(1,1000,100)
### "TimeDict"
plt.plot(counts,map(time_dict,counts))
plt.ylim(ymin=0)
### "SaveTimeDict"
plt.savefig('TimeDict.png')
plt.figure()
### "TimeEvil"
plt.plot(counts,map(time_evil,counts))
plt.ylim(ymin=0)
### "SaveTimeEvil"
plt.savefig('TimeEvil.png')
plt.figure()
### "TimeSorted"
plt.plot(counts,map(time_sorted,counts))
plt.ylim(ymin=0)
### "SaveTimeSorted"
plt.savefig('TimeSorted.png')
plt.figure()

