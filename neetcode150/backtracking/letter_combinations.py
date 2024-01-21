def find_letter_combinations(digits):
    MAPPING = ("0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")

    if digits == "":
        return []

    result = []

    partial_result = [""] * len(digits)

    def find_enumerations(digit):
        if digit == len(digits):
            result.append("".join(partial_result))
            return

        for i in MAPPING[int(digits[digit])]:
            partial_result[digit] = i
            find_enumerations(digit + 1)

    find_enumerations(0)

    return result
