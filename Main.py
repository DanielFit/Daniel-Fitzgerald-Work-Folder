
class Solution:
 def romanToInt(s: str) -> int:
    mydict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = [mydict.get(s[0])]


    for i in range(1, len(s)):
        if (mydict.get(s[i]) > number[-1]):
            number[-1] = mydict.get(s[i]) - number[-1]

        else:
            number.append(mydict.get(s[i]))
    return (sum(number))

 print (romanToInt("XIV"))