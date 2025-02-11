def longestPalindrome(s):
    max_len = 1
    result = s[0]
    if len(s) <= 1:
        return s
    
    for i in range(len(s)):
        for j in range(i+1 , len(s)):
            x = s[i:j+1]
            if x == x[::-1] and len(x) > max_len:
                result = x
                max_len = len(x)

    return result
s = "cbbd"
print(longestPalindrome(s))