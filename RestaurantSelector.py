'''
Andrew Faalevao
Random Restaurant Selector
Python Program to select random restaurant given a location
'''


import bs4
import urllib.request as request


# class to store Restaurant information
class Restaurant:
    def __init__(self, name, rating, price):
        self.name = name
        self.rating = rating
        self.price = price


def print_restaurants(restaurants):
    # iterate through each restaurant and print information
    for restaurant in restaurants:
        try:
            name = restaurant.find("a").text
            print(name)
        except:
            print("No name found.")

        try:
            rating = restaurant.find("div", {"class": "attribute__09f24__3znwq display--inline-block__09f24__3L1EB margin-r1__09f24__BCulR border-color--default__09f24__1eOdn"}).div.get("aria-label")
            print(rating)
        except:
            print("No rating found")

        try:
            price = restaurant.find("span", {"class": "priceRange__09f24__2O6le css-xtpg8e"}).text
            print(price)
        except:
            print("No pricing available")

        # newline for spacing
        print("\n")


def main():
    print("Welcome to the Random Restaurant Selector!")

    # get input from user
    city = input("Enter the city where you would like to eat: ")
    option = input("Would you like to eat a specific type of food? (y/n): ")
    food_type = ""

    if option == "y":
        food_type = input("What type of food do you want to eat? (Japanese, Mexican, etc.): ")

    url = "https://www.yelp.com/search?find_desc=" + food_type + "&find_loc=" + city
    print("\n")

    web_request = request.urlopen(url)
    page = bs4.BeautifulSoup(web_request, 'html.parser')

    # this line will need to be updated as yelp updates webpage
    restaurants = page.find_all("div", {"class": "mainAttributes__09f24__26-vh arrange-unit__09f24__3IxLD arrange-unit-fill__09f24__1v_h4 border-color--default__09f24__1eOdn"})

    print_restaurants(restaurants)


if __name__ == '__main__':
    main()
