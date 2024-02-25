def ladder_length(beginWord, endWord, wordList):
    def is_diff(s1, s2):
        count = 0
        for l1, l2 in zip(s1, s2):
            if l1 != l2:
                count += 1
            if count > 1:
                return False
        return True

    def create_graph(beginWord, wordList):
        graph = {beginWord: []}

        if beginWord in wordList:
            wordList.remove(beginWord)

        q = [beginWord]

        while len(q) != 0:
            curr_word = q.pop(0)
            for word in wordList:
                if is_diff(word, curr_word):
                    graph[curr_word].append(word)
            for word in graph[curr_word]:
                wordList.remove(word)
            for word in graph[curr_word]:
                q.append(word)
                graph[word] = []
        return graph

    graph = create_graph(beginWord, wordList)
    result = 1
    q = [beginWord]

    while len(q) != 0:
        level = len(q)
        while level != 0:
            curr_word = q.pop(0)
            for word in graph[curr_word]:
                if word == endWord:
                    return result + 1
                q.append(word)
            level -= 1
        result += 1

    return 0
