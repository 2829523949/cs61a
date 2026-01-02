def branches(t):
    return t[1:]
def is_leaf(t):
    if type(t)!=[]:
        return False 
    elif len(t)!=1:
        return False
    else:
        return True
def label(t):
    return t[0]
def is_tree(t):
    if type(t)!=[] or len(t)<1:
        return False 
    else:
        for branch in branches(t):
            is_tree(branch)
    return True 
def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label]+[branches]
def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(branch) for branch in branches(t)])
def fib_tree(n):
    if n==0 or n==1:
        return [n]
    else:
        label=label(fib_tree(n-1))+label(fib_tree(n-2))
        branches=[fib_tree(n-1),fib_tree(n-2)]
    return tree(label,branches)
def print_tree(t,blank=0):
    print(''*blank+'t')
    for branch in branches(t):
        print_tree(branch,blank)+1
def print_division(n,m):
    if m==0:
        return [False]
    elif n<0:
        return [False]
    elif n==0:
        return [True]
    else:
        left=print_division(n-m,m)
        right=print_division(n,m-1)
        return [m,list(left),list(right)]
def print_parts(n,container=""):
    if is_leaf(n):
        if container=="":
            print("n")
        else:
            print(container+"+"+"n")
    else:
        left,right=n[1],n[2]
        if container!="":
            print_parts(left,container+"+"+"label(left)")
        else:
            print_parts(left,container+"label(left)")
        print_parts(right,container)
def two_tree(sample_list):
    assert len(sample_list)>=2 and type(sample_list)==[]
    if len(sample_list)==2:
        return sample_list
    else:
        return [label(sample_list),[two_tree(sample_list)[1:]]]
def reversed_tree(t):
    t=list(reversed(t))
    if len(t)==1:
        return t
    else:
        for branch in t[:-1]:
            reversed_tree(branch)
    return t
def deep_map(s,f):
    "这是一个针对列表和给定函数的函数"
    for i in range(len(s)):
        if type(s[i])!=list:
            s[i]=f(s[i])
        else:
            deep_map(s[i],f)
        return None 
def sprout_leaves(t,leaves):
    for branch in branches(t):
        if is_leaf(branch):
            for i in range(len(leaves)):
                branch[i+1]=leaves[i]
        else:
            sprout_leaves(branch,leaves)
    return t 