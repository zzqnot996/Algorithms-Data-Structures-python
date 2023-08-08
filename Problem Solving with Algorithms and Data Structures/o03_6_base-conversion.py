from o03_2_Stack_implementation import Stack



# 将十进制转换为任意进制数
def baseConverter(decNumber, base):

    digits = "0123456789ABCDEF"
    remstack = Stack() 

    while decNumber > 0:
        rem = decNumber % base
        print(rem)
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""

    while not remstack.isEmpty(): 
         
        a = remstack.pop()
        print("-----",digits[a] )
        newString = newString +  digits[a] 

    return newString


if __name__ == "__main__":



    decNumber = 123535248
    print(baseConverter(decNumber,16))