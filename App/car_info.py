class Car_Info:
    def __init__(self):
        self.CAR_MAKE = ""
        self.CAR_MODEL = ""
        self.ZIP_CODE = ""
        self.get_car_info()

    def get_mandm_info(self,s):
        # Get the car make from the user
        INFO = input("Enter the {}:".format(s))
        # Small user input validation for now
        if not INFO:
            print("Check the {} on https://cargurus.com".format(s))
            print("Please enter a valid {}".format(s))
            get_car_info(s)
        else:
            return INFO.capitalize()


    def get_zip_code(self):
        ZIP_CODE = input("Enter your Zip Code:")
        # Small user input validation for now
        if not ZIP_CODE.isdigit() or len(ZIP_CODE) != 5:
            print("Please enter a valid zip code")
            get_zip_code()
        else:
            return ZIP_CODE


    def get_car_info(self):
        print("CAR PARAMETERS")
        print("-"*50)
        self.CAR_MAKE = self.get_mandm_info("Make")
        self.CAR_MODEL = self.get_mandm_info("Model")
        self.ZIP_CODE = self.get_zip_code()