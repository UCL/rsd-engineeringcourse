### "If"

x = 5
if x < 0:
    print "x is negative"
elif x == 0:
    print "x is zero"
else:
    print "x is positive"

### "Comparison"

1 > 2
"UCL" > "KCL"
True == "True"
False == 0
'1' < 2

### "Indentation"

if x>0:
print x

### "EmptyIndent"

if x>0:
    # print x
print "Hello"

### "Pass"

if x>0:
    pass
print "Hello"

### 'Iteration'

uptofive = range(5)
for value in uptofive:
    print value**2

### 'Sequence'

vowels="aeiou"
sarcasm = []
for letter in "Okay":
    if letter.lower() in vowels:
        repetition = 3
    else:
        repetition = 1
    sarcasm.append(letter*repetition)

print "".join(sarcasm)

### 'DictionaryIteration'

import datetime
now = datetime.datetime.now()
founded = {"James": 1976, "UCL": 1826, "Cambridge": 1209}
current_year = now.year
for thing in founded:
    print thing, " is ", current_year -  founded[thing], "years old."

### 'UnpackingIteration'

triples=[[1,2,3], [3,4,5]]
for triple in triples:
    print triple

for first, second, third in triples:
    print second, first, third

### 'Items'

print founded.items()

for thing, year in founded.items():
    print thing, " is ", current_year - year, "years old."

### 'Break'

for n in range(50):
    if n==20: break
    if n % 2 == 0:
        continue
    print n

### 'ForElse'

search_in=range(50)
for x in search_in:
    if x<0:
        first_negative = x
        break
else:
    first_negative = False

print first_negative

### 'Comprehensions'

[2**x for x in range(10)]
"".join([x.upper() for x in "Whatever" if (x in vowels)])
{ (str(x))*3: x for x in range(3) }

### 'Zip'

negatives = zip(range(10), [-1.0*x for x in range(10)])
print negatives

neg_dict=dict(negatives)
print neg_dict[5]


