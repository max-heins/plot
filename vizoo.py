import json
import os
import matplotlib.pyplot as plt
import statistics

def fileToDict():
    dir = "physics files/"
    dictList = []
    for file in os.listdir(dir):
        with open(dir+file) as jsonFile:
            dictList.append(json.load(jsonFile))
    return dictList

def plotTask(dictList):
    fig, ax = plt.subplots(figsize=(10, 10))
    for i in range(len(dictList)):
        x = dictList[i]["raw_data"]["W"]["S2"]["samplesTree"][6][::2]
        y = dictList[i]["raw_data"]["W"]["S2"]["samplesTree"][6][1::2]
        ax.plot(x, y)
        medianx = statistics.median_low(x)
        mediany = statistics.median_low(y)
        ax.plot(medianx, mediany, marker="o", markersize=5, markeredgecolor="#00acb3", markerfacecolor="#00acb3")
    plt.show()

if __name__ == '__main__':
    plotTask(fileToDict())


