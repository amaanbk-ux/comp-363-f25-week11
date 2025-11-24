def segment_dp(A: str) -> list[str] | None:
    
    n = len(A)

    # dp[i] = True if A[:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True   # empty prefix is segmentable

    # parent[i] = index j such that A[j:i] is a valid word and dp[j] = True
    parent = [-1] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and is_word(little_dictionary, A[j:i]):
                dp[i] = True
                parent[i] = j
                break   # only need one valid segmentation

    if not dp[n]:
        return None

    # Backtrack to reconstruct words
    words = []
    idx = n
    while idx > 0:
        j = parent[idx]
        words.append(A[j:idx])
        idx = j

    words.reverse()
    return words
