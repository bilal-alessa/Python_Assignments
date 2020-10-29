class private:
    #create a normal variable along with a protected attribute
    def __init__(self):
        self.age = 30
        self._name = "Sam"
        
    def callProtected(self):
        print("Name: ", self._name)
        print("Age: ", self.age)

        
    # add in a private attribute here
    def confidential(self):
        self.__personID = '12345'
    # able to print the private attribute
    def getID(self):
        print(self.__personID)


if __name__ == "__main__":
    #calling protected variable
    obj = private()
    obj.callProtected()
    #calling private variable
    obj.confidential()
    obj.getID()

