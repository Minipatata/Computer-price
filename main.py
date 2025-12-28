class Computer:
    def __init__(self,max_price):
        self.__max_price=max_price
    def display(self):
        print(self.__max_price)
    def sell(self,max_price):
        self.__max_price=max_price
c=Computer(15)
c.display()
c.sell(23)
c.display()