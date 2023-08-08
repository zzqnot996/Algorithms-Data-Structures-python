class Stack: # 有无括号  类用户大写   
    def __init__(self):
        self.items = []

        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self): 
        return self.items[0] 
 
    def size(self): 
        return len(self.items) 



if __name__ == "__main__":

    s = Stack()
    
    print(s.push(4) )
    print(s.peek())
    print(s.isEmpty())
    print(s.pop())
    print(s.push('dog'))
    print(s.peek())
    print(s.push(True) )
    print(s.peek())
    print(s.size())