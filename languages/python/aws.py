# Programming Challenge Description:
# There are two wizards, one good and one evil. The evil wizard has captured the princess. The only way to defeat the evil wizard is to recite a set of magic numbers. The good wizard has given you two numbers, A and B. Find every magic number between A and B, inclusive. 

# A magic number is a number that has two characteristics:
# 1. No digits repeat.
# 2. Beginning with the leftmost digit, take the value of the digit and move that number of digits to the right. Repeat the process again using the value of the current digit to move right again. Wrap back to the leftmost digit as necessary. A magic number will visit every digit exactly once and end at the leftmost digit. 

# For example, consider the magic number 6231.
# 1. Start with '6'. Advance 6 steps to '3', wrapping around once.
# 2. From '3', advance to '2'.
# 3. From '2', advance to '1'.
# 4. From '1', advance to '6'.

# Input:
# The input consists of two integers on a line, separated by spaces. Each integer A and B is 1 <= A <= B <= 10000.

# Output:
# Print each magic number between A and B, inclusive, on a line. If there is no magic number between A and B, print -1.

# Test 1
# Test Input
# 100 1000
# Expected Output
# 147
# 174
# 258
# 285
# 417
# 471
# 528
# 582
# 714
# 741
# 825
# 852

def build_for_path(path):
    l_path = len(path)
    for pos in range(l_path-1):
        curr = path[pos]
        next = path[pos+1]
        print 'curr:', curr
        print 'next:', next
        for value in valid_values(curr, next, l_path-1):
           print value
            
	    
def valid_values(curr, next, n_len):
    values = []
    value_base = next - curr
    if value_base < 0:
        value_base = value_base + n_len
    print 'value_base:', value_base
    val = value_base
    while val <= 9:
        if val in seen_values:
            continue
        values.append(val)
        seen_values.append(val)
        val += n_len
    
    return values


# min, max = raw_input().split()
#l_min = len(min)
#l_max = len(max)
l_min = 2

res = [0] * l_min
seen_values = []
paths = [ [0,1,0] ]
for path in paths:
    build_for_path(path)


#path2 = [0,2,1,0]
# 0,1,0
# 0,1,2,0 0,2,1,0

# 0,1,2,3,0 0,1,3,2,0
# 0,2,1,3,0 0,2,3,1,0
# 0,3,1,2 0 0,3,2,1,0

#for pos in range (l_min):
    #next = path1[pos+1]
    #print curr, next
    #val = next - curr
    #if val < 0:
    #    val += l_min
    #while val in seen:
    #    val += l_min
    #print 'val:',val
    #res[curr] = val
    #seen_val.append(val)

#print res

