from collections import Counter


def find_anagrams_brute(str1, str2):
    for i in range(0, len(str2) - len(str1) + 1):
        q = list(str1)
        temp = str2[i:i+len(str1)]
        for c in temp:
            try:
                q.remove(c)
            except ValueError:
                pass
        print '{0} -> {1}'.format(temp, 'yes' if len(q) == 0 else 'no')


def find_anagrams(str1, str2):
    str1_counter = Counter(str1)
    print 'str1_counter:', str1_counter
    print

    temp = str2[0:len(str1)]
    str2_counter = Counter(temp)
    print '{0} ({1})-> {2}'.format(temp, str2_counter, 'yes' if str1_counter == str2_counter else 'no')

    for i in range(1, len(str2)-len(str1) + 1):
        temp = str2[i:i+len(str1)]
        str2_counter[str2[i-1]] -= 1
        str2_counter[str2[i+len(str1)-1]] += 1
        print '{0} ({1})-> {2}'.format(temp, str2_counter, 'yes' if str1_counter == str2_counter else 'no')


a = 'abbc'
b = 'bbccbbabc'

print 'a:', a
print 'b:', b
print

find_anagrams_brute(a, b)
print '#' * 100
find_anagrams(a, b)
