import random

def tri_insertion(A):
    N = len(A)
    for i in range(1,N):
        print(A)
        cle = A[i]
        j = i-1
        while j>=0 and A[j] > cle:
            A[j+1] = A[j] # decalage
            j = j-1
        A[j+1] = cle



liste = []
for k in range(10):
    liste.append(random.randint(0,20))
tri_insertion(liste)








def tri_insertion(liste):
    L = list(liste)
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] > cle:
            L[j+1] = L[j] # decalage
            j = j-1
        L[j+1] = cle
    return L



liste = []
for k in range(10):
    liste.append(random.randint(0,20))
liste_triee = tri_insertion(liste)





print(liste)
print(liste_triee)