#using unittest library
import unittest

#Unit testing test cases for the inputs
#Comment out the functions not being tested in order for it to test correctly.


class Tester(unittest.TestCase):

    def initializer(self):
        print("Test")
        self.num = 1


#symbol test cases:

    def symbolTest1(self):
        symbol("GOOGL")
    # # numbers
    # def symbolTest2(self):
    #     symbol("G00GL")
    # #lowercase 
    # def symbolTest3(self):
    #     symbol("Googl")


#chart type test cases
    
    def chartTypeTest1(self):
        choice = chartType(self.num)
        self.assertEqual(choice, 1)

        self.num = 2
        choice2 = chartType(self.num)
        self.assertEqual(choice2, 2)
    # #wrong range
    # def chartTypeTest2(self):
        
    #     self.num = 3
    #     choice3 = chartType(self.num)
    #     self.assertEqual(choice3, 3)
    # #string used
    # def chartTypeTest3(self):
    #     self.num = "String"
    #     stringChoice = chartType(self.num)


#time series test cases
    #number used
    def timeSeriesTest1(self):
        choice = timeSeries(self.num)
        self.assertEqual(choice, 1)

    #     #self.num = 4
    #     #choice2 = timeSeries(self.num)
    #     #self.assertEqual(choice2, 4)
    # #string used
    # def timeSeriesTest2(self):
    #      self.num = "String"
    #      stringChoice = timeSeries(self.num)


#start and end date test cases
    def startDateTest1(self):
        
        self.testDate = "2021-01-01"
        choice = startDate(self.testDate)
        self.assertEqual(choice, self.testDate)
    # def startDateTest2(self):
    #     #wrong month
    #      self.testDate = "2021-042-01"
    #      choice = startDate(self.testDate)
    #      self.assertEqual(choice, self.testDate)
    # def startDateTest3(self):
    #     #string
    #      self.testDate = "2021-0r-01"
    #      choice = startDate(self.testDate)
    #      self.assertEqual(choice, self.testDate)

    def endDateTest1(self):
        
        self.testDate = "2021-01-01"
        choice = endDate(self.testDate)
        self.assertEqual(choice, self.testDate)
    # def endDateTest2(self):
    #     #wrong month
    #      self.testDate = "2021-042-01"
    #      choice = endDate(self.testDate)
    #      self.assertEqual(choice, self.testDate)
    # def endDateTest3(self):
    #     #string
    #      self.testDate = "2021-0r-01"
    #      choice = endDate(self.testDate)
    #      self.assertEqual(choice, self.testDate)


class Except(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error
    
    def throwException(var):
        if var.isalpha:
            raise Except("The symbol field contains numerical values", 4242)
        else:
            return True



#Validation tests for symbol, type of chart, time series, start and end date with specific criteria as part of the exception 


#symbol: capitalized, 1-7 alpha characters
def symbol_input(symbol):
    numberInput = any(map(str.isdigit, symbol))
    lowerInput = any(map(str.islower, symbol))
    if numberInput == True:
        raise ValueError("The Stock Symbol cannot be a numerical value. Please enter Uppercase alphabetical characters only")
    elif len(symbol) < 1 or len(symbol) >7:
        raise ValueError("The stock symbol has to be between 1 and 7 characters")
    elif lowerInput == True:
        raise ValueError("The Stock Symbol needs to be entered with uppercase alphabetical characters only")
    return symbol



#Condition for chart type: 1 numeric character, 1 or 2
def chartType(chart):
    if chart not in range(1,3):    
        raise ValueError("The value entered is either a string or not a value that is not 1 or 2. Please enter an acceptable value")
    else:
        return chart

#Condition for time series: 1 numeric character, 1 - 4
def timeSeries(tseries):
    if tseries not in range(1,5):    
        raise ValueError("The value entered is either a string or not a value that is not between 1 and 4. Please enter an acceptable value")
    else:
        return tseries

#Condition for start date: date type YYYY-MM-DD
def startDate(date):
    stringCheck = any(map(str.isalpha, date))
    if stringCheck == True:
        raise ValueError("The date cannot have any letters")
    if len(date) != 10:
        raise ValueError("Date format has been entered incorrectly. Please enter it in YYYY-MM-DD format")
    # splitting the date up using -
    dList = date.split("-")
    if (len(dList[0]) != 4) or (len(dList[1]) != 2) or (len(dList[2]) != 2):
        raise ValueError("Date format has been entered incorrectly. Please enter it in YYYY-MM-DD format")
    else:
        return date

#Condition for end date: date type YYYY-MM-DD
def endDate(date):
    stringCheck = any(map(str.isalpha, date))
    if stringCheck == True:
        raise ValueError("The date cannot have any letters")
    if len(date) != 10:
        raise ValueError("Date format has been entered incorrectly. Please enter it in YYYY-MM-DD format")
    # splitting using -
    dList = date.split("-")
    if (len(dList[0]) != 4) or (len(dList[1]) != 2) or (len(dList[2]) != 2):
        raise ValueError("Date format has been entered incorrectly. Please enter it in YYYY-MM-DD format")
    else:
        return date

#runs the tests
if __name__ == '__main__':
    unittest.main()
       
#Referenced:
#stock data visualizer program created with group- Project 3
#https://www.youtube.com/watch?v=HKTyOUx9Wf4
#https://www.youtube.com/watch?v=LxbiAHGkPhk
#https://www.youtube.com/watch?v=LxbiAHGkPhk
#https://realpython.com/python-map-function/
#https://www.w3schools.com/python/ref_string_isalpha.asp
#https://www.tutorialspoint.com/unittest_framework/unittest_framework_assertion.htm
#https://www.w3schools.com/python/ref_string_isdigit.asp
#https://www.w3schools.com/python/ref_string_islower.asp
