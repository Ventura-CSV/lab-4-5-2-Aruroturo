import random

def main():
    total = 0
    numbers = []
    while total<= 100:
        random_num = random.randint(1, 100)
        numbers.append(random_num)
        total += random_num
    
    
    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
