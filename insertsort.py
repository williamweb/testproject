# -*- coding:utf-8 -*-

def insert_sort(nums):
    count=len(nums)
    for i in range(1,count):
        for j in range(i,0,-1):
             if nums[j]<nums[j-1]:
                 nums[j], nums[j-1] = nums[j-1], nums[j]

def better_insert_sort(nums):
    count=len(nums)
    for i in range(1,count):
        tmp = nums[i]
        j = i
        while j>0 and nums[j-1]>tmp:
            nums[j]=nums[j-1]
            j -= 1
        nums[j]=tmp
    

list1=[2,6,1,3,9,5]
print(list1)
#insert_sort(list1)
better_insert_sort(list1)
print(list1)
