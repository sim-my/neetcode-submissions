class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        my_dict = defaultdict(list)
        for i,item in enumerate(points):
            x = item[0]
            y = item[1]
            distance = math.sqrt((y*y + x*x))
            my_dict[distance].append(item)

        keys = list(my_dict.keys())
        heapq.heapify(keys)
        answer = []
        print(keys, my_dict)

        while len(answer) < k:
            ans = heapq.heappop(keys)
            for x in my_dict[ans]:
                answer.append(x)

        return answer


