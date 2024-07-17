def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


if __name__ == '__main__':
    li = [-7, -10, 4, 1, 3, 7, 5, 2, 6, 9, 11]
    shell_sort(li)
    print(li)