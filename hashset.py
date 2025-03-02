my_set = set()

my_set.add(1)
my_set.add(2)
print(my_set)

# there can't be ny duplicates in a set
print(len(my_set))

print(1 in my_set)
print(3 in my_set)
my_set.remove(2)

# list to set
my_set = set([1,3,5])
print(my_set)

# set comprehention

my_set = { i for i in range(5)}
print(my_set)