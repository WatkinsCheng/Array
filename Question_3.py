# How do I find the maximum and minimum values in an unsorted array of integers
def Findmum(Arraylist):
    min = 999
    max = 0
    for i in Arraylist:
        maxtem = i
        mintem = i
        if max < maxtem:
            max = maxtem ^ max
            maxtem = maxtem ^ max
            max = maxtem ^ max
        if min > mintem:
            min = mintem ^ min
            mintem = mintem ^ min
            min = mintem ^ min
    return max, min
arr = [4, 2, 7, 9, 1]
maxmum, minmum = Findmum(arr)
print(maxmum, minmum)

