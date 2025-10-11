# 58. Length of Last Word

# sorc leet Code 
class Solution(object):
    def lengthOfLastWord(self, s):
        listText=s.split()
        lastValue=listText[-1]
        return len(lastValue)
    
# my test
class Solution2(object):
    def lengthOfLastWord2(self, s):
        listText=s.split()
        return len(listText[-1])
  
txt="this is My information"  
obj=Solution2()
obj2=obj.lengthOfLastWord2(txt)
print(obj2)