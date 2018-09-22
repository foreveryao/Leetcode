class Solution(object):
    def plusOne(self, digits):
        intNum=0
        for i in range(len(digits)):
            intNUm=intNum*10+digtis[i]
        intNum+=1
        str_num=str(intNum)
        res=[]
        for i in range(len(str_num)):
           res.append(int(str_num[i]))
        return res
