lines = tuple(open('data.txt', 'r'))
TOTAL_CLASS_COUNT = 17
percentageCounts = {'70': 0, '60': 0, '45': 0, '30': 0}


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


print("Name                ID     Percentage Marks")
for line in lines:
    row = line.split(' ')  # split lines with space
    id = row[0]
    name = row[1]
    attendences = row[2:]
    percentage = presencePercentage(attendences)
    printRow(name, id, percentage)
    # add percentage count
    percentageCounts[percentage] = percentage


print("\n\n")
print("Percentage                Count")
