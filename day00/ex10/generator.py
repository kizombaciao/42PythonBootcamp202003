

def sqnum(nums):
    res = []
    for i in nums:
        res.append(i*i)
    return res

def sqnum2(nums):
    for i in nums:
        yield (i*i) ################

mynum = sqnum([1,2,3,4,5])

mynum2 = sqnum2([1,2,3,4,5])

print(mynum)

for num in mynum2:
    print(num, end=' ')
print()

