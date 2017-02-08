# Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.

import math

def question2(a):
# Steps might be:

    # Split the string in half, check if the reverse of this half is in the rest of the string
    def test(s):
        stop = int(math.floor(len(a)/2))
        print stop
        b = s[0:stop]
        c = b[::-1]
        d = b + c
        e = c + b
        print b, c, d, e
        if d in a:
            return d
        if e in a:
            return e
    # Do this recursively and iteratively with successively smaller substrings at different frames within the string until we've exahusted the possibilities for two letters
    while len(a) > 2:
        test(a)

print question2('abab')
print question2('avva')
print question2('avcva')
