class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for i in operations:

            if i == "C":
                l.pop()
            elif i == "D":
                l.append(2*l[-1])
            elif i == "+":
                l.append(l[-2]+l[-1])
            else:
                l.append(int(i))
        return sum(l)

            
        