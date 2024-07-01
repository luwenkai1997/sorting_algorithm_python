# add a comment to see the commit function
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

if __name__ == '__main__':
    li = [4,1,3,7,5,2,6]
    select_sort(li)
    print(li)