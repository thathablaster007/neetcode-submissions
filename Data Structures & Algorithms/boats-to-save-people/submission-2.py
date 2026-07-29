class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = [0]*(max(people)+1)
        for i in people:
            count[i] += 1
        i,j = 0,1
        while i < len(people):
            while count[j] == 0:
                j += 1
            people[i] = j
            count[j] -= 1
            i += 1
        res = 0
        l,r = 0,len(people) - 1
        while l<=r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res

            

        