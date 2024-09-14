class employee:
    def __init__(self,name,id,password):
        self.name = name
        self.id = id
        self.__password = password


    def changepassword(self,password):
        self.__password=password

    def printpassword(self):
        print(self.__password)
        

newemploye = employee("akash",712639,43543)
print(newemploye.name)
print(newemploye.id)
newemploye.changepassword(56476)
newemploye.printpassword()
