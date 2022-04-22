from collections import defaultdict

class UndergroundSystem(object):

    def __init__(self):
        # customer_id: (start_time, start_station)
        self.check_in = defaultdict(tuple)
        # (start_station, end_station): end_time - start_time 
        self.check_out = defaultdict(list)


    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.check_in[id] = (t, stationName)


    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start_time, start_station = self.check_in[id]
        total_time = t - start_time
        self.check_out[(start_station, stationName)].append(total_time)


    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return float(sum(self.check_out[(startStation, endStation)])) / float(len(self.check_out[(startStation, endStation)]))


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
