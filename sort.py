# sorting
arr = [12, 4,5,9,7,8,0,0,3,3,2,1,4]
print("before sorting : {}".format(arr))
arr.sort()
print("after sorting : {}".format(arr))

# sorting in reverse
arr.sort(reverse=True)
print("after reverse sorting : {}".format(arr))

# we can sort strings too by default we will have alphabetical order

names = ["alice", 'katewwwwww', "boeeeb", "cat"]
names.sort()
print(names)

# customizng sort
#           by length of string for example
# lamda is a function without a name

names.sort(key=lambda x: len(x))

print(names)