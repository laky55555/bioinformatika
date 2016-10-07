f=open("acids.txt", "r")
kiselina=f.readline()
f=f.close
matrica=[]
f=open("blosum50.txt", "r")
for u in range (20):
       l=f.readline()
       l=l.split()
       matrica.append(l[:])
f.close()
    


def fja(a,b):
    suma=0
    for i in range (len(a)):
        if(a[i]!='_' and b[i]!='_'):
            index1=kiselina.index(a[i])
            index2=kiselina.index(b[i])
            suma=suma+int(matrica[index1][index2])
        else:
            suma=suma-8
    print suma





import random
f=open("nizovi.txt", "r")
niz1=f.readline()
niz2=f.readline()
niz1=niz1.rstrip()
niz2=niz2.rstrip()
f.close
lista=['0','1','0','1','0','1','0','1','0','1','0','1','0','1',
       '0','1','0','1','0','0']
for k in range (10):
    random.shuffle(lista)
    a=[]
    b=[]
    i=0
    j=0
    for l in range (20):
        if(l==0 and lista[l]=='1'):
            b.append(niz2[j])
            a.append("_")
            j=j+1
        elif (l==0 and lista[l]=='0'):
            a.append(niz1[i])
            i=i+1
        else:
            if(lista[l]=='0'):
                if(lista[l-1]=='1'):
                    a.append(niz1[i])
                    i=i+1
                if(lista[l-1]=='0'):
                    b.append('_')
                    a.append(niz1[i])
                    i=i+1
            if(lista[l]=='1'):
                if(lista[l-1]=='0'):
                    b.append(niz2[j])
                    j=j+1
                if(lista[l-1]=='1'):
                    a.append('_')
                    b.append(niz2[j])
                    j=j+1
    if (lista[l]==0):
        b.append("_")
    while (len(a)> len(b)):
        b.append("_")

       
    print a
    print b
    print lista
    fja(a,b)


