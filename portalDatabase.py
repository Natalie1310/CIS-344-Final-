import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host='127.0.0.1',
                 port="3306",
                 database="teachers_portal",
                 user='root',
                 password='Kaosnatkat1!'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)
    

    def getAllStudents(self):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            self.cursor.callproc("studentsWithGrade")
            records = self.cursor.stored_results()
            return records

    def addStudent(self, name, courseID,grade=0):
        self.cursor = self.connection.cursor()
        add_student = "insert into students(studentName, enrolledInCourseID, grade) values (%s, %s, %s)"
        self.cursor.execute(add_student, (name, courseID, grade))
        self.connection.commit()
        self.connection.close()
        
        pass
    def addCourse(self, name):
        ''' Complete the method to insert a course to
        course table'''
        pass
    
    def modifyGrade(self, studentID, grade):
        ''' Complete the method to update the grade of the student'''
        pass
