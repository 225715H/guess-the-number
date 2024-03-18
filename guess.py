import random
min_num, max_num = map(int,input().split())
ans = random.randint(min_num, max_num)
i = 1

def check_num(guess):
    if guess == ans:
        print('You got it right!!')
        exit()
    elif guess > ans:
        print('You guessed too high!!\n')
    else:
        print('You guessed too low!!\n')
    return False

def __main__():
    global i
    guess = int(input(f'{i} times \nguess the number!!\n'))
    if not check_num(guess):
        i += 1
        __main__()


if __name__ == '__main__':
    __main__()

