f1=open("acids.txt","r")
kiselina=f1.readline()
f1.close()

f1=open("blosum50.txt","r")
m=[]
for i in range (20):
    line=f1.readline()
    line=line.split()
    m.append(line[:])
f1.close()
for i in range (20):
    for j in range (20):
        m[i][j]=int(m[i][j])

f1=open("nizovi.txt", "r")
a=f1.readline()
b=f1.readline()
f1.close()
a=a.rstrip()
b=b.rstrip()

d_a=len(a)
d_b=len(b)

temp=[]
score=[]

for i in range (d_b+1):
        temp.append(0)

for i in range (d_a+1):
    score.append(temp[:])

for i in range (d_b+1):
    score[0][i]=-8*i
for i in range (d_a+1):
    score[i][0]=-8*i

niz1=[]
niz2=[]

for i in range (1,d_a+1):
    for j in range (1,d_b+1):
        temp=[]
        i1=kiselina.index(a[i-1])
        i2=kiselina.index(b[j-1])
        suma=m[i1][i2]
        temp.append(score[i-1][j-1]+suma)
        temp.append(score[i-1][j]-8)
        temp.append (score[i][j-1]-8)
        temp.sort()
        score[i][j]=temp[2]



def funkcija (i, j):
    if(i<0):
        return
    elif(j<0):
        return
    elif (i==0 and j==0):
        return
    elif(i==0): 
        niz1.append('_')
        niz2.append(b[j-1])
        funkcija(i,j-1)
    elif (j==0):
        niz1.append(a[i-1])
        niz2.append('_')
        funkcija(i-1,j)
    else:
        i1=kiselina.index(a[i-1])
        i2=kiselina.index(b[j-1])
        suma=m[i1][i2]
        dijag=score[i-1][j-1]+suma
        dolje=score[i-1][j]-8
        desno=score[i][j-1]-8
        if(score[i][j]==dijag):
            niz1.append(a[i-1])
            niz2.append(b[j-1])
            funkcija(i-1,j-1)
        elif(score[i][j]==dolje):
            niz1.append(a[i-1])
            niz2.append('_')
            funkcija(i-1,j)
        else:
            niz1.append('_')
            niz2.append(b[j-1])
            funkcija(i,j-1)

funkcija(d_a,d_b)
niz1.reverse()
niz2.reverse()








