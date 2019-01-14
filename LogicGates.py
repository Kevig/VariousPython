# Superclass of logic gate, defines label and output
class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


# 2 Input 1 output child of logic gate, provides methods for giving input
# for logic gates of AND / OR types
class BinaryGate(LogicGate):

    def __init__(self,n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+ \
                             self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+ \
                             self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: No Empty Pins Available")
        


# 1 Input gate type, child of logic gate, provides method for accepting 1 input
# for logic gate of NOT type
class UnaryGate(LogicGate):

    def __init__(self,n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+ \
                             self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error:  No Empty Pins Available")


# AndGate class, child of binary gate, uses 2 inputs, method returns result of
# boolean logic against the 2 provided inputs
class AndGate(BinaryGate):

    def __init__(self,n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a==1 and b==1:
            return 1
        else:
            return 0


# OrGate class, child of binary gate, uses 2 inputs, method returns result of
# boolean logic against the 2 provided inputs
class OrGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        
        if a==1 or b==1:
            return 1
        else:
            return 0


# NotGate class, child of UnaryGate, uses 1 input, returns the opposite       
class NotGate(UnaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        pin = self.getPin()

        if pin == 1:
            return 0
        else:
            return 1


# Connector class, takes input from 1 gate and outputs to another gate
class Connector:

    def __init__(self, fGate, tGate):
        self.fromGate = fGate
        self.toGate = tGate

        tGate.setNextPin(self)

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate
