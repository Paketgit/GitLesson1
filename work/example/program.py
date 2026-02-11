def FillArr(arr, n):
    i = 0
    while (i < n):
        tmp = int(input(""))
        arr.append(tmp)
        i += 1


def PrintArr(arr):
    print("Array:")
    for i in arr:
        print(f"{i} ")

arr = list()
n = int(input("Enter number of elements: "))
print("Enter elements:")

FillArr(arr, n)
PrintArr(arr)

print("")