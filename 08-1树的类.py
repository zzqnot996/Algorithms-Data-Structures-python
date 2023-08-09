# coding :utf-8
# 树是链表的扩充

class Node(object):
    def __init__(self,item) :
        self.elem = item
        self.lchild = None # 左孩子
        self.rchild = None  # 又孩子

class Tree(object):
    #二叉树
    def __init__(self):
        self,root = None # 跟节点


    # 类似队列
    def add(self,item):
        node = Node(item)
        queue = [self.root] # 初始化

        if self.root is None:
            self.root = node
            return
        
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)




if __name__ == "__main__":

    tree = Tree()

