import datetime
import filecmp
import unittest

import uposatha
from datetime import date

#startDate = datetime.date(2011, 07, 15)
#endDate = datetime.date(2011, 07, 23)
#weekNum = 1

#uposatha.printWeek(weekNum, startDate, endDate)

class OriginalScriptTest(unittest.TestCase):
    def testOriginalScript(self):
        unit_good = "test_output.txt"
        unit_out = "unit_out/test_output.txt"

        uposatha.originalScript(unit_out)

        self.assertTrue(filecmp.cmp(unit_good, unit_out))

suite = unittest.TestLoader().loadTestsFromTestCase(OriginalScriptTest)
unittest.TextTestRunner(verbosity=2).run(suite)            
    
