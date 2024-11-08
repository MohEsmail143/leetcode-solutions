class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        ids = list(range(len(position)))
        ids.sort(key=lambda x: position[x], reverse=True)
        
        prev_time = (target - position[ids[0]]) / speed[ids[0]]
        fleet_count = 1

        for i in ids[1:]:
            curr_time = (target - position[i]) / speed[i]

            if curr_time > prev_time:
                prev_time = curr_time
                fleet_count += 1
        
        return fleet_count