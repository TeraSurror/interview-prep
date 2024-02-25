def group_anagrams(strs):
    groups = {}

    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = [word]
        else:
            groups[key].append(word)

    return groups.values()
