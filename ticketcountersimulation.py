# Implementation of the main simulation class.
from arrays import Array
from arrayqueue import ArrayQueue
from people import TicketAgent, Passenger
import random

random.seed(4500)


class TicketCounterSimulation:
    '''Create a simulation object.'''

    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        '''Initialises TicketCounterSimulation class.'''
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        # Simulation components.
        self._passengerQ = ArrayQueue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)
        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0
        self.count = 0

    def run(self):
        '''
        Run the simulation using the parameters supplied earlier.
        '''
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    def _handleArrival(self, curTime):
        '''Handles simulation rule1 - arrival'''
        # if self._passengerQ.isEmpty():
        #     self._passengerQ.add(Passenger(1, curTime))
        # else:
        if random.random() <= self._arriveProb:
            self._numPassengers += 1
            pas = Passenger(self._numPassengers, curTime)
            self._passengerQ.add(pas)
            print("Time {0}: Passenger {1} arrives".format(curTime, pas.idNum()))

    def _handleBeginService(self, curTime):
        '''Handles simulation rule2 - start of the service'''
        for el in self._theAgents:
            if el.isFree():
                if not self._passengerQ.isEmpty():
                    pas = self._passengerQ.pop()
                    # print("time:", curTime - pas._arrivalTime)
                    self._totalWaitTime += curTime - pas._arrivalTime
                    el.startService(pas, curTime + self._serviceTime)
                    print("Time {0}: Agent {1} started serving passenger {2}".format(curTime, el._idNum, pas.idNum()))

    def _handleEndService(self, curTime):
        '''Handles simulation rule3 - end of the service'''
        for el in self._theAgents:
            if el.isFinished(curTime):
                print("Time {0}: Agent {1} stopped serving passenger {2}".format(curTime, el._idNum,
                                                                                 el._passenger.idNum()))
                el.stopService()

    def printResults(self):
        '''Print the simulation results.'''
        # print(self._numPassengers)
        # print("wait time", self._totalWaitTime)
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" % len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)


simu1 = TicketCounterSimulation(2, 25, 2, 3)
simu1.run()
simu1.printResults()
