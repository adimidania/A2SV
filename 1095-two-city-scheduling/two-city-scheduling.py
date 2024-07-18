class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        greedy_cost = []
        for cost_a, cost_b in costs:
            greedy_cost.append([cost_a - cost_b, cost_a, cost_b])
        greedy_cost.sort()
        output = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                output += greedy_cost[i][1]
            else:
                output += greedy_cost[i][2]
        return output
        