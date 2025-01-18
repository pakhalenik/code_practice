def rev_first(lst, num):
    firstn = lst[:num]
    rest = lst[num:]
    return firstn[::-1] + rest

def rev_last(lst, num):
    firstn = lst[:num]
    rest = lst[num:-num]
    lastn = lst[-num:]
    return firstn + rest + lastn[::-1]

num = 3
lst = [1, 2, 3, 4, 5,6]
result1 = rev_first(lst, num)
result2 = rev_last(lst, num)
print(result1)  # Output: [2, 1, 3, 4, 5]
print(result2)  # Output: [1, 2, 3, 5, 4]
