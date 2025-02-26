class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        strl = list(s)
        maxi = 0
        maxi_R = ''
        for index,value in enumerate(strl):
            if roman_to_int[value] >= maxi:
                maxi = roman_to_int[value]
                maxi_R = value

        start = strl.index(maxi_R)
        sum = 0
        for i in strl[start:]:
            sum = sum + roman_to_int[i]
        for i in strl[:start]:
                sum = sum - roman_to_int[i]

        print(sum)



a = Solution()
a.romanToInt("III")