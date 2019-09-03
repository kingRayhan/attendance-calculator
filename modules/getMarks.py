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
