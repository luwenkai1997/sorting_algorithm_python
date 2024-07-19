def sift(li, low, high):
    """

    :param li: data list
    :param low: root of the heap
    :param high: the last element of the heap
    :return: NA
    """
    i = low  # root
    j = 2*i+1  # left child of the root
    tmp = li[i]  # save the root

    while j <= high:
        if j+1 <= high and li[j+1] > li[j]:
            j = j + 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2*i+1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def heap_sort(li):
    n = len(li)
    # build the heap
    for i in range(n//2-1, -1, -1):
        sift(li, i, n-1)

    # now take out the root once at a time
    high = n-1
    while high > 0:
        li[0], li[high] = li[high], li[0]
        high -= 1
        sift(li, 0, high)



if __name__ == '__main__':
    li = [4,1,3,7,5,2,6,9,8,11]
    heap_sort(li)
    print(li)
