arr = [54,26,93,17,77,31,44,55,20]
print('arr: \t',arr)
n = len(arr)


gap = n // 2
print('gap:\t',gap)
while gap >= 1:
    # 插入排序算法
    for j in range(gap,n):
        
        # j= [gap,gap + 1,... n-1]
        # 处理元素向前遍历插入到相应的位置上

        i= j

        # 处理希尔分组里面的数据，如果当前索引减去分组数量大于0，5
        # (i - gap) = [4,5,....,n-4]
        # 按照一个分组间隔 在每个分组间隔内进行操作 直到小于gap就退出
        while (i - gap) >= 0:
            # 如果当前数据小于之前的数据，就进行交换，并且计算下
            if arr[i] < arr[i - gap]:
                arr[i],arr[i - gap] = arr[i - gap],arr[i]
                i-= gap
            else:
                break

    # 缩短 gap 间隔
    gap //= 2
    print('gap:\t',gap)
    print(arr)