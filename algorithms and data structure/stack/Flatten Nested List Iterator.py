# https://leetcode.com/problems/flatten-nested-list-iterator/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

# unnest the list recursively, then return item one by one
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        self.idx = 0
        self.unnest(nestedList)
        
    def unnest(self, l):
        for i in range(len(l)):
            if not l[i].isInteger():
                self.unnest(l[i].getList())
            else:
                self.res.append(l[i].getInteger())
        
    def next(self) -> int:
        r = self.res[self.idx]
        self.idx += 1

        return r
    
    def hasNext(self) -> bool:
        return self.idx < len(self.res)
    