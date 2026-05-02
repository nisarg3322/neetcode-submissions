class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles) 
        print(l,r)
        mid = (l+r) // 2
        print(mid)
        result = r
        while l <= r:
            speed = mid
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/speed)
            if total_time <= h:
                
                result = min(speed, result)
                print("set result", result)
            
            if total_time <= h:
                print("in second if", total_time)

                r = mid -1
                mid = (l+r) //2
            elif total_time > h:
                print("in first if", total_time)
                l = mid +1
                mid = (l + r) // 2
            

        return result
        