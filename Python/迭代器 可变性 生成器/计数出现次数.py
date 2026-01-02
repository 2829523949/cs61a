def count_occurrences(t,n,x):
    'next(迭代器)的返回值可以直接参与运算'
    if n==0:
        return 0
    if x==next(t):
        return 1+count_occurrences(t,n-1,x)
    else:
        return count_occurrences(t,n-1,x)