arr = [1] * 5
print(arr)
print(len(arr))

# output : [1, 1, 1, 1, 1]  5 

arr[-1] = 7
print(arr)

# -1 index is the last case
arr[-2] = 2
print(arr)
print(arr[-2])
# the second last value s 2 now [1, 1, 1, 2, 7]


#sublists :
print(arr[1:3])
print(arr[0:7])
# output [1, 1]   [1, 1, 1, 2, 7]


# unpacking
a,b,c = [1,2,3]

print(a, b, c)

# using index

nums = [1,2,3]
for i in range (len(nums)):
    print(i)

# no index
for n in nums :
    print(n)

# if u need index and value
for i, n in enumerate(nums):
    print(i, n)

# loop through multiple arrays simultaneously
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2) :
    print(n1, n2)

# reverse
nums = [1, 2 ,3]
nums.reverse()
print(nums)


