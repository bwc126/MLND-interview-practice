# Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(s,t):

    s_list = list(s)
    t_list = list(t)

    s_list.sort()
    t_list.sort()

    # print s_list, t_list

    key = []
    test = ''
    for char in t:
        # print char
        s = s.replace(char, '-')
        # print s
    for i in range(len(t)):
        test += '-'
    # print test, s
    if test in s:
        return True

    # for letter in t_list:
    #     if letter in s_list:
    #         # print letter
    #         index = s.find(letter)
    #         s = s[0:index] + '-' + s[index+1:len(s)]
    #         print s
    #
    #         key.append(index)
    #
    # if len(key) > 0:
    #     key.sort()
    #     # print key
    #     for value in range(1,len(key)):
    #         # print value
    #         if key[value] != key[value-1] + 1:
    #             return False
    #     return True



    # print key
    return False


print question1('udacity','da') # Should be True
print question1('udacity','ad') # Should be True
print question1('udacity','ciud') # Should be False
print question1('udacity','uy') # Should be False
print question1('sarsaparilla','apas') # Should be True
