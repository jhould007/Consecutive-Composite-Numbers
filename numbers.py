def isPrime(n):
    for k in range(2,int(n**0.5)+1):
        if n%k==0:
            return False
    return True
                
# Finds the first sequence of n consecutive composite numbers
def findCompositeSequence(n): 
    print()
    currentNumber = 1
    currentStreak = 1
    
    while True: 
        if currentStreak == n: 
            print("The starting value for the first sequence of " + str(n) + " composite numbers is " + str(currentNumber - n) + ".")
            print("The ending value for the first sequence of " + str(n) + " composite numbers is " + str(currentNumber - 1) + ".")
            print()
            break
        
      #  print("Checking " + str(currentNumber))
        if isPrime(currentNumber): 
            currentStreak = 0
        else: 
            currentStreak += 1
        currentNumber += 1
        
findCompositeSequence(7)
findCompositeSequence(13)
findCompositeSequence(100)