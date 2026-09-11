class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []

        for ch in s:
            if ch == "#":
                if len(s1) > 0:
                    s1.pop()
            else:
                s1.append(ch)

        for ch in t:
            if ch == "#":
                if len(t1) > 0:
                    t1.pop()
            else:
                t1.append(ch)

        return s1 == t1