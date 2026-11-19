class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for i in nums:
            map[i]= map.get(i,0)+1

        result= sorted(map.keys(), key= lambda x:map[x],reverse=True)[:k]
        return result