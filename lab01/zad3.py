def andGate(firstParam, secondParam):
    return firstParam & secondParam

def orGate(firstParam, secondParam):
    return firstParam | secondParam

def xorGate(firstParam, secondParam):
    return firstParam ^ secondParam

def notGate(param):
    return ~param

if __name__ == '__main__':
    print(andGate(10, 2))
    print(orGate(10, 2))
    print(xorGate(10, 2))
    print(notGate(1))

