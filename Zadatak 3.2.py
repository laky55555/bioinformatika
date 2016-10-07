
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
f1.close()
x=''
y=''
f1=open("nizovi.txt", "r")
x=f1.readline()
x=x.rstrip()
y=f1.readline()
y=y.rstrip()
f1.close()
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
print 'Score poravnanja je', sm[n][m]
for i in range (m+n):
    if (sm[n][m]==sm[n][m-1]-8):
        a.append(x[m-1])
        b.append('_')
        m=m-1
    elif (sm[n][m]==sm[n-1][m]-8):
        a.append('_')
        b.append(y[n-1])
        n=n-1
    else:
        a.append(x[m-1])
        b.append(y[n-1])
        m=m-1
        n=n-1
    if (n==0 and m==0):
        break
a.reverse()
b.reverse()
f2=open("poravnanje01.txt", "w")
for i in range (len(a)):
    f2.write(a[i])
f2.write('\n')
for i in range (len(b)):
    f2.write(b[i])
