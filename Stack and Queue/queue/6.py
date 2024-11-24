def movesToStamp(stamp: str, target: str) -> list[int]:
    n, m = len(target), len(stamp)
    target = list(target)  
    stamp_indices = []
    replaced = [False] * n  
    total_replaced = 0

    def canStamp(start: int) -> bool:
        """
        Check if the stamp can be applied at index `start`.
        """
        matched = False
        for i in range(m):
            if target[start + i] == '?':
                continue
            if target[start + i] != stamp[i]:
                return False
            matched = True
        return matched

    def doStamp(start: int) -> None:
        """
        Replace a portion of the target with '?' starting from index `start`.
        """
        nonlocal total_replaced
        for i in range(m):
            if target[start + i] != '?':
                target[start + i] = '?'
                total_replaced += 1

    while total_replaced < n:
        stamped = False
        for i in range(n - m + 1):
            if not replaced[i] and canStamp(i):
                doStamp(i)
                stamp_indices.append(i)
                replaced[i] = True
                stamped = True
        if not stamped:
            return []

    return stamp_indices[::-1] 

print(movesToStamp("abc", "ababc"))      # Output: [0, 2]
print(movesToStamp("abca", "aabcaca"))  # Output: [3, 0, 1]
