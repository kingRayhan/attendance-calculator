TOTAL_CLASS_COUNT = 17


def presencePercentage(attendences):
    totalPresence = 0
    for i in attendences:
        totalPresence += int(i)
    return (totalPresence * 100) / TOTAL_CLASS_COUNT
