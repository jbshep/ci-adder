from sys import argv


# python main.py
# -> 0
# python main.py 1 2 3
# -> 6

def add(args):
    # convert the list of strings to a list of ints
    numbers = list(map(lambda s: int(s), args))

    return sum(numbers)

def main(argv):
    if len(argv) == 1:
        print(0)
    else:
        print(add(argv[1:]))

if __name__ == '__main__':
    main(argv)



