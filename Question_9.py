def Exchange(Arraylist, start, end):
    while start < end:
        Arraylist[start], Arraylist[end] = Arraylist[end], Arraylist[start]
        start += 1
        end -= 1
    return Arraylist
array = [1, 2, 3, 5, 6, 7]
start = 0
end = len(array)-1
print(Exchange(array, start, end))