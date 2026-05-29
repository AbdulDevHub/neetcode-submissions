class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(passenger[11:13] > "60" for passenger in details)