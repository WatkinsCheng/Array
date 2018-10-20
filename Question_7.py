def sub_sort(Arraylist, start, end):
    key = Arraylist[start]
    while start < end:
        while start < end and Arraylist[end] >= key:
            end -= 1
        while start < end and Arraylist[end] < key:
            Arraylist[start] = Arraylist[end]
            start += 1
            Arraylist[end] = Arraylist[start]
    Arraylist[start] = key
    return start


def quick_sort(Arraylist, start, end):
    if start < end:
        key_index = sub_sort(Arraylist, start, end)
        quick_sort(Arraylist, start, key_index)
        quick_sort(Arraylist, key_index+1, end)


if __name__ == '__main__':
    array = [8, 10, 9, 6, 4, 16, 5, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3]
    print(array)
    quick_sort(array, 0, len(array)-1)
    print(array)


