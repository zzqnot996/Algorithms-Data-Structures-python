arr = [54,26,93,17,77,31,44,55,20]
print('arr: \t',arr)
n = len(arr)
for j in range(n - 1):
    min_index = j # 记录最小值的位置# 遍历所有元素，获取最小值的位置
    for i in range(j + 1,n):
        if arr[i] < arr[min_index]:
            # 更新最小值的位置
            min_index = i
    if min_index != j:
        arr[j],arr[min_index] = arr[min_index],arr[j]
print('arr; \t',arr)