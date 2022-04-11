"""
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions *= 4

        direction = ["N", "W", "S", "E"]
        direction_index = 0
        location = (0, 0)

        for instruction in instructions:
            if instruction == "G":
                if direction[direction_index] == "N":
                    location = (location[0], location[1] + 1)
                elif direction[direction_index] == "W":
                    location = (location[0] - 1, location[1])
                elif direction[direction_index] == "S":
                    location = (location[0], location[1] - 1)
                elif direction[direction_index] == "E":
                    location = (location[0] + 1, location[1])
            elif instruction == "L":
                direction_index = (direction_index + 1) % 4
            elif instruction == "R":
                direction_index = (direction_index - 1) % 4

        return location == (0, 0)
"""
Success
Details
Runtime: 36 ms, faster than 74.61% of Python3 online submissions for Robot Bounded In Circle.
Memory Usage: 13.9 MB, less than 25.17% of Python3 online submissions for Robot Bounded In Circle.
"""