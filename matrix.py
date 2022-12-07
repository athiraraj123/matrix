m=int(input("Enter the number of rows: "))
n=int(input("Enter the number of cloumns : "))
last=m*n
test = list(range(1,last+1))
for i in range(1,len(test)):
    if i%3==0:
        if i==last:
            pass
        else:
            test[i-1],test[i]=test[i],test[i-1]
a=[]
b=[]
c=[]
for i in range(0,len(test)):
    if i%3==0:
        a.append(test[i])
    elif i%3==1:
        b.append(test[i])
    else:
        c.append(test[i])
print(a)
print(b)
print(c)