def myAtoi(s):
    s = s.strip()
    sign = 1
    num = ''
    res = 0
    if len(s) == 0:
        return 0

    if s.startswith('-'):
        sign = -1
        num = s[1:]
    elif s.startswith('+'):
        num = s[1:]
    else:
        num = s

    for ech in num:
        if ech.isdigit():
            res = res * 10 + int(ech)
        else:
            break
    res *= sign
    max_range = 2**31 -1
    min_range = -(2**31)
    if res < min_range:
        return min_range
    elif res > max_range:
        return max_range
    else:
        return res
        
s1 = "   -042"
s2 = "42"
s3 = "1337c0d3"
s4 = "0-1"
s5 = "words and 987"

result = myAtoi(s1)
print(result)