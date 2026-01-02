def fib_all():
    start,second=1,1
    while True:
        yield start
        start=second 
        second=second+start 
next(filter(lambda x:x>2025,fib_all()))
'用迭代器运算快捷地实现了找到第一个大于2025的斐波拉契数'