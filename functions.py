def myFunc(n, m):
    return n*m

print(myFunc(3, 4))


# nested functions have access to outer variables
def outer(a, b):
    c = "c"
    def inner():
        return a + b + c
    return inner()

print(outer('a', 'b'))


# can modufy objects but not reassign vales , unless 
# using nonlocal keyword

def double(arr, val):
    def helper():
        #  modifying arryas works
        for i , n in enumerate(arr):
            arr[i] *=2
        nonlocal val  # Allows modifying val in the enclosing scope
        val *=2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)