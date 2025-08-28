class Solution:
    def reverse(self, x: int) -> int:
        MIN= -2**31
        MAX= 2**31
        res=0
        while x:
            dig= int(math.fmod(x,10))
            x= int(x/10)
            if(res > MAX//10 or (res == MAX//10 and dig >= MAX%10)):
                return 0
            if(res < MIN//10 or (res == MIN//10 and dig <= MIN%10)):
                return 0
            res= (res*10)+ dig
        return res