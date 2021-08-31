from KP3_main_file import List

class BusStop:
    def __init__(self, name: str, arrival_time, stop_duration_minutes):
        self.name = name
        self.arrival_time = arrival_time
        self.stop_duration_minutes = stop_duration_minutes


class BusRoute:
    def __init__(self, name: str, bus, stops: List[BusStop], time_of_stops: List[BusStop]):
        self.name = name
        self.stops = stops
        self.time_of_stops = time_of_stops
        self.bus = bus

    def get_route_date(self):
        return self.time_of_stops[0] #остановки отсортированы по времени, поэтому первое время маршрута - первая остановка

    def get_route_duration(self, dot_a, dot_b):
        time_needed, flag = 0, 0
        for i in self.stops:
            if i == dot_a:
                flag = 1
            if i == dot_b:
                flag = 0
            if flag == 1:
                time_needed += i.stop_duration_minutes
        if time_needed == 0 or flag == 1:
            return None
        else:
            return time_needed

    def get_route_itself(self, dot_a: str, dot_b: str):
        route_needed, flag = [self.name, self.bus], 0
        for i in self.stops:
            if i == dot_a:
                flag = 1
            if i in dot_b:
                flag = 0
            if flag == 1:
                route_needed += [i]
        if len(route_needed) == 0 or flag == 1:
            return "No route"
        else:
            for i in route_needed:
                return i


class Bus:
    def __init__(self, number, max_sits_count):
        self.number = number
        self.max_sits_count = max_sits_count


