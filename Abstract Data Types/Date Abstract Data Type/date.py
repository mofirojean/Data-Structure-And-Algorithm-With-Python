# implements a proleptic Gregorian calender date as a Julian day number

class Date:
    """Create an object instance for the specified Gregorian date"""

    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self._isValidGregorian(month, day, year), \
            "Invalid Gregorian date."
        # The first line of the equation, T = (M-14)/12, has to be changed
        # since python's implementation of integer division is not the same
        # as mathematical definition.
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + \
                          (1461 * (year + 4800 + tmp) // 4) + \
                          (367 * (month - 2 - tmp * 12) // 12) - \
                          (3 * ((year + 4900 + tmp) // 100) // 4)

    # Extract the appropriate Gregorian components
    def month(self):
        return (self._toGregorian())[0]  # returning M from (M, d, y)

    def day(self):
        return (self._toGregorian())[1]  # returning M from (m, D, y)

    def year(self):
        return (self._toGregorian())[2]  # returning M from (m, d, Y)

    # Return day in the week as in int (0) Mon and (6) Sun.
    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + \
                year + year // 4 - year // 100 + year // 400) % 7

    # Returns the dat as a string in Gregorian format
    def __str__(self):
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04" % (month, day, year)

    # Logically compares the two dates
    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay

    #These functions are still be implemented
    #monthName(), isLeapYear(), numDays(), advanceBy() and 
    #isValidGregorian(). The isValidGregorian()  
    # at these level .......  
    def advanceBy(self, days):
        new = self._julianDay + days
        month, day, year = self._toGregorian()
        
        
    


    # Return Gregorian date as tuple: (month, day, year).
    """Gregorian conversion Helper method that converts our julian day to a gregorian day """
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year


firstDay = Date(9, 1, 2000)
print(firstDay)
