
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

if __name__ == '__main__':
    li = [4,1,3,7,5,2,6]
    bubble_sort(li)
    print(li)