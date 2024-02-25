class Solution:
    def merge_triplets(self, target, triplets):
        present = set()

        for tripet in triplets:
            if tripet[0] > target[0] or tripet[1] > target[1] or tripet[2] > target[2]:
                continue

            for i, val in enumerate(tripet):
                if target[i] == val:
                    present.add(i)

        return len(present) == 3
