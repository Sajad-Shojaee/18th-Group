# Prime Number
for num in range(1, 1001):
    if num > 1:
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            if num % i == 0:
                break
        else:
            print('#{},is prime number'.format(num))
    else:
        print('#{},is prime number'.format(num))