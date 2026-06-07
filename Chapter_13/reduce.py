from functools import reduce
a = [111,34,564,75,43,7,6909,675]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater ,a))