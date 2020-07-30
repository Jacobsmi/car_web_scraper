from App.car_info import Car_Info
from App.user_parameters import User_Params
from App.scraper import Scraper


class App:
    def __init__(self):
        print("Welcome to the Car Finder Web Scraper")
        print("*"*50)

        # Create a new instance of the class creates variables and then calls set method
        self.user_params = User_Params()
        # Create a new instance of the class creates variables and then calls set method
        self.user_car = Car_Info()

        self.web_scraper = Scraper()
        # Call the get_car_page which opens the webpage and scrapes for the information
        query_result = self.web_scraper.get_car_page(
            self.user_car.CAR_MAKE, self.user_car.CAR_MODEL, self.user_car.ZIP_CODE)
        if type(query_result) is str:
            print(f"ERROR: {query_result}")
        else:
            matching_cars = self.find_matching_cars()
        self.print_matching_cars(matching_cars)

    def print_matching_cars(self, matching_cars):
        x = 1
        for car in matching_cars:
            print("CAR #{}:".format(x))
            print("YEAR: {}".format(matching_cars[0]))
            print("MAKE AND MODEL: {} {}".format(matching_cars[1], matching_cars[2]))
            print("PRICE: {}".format(matching_cars[4]))
            print("MILEAGE: {}".format(matching_cars[5]))


    def find_matching_cars(self):
        matching_cars = []
        for car in self.web_scraper.CARS:
            index = self.web_scraper.CARS.index(car)

            year_num = int(car[0])
            cost_num = int(car[4])
            mileage_num = int(car[5])
            # NEED A WAY TO CHECK FOR NEGATIVE 1
            correct_year_value = self.check_if_fit(
                year_num, self.user_params.EARLIEST_YEAR, self.user_params.LATEST_YEAR)
            correct_price_value = self.check_if_fit(
                cost_num, self.user_params.LOW_PRICE, self.user_params.HIGH_PRICE)
            correct_mileage_value = self.check_if_fit(
                mileage_num, self.user_params.LOW_MILEAGE, self.user_params.HIGH_MILEAGE)
            #print("CAR: {} \nCORRECT YEAR: {}\nCORRECT PRICE: {}\nCORRECT MILEAGE: {}\n".format(car, correct_year_value, correct_price_value, correct_mileage_value))
            # NOT SURE IF THINGS ARE BEING PROPERLY ADDED MORE TESTING IS NEEDED
            if (correct_year_value == True and correct_price_value == True) and correct_mileage_value == True:
                    matching_cars.append(car)
        return matching_cars

    def check_if_fit(self, value, low_expected, high_expected):
        if low_expected == -1 and high_expected == -1:
            return True
        elif low_expected == -1 and (high_expected != -1 and value < high_expected):
            return True
        elif (low_expected != -1 and value > low_expected) and high_expected == -1:
            return True
        elif value < low_expected or value > high_expected:
            return False
        return True
