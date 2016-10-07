f=open("niz.txt", "r")
y=f.readline()
y=y.rstrip()
f.close()
x=[]
for i in range (len(y)):
    x.append(int(y[i]))

print x

f1=open("kocke_e.txt", "r")
p=f1.readline()
p=p.split()
for i in range (len(p)):
    p[i]=float(p[i])
n=f1.readline()
n=n.split()
for i in range (len(n)):
    n[i]=float(n[i])
f1.close()

a=[]
f1=open("kocke_t.txt", "r")
for i in range (2):
    tmp=f1.readline()
    tmp=tmp.split()
    for j in range (2):
        tmp[j]=float(tmp[j])
    a.append(tmp)


print p
print n
print a

def maxi (a,b):
    if(a>=b):
        return a
    else:
        return b

s=[]
polje=[]
tmp=[]

for j in range (2):
    tmp=[]
    for i in range (len(x)):
        tmp.append(0)
    polje.append(tmp)


polje[0][0]=p[x[0]-1]
polje[1][0]=n[x[0]-1]

for i in range (1,len(x)):
    polje[0][i]=maxi(polje[0][i-1]*0.9*p[x[i]-1],polje[1][i-1]*0.1*p[x[i]-1])
    polje[1][i]=maxi(polje[0][i-1]*0.2*n[x[i]-1],polje[1][i-1]*0.8*n[x[i]-1])
    
print maxi(polje[0][len(x)-1], polje[1][len(x)-1])

print polje

def rek (u, v):
    if(v==0):
        return
    elif(u==0):
        s.append('f')
        if(polje[0][v-1]*0.9*p[x[v]-1]>polje[1][v-1]*0.1*p[x[v]-1]):
            rek(0,v-1)
        else:
            rek(1,v-1)
    else:
        s.append('l')
        if(polje[0][v-1]*0.2*n[x[v]-1]>polje[1][v-1]*0.8*n[x[v]-1]):
            rek(0,v-1)
        else:
            rek(1,v-1)


if(polje[0][len(x)-1]>polje[1][len(x)-1]):
    
    rek(0,len(x)-1)
else:
    rek(1,len(x)-1)

if(p[x[0]-1]>n[x[0]-1]):
    s.append('f')
else:
    s.append('l')

s.reverse()
print s
        
