arr = [54,26,93,17,77,31,44,55,20]
print('arr: \t',arr)
n = len(arr)

for j in range(1,n):
    # j= [1,2,3...,n-1]
    # j= 5 i = [5,4,3,4,1,0]
    for i in range(j,0,-1):
        if arr[i] < arr[i - 1]:
            arr[i],arr[i - 1] = arr[i - 1],arr[i]
        else:
            break
print('arr:\t', arr)

# 每一次都需要重复操作对前面 新的数字出现 前面都要重新排