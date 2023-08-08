

class LogicGate:
    
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    

class BinaryGate(LogicGate):
    
    def __init__(self,n):  # 对象一旦建立就会执行 首先执行父类的__init__
        LogicGate.__init__(self,n)  

        self.pinA = None
        self.pinB = None

    def getPinA(self):   # 继承过来的也可以用 self.getLabel()
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
    

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
            

class OrGate(BinaryGate):
    
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0




 # 创建 
class UnaryGate(LogicGate):
    
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
    
    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


# 创建与门
class AndGate(BinaryGate):   # 自己的__init__，AndGate的_init__，LogicGate的_init__ 都会执行
    
    def __init__(self,n):
        super(AndGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1       
# 构建电路
class Connector:
    
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate


        print(tgate)
        tgate.setNextPin(self)
        print(tgate)


    # 输入
    def getFrom(self):
        return self.fromgate
    
    # 输出
    def getTo(self):
        return self.togate
    


if __name__ == "__main__":

   g1 = AndGate("G1")
   print("g1",g1)
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

