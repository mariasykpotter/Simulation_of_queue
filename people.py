class Passenger:
    '''Used to store and manage information related to an airline passenger.'''

    def __init__(self, idNum, arrivalTime):
        '''Creates a passenger object.'''
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    def idNum(self):
        '''
        Gets the passenger's id number.
        :return: int
        '''
        return self._idNum

    def timeArrived(self):
        '''
        Gets the passenger's arrival time.
        :return: int
        '''
        return self._arrivalTime


class TicketAgent:
    '''Used to store and manage information related to an airline ticket agent.'''

    def __init__(self, idNum):
        '''Creates a ticket agent object.'''
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1

    def idNum(self):
        '''
        Gets the ticket agent's id number.
        :return: int
        '''
        return self._idNum

    def isFree(self):
        '''
         Determines if the ticket agent is free to assist a passenger.
        :return: bool
        '''
        return self._passenger is None

    def isFinished(self, curTime):
        '''
         # Determines if the ticket agent has finished helping the passenger.
        :param curTime: int
        :return: bool
        '''
        return self._passenger is not None and self._stopTime == curTime

    def startService(self, passenger, stopTime):
        '''
        Indicates the ticket agent has begun assisting a passenger.
        :param passenger: Passenger
        :param stopTime: int
        :return: None
        '''
        self._passenger = passenger
        self._stopTime = stopTime

    def stopService(self):
        '''
         Indicates the ticket agent has finished helping the passenger.
        :return: Passenger
        '''
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger
