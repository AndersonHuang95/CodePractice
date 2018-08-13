#!/usr/bin/env python3

def failure_function(pattern):
    m = len(pattern)
    ret = [0 for _ in range(m)]

    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret[i] = j + 1 if pattern[j] == pattern[i] else j
    return ret


def main():
    print(failure_function('ABABAC'))

if __name__ == '__main__':
    main()
