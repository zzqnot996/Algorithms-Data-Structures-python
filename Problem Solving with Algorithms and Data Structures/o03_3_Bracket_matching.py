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
    

def parChecker(symbolString):
    s = Stack() 

    balanced = True   # 是否匹配
    index = 0 

    while index < len(symbolString) and balanced:

        symbol = symbolString[index]
        # if symbol == "(":
        if symbol in "([{":
            s.push(symbol) 
        else:
           if s.isEmpty(): 
               balanced = False 
           else:
               # print(s.pop())
               top = s.pop() 
               if not matches(symbol,top):
                    balanced = False

        index = index + 1 

    if balanced and s.isEmpty(): 
        return True
    else:
        return False

def matches(symbol,top):
    opens = "([{ "
    closers = ")]}"
    return opens.index(top) == closers.index(symbol)

if __name__ == "__main__":

    symbolString = "((([])))"
    print(parChecker(symbolString))