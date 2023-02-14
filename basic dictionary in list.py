travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(n_country,c_visits,city):
    add_country = {}
    add_country["country"] = n_country
    add_country["visits"] = c_visits
    add_country["cities"] = city
    travel_log.append(add_country)
    print(travel_log)
def inputs():
    country = input("What country did you visit?: ")
    visit = int(input("How many times have you visit it?: "))
    num_city = int(input("How many cities did you visit?: "))
    cities = []
    for ct in range(num_city):
        city = input("What city did you visit?: ")
        cities.append(city)
    add_new_country(country, visit, cities)

inputs()
again = True
while again:
    try_again = input("Do you want to add another country? Yes or No: ").lower()
    if try_again != "yes" and try_again != "no":
        print("Yes or No only Please!")
    elif try_again == "no":
        again = False
    else:
        inputs()


