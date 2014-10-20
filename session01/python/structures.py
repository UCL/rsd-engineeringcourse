### "Numerical"

one=1
ten=10
one_float=1.
ten_float=10.
print one/ten
tenth= one_float/ten_float
print type(one), type(one_float)
print type(one/ten), type(tenth)

### "String"

given = "James"
family = "Hetherington"
full = given+" "+family
print full.upper()

### "Coersion"

print float(str(ten)+str(one))

### "Array"

count_to_five = range(5)
various_things = [1, 2, "banana", 3.4, [1,2] ]
name = ["James", "Philip", "John", "Hetherington"]
print " ".join(name)

### "Sequence"

print count_to_five[1]
print full[3:-4]
print len(various_things)
print "John" in name
print count_to_five[0:2]*3

### "Mutable"

name[0] = "Dr"
name[2:3] = ["Griffiths-"]
name.append("PhD")
print " ".join(name)

### "Tuple"

my_tuple = ("Hello", "World")
my_tuple[0]="Goodbye"

### "Unpacking"

zero, one, two = range(3)
print one

### "Equality"

print "Hello" == "Hello"
print "Hello" is "Hello"
print [1] == [1]
print [1] is [1]

### "Memory"

x = range(3)
y = x
z = x[:]
y[1] = "Gotcha!"
z[2] = "Really?"
print x, y, z

### "Dictionary"

ages = {"James": 38, "Bilbo": 111, "Universe": 14e9}
print "James is "+ str(ages["James"]) + " years old"
print ages.values()
print ages.keys()
print "Bilbo" in ages
print "photon" in ages

### "ImmutableKeys"
good_match = {("Lamb", "Mint"): True, ("Bacon", "Chocolate"): False}
illegal = {[1,2]: 3}

### "Unordered"

my_dict = {}
for x in range(5):
  my_dict[str(x)] = x

print my_dict

### "Set"

unique_letters = set("".join(name))
print unique_letters
print "".join(sorted(unique_letters))
