def locker(x,y):
    locker=[False]*x
    for i in range (1,y+1):
        for k in range (i,x+1,i):
            locker[k-1] = not locker[k-1]
    return locker.count(True)
