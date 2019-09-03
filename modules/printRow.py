from modules.getMarks import getMarks


def printRow(name, id, percentage):
    print(name + "\t" + id + "\t" + str(int(percentage)) +
          '%' + "\t" + str(getMarks(percentage)))
