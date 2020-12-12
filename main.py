import random


def main():
    n = None
    while 1:
        try:
            n = int(input('Number of participants:'))
            if n <= 0:
                raise ValueError
        except:
            print('Incorrect input...')
        else:
            break

    seq = list(range(1, n+1))
    random.shuffle(seq)
    for num in seq:
        input('press Enter for the next participant')
        print(f'participant_{num}')
    print("That's all")

if __name__ == '__main__':
    main()