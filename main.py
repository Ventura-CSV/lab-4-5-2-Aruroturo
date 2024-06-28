import random

def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while total <= 100:
        num = random.randint(1,100)
        numbers.append(num)
        total = total + num
    if total > 100:
        total = total - numbers[len(numbers)- 1]
    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
