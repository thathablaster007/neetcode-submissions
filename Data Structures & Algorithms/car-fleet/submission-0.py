class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        pairings = [(p,s) for p,s in zip(position,speed)]
        pairings.sort(reverse = True)
        for p,s in pairings:
            time.append((target-p)/s)
            if len(time) >= 2 and time[-1] <= time[-2]:
                time.pop()
        return len(time)
        