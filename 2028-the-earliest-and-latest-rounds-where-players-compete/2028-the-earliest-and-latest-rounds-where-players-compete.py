from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int):
        @lru_cache(None)
        def dfs(players):
            m = len(players)
            res = [float('inf'), -float('inf')]

            for i in range(m // 2):
                a, b = players[i], players[-i - 1]
                if {a, b} == {firstPlayer, secondPlayer}:
                    return [1, 1]

            next_rounds = []

            def backtrack(i, curr):
                if i >= m // 2:
                    if m % 2 == 1:
                        curr.append(players[m // 2])
                    next_rounds.append(tuple(sorted(curr)))
                    return

                a, b = players[i], players[-i - 1]
                if {a, b} == {firstPlayer, secondPlayer}:
                    return

                if a in (firstPlayer, secondPlayer):
                    backtrack(i + 1, curr + [a])
                elif b in (firstPlayer, secondPlayer):
                    backtrack(i + 1, curr + [b])
                else:
                    backtrack(i + 1, curr + [a])
                    backtrack(i + 1, curr + [b])

            backtrack(0, [])

            for nxt in next_rounds:
                a, b = dfs(nxt)
                res[0] = min(res[0], a + 1)
                res[1] = max(res[1], b + 1)

            return res

        return dfs(tuple(range(1, n + 1)))