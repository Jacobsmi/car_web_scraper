import scraper_app
import get_user_info
def main():
    print("Welcome to the Car Finder Web Scraper")
    print("*"*50)
    query_data = get_user_info.get_car_info()
    query_status = scraper_app.get_car_page(query_data[0], query_data[1], query_data[2])
    if query_status != None:
        print(f"ERROR: {query_status}")
    
    

if __name__ == "__main__":
    main()