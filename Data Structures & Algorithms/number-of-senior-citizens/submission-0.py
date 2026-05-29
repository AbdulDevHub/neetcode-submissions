class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniorCount = 0
        for citizen in details:
            if (int(citizen[11:13]) > 60): seniorCount += 1
        return seniorCount