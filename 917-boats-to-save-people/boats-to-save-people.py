class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        boats = 0
        while l<r:
            while l<r and people[r]>=limit:
                boats+=1
                r-=1
            if l<r and people[l]+people[r]>limit:
                r-=1
                boats+=1
            else:
                l+=1
                r-=1
                boats+=1
        if l==r:
            boats+=1
        return boats