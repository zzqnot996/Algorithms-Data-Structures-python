


from o03_2_Stack_implementation import Stack

def divideBy2(decNumber):
    remstack = Stack() 

    while decNumber > 0:
        rem = decNumber % 2 
        print(rem)
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""

    while not remstack.isEmpty(): 
        binString = binString + str(remstack.pop()) 

    return binString


if __name__ == "__main__":



    decNumber = 123535
    print(divideBy2(decNumber))