'''
Andrew Faalevao
Random Restaurant Selector
Python Program to select random restaurant given a location
'''


from geopy.geocoders import Nominatim
import bs4
import urllib.request as request


def main():
    print("Welcome to the Random Restaurant Selector!")

    # get input from user
    city = input("Enter the city where you would like to eat: ")
    option = input("Would you like to eat a specific type of food? (y/n): ")
    type = ""

    if option == "y":
        type = input("What type of food do you want to eat? (Japanese, Mexican, etc.): ")

    url = "https://www.yelp.com/search?find_desc=" + type + "&find_loc=" + city
    print(url)

    web_request = request.urlopen(url)
    page = bs4.BeautifulSoup(web_request, 'html.parser')

    # this line will need to be updated as yelp updates webpage
    restaurants = page.find_all("div", {"class": "mainAttributes__09f24__26-vh arrange-unit__09f24__3IxLD arrange-unit-fill__09f24__1v_h4 border-color--default__09f24__1eOdn"})

    for restaurant in restaurants:
        try:
            name = restaurant.find("a").text
            print(name)
        except:
            print("No information found.")


if __name__ == '__main__':
    main()
