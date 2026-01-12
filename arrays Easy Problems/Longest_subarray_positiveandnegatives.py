class SubarraySolver:
    def get_longest_subarray(self, a, k):
        n = len(a)
        max_len = 0

        for i in range(n):
            for j in range(i, n):
                sub_sum = 0

                for idx in range(i, j + 1):
                    sub_sum += a[idx]

                if sub_sum == k:
                    max_len = max(max_len, j - i + 1)

        return max_len


