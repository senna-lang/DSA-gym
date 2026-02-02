# O(n)
# https://leetcode.com/problems/find-the-highest-altitude/submissions/1905384513
class MySolution:
    def largestAltitude(self, gain: list[int]) -> int:
      highest = 0
      current = 0
      for a in gain:
        current = current + a
        highest = max(highest, current)

      return highest