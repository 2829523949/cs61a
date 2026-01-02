def label(t):
    return t[0]
def branches(t):
    return [branch for branch in t[1:]]
def yield_path(t,value):
    '生成从树根到特定value值的路径的生成器，每个元素都是路径上标签的集合'
    total=[]
    if label(t)==value:
        yield[[value]]
    else:
        for branch in branches(t):
            for path in yield_path(branch,value):
                '注意，这里是label(t)而不是label(branch)否则会漏掉树根的标签，反之并不会漏掉branch的标签（从第二个开始思考）'
                yield [label(t)]+path 
     