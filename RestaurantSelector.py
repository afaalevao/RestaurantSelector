'''
Andrew Faalevao
Random Restaurant Selector
Python Program to select random restaurant given a location
'''


import bs4
import urllib.request as request
import random
import secrets
import tkinter


# class to store Restaurant information
class Restaurant:
    def __init__(self, name, rating, price):
        self.name = name
        self.rating = rating
        self.price = price


# print restaurant information
def get_info(restaurants):
    restaurant_list = []

    # iterate through each restaurant and print information if present
    for restaurant in restaurants:
        try:
            name = restaurant.find("a").text
            print(name)
        except:
            print("No name found.")
            name = ""

        try:
            rate = restaurant.find("div", {"class": "attribute__09f24__3znwq display--inline-block__09f24__3L1EB margin-r1__09f24__BCulR border-color--default__09f24__1eOdn"}).div.get("aria-label")
            rating = rate.split(" ")[0]
            print("Rating: " + rating)
        except:
            print("No rating found")
            rating = ""

        try:
            price = restaurant.find("span", {"class": "priceRange__09f24__2O6le css-xtpg8e"}).text
            print(price)
            if price == "$":
                price = 1
            elif price == "$$":
                price = 2
            else:
                price = 3
        except:
            print("No pricing available")
            price = 0

        # newline for spacing
        print("\n")

        r = Restaurant(name, rating, price)
        restaurant_list.append(r)

    return restaurant_list


# select restaurant from list
def select_restaurant(r_list):
    random.shuffle(r_list)  # shuffle items in list
    rand_index = secrets.randbelow(len(r_list))  # select random index
    return r_list[rand_index]


def main():

    print("Welcome to the Random Restaurant Selector!")

    # get input from user
    city = input("Enter the city where you would like to eat: ")
    food_type = input("What type of food are you craving? (Press Enter if you don't care): ")

    city = city.replace(" ", "")  # remove whitespace from city name

    url = "https://www.yelp.com/search?find_desc=" + food_type + "&find_loc=" + city
    print("\n")

    web_request = request.urlopen(url)
    page = bs4.BeautifulSoup(web_request, 'html.parser')

    # this line will need to be updated as yelp updates webpage
    restaurants = page.find_all("div", {"class": "mainAttributes__09f24__26-vh arrange-unit__09f24__3IxLD arrange-unit-fill__09f24__1v_h4 border-color--default__09f24__1eOdn"})

    print("Here are your options:\n")

    # stores restaurant name, rating, and pricing
    res_info_list = get_info(restaurants)

    select = input("Would you like the program to select a random restaurant for you from this list? (y/n)\n")

    if select.lower() == 'y':
        # get randomly selected restaurant
        rand_restaurant = select_restaurant(res_info_list)

        # print output
        print("All finished!")
        print("Looks like you're eating at " + rand_restaurant.name + " today!")
        print("Here is some info about your restaurant:")
        print("Rating (Out of 5): " + rand_restaurant.rating)
        if rand_restaurant.price is not None:
            print("Price: " + str(rand_restaurant.price))
        else:
            print("Price: Unavailable")

    print("Enjoy your meal!")


if __name__ == '__main__':
    main()
