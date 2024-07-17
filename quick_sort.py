def _quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        _quick_sort(data, left, mid - 1)
        _quick_sort(data, mid + 1, right)


def partition(data, left, right):
    cur = data[left]
    while left < right:
        while left < right and data[right] > cur:
            right -= 1

        data[left] = data[right]

        while left < right and data[left] < cur:
            left += 1

        data[right] = data[left]
    data[left] = cur
    return left


def quick_sort(data):
    _quick_sort(data, 0, len(data) - 1)


if __name__ == '__main__':
    li = [4, 1, 3, 7, 5, 2, 6]
    quick_sort(li)
    print(li)
