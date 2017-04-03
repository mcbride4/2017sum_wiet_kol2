#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class Class_id(object):
  def __init__(class_id):
    self.class_id = class_id
    self.students = []

  def add_student(self, student):
    self.students.append(student)

  def get_students(self):
    return self.students

  def get_avg_score(self):
    #for i in len(self.students):
    pass 

class Student(object):
  
  def __init__(name, surname, subjects, class_object, year=2016):
    self.name = name
    self.surname = surname
    self.subjects = subjects
    self.scores = []
    self.attendances = []
    self.class_id = class_object
    

  def add_score(self, score, subject, date):
    self.scores.append([score, subject, date])

  def get_all_scores(self):
    ret = []
    for i in len(self.scores):
      i.append(self.scores[i][0])

    return ret

  def add_attendande(self, date):
    self.attendances.append(date)

  def get_avg_score_in_class(self):
    students = self.class_object.get_students()
    students_scores = []
    for i in len(students):
      students_scores.append(i.get_all_scores)

############

class1 = Class_id(1)

subjects = ["maths", "english", "bio"]
s1 = Student("Marian", "Wozniak", subjects, class1)
s2 = Student("Wojtek", "Marian", subjects, class1)

class1.add_student(s1)
class1.add_student(s2)







