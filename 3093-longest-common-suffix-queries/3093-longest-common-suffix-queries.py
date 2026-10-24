class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        lengths = [len(w) for w in wordsContainer]

        children = [{}]
        best = [min(range(len(wordsContainer)), key=lengths.__getitem__)]

        for i, word in enumerate(wordsContainer):
            length = lengths[i]
            node = 0
            for ch in reversed(word):
                nxt = children[node].get(ch)
                if nxt is None:
                    nxt = len(children)
                    children[node][ch] = nxt
                    children.append({})
                    best.append(i)
                elif length < lengths[best[nxt]]:
                    best[nxt] = i
                node = nxt

        result = []
        for q in wordsQuery:
            node = 0
            for ch in reversed(q):
                nxt = children[node].get(ch)
                if nxt is None:
                    break
                node = nxt
            result.append(best[node])

        return result