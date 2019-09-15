#»ù±¾¼ÆËãÆ÷II
#2019-03-31 11:18:20

class Solution:
    def calculate(self, s: str) -> int: 
        listS = re.split(r'([+*/-])',s.replace(' ',''))
        # print(listS)
        nums = []
        
        i = 0
        while i<len(listS):            
            if listS[i] in '+-':                
                nums.append(listS[i])
                
            elif listS[i] == '*':                
                nums.append(nums.pop()*int(listS[i+1]))
                i += 1
                            
            elif listS[i] == '/':                            
                nums.append(nums.pop()//int(listS[i+1]))
                i += 1
            else:
                nums.append(int(listS[i]))
            i += 1
        
        i = 0
        ans = 0
        while i<len(nums):
            # print(nums)
            if nums[i] == '-':
                ans -= nums[i+1]
                i += 2
            elif nums[i] == '+':
                ans += nums[i+1]
                i += 2
            else:
                ans += nums[i]
                i += 1
        return ans