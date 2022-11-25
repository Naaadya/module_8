from peewee import *
import datetime

conn = SqliteDatabase('orm.db')

class Student(Model):
    id = PrimaryKeyField()
    name = TextField(column_name="name")
    surname = TextField(column_name="surname")
    age = IntegerField(column_name="age")
    city = TextField(column_name="city")
    class Meta:
        database = conn


class Course(Model):
    id = PrimaryKeyField()
    name = TextField(column_name="name")
    time_start = DateField()
    time_end = DateField()
    class Meta:
        database = conn


class Student_Course(Model):
    student_id = ForeignKeyField(Student, to_field="id")
    course_id = ForeignKeyField(Course, to_field="id")
    class Meta:
        database = conn

Student.create_table()
Course.create_table()
Student_Course.create_table()


student1 = Student(name="Max", surname="Adams", age=24, city="Spb")
student1.save()
student2 = Student(name="John", surname="Stones", age=15, city="Spb")
student2.save()
student3 = Student(name="Andy", surname="Wings", age=45, city="Manhester")
student3.save()
student4 = Student(name="Kate", surname="Brooks", age=34, city="Spb")
student4.save()

course1 = Course(name="python", time_start=datetime.date(2021, 7, 21), time_end=datetime.date(2021, 8, 21))
course1.save()
course2 = Course(name="java", time_start=datetime.date(2021, 7, 13), time_end=datetime.date(2021, 8, 16))
course2.save()

student_course1 = Student_Course(student_id = student1, course_id = course1)
student_course1.save()
student_course2 = Student_Course(student_id = student2, course_id = course1)
student_course2.save()
student_course3 = Student_Course(student_id = student3, course_id = course1)
student_course3.save()
student_course4 = Student_Course(student_id = student4, course_id = course2)
student_course4.save()

query1 = Student.select().where(Student.age>30)
for row in query1:
    print(f'student={row.name}, age={row.age}')

query2 = Student.select(Student,Student_Course,Course).join(Student_Course).join(Course).where(Course.name=="python")
for row in query2:
    print(f'student={row.name}, course={row.student_course.course_id.name}')

query3 = Student.select(Student,Student_Course,Course).join(Student_Course).join(Course).where(Student.city=='Spb').where(Course.name=="python")
for row in query3:
    print(f'student={row.name}, city={row.city}')