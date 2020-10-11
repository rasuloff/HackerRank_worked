'''
Task

Given a string, S, of length N that is indexed from 0 to N - 1, print its
even-indexed and odd-indexed characters as 2 space-separated strings on a
single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input format:

The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a String, S.

Constraints:
1 <= T <= 10
2 <= length of S <= 10000

Output format:
For each string Sj (where 0 <= j <= T-1), print Sj's even indexed characters,
followed by a space, followed by Sj's odd-indexed characters.

'''

T = int(input())

for i in range(T):
    S = str(input())
    if len(S) < 2 and len(S) > 10000:
        print('Letters are out of range. Please, try again')
        pass
    else:
        print('%s %2s' % (S[::2], S[1::2]))
