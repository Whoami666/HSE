import datetime
from KP3_classes_file import BusStop, Bus, BusRoute

buses = [
    Bus("bus1", 20),
    Bus("bus2", 15),
    Bus("bus3", 31)
]

routes = [
    BusRoute("Route1", buses[0], ["stop1", "stop2"], [datetime.date(2000, 3, 12), datetime.date(2000, 4, 13)]),
    BusRoute("Route2", buses[1], ["stop2", "stop3"], [datetime.date(2001, 3, 12), datetime.date(2001, 4, 13)]),
    BusRoute("Route3", buses[2], ["stop4", "stop5"], [datetime.date(2002, 3, 12), datetime.date(2002, 4, 13)])
]

busstops = [
    BusStop("stop1", datetime.date(2000, 3, 12), 23),
    BusStop("stop2", datetime.date(2000, 4, 13), 20),
    BusStop("stop3", datetime.date(2001, 4, 13), 5),
    BusStop("stop4", datetime.date(2002, 3, 12), 1),
    BusStop("stop5", datetime.date(2002, 4, 13), 10)
]


def find_routes_by_date(date):
    for route in routes:
        if route.get_route_date() == date:
            print(route[0], "-", route[2][0])
            for i in range(len(route[2])):
                print(route[2][i], "-", route[3][i])


while True:
    print("введите название 1 точки")
    dotA = input()
    print("введите название 2 точки")
    dotB = input()
    print(BusRoute.get_route_itself(dotA, dotB))

