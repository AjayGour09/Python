def divisibe5(n):
    if(n%5==0):
        return True
    return False
a = [10,854,3245,15,98542135,8797,36,85,125]
f = list(filter(divisibe5 ,a))
print(f)