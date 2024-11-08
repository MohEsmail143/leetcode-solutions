class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        zipped = sorted(list(zip(position, speed)))
        curr_max_time = (target - zipped[-1][0]) / zipped[-1][1]
        # print(f"curr_max_time = {curr_max_time}")
        fleet_count = 1
        for i in range(len(zipped) - 2, -1, -1):
            pos_i, speed_i = zipped[i]
            time_i = (target - pos_i) / speed_i
            if time_i > curr_max_time:
                curr_max_time = time_i
                fleet_count += 1
        
        return fleet_count