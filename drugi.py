f1 = open("acids.txt", "r")
aminokiseline = f1.readline()
f1.close()
f1 = open("blosum50.txt", "r")
matrica=[]
for i in range (20):
    line = f1.readline()
    vec = line.split()
    matrica.append(vec[:])
for i in range (20):
    for j in range (20):
        matrica[i][j] = int(matrica[i][j])
f1.close()
f1 = open("por001.txt", "r")
a = f1.readline()
b = f1.readline()
i=0
suma=0
while (a[i] != '\n'):
    if (a[i] != '_' and b[i] != '_'):
        x = aminokiseline.index(a[i])
        y = aminokiseline.index(b[i])
        suma = suma + matrica[x][y]
    else:
        suma = suma - 8
    i = i +1
        
        
