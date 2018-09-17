class Solution(object):
        def singleNumber(self, nums):
            dic={}
            for i in nums:
                dic[i]=dic.get(i,0)+1
            for key,value in dic.items():
                if value==1:
                    return key


class Solution(object):
    def singleNumber(self,nums):
        single_list=[]

        for i in nums:
            if i not in single_list:
                single_list.append(i)
            else:
                single_list.remove(i)
        return single_list.pop()

