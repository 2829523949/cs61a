def sevens(n,k):
    def has_sevens(x):
        if x%10==7:
            return True 
        elif x==0:
            return False
        else:
            return has_sevens(x//10)
    time=0
    direction=1
    def work(time,num):
        time=time+1
        if time==n:
            return num 
        elif direction==1:
            if time%7==o or has_sevens(time):
                direction=-1
                if num==1:
                    return work(time,k)
                else:
                    return work(time,num-1)
            elif num==k:
                return work(time,1)
            else:
                return work(time,num+1)
        else:
            if time%7==0 or has_sevens(time):
                direction=1
                if num==k:
                    return work(time,1)
                else:
                    return work(time,num+1)
            elif num==1:
                return work(time,k)
            else:
                return work(time,num+1)
    return work(time,1)