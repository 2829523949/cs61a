def diffenerces(t):
    first=next(t)
    second=next(t)
    while second:
        yield second-first
        first=second
        second=next(t)
        '抛出StopIteration会停止但是不会报错，list不会显示，不影响'
        