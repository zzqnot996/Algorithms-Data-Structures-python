
class LinkList:

    class Node:

        def __init__(self,item=None):
            self.item = item
            self.next = None


    # 迭代器 支持next
    class LinkListIterator:  

        def __init__(self,node):
            self.node = node
        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node =cur_node.next
                return cur_node.item
            else:
                raise StopIteration 
            
        def  __iter__(self):
            return self
        
        
    def __init__(self,iterable=None):
        
        self .head =None
        self.tail =None

        if iterable:
            self.extend(iterable) # 链表创建

    def append(self,obj):
            s = LinkList.Node(obj)
            
            if not self.head:
                self.head =s
                self.tail = s

            else:
                self.tail.next = s
                self.tail = s


    def extend(self,iterable):

            for obj in iterable:
                self.append(obj)

    def find (self,obj):
        for n in self:
            if n== obj:
                return True
        return False
        
    def __iter__(self):
        return self.LinkListIterator(self.head)
        
    def  __repr__(self):
        return "<<"+",".join(map(str,self))+">>"
            

class Hashtable:
    def __init__(self,size = 101) : # size = 101 --> T开辟了空间

        self.size = size
        self.T = [LinkList() for  i in range(self.size)]

    def hash_b(self,k):
        return k % self.size
    
    def insert(self,k):

        i =self.hash_b(k)
        if self.find(k):
            print("Duplicated Insert",k)
        else:
            self.T[i].append(k)

    def find(self,k):
        i = self.hash_b(k)
        return self.T[i].find(k)




if __name__ == "__main__":
    
    '''
    Lk = LinkList([17,20,26,31,44,54,55,77,93])
    for ele in Lk:
        print(ele)
    '''

    hash_ta = Hashtable()
    hash_ta.insert(2)
    hash_ta.insert(1)
    hash_ta.insert(2)
    hash_ta.insert(102)
    hash_ta.insert(3)
    hash_ta.insert(508)
    print(",".join(map(str,hash_ta.T)))
    print(hash_ta.find(203))
