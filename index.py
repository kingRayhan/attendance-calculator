from modules.getMarks import getMarks
from modules.presencePercentage import presencePercentage
from modules.percentageCount import percentageCount
from modules.result import result
from modules.printRow import printRow

lines = tuple(open('data.txt', 'r'))


"""
Part 1: Calculated Attendance Percentage
"""
print("Calculated	Attendance	Percentage:")
print("Name                ID     Percentage Marks")
for row in result(lines):
    printRow(row[0], row[1], row[2])

"""
Part 2: Attendance	Percentage	(Student	Count)
"""

print("\n\n")
print("Attendance Percentage (Student Count):")
print("Percentage     Count")
p = [70, 60, 45, 30]
for i, percentage in enumerate(p):
    upper = p[i - 1] - 1
    lower = p[i]
    if i == 0:
        upper = 100
    if percentage == 30:
        lower = 0

    print(str(percentage) + "%\t\t" +
          str(percentageCount([upper, lower], lines)))
