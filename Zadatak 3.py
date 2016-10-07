
f1=open("acids.txt", "r") ## reading acids
ak=f1.readline()
f1.close()

bm=[] ## reading matrix
f1=open("blosum50.txt", "r")
for i in range(20):
    line=f1.readline()
    vc=line.split()
    bm.append(vc[:])
for i in range(20): ## integer matrix
    for j in range(20):
        bm[i][j]=int(bm[i][j])

x='HPEW'
y='PW'
print x, y
m=len(x)
n=len(y)
sm=[] ## score matrix
tmp=[]
for i in range(m+1):
    tmp.append(0)
for i in range(n+1):
    sm.append(tmp[:])
## rubni uvjeti
for i in range(n+1):
    sm[i][0]=-8*i
for i in range(m+1):
    sm[0][i]=-8*i
## rekurzija
for i in range(1,n+1):
    for j in range(1,m+1):
        tmp=[]
        tmp.append(sm[i-1][j]-8)
        tmp.append(sm[i][j-1]-8)
        bb=bm[ak.index(y[i-1])][ak.index(x[j-1])]
        tmp.append(sm[i-1][j-1]+bb)
        tmp.sort()
        sm[i][j]=tmp[2]
a=[]
b=[]
for i in range (m+n):
    a.append('0')
    b.append('0')
for i in range (m+n):
    if (sm[n][m]==sm[n][m-1]-8):
        a[i]=x[m-1]
        b[i]='_'
        m=m-1
    elif (sm[n][m]==sm[n-1][m]-8):
        a[i]='_'
        b[i]=y[n-1]
        n=n-1
    else:
        a[i]=x[m-1]
        b[i]=y[n-1]
        m=m-1
        n=n-1
    if (n==0 and m==0):
        break
du=len(a)
c=[]
d=[]
for i in range (du):
    if (a[du-i-1] != '0'):
        c.append(a[du-1-i])
for i in range (du):
    if (a[du-i-1] != '0'):
        d.append(b[du-i-1])
f2=open("poravnanje01.txt", "w")
for i in range (len(c)):
    f2.write(c[i])
f2.write('\n')
for i in range (len(d)):
    f2.write(d[i])
