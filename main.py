import hashlib


def decorator_for_just_func(func):
    memo = dict()

    def wrapper(*args):
        if args not in memo:
            memo[args] = hashlib.sha256(func(*args).encode()).hexdigest()
            print('new string added')
        return memo[args]
    return wrapper


@decorator_for_just_func
def just_func(name):
    print(name)
    return name


if __name__ == '__main__':
    print(just_func('PyCharm'))
    print(just_func('corgi'))
    print(just_func('dfvgm'))
    print(just_func('corgi'))
