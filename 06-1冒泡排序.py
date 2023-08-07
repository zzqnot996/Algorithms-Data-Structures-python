arr = [54,26,93,17,77,31,44,55,20]
print('arr:',arr)

n = len(arr)
# 多少轮
for j in range(n - 1):
    for i in range(0,n - 1 - j):  # - j 节省时间 避免重复
        if arr[i] > arr[i + 1]:
            arr[i],arr[i + 1] = arr[i + 1],arr[i]

print('arr:',arr)