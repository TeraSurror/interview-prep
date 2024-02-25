class Solution:
    def car_fleet(self, target, position, speed):
        pairs = [(i, j) for i, j in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []

        for pair in pairs:
            stack.append((target - pair[0]) / pair[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
