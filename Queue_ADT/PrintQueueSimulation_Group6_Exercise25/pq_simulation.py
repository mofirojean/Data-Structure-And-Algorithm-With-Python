# implementation of the main simulation class
from pq_array import Array
from pq_llistqueue import Queue
from pq_simpeople import Printer, UserFile


class TicketCounterSimulation:
    """Creates a simulation object"""

    def __init__(self, numPrinters, numMinutes, betweenTime, printTime):
        """Parameter supplied by the user"""
        self._betweenTime = betweenTime
        self._arriveProb = 1.0 / betweenTime
        self._printTime = printTime
        self._numMinutes = numMinutes

        # Simulation components
        self._userFileQ = Queue()
        self._thePrinters = Array(numPrinters)
        for i in range(numPrinters):
            self._thePrinters[i] = Printer(i + 1)

        # Computed during the simulation
        self._totalWaitTime = 0
        self._numUserFiles = 0

        self._prev_time = 0

    # Run the program using parameters supplied earlier
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginPrinting(curTime)
            self._handleEndPrinting(curTime)

    # Print the simulation results
    def printResults(self):
        numServed = self._numUserFiles - len(self._userFileQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of files printed = ", numServed)
        print("Number of files remaining in the queue = %d" % len(self._userFileQ))
        print("The average wait time was %4.2f minutes." % avgWait)

    # Handles the arrival of every new customer
    def _handleArrival(self, currentTime):
        if currentTime == 0 or currentTime == self._prev_time + self._betweenTime:
            p: UserFile = UserFile(self._numUserFiles + 1, currentTime)
            self._userFileQ.enqueue(p)
            self._numUserFiles += 1
            self._prev_time = currentTime

    def _handleBeginPrinting(self, currentTime):
        for printer in self._thePrinters:
            a: Printer = printer
            if a.isFree() and (self._userFileQ.isEmpty() is False):
                a.startPrinting(self._userFileQ.dequeue(), currentTime + self._printTime)

    def _handleEndPrinting(self, currentTime):
        for printer in self._thePrinters:
            a: Printer = printer
            if a.isFinished(currentTime):
                a.stopPrinting()
                self._totalWaitTime += self._printTime
