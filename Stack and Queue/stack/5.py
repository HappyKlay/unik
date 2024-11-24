def decodeString(s: str) -> str:
    stack = []
    current_string = ''
    current_num = 0
    
    for char in s:
        if char.isdigit():  
            current_num = current_num * 10 + int(char)
        elif char == '[': 
            stack.append((current_string, current_num))
            current_string = ''
            current_num = 0
        elif char == ']': 
            prev_string, repeat_count = stack.pop()
            current_string = prev_string + current_string * repeat_count
        else:  
            current_string += char
    
    return current_string

print(decodeString("3[a]2[bc]"))  # Output: "aaabcbc"

print(decodeString("3[a2[c]]"))  # Output: "accaccacc"

print(decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
