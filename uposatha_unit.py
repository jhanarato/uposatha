import datetime
import filecmp
import os
import unittest

import uposatha
from datetime import date

    
class UposathaTest(unittest.TestCase):
    calcWeekDates_out = "unit_out/calcWeekDates_out.txt"

    originalScript_good = "test_output.txt"
    originalScript_out = "unit_out/test_output.txt"
    
##  def setUp(self):
##        if os.path.exists(self.originalScript_out):
##            os.remove(self.unit_out)

    def testFormatWeek(self):
        uposathaInstance = uposatha.Uposatha()
        uposathaInstance.nextWeekStartDate = datetime.date(2011, 07, 16)
        uposathaInstance.nextWeekEndDate = datetime.date(2011, 07, 23)
        uposathaInstance.weekNum = 1
        
        expected = "Week 01: 2011-07-16 TO 2011-07-23"
        
        actual = uposathaInstance.formatWeek()
        self.assertMultiLineEqual(expected, actual)
        
    def testOriginalScript(self):
        uposathaInstance = uposatha.Uposatha()
        uposathaInstance.setOutput(self.originalScript_out)
        uposathaInstance.originalScript()

        self.assertTrue(filecmp.cmp(self.originalScript_good, self.originalScript_out))

    def testCalcWeekDates(self):
        lastWeekEndDate = datetime.date(2011, 07, 15)
        expectedStartDate = datetime.date(2011, 07, 16)
        expectedEndDate = datetime.date(2011, 07, 23)
        
        uposathaInstance = uposatha.Uposatha()
        uposathaInstance.setOutput(self.calcWeekDates_out)
        uposathaInstance.calcWeekDates(lastWeekEndDate)
        self.assertEquals(uposathaInstance.nextWeekStartDate, expectedStartDate) 
        self.assertEquals(uposathaInstance.nextWeekEndDate, expectedEndDate)
        


suite = unittest.TestLoader().loadTestsFromTestCase(UposathaTest)
unittest.TextTestRunner(verbosity=2).run(suite)            
    
