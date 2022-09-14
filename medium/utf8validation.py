from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        bytes = 0
        if len(data) == 1:
            bitNum = format(data[0], '08b')
            if bitNum[:1] != "0":
                return False
            return True
        for num in data:
            bitNum = format(num, '08b')
            if bytes > 1:
                if bytes > 4:
                    return False
                if bitNum[:2] != "10":
                    return False
                bytes -= 1
            else:
                bytes = 0
                if bitNum[:2] == "10":
                    return False
                while bitNum[0] != "0":
                    bytes += 1
                    bitNum = bitNum[1:]
                    if bitNum == "":
                        break
                if bytes == 8:
                    return False
        return True and (bytes == 0 or bytes == 1)

data = [240,162,138,147,145]
print(Solution().validUtf8(data))