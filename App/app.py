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
        query_result = self.web_scraper.get_car_page(self.user_car.CAR_MAKE, self.user_car.CAR_MODEL, self.user_car.ZIP_CODE)
        if type(query_result) is str:
            print(f"ERROR: {query_result}")
        else:
            self.find_matching_cars()

    def find_matching_cars(self):
        print("This will find matching cars")