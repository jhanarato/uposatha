import datetime
import filecmp
import os
import unittest

import uposatha
from datetime import date

##startDate = datetime.date(2011, 07, 15)
##endDate = datetime.date(2011, 07, 23)
##weekNum = 1
##
##uposatha.printWeek(weekNum, startDate, endDate)
    
class UposathaTest(unittest.TestCase):
    unit_good = "test_output.txt"
    unit_out = "unit_out/test_output.txt"
    
    def setUp(self):
        if os.path.exists(self.unit_out):
            os.remove(self.unit_out)
        
    def testOriginalScript(self):
        
        uposathaInstance = uposatha.Uposatha()
        uposathaInstance.originalScript(self.unit_out)

        self.assertTrue(filecmp.cmp(self.unit_good, self.unit_out))

suite = unittest.TestLoader().loadTestsFromTestCase(UposathaTest)
unittest.TextTestRunner(verbosity=2).run(suite)            
    
