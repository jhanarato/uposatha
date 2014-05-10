#!/usr/bin/env python3

from datetime import date, datetime, timedelta

class Uposatha:
    def __init__(self, filename, prevUpo):
        self.rains = [8,7, 8,7, 7,7, 8,7, 8,7, 8,7, 7,7, 8,7]
        self.weekNo = 0 # Current week index
        
        """prevUpo: the Uposatha prior to season
        Begins as yyyy/mm/dd str, converted to date"""
        prevUpo = datetime.strptime(prevUpo, "%Y/%m/%d").date()
        self.nextB = prevUpo
        self.nextA = None # initialised by advance()
    
    def calendar(self):
        """Print starting and ending date for week ending in Uposatha"""
        for i in range(1, 12):
            self._advance()
            print(self._getWeek())
        self._advance()
        print(self._getWeek()) # Last line has no line feed
    
    def _getWeek(self):
        return "Week {no:02d}: {start} -> {end}".format(
            no=self.weekNo,
            start=self.nextA.isoformat(),
            end=self.nextB.isoformat()
        )
    
    def _advance(self):
        lastB = self.nextB
        self.nextA = lastB + timedelta(1)
        self.nextB = lastB + timedelta(self.rains[self.weekNo])
        self.weekNo += 1

if __name__ == "__main__":
    u = Uposatha("out.txt", "2014/7/11")
    u.calendar()
