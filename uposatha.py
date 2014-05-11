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
        
        # Print headers for table
        self._getEdge()
        self._getRow("Week", "Start", "End")
        self._getSeparator("=")
        
        for i in range(1, 12):
            self._advance()
            self._getWeek()
        self._advance()
        self._getWeek() # Last line has no line feed
        self._getEdge()
    
    def _getRow(self, col1="", col2="", col3="", page="|", fill=" ", corner="|", cornerSpace=" "):
        """
        Print the data for a row with all the widths and separators
        The output is now an ASCII table
        """
        spec = "{c:{cs}<2}{c1:{f}^4}{p:{f}^3}{c2:{f}^10}{p:{f}^3}{c3:{f}^10}{c:{cs}>2}" # Abandon all hope
        print(spec.format(
            c1=col1,
            c2=col2,
            c3=col3,
            f=fill,
            p=page,
            c=corner,
            cs=cornerSpace
        ))

    def _getSeparator(self, char):
        """Print separator row with specified character"""
        self._getRow(page="+", fill="-", corner="+", cornerSpace="-")
        
    def _getEdge(self):
        """Print table edges"""
        self._getRow(page="+", fill="-", corner="+", cornerSpace="-")
    
    def _getWeek(self):
        self._getRow(
            "{: >2d}".format(self.weekNo),
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
