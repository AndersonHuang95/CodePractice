#!/usr/bin/env python3

def say(n):
    """
    Asssumes n nonnegative
    """
    if not n: return ""
    x, y = "1", ""
    for i in range(n - 1):
        count = 1
        for idx in range(1, len(x)):
            if x[idx] == x[idx - 1]: count += 1
            else:
                y = y + str(count) + x[idx - 1]
                count = 1
        if x: y = y + str(count) + x[-1]
        x, y = y, ""
    return x

print(say(0))
print(say(1))
print(say(2))
print(say(3))
print(say(4))
print(say(5))
print(say(6))
