from dbhelpers import conn_exe_close

def number_of_rooms():
    number_of_rooms = input('Please enter number of rooms: ')
    houses = conn_exe_close('call number_of_rooms(?)',[number_of_rooms])
    if(type(houses) == list):
        return houses
    else:
        print('something went wrong')

houses = number_of_rooms()
for house in houses:
    print(house)

def house_by_city():
    city = input('Please enter the name of the city: ')
    houses = conn_exe_close('call house_in_city(?)',[city])
    if(type(houses) == list):
        return houses
    else:
        print('something went wrong')

houses_city = house_by_city()
for one_house in houses_city:
    print(one_house)