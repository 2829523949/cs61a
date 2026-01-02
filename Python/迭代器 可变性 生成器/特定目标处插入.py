def insert_element(s,before,after):
    for i in range(len(s)):
        if s[i]==before:
            s.insert(i+1,after)
            s[i+2]=insert_element(s[i+2:],before,after)
    return s     