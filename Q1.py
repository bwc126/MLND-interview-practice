# Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(s='',t=''):
    # We can replace within s each character that's in t with some placeholder character (hyphen in this example), and then check to see if there's a string of placeholder characters within s that correspond to the length of t. Since we want all possible anagrams of t to be covered, any of the characters in t can be in any position within s, and as long as they're adjacent in s and there are at least as many in s as there are in t, we can confidently declare some anagram of t is within s.

    # For each letter in t, if count in t > count in s, return false. This will handle counterexample when t has repeats that s lacks, and s has repeats that t lacks, but both have at least one of same letter such that the remaining logic int this program would mistakenly return true for a string of special characters with t's length appearing in s. 
    if not s or not t:
        return
    test = ''
    for char in t:
        if t.count(char) > s.count(char):
            return False
    for char in t:
        s = s.replace(char, '-')
    for i in range(len(t)):
        test += '-'
    if test in s:
        return True
    return False

print question1('udacity','da') # Should be True
print question1('udacity','ad') # Should be True
print question1('udacity','ciud') # Should be False
print question1('udacity','uy') # Should be False
print question1('sarsaparilla','apas') # Should be True
print question1('','') # Should be None
print question1() # Should be None
print question1('aaab','bbba') # Should be False
