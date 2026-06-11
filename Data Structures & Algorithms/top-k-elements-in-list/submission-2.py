class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items_count_map = defaultdict(int)
        for number in nums:
            items_count_map[number] += 1
    
        return heapq.nlargest(k, items_count_map, key=items_count_map.get)        