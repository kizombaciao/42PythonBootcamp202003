def func(n):
    return n%2 == 0

def ft_filter(function_to_apply, list_of_inputs):
    tt1 = [n for n in list_of_inputs if function_to_apply(n)]
    return tt1

nums = range(5)
t1 = filter(lambda n: n%2 == 0, nums)
print(t1)

t2 = ft_filter(func, nums)
print(t2)

t3 = filter(func, nums)
print(t3)
# note, that filter does not return T or F but the corresponding data !