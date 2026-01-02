class Link:
    empty=()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first=first
        self.rest=rest 
    
    def __repr__(self):
        if not self.rest:
            return 'Link('+str(self.first)+')'
        else:
            return 'Link('+str(self.first)+','+f'{self.rest.repr}'+')'
            '注意，这里其实也可以直接写repr(self.rest)，会优先调用self.rest的实例方法repr而不是object的repr'
    
    def __str__(self):
        total='<'
        total=total+str(self.first)
        while self.rest!=():
            '注意用while和新的名称self进行递归，好好看好好学'
            '在实例函数内部重新定义一个名称self与原self无关，每次while都会调用当前帧的self名称，实现递归'
            self=self.rest
            total=total+' '+str(self.first)
        return total+'>'
        
    def range_link(start,end):
        assert end>=start+1
        if end==start+1:
            return Link(start)
        else:
            return Link(start,range(start+1,end))
        
    def map_link(func,orgin_link):
        assert type(orgin_link)==Link 
        if orgin_link.rest==Link.empty:
            return Link(func(orgin_link.first))
        else:
            rest=map_link(func,orgin_link.rest)
            return Link(func(orgin_link.first),rest)    

    def filter_link(filter_func,orgin_link):
        assert type(orgin_Link)==Link
        if not filter_func(orgin_link.first):
            if orgin_link.rest==Link.empty:
                return None
            else:
                return filter_link(filter_func,orgin_link.rest)
        else:
            return Link(orgin_link.first,filter_link(filter_func,orgin_link.rest))
        
def add_link(orgin_link,adder):
    '这是一个函数变异的实例，初始链表是一个递增的链表，将数字加入其中（如果没有相同的），然后返回一个仍然是递增顺序的链表'
    current_link=orgin_link
    if current_link.first>adder:
        orgin_link=Link(adder,orgin_link)
    else:
        while current_link.rest:
            if current_link.first<adder<current_link.rest.first:
                current_link.rest=Link(adder,current_link.rest)
            current_link=current_link.rest
        if current_link.first<adder:
            '注意，这里一个用current_link.first而不是直接current_link,与树区别，current_link仍然是一个Link实例'
            '同理，这里应该写Link(adder)而不是直接adder,current_link.rest仍然应该是一个Link实例'
            current_link.rest=Link(adder)
    return orgin_link 

def duplicate_link(s,val):
    "此函数会修改链表 s，将每个值为 val 的元素后都添加一个额外的 val (复制节点)。函数返回 None。"
    copy=s
    while copy.rest:
        if copy.first==val:
            copy.rest=Link(val,copy.rest)
        copy=copy.rest
    return None 

def strange_loop():
    '它不接受参数，返回一个Link对象s，满足s.rest.first.rest 就是 s。'
    s=Link(1,Link(0))
    s.rest.first=Link(0,s)
    return s 

'实现 sum_rec 和 sum_iter。每个函数都接收一个数字链表 s，并返回其元素的总和。'
'使用递归来实现 sum_rec。不要使用递归来实现 sum_iter；而是使用 while 循环。'
def sum_rec(s):
    if s.rest:
        return 0
    return s.first+sum_rec(s.rest)

def sum_iter(s):
    total=s.first
    current_link=s.rest
    while current_link:
        '注意，自定义类默认是True'
        total=total+current_link.first
        current_link=current_link.rest
    return total
 
'尝试对于一个链表返回按照大小从小到大排序的链表'
def sort(link):
    copy=[link.first]
    current=link.rest
    while current is not Link.empty:
        i=0
        while copy[i]<current.first and i<len(copy):
            i=i+1 
        if i<len(copy):
            copy=copy[:i]+[current.first]+copy[i:]
        else:
            copy=copy+[current.first]
        current=current.rest
    copy[0]=Link(copy[0])
    '这里要注意逻辑问题，先创建一个Link类的copy[0]然后才可以转给total(其实也可以不写赋值给total,最后直接给copy[o])'
    total=copy[0]
    i=1
    'Link的递归需要用rest进行，如果不需要返回最终列表，可以不用给标签，这里为了将赋值于返回值区分给了标签'
    'a=(可变对象)，如果再对a赋值只会再创建一个新的a，覆盖掉原来的a，如果要进行递归，需要对a的属性进行修改，这样原可变对象也会跟着改变'
    while i<len(copy):
        copy[i]=Link(copy[i])
        copy[i-1].rest=copy[i]
        i=i+1
    return total 
    '实际上，有更加简单的实现方式'
    'total=Link(copy[0])'
    'simulate=total'
    'for i in copy[1:]:'
    'simulate.rest=Link(i)'
    'simulate=simulate.rest'