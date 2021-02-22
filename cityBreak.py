# cityBreak.py

cities = {'Paris': {'Flight' : 200, 'Hotel' : 20, 'Car' : 200},
            'London': {'Flight' : 250, 'Hotel' : 30, 'Car' : 120},
            'Dubai': {'Flight' : 370, 'Hotel' : 15, 'Car' : 80},
            'Mumbai': {'Flight' : 450, 'Hotel' : 10, 'Car' : 70},}

def one_week_cost(cities,days, budget):
    '''
    Using the dict of dicts (cities), work out the cost of a seven day stay for each city.

    Flight * 2      Cost is per flight
    Hotel * 7       Cost is per day
    Car * 1         Cost is per week
    
    '''
    flights = 0
    hotel = 0
    car = 0
    total = 0
    
    for city in cities:
        print()
        print(city)  # This is the name of the city
        city_item = cities[city]
        for item in city_item:
            amount = city_item[item]
                
            if item == 'Flight':
                flights = amount *2
                amount = flights
            if item == 'Hotel':
                hotel = amount * days
                amount = hotel
            if item == 'Car':
                car = amount 
                amount = car
            total = flights + hotel + car
            print(f' {item} Costing: £{amount}')
        print(f'Total cost for {city} is: £{total}')
        if total >= budget:
            print(f'Your budget is short by {(total-budget)}')
        else:
            print('Your budget is enough.')


one_week_cost(cities, 4,800)