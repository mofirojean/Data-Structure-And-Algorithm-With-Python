# Used to store and manage information related to the airline passenger
class UserFile:
    """Creates a passenger object"""
    def __init__(self, idNum, arrivalTime):
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    # Gets the passenger's id number
    def idNum(self):
        return self._idNum

    # Get's the passenger's arrival time
    def timeArrived(self):
        return self._arrivalTime


# Used to store and manage information related to an airline agent
class Printer:
    """Creates a ticket agent object"""
    def __init__(self, idNum):
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1

    # Gets the ticket agent's id number
    def idNum(self):
        return self._idNum

    # Determine if the ticket agent is free to assist a passenger
    def isFree(self):
        return self._passenger is None

    # Determine if the ticket agent has finished
    def isFinished(self, curTime):
        return self._passenger is not None and self._stopTime == curTime

    # Indicates the ticket agent has begun assisting a passenger
    def startPrinting(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    # Indicates the ticket agent has finished helping the passenger
    def stopPrinting(self):
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger
