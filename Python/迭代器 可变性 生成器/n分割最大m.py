def division(n,m):
    '这是分割n的最大值不超过m的显示的生成器表达'
    'yield from可以对生成器使用也可以对任意可迭代对象使用'
    if m>0 and n>0:
        if n==m:
            "这一步与后两步是并列的，用于补充在n-m=0时，实际上有表达但是会因为n'=n-m=0被筛掉的问题"
            yield str(n)
        for element in division(n-m,m):
            yield element+"+"+"m"
        for element in divison(n,m):
            yield element 
