# https://www.bilibili.com/video/BV1Hd4y1B7Mg?p=19&spm_id_from=pageDriver&vd_source=e1de9f6d02128b9c85f5fdd03c7e72fc

def quick_sort(arr,start,end):
    '''快速排序'''

    # 递归的退出条件
    if start > end:
        return
    

    # 设定起始元素为要寻找位置的基准元素
    mid = arr[start]
    # # Left 为序列左边的由左向右移动的游标
    left = start
    # right为序列右边的由右向左移动的游标
    right = end
    while left < right:
        # 如果Left与right未重合，right指向的元素不比基准元素小
        while left < right and arr[right] >= mid:
            right -= 1 
        # 将right指向的元素放到Left的位置上
        arr[left] = arr[right]
        # 如果Left与right未重合，Left指向的元素比基准元素小
        while left < right and arr[left] < mid:
            left += 1
        # Left指向的元素放到right的位置上
        arr[right] = arr[left]
        # 退出循环后，Left与right重合，此时所指位置为基准元素的正确
        # 将基准元素放到该位置
        arr[left] = mid
        # 对基准元素左边的子序列进行快速排序
        quick_sort(arr,start,left - 1)
        # 对基准元素右边的子序列进行快速排序
        quick_sort(arr,left + 1, end)

arr = [54,26,93,17,77,31,44,55,20]
print('arr:\t',arr)
quick_sort(arr,0,len(arr) - 1)
print('arr:\t',arr)