''' 
In this module we will set user parameters to be checked against once information has been retrieved and parsed
'''
class User_Params:
    def __init__(self):
        self.LOW_PRICE = -1
        self.HIGH_PRICE = -1
        self.LOW_MILEAGE = -1 
        self.HIGH_MILEAGE = -1
        self.EARLIEST_YEAR = -1
        self.LATEST_YEAR = -1
        self.set_user_params()


    def set_numbers(self,category,hol):
        in_num = input("Enter the {} {} you want: ".format(hol, category))
        try:
            if not in_num:
                return -1
            else:
                return int(in_num)
        except:
            print("Enter valid input please")
            set_numbers(category,hol)


    def set_user_params(self):
        print("USER PARAMETERS")
        print("-"*50)
        self.LOW_PRICE = self.set_numbers("price","lowest")
        self.HIGH_PRICE = self.set_numbers("price","highest")
        self.LOW_MILEAGE = self.set_numbers("mileage","lowest")
        self.HIGH_MILEAGE = self.set_numbers("mileage","highest")
        self.EARLIEST_YEAR = self.set_numbers("year","earliest")
        self.LATEST_YEAR = self.set_numbers("year","latest")