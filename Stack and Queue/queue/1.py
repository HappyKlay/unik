from collections import Counter

def first_unique_character(s: str) -> int:
    char_count = Counter(s)
    
    for idx, char in enumerate(s):
        if char_count[char] == 1:
            return idx
    
    return -1

print(first_unique_character("leopard"))        # Output: 0
print(first_unique_character("loveleopard"))    # Output: 2
print(first_unique_character("aabb"))           # Output: -1
