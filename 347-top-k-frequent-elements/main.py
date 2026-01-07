from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(count)
        bucket = [[] for i in range(len(nums) + 1)]
        for num, count in count.items():
            bucket[count].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for f in bucket[i]:
                res.append(f)
                if len(res) == k:
                    return res

print(Solution().topKFrequent([1,1,1,2,2,3], 2))