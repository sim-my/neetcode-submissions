class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)   # closest to target first
        fleets = 0
        slowest = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > slowest:        # can't catch the fleet ahead → new fleet
                fleets += 1
                slowest = time

        return fleets