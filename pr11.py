class Solution:
    def mostWordsFound(sentences: list[str]) -> int:
        result = 0

        for s in sentences:
            w = s.split()
            result = max(result, len(w))

        return result
    print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
