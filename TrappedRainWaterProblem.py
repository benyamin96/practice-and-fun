def trapped_rain_water_problem(heights):

    if len(heights) < 3:
        return 0

    right_max = [0 for _ in range(len(heights))]
    left_max = [0 for _ in range(len(heights))]

    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i - 1], heights[i - 1])

    for i in range(len(heights) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i + 1])

    trapped = 0

    for i in range(1, len(heights) - 1):
        if min(right_max[i], left_max[i]) > heights[i]:
            trapped += min(right_max[i], left_max[i]) - heights[i]
    return trapped


print(trapped_rain_water_problem([4, 1, 2, 5, 3, 1]))
