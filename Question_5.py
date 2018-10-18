# If there are multiple duplicates in the array, how do you find duplicate Numbers
arr = [1, 4, 4, 2, 2, 5, 6, 7, 8, 1]
arrset = set(arr)
for item in arrset:
    num = arr.count(item)
    if num > 1:
        print(item)
