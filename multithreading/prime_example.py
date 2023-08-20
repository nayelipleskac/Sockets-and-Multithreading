def prime():
    numInput = int(input('enter any number: '))
    prime_flag = True

    for i in range(2,int(numInput**0.5)):
        if numInput % i == 0:
            prime_flag = False
            break
    if prime_flag == False:
        print(numInput, 'is not a prime number')

    else:
        print(numInput, 'is a prime number')
            
    