'''
Andrew Faalevao
Random Restaurant Selector
Python Program to select random restaurant given a location
'''


from geopy.geocoders import Nominatim


def main():
    geolocator = Nominatim(user_agent="my_user_agent")
    location = input("Enter your location (city, state, country): ")

    city = location.split(',')[0]
    state = location.split(',')[1]
    country = location.split(',')[2]

    loc = geolocator.geocode(city + ',' + state + ',' + country)
    print("latitude:", loc.latitude, "\nlongtitude:", loc.longitude)


if __name__ == '__main__':
    main()
