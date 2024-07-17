def merge(li, low, mid, high):
    i = low
    j = mid + 1
    tmp_result = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            tmp_result.append(li[i])
            i += 1
        else:
            tmp_result.append(li[j])
            j += 1
    while i <= mid:
        tmp_result.append(li[i])
        i += 1
    while j <= high:
        tmp_result.append(li[j])
        j += 1
    li[low:high + 1] = tmp_result


def _merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


def merge_sort(li):
    _merge_sort(li, 0, len(li) - 1)


if __name__ == '__main__':
    li = [-7, -10, 4, 1, 3, 7, 5, 2, 6, 9, 11]
    merge_sort(li)
    print(li)
