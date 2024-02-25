def merge_intervals(intervals):
    result = [intervals[0]]

    for start, end in intervals:
        last_end = result[-1][1]

        if start <= last_end:
            result[-1][1] = max(last_end, end)
        else:
            result.append([start, end])

    return result
