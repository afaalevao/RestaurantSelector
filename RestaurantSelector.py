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


# print restaurant information
def print_restaurants(restaurants):
    restaurant_list = []

    # iterate through each restaurant and print information
    for restaurant in restaurants:
        try:
            name = restaurant.find("a").text
            print(name)
        except:
            print("No name found.")

        try:
            rate = restaurant.find("div", {"class": "attribute__09f24__3znwq display--inline-block__09f24__3L1EB margin-r1__09f24__BCulR border-color--default__09f24__1eOdn"}).div.get("aria-label")
            rating = rate.split(" ")[0]
            print("Rating: " + rating)
        except:
            print("No rating found")

        try:
            price = restaurant.find("span", {"class": "priceRange__09f24__2O6le css-xtpg8e"}).text
            print(price)
        except:
            print("No pricing available")

        # newline for spacing
        print("\n")

        r = Restaurant(name, rating, price)
        restaurant_list.append(r)

    return restaurant_list


def main():
    print("Welcome to the Random Restaurant Selector!")

    # get input from user
    city = input("Enter the city where you would like to eat: ")
    price_range = input("How much money would you like to spend? ($, $$, $$$): ")
    want_type = input("Would you like to eat a specific type of food? (y/n): ")
    want_rating = input("Would you like to filter out restaurants less than a certain rating? (y/n): ")

    city = city.replace(" ", "")  # remove whitespace from city name
    food_type = ""
    min_stars = 0

    if want_type == "y":
        food_type = input("What type of food do you want to eat? (Japanese, Mexican, etc.): ")

    if want_rating == "y":
        min_stars = input("What is the minimum number of stars you would like? (out of 5): ")

    url = "https://www.yelp.com/search?find_desc=" + food_type + "&find_loc=" + city
    print("\n")

    web_request = request.urlopen(url)
    page = bs4.BeautifulSoup(web_request, 'html.parser')

    # this line will need to be updated as yelp updates webpage
    restaurants = page.find_all("div", {"class": "mainAttributes__09f24__26-vh arrange-unit__09f24__3IxLD arrange-unit-fill__09f24__1v_h4 border-color--default__09f24__1eOdn"})

    res_info_list = print_restaurants(restaurants)


if __name__ == '__main__':
    main()
