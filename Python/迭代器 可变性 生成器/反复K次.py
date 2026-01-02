def repeated(t,k):
    container=[]
    def inside(t,k):
        nonlocal container 
        container=container+next(t)
        if len(container)>=k:
            for i in range(k-1):
                if container[len(container)-i-1]!=container[len(container)-i-2]:
                    inside(t,k)
            return container[-1]
        else:
            inside(t,k)
    return inside(t,k)