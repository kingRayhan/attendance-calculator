import matplotlib.pyplot as plt


def openChart(percentages):
    labels = ['70%', '60%', '45%', '30%']
    sizes = [] + percentages
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
