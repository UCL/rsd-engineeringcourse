### "Starting"
import numpy
data=numpy.loadtxt(fname='../data/inflammation-01.csv', delimiter=',')
print data

### "Types1"
print type(data)
print data.shape

### "Types2"
print [type("Hello"),type(1), type([1,2,3])]

### "Slicing"
print 'first value in data:', data[0, 0] #Top left element
print data[0:4, 0:10] # Top left few elements
print data[:3, 36:] #First three lines, last few columns
print data[:-1,:] #All but the last line, all columns

### "Methods"
print data.mean() # 6.14875
print data.std() # 4.613
patient_zero=data[0, :]
print 'maximum inflammation for patient 0:', patient_0.max()
print 'maximum inflammation for patient 2:', data[2, :].max()

### "Axes"
print data.mean(axis=1) # Average over days, per patient
print data.mean(axis=0) # Average over patients, per day

