# https://runestone.academy/ns/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#a-fraction-class

#  约分
#  https://www.cnblogs.com/kirito-c/p/6910912.html
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

# print(gcd(20,10))



class Fraction:
    
    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom



    def show(self):
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)  # 约分
        return Fraction(newnum//common,newden//common)
    

    # 判断值相等 而不是引用 == 不是 =
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

if __name__ == "__main__":

    myf = Fraction(3,5)
    print(myf) # <__main__.Fraction object at 0x0000023DBDA27488>
    myf.show() # 3 / 5
    print("I ate", myf, "of the pizza") # I ate 3/5 of the pizza
    print(myf.__str__()) # '3/5'
    print(str(myf))  # '3/5'

    f1=Fraction(1,4)
    f2=Fraction(1,2)
    f3=f1+f2
    print(f3)
