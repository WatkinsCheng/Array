# How do I find the maximum and minimum values in an unsorted array of integers
def Findmum(Arraylist):
    min = 999
    max = 0
    for i in Arraylist:
        maxtem = i
        mintem = i
        if max < maxtem:
            max ^= maxtem
            maxtem ^= max
            max ^= maxtem
        if min > mintem:
            min ^= mintem
            mintem ^= min
            min ^= mintem
    return max, min
arr = [4, 2, 7, 9, 1]
maxmum, minmum = Findmum(arr)
print(maxmum, minmum)

