import sys

def collatz(number):
    # This function shows the collatz sequence  
    
    if (number % 2 == 0):
        val =  number // 2
    else:
        val = 3 * number + 1
    
    print(val)
    return val
    

while True:
    try:
        user_number = int(input('Please enter a number: '))
        result = collatz(user_number)

        while True:        
            if(result == 1):
                sys.exit()
            else:
                result = collatz(result)
                
    except ValueError:
        print('PLEASE enter only numbers! ')
        continue        