import datetime
import filecmp
import os
import unittest

import uposatha
from datetime import date

    
class UposathaTest(unittest.TestCase):
    unit_good = "test_output.txt"
    unit_out = "unit_out/test_output.txt"
    
    def setUp(self):
        i = 1
        if os.path.exists(self.unit_out):
            os.remove(self.unit_out)

    def testFormatWeek(self):
        uposathaInstance = uposatha.Uposatha()
        uposathaInstance.nextWeekStartDate = datetime.date(2011, 07, 16)
        uposathaInstance.nextWeekEndDate = datetime.date(2011, 07, 23)
        weekNum = 1
        expected = "Week 01: 2011-07-16 TO 2011-07-23"
        
        actual = uposathaInstance.formatWeek(weekNum)
        self.assertMultiLineEqual(expected, actual)

    def testcalcWeekDates(self):
        lastWeekEndDate = datetime.date(2011, 07, 15)
        expectedStartDate = datetime.date(2011, 07, 16)
        expectedEndDate = datetime.date(2011, 07, 23)
        
        uposathaInstance = uposatha.Uposatha()
        uposathaInstance.setOutput(self.unit_out)
        uposathaInstance.calcWeekDates(1, lastWeekEndDate)
        self.assertEquals(uposathaInstance.nextWeekStartDate, expectedStartDate) 
        self.assertEquals(uposathaInstance.nextWeekEndDate, expectedEndDate) 
        
    def testOriginalScript(self):
        uposathaInstance = uposatha.Uposatha()
        uposathaInstance.setOutput(self.unit_out)
        uposathaInstance.originalScript()

        self.assertTrue(filecmp.cmp(self.unit_good, self.unit_out))

suite = unittest.TestLoader().loadTestsFromTestCase(UposathaTest)
unittest.TextTestRunner(verbosity=2).run(suite)            
    
