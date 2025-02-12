def convert(s, numRows):
    result = ""
    if numRows == 1:
        return s
    for i in range(numRows):
        for j in range(i , len(s), 2*(numRows - 1)):
            result += s[j]
            print(i ,j )
            print(j+2*(numRows-1)-2*i)
            print("---")
            if(i>0 and i<numRows-1 and j+2*(numRows-1)-2*i < len(s)):
                result += s[j+2*(numRows-1)-2*i]
    
    return result

s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))
#Output: "PAHN APLSII GYIR"
# P   A   H   N
# A P L S I I G
# Y   I   R


        


        