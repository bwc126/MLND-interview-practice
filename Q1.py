# Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(s,t):
    if t in s:
        return True
    def reverse(a):
        return a[::-1]
    if reverse(t) in s:
        return True
    else:
        for position in range(len(t)):
            if t[position]+reverse(t[position+1:position+2]) in s:
                return True
    return False


print question1('udacity','da')
print question1('udacity','ad')
print question1('udacity','ciud')
