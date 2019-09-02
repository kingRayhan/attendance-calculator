lines = tuple(open('data.txt', 'r'))
TOTAL_CLASS_COUNT = 17


def getMarks(percentage):
    marks = 2
    if percentage >= 70:
        marks = 5
    elif percentage >= 60:
        marks = 4
    elif percentage >= 45:
        marks = 3
    elif percentage <= 30:
        marks = 2
    return marks


def presencePercentage(attendences):
    totalPresence = 0
    for i in attendences:
        totalPresence += int(i)
    return (totalPresence * 100) / TOTAL_CLASS_COUNT


def printRow(name, id, percentage):
    print(name + "\t" + id + "\t" + str(percentage) +
          '%' + "\t" + str(getMarks(percentage)))


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


print("Name                ID     Percentage Marks")
for row in result(lines):
    printRow(row[0], row[1], row[2])

print("\n\n")
print("Percentage     Count")


def percentageCount(percentage_range):
    count = 0
    for i in result(lines):
        if percentage_range[0] >= i[2] >= percentage_range[1]:
            count = count + 1
    return count


p = [70, 60, 45, 30]
for i, percentage in enumerate(p):
    upper = p[i - 1] - 1
    lower = p[i]
    if i == 0:
        upper = 100
    if percentage == 30:
        lower = 0

    print(str(percentage) + "%\t\t" + str(percentageCount([upper, lower])))
