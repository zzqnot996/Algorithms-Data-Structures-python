# python 库里面的内置模块
# https://www.bilibili.com/video/BV1uA411N7c5/?p=52&vd_source=e1de9f6d02128b9c85f5fdd03c7e72fc

'''
Python队列内置模块
使用方法: from collections import deque
创建队列: queue = deque()
进队: append()
出队: popleft()
双向队列队首进队: appendleft()
双向队列队尾出队: pop()

'''


# deque 双向队列
from collections import deque

q = deque([1,2,3,4,5],5)  # 5 是队列的容量 多余这个会从头部出去
q.append(6) # 队尾进队
print(q.popleft()) # 队首出队

# 用于双向队列
# q.appendleft(1) # 队首进队
# q.pop(O)#.队尾出队

def tail(n):
    with open('test.txt','r') as f:
        q = deque(f,n)
        return q
    
# 取出一个文件的后无行 不用全部读取  这样可以节省内存 前5行可以用for循环  
print(tail(5))

for line in tail(5):
    print(line,end="")