# tuples are similar than arrays
tup=(1,2,3)
print(tup)

# they are immutable, we can index them but we can't modify them
print("this is tup[0] : {}".format(tup[0]))

# can be used as keys for a hashmap
my_map = {(1, 2) : "Ok"}
print(my_map)

# for sets too
my_set = set((1,2,3))
print(my_set)
# lists can't be keys cuz theyre not hashable
# hashable means:Hashable means an object has a fixed hash value,
#  meaning its hash (hash(obj)) remains the same throughout its lifetime. 
# Hashable objects must be immutable (unchangeable) 
# and implement __hash__() and __eq__() methods.

# Hashing is the process of converting data into a 
# fixed-size numerical value (a "hash") using a hash 
# function. The same input always produces the same hash,
#  but even a small change in the input results in a completely different hash.

# Why is hashing useful?
# Fast lookups: Hash-based structures like dictionaries (dict) and sets
#  (set) use hashes to quickly find values.
# Data integrity: Hashing can verify data integrity (e.g., checksums, cryptographic hashes).
# Uniqueness: Hash functions help in creating unique identifiers for data.