# LCS Problem Statement: Given two sequences, find the length of longest subsequence present in
# both of them. A subsequence is a sequence that appears in the same relative order, but not
# necessarily contiguous. For example, "abc", "abg", "bdf", "aeg", "acefg", .. etc are subsequences
# of "abcdefg". So a string of length n has 2^n different possible subsequences.
#
# It is a classic computer science problem, the basis of diff (a file comparison program that outputs
# the differences between two files), and has applications in bioinformatics.
#
# Examples:
# LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
# LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.


def lcs(str1, str2):
    # find the length of the strings
    m = len(str1)
    n = len(str2)

    # declaring the array for storing the dp values
    lcs_table = [[None] * (n + 1) for _ in xrange(m + 1)]

    """Following steps build lcs_table[m+1][n+1] in bottom up fashion
    Note: lcs_table[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # lcs_table[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return lcs_table[m][n]

if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    print "Length of LCS is ", lcs(X, Y)
