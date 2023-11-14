
















class NumList:
    def __init__(self) -> None:
        self.__list = []

    def add_value(self, value):
        self.__list.append(value)

    def remove_value(self, value):
        rv = self.__list[-1]
        del self.__list[-1]
        return rv

    def get_list(self):
        return self.__list
    
    def print_list(self):
        return self.__list

class Customer01(NumList):
    def __init__(self):
        # NumList.__init__(self)
        super().__init__()

    def get_total(self):
        return sum(self.get_list())

# cus = Customer01()
# num = NumList()
# print(cus.print_list())
# print(cus.add_value(2))
# print(cus.add_value(3))
# print(cus.print_list())
# print(cus.remove_value(2))
# print(cus.get_total())


class NumListB:
    def __init__(self, name= ""):
        pass




    # def get_total(self):
    #     tot = sum(self.__list)
    #     return tot
