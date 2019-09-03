from modules.presencePercentage import presencePercentage


def result(lines):
    result = []
    for line in lines:
        row = line.split(' ')  # split lines with space
        id = row[0]
        name = row[1]
        attendences = row[2:]
        percentage = presencePercentage(attendences)
        result.append([name, id, percentage])
    return result
