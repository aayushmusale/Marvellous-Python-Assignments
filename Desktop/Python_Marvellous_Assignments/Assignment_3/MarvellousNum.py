def CheckPrime(num):
    i = 2
    bFlag = True
    while i <= num/2:
        if(num % i == 0):
            bFlag = False
        
        i += 1
    
    return bFlag
