#def function_to_appy(lst):
#    t1 = [n * n for n in lst]
#    return t1

def func(n):
    return n * n * n

def ft_map(function_to_apply, list_of_inputs):
    t1 = [function_to_apply(n) for n in list_of_inputs]
    return t1

nums = range(5)
t1 = map(lambda n: n * n, nums)
print(t1)

t2 = map(func, nums)
print(t2)

t3 = ft_map(func, nums)
print(t3)

#t2 = function_to_appy(nums)
#print(t2)

