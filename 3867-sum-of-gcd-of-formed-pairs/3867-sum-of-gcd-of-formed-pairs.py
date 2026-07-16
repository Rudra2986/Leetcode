class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = 0
        

        for i in nums:
            num = i
            if i > mx:
                mx = i
            
            temp = mx
            # GCD(nums,temp)
            while temp != 0:
                a = temp                      
                temp = num % temp
                num = a
            
            prefixGcd.append(num)
        
        final_list = []
        prefixGcd.sort()
        for i in range(len(prefixGcd)//2):
            b = prefixGcd[i]
            c = prefixGcd[-(i+1)]
            if (b != c):

                # GCD(b, c)
                while b != 0:
                    a = b
                    b = c % b
                    c = a
                final_list.append(c)
            else:
                final_list.append(b)
        op = 0
        for i in final_list:
            op += i
        return op