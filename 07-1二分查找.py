# coding:utf-8

# 最好是使用递归

def binary_search1(alist,item):
    """二分查找  递归版本"""
    n = len(alist)
    mid = n//2

    if n > 0:
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search1(alist[:mid],item)
        else:
            return binary_search1(alist[mid+1:],item)
    
    return False


def binary_search2(alist,item):
    """二分查找  非递归版本"""
    n = len(alist)
    first = 0
    last = n-1

    while first <=  last:

        mid= (first + last)//2

        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid -1
        else:
            first = mid + 1

    return False


if __name__ == "__main__":

    Li = [17,20,26,31,44,54,55,77,93]
    print(binary_search2(Li ,535))
