#!/usr/bin/env python3
result = ""

for code in range(ord('a'), ord('z') + 1):
    letter = chr(code)
    if letter != 'q' and letter != 'e':
        result += letter

print(result)
