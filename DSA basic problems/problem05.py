def getDivisors(self, N):
        res = []
        for i in range(1, N + 1):
            if N % i == 0:
                res.append(i)
        return res