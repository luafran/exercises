

def short_bubble_sort(a_list):

    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        pass_num -= 1

if __name__ == '__main__':
    list1 = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    print list1
    print 'short_bubble_sort'
    short_bubble_sort(list1)
    print list1
