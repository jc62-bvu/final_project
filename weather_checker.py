import requests


welcome = input("Press enter if you would like to get a weather report!")

# requesting the weather information by city name.


def by_city():
    city = input('Please Enter Your City Name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=d84effb4f71a226b0846eaea10b9c1bb&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Enjoy the rest of your day!")
        exit()

# requesting the weather information by zip code.


def by_zip():
    zip_code = int(input('Please Enter Your Zip code: '))
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=d84effb4f71a226b0846eaea10b9c1bb'.format(zip_code)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Do you want to do another search? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Enjoy your day!")
        exit()

# This will display the weather information for the weather report.


def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature : {} degree fa'.format(temp))
    print('High Temperature : {} degree fa'.format(hightemp))
    print('Low Temperature : {} degree fa'.format(lowtemp))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))


# defining main function with while loop code to run the program


def main():
    while True:
        answer = input("Want to know the weather? Please type zip for zip code or city for city name: ")
        if answer == 'city':
            try:
                print("Alright, Connection established.")
                by_city()

            except Exception:
                print("Error, You did not enter a valid name. Try again")
                by_city()

        if answer == 'zip':
            try:
                print("Alright, Connection established.")
                by_zip()

            except Exception:
                print("Error, You did not enter a valid zipcode. Try again")
                by_zip()

        else:
            print("Please select either zip or city. Try again.")


main()