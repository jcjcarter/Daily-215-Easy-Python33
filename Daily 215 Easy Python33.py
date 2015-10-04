from functools import partial

get_ints = lambda i_n_t: map(int, str(i_n_t))

def user_input():
    start = input('Enter starting number: ')
    base = input('Enter base: ')
    return list(map(int, (start, base)))

def find_cycle(start, base):
    cycle = set()
    _cycle = list()
    current = start
    get_current = partial(lambda x, n: n**x, base)
    while not current & cycle:
        cycle.add(current)
        _cycle.append(current)
        current = sum(map(get_current, get_ints(current)))
    return _cycle[_cycle.index(current):]


if __name__ == "__main__":
    start, base = user_input()
    print(find_cycle(start, base))