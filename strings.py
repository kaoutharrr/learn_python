s = "abc"
s = 'abc'
print(s[0:2])

# but strings are immutable i cant reassign a value

s+="def"
# this creates a new striing
print(s)
# numeric strngs can be converted to numbers
print(int("123") + int("123"))

# and numbers can be converted to strings too
print(str(123) + str(123))

# if u need ascii of a chaar
print(ord('8'))
# we can join srings with a delimeter

strings = ["appah", "ok", "alright"]
print(strings)
print(" ".join(strings))