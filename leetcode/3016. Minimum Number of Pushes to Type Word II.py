class Solution:
    def minimumPushes(self, word: str) -> int:
        keys = set(word)
        d = {}
        i, answer = 0, 0

        for c in keys: d[c] = word.count(c)
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

        for k, v in d.items():
            if i // 8 == 0: answer = answer + (1 * v)
            elif i // 8 == 1: answer = answer + (2 * v)
            elif i // 8 == 2: answer = answer + (3 * v)
            else: answer = answer + (4 * v)
            i += 1

        return answer