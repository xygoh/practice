def areSimilar(a,b):
    if len(a) != len(b):
        return False
    if sorted(a) != sorted(b):
        return False
    c=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            c+=1
        if c>2:
            return False
    return True
        
