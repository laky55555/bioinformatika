x=[]
for i in range (6):
 x.append (i+1)
x.append(6)
x.append(6)
a='ffffflll'
f1=open("kocke_e.txt", "r")
p=f1.readline()
p=p.rsplit()
for i in range (len(p)):
    p[i]=float(p[i])
n=f1.readline()
n=n.rsplit()
for i in range (len(n)):
    n[i]=float(n[i])
f1.close()

b=[]
f1=open("kocke_t.txt", "r")
for i in range (2):
    tmp=f1.readline()
    tmp=tmp.rsplit()
    for j in range (2):
        tmp[j]=float(tmp[j])
    b.append(tmp)
v=1
print len(x)
print len(a)
print b

for i in range (len(x)):
    if(i==0):
        if(a[0]=='f'):
            v=p[x[0]-1]
        else:
            v=n[x[0]-1]
    else:
        if(a[i-1]=='f' and a[i]=='f'):
            v=v*b[0][0]*p[x[i]-1]
        elif(a[i-1]=='f' and a[i]=='l'):
            v=v*b[0][1]*n[x[i]-1]
        elif (a[i-1]=='l' and a[i]=='f'):
            v=v*b[1][0]*p[x[i]-1]
        else:
            v=v*b[1][1]*n[x[i]-1]
