'''enumerate is a built-in function in Python that allows you to iterate over a sequence (e.g. a list, tuple, or string) 
while keeping track of the index of each item in the sequence.'''
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("\n")

# you can add second argument to change starting index

fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits, 5):
    print(index, fruit)



# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
from typing import List
"""

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list = []
        num_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_index:
                index_list.append(num_index[complement])
                index_list.append(i)
                return index_list
            else:
                num_index[num] = i
        
        return index_list

x = Solution()
print(x.twoSum(nums=[2, 7, 11, 15], target=9))