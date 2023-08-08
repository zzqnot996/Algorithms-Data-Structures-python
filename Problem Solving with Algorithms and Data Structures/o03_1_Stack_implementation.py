class Stack: # 有无括号  类用户大写   
    def __init__(self):
        self.items = []

        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self): 
        return self.items[len(self.items)-1] 
 
    def size(self): 
        return len(self.items) 



if __name__ == "__main__":

    s = Stack()
    
    print(s.push(4) )
    print(s.peek())
    print(s.isEmpty())
    print(s.push('dog'))
    print(s.peek())
    print(s.push(True) )
    print(s.peek())
    print(s.size())