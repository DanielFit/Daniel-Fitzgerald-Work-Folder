"""This code is designed to calculate Roman numerals an return
an int ie: the Roman numerals XV = 15 """



def romanToInt(self: str) -> int:

        # A dictionary is created so each numeral has its correct value to reference
        RomanNumerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = [RomanNumerals.get(self[0])]

# As Roman numerals will add or subtract when adjacent depending on their values,
# I have started at the end of the string to determine if a subtraction is needed
        for numeral in range(1, len(self)):
            if RomanNumerals.get(self[numeral]) > number[-1]:
                number[-1] = RomanNumerals.get(self[numeral]) - number[-1]

# If no subtraction is needed the Roman numerals can be summed for the result.
            else:
                number.append(RomanNumerals.get(self[numeral]))
        return sum(number)

print(romanToInt("XIV"))
