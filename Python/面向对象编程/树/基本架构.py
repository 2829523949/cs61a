class Tree:
    empty=[]
    def __init__(self,label,branches=empty):
        self.label=label
        for branch in branches:
            assert isinstance(branch,Tree)
        self.branch=list[branch]
        '注意，因为branch都要求类型是Tree，因此创建的时候不能直接使用列表，而要创造Tree实例，这点在面向对象编程中一直出现'
    
    def is_leaf(self):
        return not isinstance(self.branches,Tree)
    
    def __str__(self):
        '事实上，也可以设置内置函数后把结果赋值给string然后在外层函数返回string，避免变量名混乱'
        gap=''
        string=str(self.label)
        def recursive(self):
            nonlocal gap,string 
            gap=gap+' '
            for branch in self.branches:
                string=string+'\n'+gap+str(branch.label)
                recursive(branch)
            return string 
        return recursive(self)
    
    def __repr__(self):
        if not self.branches:
            return'Tree('+str(self.label)+')'
        else:
            the_rest=','.join(repr(branch) for branch in self.branches)
            return 'Tree({1},{2})'.format(self.label,the_rest)
        '注意，使用format时，后续的填充可以不使用字符串形式，会自动调用str/repr'

    def height(self):
        if self.is_leaf:
            return 1
        else:
            return 1+max([branch.height for branch in self.branches])
        '注意，max只接收一个可迭代对象，要写成([])的形式'

def fib(n):
    if n==0 or n==1:
        return Tree(n)
    else:
        label=fib(n-1).label+fib(n-2).label
        return Tree(label,[fib(n-1),fib(n-2)])
    
'编写一个名为 cumulative_mul 的函数，该函数会修改树 t，将每个节点的标签替换为该节点及其所有子节点标签的乘积。'
def cumulative_mul(t):
    def get_label(x):
        return [x.label]+[get_label(branch) for branch in x.branches]
    for label in get_label(t):
        t.label=t.label*label 
    for branch in t.branches:
        cumulative_mul(branch)