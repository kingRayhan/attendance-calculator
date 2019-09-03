def percentageCountList(percentageCount, lines):
    p = [70, 60, 45, 30]
    result = []
    for i, percentage in enumerate(p):
        upper = p[i - 1] - 1
        lower = p[i]
        if i == 0:
            upper = 100
        if percentage == 30:
            lower = 0
        result.append(percentageCount([upper, lower], lines))
    return result
