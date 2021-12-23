a, b, c, d = [int(i)for i in input().split()]
tot = 0
pr = 0
while 1:
    if tot >= 2 and tot <= 10:
        if d >= b:
            d -= b
            tot += 1
        else:
            break
    if tot == 0 or tot == 1:
       if d >= a:
           d -= a
           tot += 1
        else:
            break
    if tot>10:
        if d>=c:
            d-=c
            tot+=1
        else:
            break

print(tot)