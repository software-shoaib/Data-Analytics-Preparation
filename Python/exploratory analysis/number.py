import random
def lottery(num):
    '''lottlery takes an integer value from 1 to 10
    as guess value. If you guessed corect you will win else loss'''
    lucky_number = random.randint(0,10)
    if num == lucky_number:
        print(f"lucky number is {lucky_number } You win!")
    else:
        print(f'lucky number is {lucky_number } you loss')


def isEven(num):
    ''' isEven takes any iteger and return if integer is even or not '''
    if num%2==0:
        return f"{num} is even"
    else:
        return f"{num} is not even" 

    
    
    
def isOdd(num):
    ''' isOdd takes any iteger and return if integer is odd or not '''
    if num%2 != 0:
        return f"{num} is odd"
    else:
        return f"{num} is not odd" 