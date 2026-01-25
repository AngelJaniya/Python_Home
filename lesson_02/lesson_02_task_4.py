def fizz_buzz(n):
    for i in range(n):
        j = i + 1
        if j % 5 == 0 and j % 3 == 0:
            print('FizzBuzz')
        elif j % 3 == 0:
            print('Fizz')
        elif j % 5 == 0:
            print('Buzz')
        else:
            print(j)


fizz_buzz(17)
