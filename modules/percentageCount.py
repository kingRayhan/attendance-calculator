from modules.result import result


def percentageCount(percentage_range, lines):
    count = 0
    for i in result(lines):
        if percentage_range[0] >= i[2] >= percentage_range[1]:
            count = count + 1
    return count
