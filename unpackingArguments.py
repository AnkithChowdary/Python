def multiply(*args):
    print(args)
    total=1
    for arg in args:
        total*=arg
    return total

def myadd(x,y):
    return x+y

def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total


def apply(*args,operator):
    # If we don't put * here then we are going to send tuple of tuples
    #
    if operator=="*":
        return multiply(*args) 
    elif operator=="+":
        return add(*args)
    else:
        return "No valid operator provided to apply()"

print(multiply(1,3,5))
nums=[3,4]
print(add(*nums))

nums1={"x":15,"y":25}
#It will pass each key as named argument
print(myadd(**nums1))
print(apply(1,2,3,4,operator="*"))

