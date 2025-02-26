def isPalindrome(x):
               
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

x = -121
res = isPalindrome(x)
print(res)