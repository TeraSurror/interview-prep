def is_anagram(s, t):
    s_dict = dict()

    for letter in s:
        if letter not in s_dict:
            s_dict[letter] = 1
        else:
            s_dict[letter] += 1

    for letter in t:
        if letter in s_dict:
            s_dict[letter] -= 1
            if s_dict[letter] == 0:
                del s_dict[letter]
        else:
            return False

    if len(s) != len(t):
        return False
    return True
