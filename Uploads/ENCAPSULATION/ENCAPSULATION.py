class private:
    #create a normal variable along with a protected attribute
    def __init__(self):
        self.age = 20
        self._name = 'Sam'
    # add in a private attribute here
    def confidential(self):
        self.__personID = '12345'
    # able to print the private attribute
    def getID(self):
        print(self.__personID)



if __name__ == "__main__":
    obj = private()
    print(obj._name, obj.age)
    obj.confidential()
    obj.getID()

