#!/usr/bin/env python3

import argparse
from datetime import date, datetime, timedelta

class Uposatha:
    def __init__(self, prevUpo):
        """
        Constructor
        
        prevUpo: the Uposatha prior to season. Begins as yyyy/mm/dd str,
        converted to date.
        
        nextA, nextB = start/end days of next week
        lastB = end day of last week
        """
        self.rains = [8,7, 8,7, 7,7, 8,7, 8,7, 8,7, 7,7, 8,7]
        self.weekNo = 0 # Current week index
        
        self.nextB = datetime.strptime(prevUpo, "%Y/%m/%d").date()
        self.nextA = None # initialised by advance()
    
    def calendar(self):
        """Print starting and ending date for week ending in Uposatha"""
        
        """
        Print headers for table
        * three columns of 8, 10, and 10 chars
        * the center() string pads out those columns with desired character
        """
        self._getRow("Week", "Start", "End", page="")
        self._getSeparator("=")
        
        for i in range(1, 12):
            self._advance()
            self._getWeek()
        self._advance()
        self._getWeek() # Last line has no line feed
    
    def _getRow(self, col1="", col2="", col3="", page="|", fill=" "):
        """Print the data for a row with all the widths and separators"""
        spec = "{c1:{f}^7}{p:{f}^3}{c2:{f}^10}{p:{f}^3}{c3:{f}^10}"
        print(spec.format(
            c1=col1,
            c2=col2,
            c3=col3,
            f=fill,
            p=page
        ))

    def _getSeparator(self, char):
        """Print separator row with specified character"""
        self._getRow(page="+", fill="-")
    
    def _getWeek(self):
        self._getRow(
            "Week {:02d}".format(self.weekNo),
            self.nextA.isoformat(),
            self.nextB.isoformat()
        )
    
    def _advance(self):
        lastB = self.nextB
        # next week's start is the day after last week's end
        self.nextA = lastB + timedelta(1)
        # next week's end depends on the pattern of days in self.rains
        self.nextB = lastB + timedelta(self.rains[self.weekNo])
        self.weekNo += 1

if __name__ == "__main__":
    """Command-line arguments"""
    arg = argparse.ArgumentParser()
    arg.add_argument("prevUpo", help="yyyy/mm/dd of Uposatha prior to season, E.g. 2011/07/15, 2014/07/11")
    args = arg.parse_args()

    """Make Uposatha calendar"""
    u = Uposatha(args.prevUpo)
    u.calendar()
