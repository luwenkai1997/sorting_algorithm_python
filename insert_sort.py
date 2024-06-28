def insert_sort(li):
    for i in range(1, len(li)-1):
        cur = li[i]
        j = i - 1
        while j >= 0 and li[j] > cur:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = cur

if __name__ == '__main__':
    li = [4,1,3,7,5,2,6]
    insert_sort(li)
    print(li)