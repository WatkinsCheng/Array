# Find repeated Numbers in the given array of integers
def FindRepetition(Arraylist):
    Arraylen = len(Arraylist)
    result = 0
    for i in Arraylist:
        result ^= i
    for j in range(1, Arraylen):
        result ^= j
    return result

arr = [1, 2, 3, 1]
print(FindRepetition(arr))