# Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.

import math

def question2(a):
# Steps might be:

    # Split the string in half, check if the reverse of this half is in the rest of the string
    def test(s, offset, width):
        # stop = int(math.floor(len(s)/2))
        # print stop
        b = s[0+offset:width+offset]
        c = b[::-1]
        d = b + c
        e = c + b
        print b, c, d, e
        if d in s:
            return d
        if e in s:
            return e
    # Do this recursively and iteratively with successively smaller substrings at different frames within the string until we've exahusted the possibilities for two letters
    result = ''
    width = int(math.floor(len(a)/2))
    while width >= 2:
        rec = len(a) - (2 * width) + 1
        for it in range(rec+1):
            result = test(a, it, width)
        width -= 1
    return result
print question2('abab')
print question2('avva')
print question2('avcva')
print question2('ls;dnfuewhrojaaajjaaaa;sdlkfnlk')
