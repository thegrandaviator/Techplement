# WeatherAPI command-line application including CRUD operations.
 
# importing libraries. 
import requests,time

# function to fetch weather data using api calls.
def fetch_data(city_name, api_key):
    try:
        base_url = "http://api.weatherapi.com/v1/current.json"
        parameters = {
            "q" : city_name,
            "key" : api_key,
        }
        response = requests.get(base_url, params=parameters)
        if response.status_code == 200:
            print("Weather data fetched successfully.")
            print_weather_data(response.json())
        else:
            print(f"Failed to fetch current weather data for the city {city_name}. Status code: {response.status_code}\n")
            return None
    except Exception as e:
        print(f"An error occurred while fetching weather data: {str(e)}\n")
        return None

# function to print weather data in a clean format.
def print_weather_data(weather_data, indent=0):
    if weather_data:
        for key, value in weather_data.items():
            if type(value) == dict:
                print(" " * indent + f"{key}:")
                print_weather_data(value, indent+1)
            else:
                print(" " * indent + f"{key}: {value}")

# CRUD operations start here.

# function to create a city and add it to the city list.        
def create_city(city_list):
    city_name = input("Enter city name: \n")
    city_list.append(city_name)
    print(f"City '{city_name}' is added successfully.\n")

# function to read weather data.
def read_weather_data(api_key):
    city_name = input("Enter city name: \n")
    weather_data = fetch_data(city_name, api_key)
    if weather_data:
        print(f"Weather data for {city_name}: \n")
        print_weather_data(weather_data)

# function to update city names in the city list.
def update_city(city_list):
    old_city_name = input("Enter the city that you want to update: \n")
    new_city_name = input("Enter the new name for the city: \n")
    if old_city_name in city_list:
        index = city_list.index(old_city_name)
        city_list[index] = new_city_name
        print(f"'{old_city_name}' is updated to '{new_city_name}'.\n")
    else:
        print(f"'{old_city_name}' is not found.\n") 

# function to delete city names in the city list.
def delete_city(city_list):
    city_name = input("Enter city name that you want to delete: \n")
    if city_name in city_list:
        city_list.remove(city_name)
        print(f"'{city_name}' is deleted successfully.\n")
    else:
        print(f"'{city_name}' is not found.\n")

# CRUD operations end here.

# main function to initialize the api key and the city list.
def main():
    api_key = '4a607ff97a9f47dfaef111910240204'
    list_of_cities = []

# Menu driven interface for CRUD operations.
    while True:
        print("\nWeatherAPI application CRUD operation menu: ")
        print("\n")
        print("*" * 20)
        print("1. Create a city")
        print("2. Read Weather Data")
        print("3. Update a city")
        print("4. Delete a city")
        print("5. Exit the application")
        print("*" * 20)
        print("\n\n")
        print("#" * 30)
        print("Press 1 to select 'Create a city'")
        print("Press 2 to select 'Read Weather Data'")
        print("Press 3 to select 'Update a city'")
        print("Press 4 to select 'Delete a city'")
        print("Press 5 to select 'Exit the application'")
        print("#" * 30)
        print("\n\n")

        choice = input("Enter your selection: ")
        print("\n")


        if choice == '1':
            create_city(list_of_cities)
        elif choice == '2':
            print("Refreshing weather data in 15 seconds...")
            time.sleep(15)
            read_weather_data(api_key)
        elif choice == '3':
            update_city(list_of_cities)
        elif choice == '4':
            delete_city(list_of_cities)
        elif choice == '5':
            print("Exiting the application...\n")
            print("Thank you! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!\n")

# ensures that the python script is run independently and not imported anywhere.
if __name__ == '__main__':
    main()
        
          