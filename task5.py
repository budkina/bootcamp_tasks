def partition(A, p, r):
    x=A[r]
    pivot = p
    for j in range(p, r):
        if A[j] <= x:
            A[j], A[pivot] = A[pivot], A[j]
            pivot += 1            
    A[pivot], A[r] = A[r], A[pivot]
    return pivot

def quicksort(A, p=0, r=None):
    if r==None:
        r=len(A)-1
    if p<r:
        pivot=partition(A,p,r)
        quicksort(A, p, pivot-1)
        quicksort(A, pivot+1, r)
    return A

ex1=[2,8,7,1,3,5,6,4]
ex2=[5,-2,4,7,8,-10,11]
print(ex1, " sorted:", quicksort(ex1))
print(ex2, " sorted:", quicksort(ex2))