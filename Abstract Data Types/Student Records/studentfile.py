"""Implementation of the the StudentFile Record ADT using a text file
 as the input source in which each field is stored in a separate line"""


class StudentFileReader:
    """Create a new student reader instance"""
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc   # file name
        self._inputFile = None  # stores the file

    # Open a connection to the input file
    def open(self):
        self._inputFile = open(self._inputSrc, "r")

    # Close the connection to the input file
    def close(self):
        self._inputFile.close()     # function closes our open file
        self._inputFile = None  # the reset its value back to Nne

    # Extract all the student records and store them in a list.
    def fetchAll(self):
        theRecord = list()
        student = self.fetchRecord()
        while student is not None:
            theRecord.append(student)
            student = self.fetchRecord()
        return theRecord

    # Extract the next student record from the file
    def fetchRecord(self):
        """Read thr first line of the record"""
        line = self._inputFile.readline()
        if line == "":
            return None

        #   If there is another record create a storage object and fill it
        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
        return student


# Storage class used for an individual student record
class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0
