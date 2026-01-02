def sevens(n,k):
    time=0
    def has_seven(n):
        if n%10==7:
            return True 
        elif n==0:
            return False  
        else: 
            return has_seven(n//10)
    def range(a,b):
        nonlocal time 
        time=time+1
        if time==n:
            return b 
        elif a%7==0 or has_seven(a):
            if b==1:
                return anti_range(a+1,k)
            else:
                return anti_range(a+1,b-1)
        elif b==k:
            return range(a+1,1)
        else:
            return range(a+1,b+1)
    def anti_range(a,b):
        nonlocal time 
        time=time+1
        if time==n:
            return b 
        elif a%7==0 or has_seven(a):
            if b==7:
                return range(a+1,1)
            else:
                return range(a+1,b+1)
        elif b==1:
            return anti_range(a+1,k)
        else:
            return anti_range(a+1,b-1)
    return range(1,1)