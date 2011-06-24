import datetime
import filecmp
import uposatha
from datetime import date

startDate = datetime.date(2011, 07, 15)
endDate = datetime.date(2011, 07, 23)
weekNum = 1

#uposatha.printWeek(weekNum, startDate, endDate)

unit_good = "test_output.txt"
unit_out = "unit_out/test_output.txt"

uposatha.originalScript(unit_out)

if filecmp.cmp(unit_good, unit_out) == True:
    print "unit test passed"
else:
    print "unit test failed"

    
