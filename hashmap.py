# aka dictionnary

my_map = {}

my_map["keyyy"] = "value"
my_map["keyy"] = 9
print(my_map)
# we cant have duplicates keyy
my_mao = {"alice" : 90, "bob ": 85}
print(my_mao)


# dict comprehension 
mapp = { i : i for i in range(5)}
print(mapp)


# loopig through maps
for key in my_map :
    print(key, my_map[key])

for val in my_mao.values() :
    print(val)

for key, val in my_mao.items() :
    print(key, val)

