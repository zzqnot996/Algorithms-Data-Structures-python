
def bucket_sort(li,n=100,maxnum=10000):

    buckets =[[] for _ in range(n)] #创建桶
    
    for var in li:

        i = min(var // (maxnum // n),n-1) #i 表示var放到几号桶里
        buckets[i].append(var)

        # 保持桶内的顺序  使用插入排序
        for j in range(len(buckets[i])-1,0,-1):

            if buckets[i][j] < buckets[i][j-1]:
                
                buckets[i][j],buckets[i][j-1] = buckets[i][j-1],buckets[i][j]

            else:
                break


    sorted_li = []
    for buc  in buckets:

        sorted_li.extend(buc)

    return sorted_li


if __name__ == "__main__":
    
    import random 

    li = [random.randint(0,10000) for  i in range(100000)]
    print(li)
    print("==========================")
    li = bucket_sort(li)
    print(li)
          

