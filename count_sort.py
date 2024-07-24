def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


if __name__ == '__main__':
    li = [-7, -10, 4, 1, 3, 7, 5, 2, 6, 9, 11]
    count_sort(li)
    print(li)