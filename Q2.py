# Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.

import math

def question2(a):
# Steps might be:

    # Split the string in half, check if the reverse of this half is in the rest of the string
    def test(s, offset, width):
        stop = int(math.ceil(width/2))
        # print stop
        b = s[0+offset:stop+offset]
        c = s[stop+offset:width+offset]
        # print b, c
        if b in c[::-1]:
            return b+c
        else:
            return ''
        # d = b + c
        # e = c + b
        # print b, c, d, e
        # if d in s:
        #     return d
        # if e in s:
        #     return e
    # Do this recursively and iteratively with successively smaller substrings at different frames within the string until we've exahusted the possibilities for two letters
    result = ''
    width = len(a)
    old_result = ''
    new_result = ''
    while width >= 2:
        offsets = len(a) - width + 1
        for offset in range(offsets):
            new_result = test(a, offset, width)
            # print 'exiting at ', offset, len(new_result), len(old_result)
        if (len(new_result) < len(old_result)):
            # print 'returning ', old_result
            return old_result
        if (len(new_result) > len(old_result)):
            # print 'setting new result', new_result
            old_result = new_result
        width -= 1
    return old_result
print question2('abab')
print question2('avva')
print question2('avcva')
print question2('racecar')
print question2('ihaveafastracecar')
