from queue import *
from printer import *
from task import *

import random

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and \
                (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append( \
            nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/float(len(waitingtimes))
    print "Average Wait Time%6.2f seconds"%(averageWait),
    print "Tasks Remaining %3d"%(printQueue.size())


def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False
