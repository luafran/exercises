import sys
import char_in_both_strings

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "usage:",sys.argv[0],"string1 string2"
        raise SystemExit

    string1 = sys.argv[1]
    string2 = sys.argv[2]

    char_in_both_strings.chars_in_both_strings(string1, string2)
