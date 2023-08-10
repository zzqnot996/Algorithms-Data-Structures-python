

# 顺序存储的大根堆

def sift(li,low,high):
    """
    :param li:列表:
    :param low; 堆的根节点位置:
    :param high:堆的最后一个元素的位置:
    return:  
      
    """

    i= low # i最开始指向根节点
    j=2*i+1  # j 开始是左孩子
    tmp = li[low] #把堆顶存起来
    while j<= high: # 只要i位置有数
        if j + 1 <= high and li[j+1] < li[j]:# 如果右孩子有并且比较小
            j= j + 1 #指向右孩子

        if li[j] < tmp:
            li[i] = li[j]
            i=j #往下看一层
            j=2*i+1

        else:  # tmp更大，把tmp放到i的位置上
            li[i] = tmp #把tmp放到某一级领导位置上
            break
            
    
    else:
        li[i] = tmp # 把tmp放到叶子节点上



#=========堆排序===========================

# 构造堆
def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1):  #根据子节点找父节点 根据规律 左孩子i 则父节点等于(i-1 )//2  因为最后的节点的索引是n- 1  所以将i = n -1  带入得到（n-2）//2
        #i表示建堆的时候调整的部分的根的下标s
        sift(li,i,n-1)
        #建堆完成了

    # 挨个出数
    for i in range(n-1,-1,-1):
        # i 指向当前堆的最后一个元素
        li[0],li[i] = li[i],li[0]
        sift(li,0,i-1) # i-1是新的high

#=============topk问题================================ 
def topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    #1建堆
    for i in range(k,len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap,0,k-1)
    #2.遍历
    for i in range(k-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        sift(heap,0,i-1)
    #3.出数
    return heap


if __name__ == "__main__":

    import random 

    li = [i for i in range(1000)]
    random.shuffle(li) 

    heap_sort(li)
    print(topk(li,10))