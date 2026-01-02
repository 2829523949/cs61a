def partial_reverse(start,s):
    length=len(s)-start
    if length%2==0:
        for i in range(length%2):
            s[start+i],s[len(s)-1-i]=s[len(s)-1-i],s[start+i]
            '这是合法的做法，注意，如果只赋值一个元素，另外一个对称元素并不会改变'
    else:
        for i in range((length-1)%2):
            s[start+i],s[len(s)-1-i]=s[len(s)-1-i],s[start+i]
    return None