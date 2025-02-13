def reverse(x):
    sign = -1 if x < 0 else 1
    reverse_x = int(str(abs(x))[::-1]) * sign

    if reverse_x <= (2**31 -1) and reverse_x >= -(2**31):
        return reverse_x
    else:
        return 0     

x = 123 
print(reverse(x))  