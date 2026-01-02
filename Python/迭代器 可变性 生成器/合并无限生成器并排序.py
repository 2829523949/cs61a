def merge(a,b):
    'a和b为两个无限迭代器，merge(a,b)返回一个生成器，按照大小顺序将a,b中的对象排列'
    start_a=next(a)
    start_b=next(b)
    def judge(current_a,current_b):
        if current_a>current_b:
            yield current_b
            current_b=next(b)
        else:
            yield current_a
            current_a=next(a)
        yield from judge(current_a,current_b)
    yield from judge(start_a,start_b)
'while True是处理的一个好方式，不能因为有递归或者for就抛弃while'
def merge(a,b):
    current_a=next(a)
    current_b=next(b)
    while True:
        if current_a<current_b:
            yield current_a
            current_a=next(a)
        else:
            yield current_b
            current_b=next(b)