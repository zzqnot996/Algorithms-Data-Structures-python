
'''
深度优先搜索
回溯法
思路: 
从一个节点开始，任意找下一个能走的点，当找不到能走的点时，退回上一个点寻找是否有其他方向的点。
使用栈存储当前路径


路径不一定是最短的  怎么使用最短的 队列
'''


maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]

]

dirs = [
    lambda x,y:(x+1,y),
    lambda x,y:(x-1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1)
]



def maze_path(x1,y1,x2,y2):
    stack = []
    stack.append((x1,y1))

    while(len(stack)>0):
        curNode = stack[-1]# 当前的节点
        if curNode[0] == x2 and curNode[1] == y2:#走到终点了
            for p in stack:
                print(p)
            return True
        
        # 有路则进栈 标记 无路就
        #x,y 四个方向 x-1,y;x+1,y; x,y-1;x,y+1
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1]) #如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] ==0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]]= 2 # 2表示为已经走过
                break  # 找到一个就不用循环了
        else:
            
            stack.pop()
    else:
        print("没有路")
        return False
    
if __name__ == "__main__":
    maze_path(1,1,8,8)