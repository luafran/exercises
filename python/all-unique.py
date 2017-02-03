# if elements of x are hashable
def all_unique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)


# if elements of x are not hashable
def all_unique2(x):
    seen = list()
    return not any(i in seen or seen.append(i) for i in x)


if __name__ == '__main__':
    print all_unique("ABCDEF")
    print all_unique("ABACDEF")
