# Given an array of 1-100 integers,find the missing Numbers
def FindMissing(Arraylist):
    Arraylen = len(Arraylist)
    sum = 0
    for i in Arraylist:
        sum += i
    return Arraylen, sum

arr = [1, 2, 4, 5]
num, Sum = FindMissing(arr)
print((2+num)*(1+num)/2-Sum)





