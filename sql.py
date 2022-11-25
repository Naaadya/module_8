import sqlite3

conn = sqlite3.connect('sql.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE if not exists students(id INT PRIMARY KEY, name TEXT, surname TEXT, age INT, city TEXT)''')
conn.commit()
cursor.execute('''INSERT INTO students (id,name,surname,age,city) VALUES (1,'Max','Brooks',24,'Spb')''')
cursor.execute('''INSERT INTO students (id,name,surname,age,city) VALUES (2,'John','Stones',15,'Spb')''')
cursor.execute('''INSERT INTO students (id,name,surname,age,city) VALUES (3,'Andy','Wings',45,'Manhester')''')
cursor.execute('''INSERT INTO students (id,name,surname,age,city) VALUES (4,'Kate','Brooks',34,'Spb')''')
conn.commit()
#print('''SELECT * FROM students ''')
#cursor.execute('''SELECT * FROM students ''')
#print(cursor.fetchall())



cursor.execute('''CREATE TABLE if not exists courses(id INT PRIMARY KEY, name TEXT, time_start DATE, time_end DATE)''')
conn.commit()
cursor.execute('''INSERT INTO courses (id,name,time_start,time_end) VALUES (1,'python',DATE('2021-07-21'),DATE('2021-08-21')) ''')
cursor.execute('''INSERT INTO courses (id,name,time_start,time_end) VALUES (2,'java',DATE('2021-07-13'),DATE('2021-08-16')) ''')
conn.commit()
#print('''SELECT * FROM courses ''')
#cursor.execute('''SELECT * FROM courses ''')
#print(cursor.fetchall())


cursor.execute('''CREATE TABLE if not exists student_courses(student_id INT, course_id INT, FOREIGN KEY (student_id) REFERENCES students(id), FOREIGN KEY (course_id) REFERENCES courses(id))''')
conn.commit()
cursor.execute('''INSERT INTO student_courses (student_id,course_id) VALUES (1,1) ''')
cursor.execute('''INSERT INTO student_courses (student_id,course_id) VALUES (2,1) ''')
cursor.execute('''INSERT INTO student_courses (student_id,course_id) VALUES (3,1) ''')
cursor.execute('''INSERT INTO student_courses (student_id,course_id) VALUES (4,2) ''')
conn.commit()
#print('''SELECT * FROM student_courses ''')
#cursor.execute('''SELECT * FROM student_courses ''')
#print(cursor.fetchall())

print('''select * from students where age > 30:''')
cursor.execute('''select * from students where age > 30 ''')
for row in cursor.fetchall():
    print(f'student={row[1]}, age={row[3]}')

print('''select s.* from students s inner join student_courses sc on s.id = sc.student_id inner join courses c on sc.course_id = c.id where c.name = 'python':''')
cursor.execute('''select s.* from students s inner join student_courses sc on s.id = sc.student_id inner join courses c on sc.course_id = c.id where c.name = 'python' ''')
print(cursor.fetchall())

print('''select s.* from students s inner join student_courses sc on s.id = sc.student_id inner join courses c on sc.course_id = c.id where c.name = 'python' and s.city = 'Spb':''')
cursor.execute('''select s.* from students s inner join student_courses sc on s.id = sc.student_id inner join courses c on sc.course_id = c.id where c.name = 'python' and s.city = 'Spb' ''')
print(cursor.fetchall())
conn.close()
