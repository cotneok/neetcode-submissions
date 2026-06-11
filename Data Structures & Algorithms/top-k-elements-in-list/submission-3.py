class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items_count_map = defaultdict(int)
        for number in nums:
            items_count_map[number] += 1
        return [key for key, value in sorted(items_count_map.items(), key= lambda item: item[1], reverse=True)[:k]]        
        