class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        currency = {
            5: 0,
            10: 0,
            20: 0,
        }

        for bill in bills:
            currency[bill] += 1
            if bill != 5 and currency[5] == 0:
                return False
            elif bill == 10:
                currency[5] -= 1
            elif bill == 20:
                if currency[10]:
                    
                    currency[10] -= 1
                    currency[5] -= 1
                else:
                    if currency[5] >= 3:
                        currency[5] -= 3
                    else:
                        return False
        return True
            
        