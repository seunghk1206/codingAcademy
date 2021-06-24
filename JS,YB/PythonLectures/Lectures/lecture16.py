def insertion_sort(L):
    for each in range(0, len(L)):
        for i in range(0, len(L)):
            if L[each] < L[i]:
                L[each], L[i] = L[i], L[each]
    return L

print(insertion_sort([1,5,2,7,3,8,1,7,9,2,4,7,1]))
ListA = [1,5,2,7,3,8,1,7,9,2,4,7,1]
ListB = ['A', 'B', 'C', 'D']

def selection_sort(L):
    for i in range(0, len(L)):
        minIndex = i
        for j in range(i+1, len(L)):
            if L[j] < L[minIndex]:
                L[j], L[minIndex] = L[minIndex], A[j]
    return L

def bubbleSort(listA):
    for i in range(0, len(listA)):
        for j in range(0, len(listA) - 1 - i):
            if listA[j] > listA[j+1]:
                listA[j], listA[j+1] = listA[j+1], listA[j]
    return listA

print(bubbleSort([1,6,3,87,56,4,8,5,5,456,435,2,3,4,4]))