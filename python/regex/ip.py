import re
import sys

if __name__ == "__main__":
    input_str = sys.argv[1]
    print "input = ", input_str
    # input = "http://[ipaddress]/SaveData/127.0.0.1/00-0C-F1-56-98-AD/"
    # mac = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', input, re.I).group()
    ip = re.search(r'((2[0-5]|1[0-9]|[0-9])?[0-9]\.){3}((2[0-5]|1[0-9]|[0-9])?[0-9])',
                   input_str, re.I).group()

    # print mac
    print ip
