from functools import reduce

def func(x, y):
    return x + y

def ft_reduce(function_to_apply, list_of_inputs):
    res = function_to_apply(list_of_inputs[0], list_of_inputs[1])
    for i in list_of_inputs[2:]:
        res = function_to_apply(res, i)
    return res

nums = range(5)
print(nums)

t1 = reduce(lambda x, y: x + y, nums)
print(t1)

t2 = ft_reduce(func, nums)
print(t2)
