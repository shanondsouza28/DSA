class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #first number is an offset
        #low- left - sum bigger
        #high - right sum smaller
        #squeeze through low and high
        nums.sort() #inplace sort
        answer =[] #list of lists
        for i in range(len(nums)):
            if nums[i] > 0:
                break # all positives offset has to be negative to balance things out on the way
            elif i > 0 and nums[i] == nums[i-1]:
                continue # move on to the next offset , we dont want duplicates
            
            low,high = i+1, len(nums) -1
            while (low < high):
                threeSum = nums[i] + nums[low] + nums[high]
                if threeSum == 0:
                    answer.append([nums[i], nums[low], nums[high]])
                    low, high = low+1, high-1
                    while low < high and nums[low] == nums[low-1]:
                        low= low+1
                    while low< high and nums[high] == nums[high+1]:
                        high = high - 1
                elif threeSum > 0:
                    high -=1
                else:
                    low +=1
        return answer
                    

            
    
        