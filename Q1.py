# Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(s,t):

    s_list = list(s)
    t_list = list(t)

    s_list.sort()
    t_list.sort()

    # print s_list, t_list

    key = []

    for letter in t_list:
        if letter in s_list:
            # print letter
            key.append(s.index(letter))

    if len(key) > 0:
        key.sort()
        # print key
        for value in range(1,len(key)):
            # print value
            if key[value] != key[value-1] + 1:
                return False
        return True



    # print key
    return False


print question1('udacity','da')
print question1('udacity','ad')
print question1('udacity','ciud')
print question1('udacity','uy')
print question1('udacity','cdaityu')
