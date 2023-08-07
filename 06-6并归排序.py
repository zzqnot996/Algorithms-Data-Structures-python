# https://www.bilibili.com/video/BV1Hd4y1B7Mg?p=21

def merge_sort(arr):
    """归并排序"""

    n = len(arr)
    if 1 == n:
        return arr
    mid = n // 2

    # 对左半部分进行归并排序
    left_arr = merge_sort(arr[:mid])

    # 对右半部分进行归并排序
    right_arr = merge_sort(arr[mid:])

    # 合并两个有序集台
    left,right = 0,0
    new_arr = []

    left_n = len(left_arr)
    right_n = len(right_arr)

    while left < left_n and right < right_n:
        if left_arr[left] < right_arr[right]:
            new_arr.append(left_arr[left])
            left += 1
        else:
            new_arr.append(right_arr[right])
            right += 1
    new_arr += left_arr[left:]
    new_arr += right_arr[right:]

    return new_arr


arr = [54,26,93,17,77,31,44,55,20]
print('arr: \t',arr)
sorted_arr = merge_sort(arr)
print("排序之后:\t",sorted_arr)
