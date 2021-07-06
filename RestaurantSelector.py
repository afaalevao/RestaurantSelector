'''
Andrew Faalevao
Random Restaurant Selector
Python Program to select random restaurant given a location
'''


import bs4
import urllib.request as request
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


def main():

    print("Welcome to the Random Restaurant Selector!")

    # get input from user
    city = input("Enter the city where you would like to eat: ")
    food_type = input("What type of food are you craving? (Japanese, Mexican, etc.): ")

    city = city.replace(" ", "")  # remove whitespace from city name
    # min_stars = 0

    url = "https://www.yelp.com/search?find_desc=" + food_type + "&find_loc=" + city
    print("\n")

    web_request = request.urlopen(url)
    page = bs4.BeautifulSoup(web_request, 'html.parser')

    # this line will need to be updated as yelp updates webpage
    restaurants = page.find_all("div", {"class": "mainAttributes__09f24__26-vh arrange-unit__09f24__3IxLD arrange-unit-fill__09f24__1v_h4 border-color--default__09f24__1eOdn"})

    print("Here are your options:\n")

    # stores restaurant name, rating, and pricing
    res_info_list = get_info(restaurants)



    '''
    # ask if user wants program to select restaurant for them
    select = input("Would you like us to randomly select a restaurant for you? (y/n)")

    if select == "y":
        print("hi")
    else:
        print("Thank you, enjoy your meal!")
    '''


if __name__ == '__main__':
    main()
