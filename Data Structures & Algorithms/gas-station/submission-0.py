class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) != len(cost):
            return -1
        
        for i in range(0, len(gas)):
            if gas[i] < cost[i]:
                continue
            print("started loop:", i)
            curr = i
            visited_gas_stations = 0
            gas_tank = 0

            while visited_gas_stations < len(gas):
                print("inside loop")
                print("curr: ", curr,)
                print("visited_gas_stations: ", visited_gas_stations)
                print("gas_tank", gas_tank)
                if curr > len(gas)-1:
                    print("curr high: ", curr)
                    curr = 0
                gas_tank += gas[curr]
                can_travel = gas_tank - cost[curr] 
                print("can_travel: ", can_travel)
                if can_travel >= 0:
                    print("can travel: ", can_travel)
                    gas_tank -= cost[curr]
                    curr += 1
                    visited_gas_stations += 1
                else:
                    break
            
            if visited_gas_stations == len(gas):
                return i
        
        return -1
                