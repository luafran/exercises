
def solution(N):
    binstr = '{0:b}'.format(N).rstrip('0')
    print binstr
    count = 0
    gap = 0
    for c in binstr:
        if c == '0':
            count += 1
            if count > gap:
                gap = count
        else:
            count = 0
    return gap

# print solution(2147483647)
# print solution(2147483648)
print solution(1024)
