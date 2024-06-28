import random

def main():
    total = 0
    numbers = []
    while  total <= 100:
        random_num = random.randint(0, 100)
        numbers.append(random_num)
        total = total + random_num
        if total > 100:
            total = total - numbers[len(numbers)-1]
    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
