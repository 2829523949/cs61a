def hailstone(n):
    '这是一个无限冰雹生成器'
    yield n 
    if n==1:
        yield from hailstone(1)
    else:
        if n%2==0:
            yield from hailstone(n/2)
        else:
            yield from hailstone(3*n+1)
