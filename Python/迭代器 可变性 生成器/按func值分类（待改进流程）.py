def group_the_same(s,fn):
    dic={}
    for element in s:
        if not fn(element) in [fn(established[0]) for established in dic]:
            dic[[element]]=fn(element) 
        else:
            for established in s.keys():
                if fn(established[0])==fn(element):
                    established.append(element)
    return dic        