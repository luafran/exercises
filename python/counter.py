import re
import sys
from collections import Counter

# Find the ten most common words in stdin

input_data = sys.stdin.read().lower()
words = re.findall(r'\w+', input_data)
print Counter(words).most_common(10)

words2 = input_data.split()
print Counter(words2).most_common(10)
