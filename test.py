ban = True
for i in range(6,23):
    s = "%d:00 - %d:30"%(i,i)
    print(s)
    s = "%d:30 - %d:00"%(i, i+1)
    print(s)