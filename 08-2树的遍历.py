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
        self.root = None # 跟节点


    # 类似队列  先进先出
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



    # ========广度优先遍历=============
    def breadth_travel(self):
        '''广度遍历'''
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)


    # ========深度优先遍历=============
    def preorder(self,node):
        ##先序遍历##
        if node is None:
            return
        print(node.elem)
        self.preorder(node.lchild)
        self.preorder(node.rchild)
    
    def inorder(self,node):
        ##中序遍历##
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem)
        self.inorder(node.rchild)

    def postorder(self,node):
        ##后序遍历##
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem)





if __name__ == "__main__":

    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print("")
    tree.preorder(tree.root)
    print("")
    tree.inorder(tree.root)
    print("")
    tree.postorder(tree.root)
    print("")
    # tree.breadth_travel()

