def start_at(start):

    return lambda inc: start + inc


if __name__ == '__main__':
    closure1 = start_at(10)
    closure2 = start_at(100)

    print 'closure1(3) = %s' % (closure1(3))
    print 'closure2(3) = %s' % (closure2(3))
