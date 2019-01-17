class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return input("Enter Pin A input for gate "+ \
                           self.getLabel()+"-->")

    def getPinB(self):
        return input("Enter Pin B input for gate "+ \
                           self.getLabel()+"-->")
