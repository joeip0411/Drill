# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        # key = (start_station, end_station), val = [total_duration, trip_count]
        self.trip_stats = {}

        # key = id, val = (start_station, start_time)
        self.customer_trip = {}

    # O(1)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # create an entry in customer_trips
        self.customer_trip[id] = (stationName, t)

    # O(1)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # complete entry in customer_trips
        start_station = self.customer_trip[id][0]
        duration = t - self.customer_trip[id][1]

        key = (start_station, stationName)

        # update trip_stats  
        if key not in self.trip_stats:
            self.trip_stats[key] = [duration, 1]
        else:
            self.trip_stats[key][0] += duration
            self.trip_stats[key][1] += 1

        # remove entry from customer_trips
        del self.customer_trip[id]

    # O(1)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # retrieve from trip stats
        key = (startStation, endStation)

        total, count = self.trip_stats[key]
        
        return total / count