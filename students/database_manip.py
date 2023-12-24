import sqlite3

# Create a student database to create python_programming table.
db = sqlite3.connect('student_db')

# Get cursor object.
cursor = db.cursor()

cursor.execute(''' 
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade
               INTEGER)
''')
db.commit()

id1 = 55
name1 = 'Carl Davis'
grade1 = 61

id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

id3 = 77
name3 = 'Jane Richards'
grade3 = 78

id4 = 12
name4 = 'Peyton Swayer'
grade4 = 45

id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

# List to store students id, name, grade.
students_grades = [(id1, name1, grade1), (id2, name2, grade2),
                  (id3, name3, grade3), (id4, name4, grade4),
                  (id5, name5, grade5)]

# Insert student grades into python_programming table.
cursor.executemany('''INSERT INTO python_programming(id, name, grade)
                    VALUES(?,?,?)''', students_grades)
db.commit()
print('Information has been inserted.')

# Retrieve information from python_programming table.
cursor.execute('''SELECT id, name, grade FROM python_programming 
               WHERE grade BETWEEN 60 AND 80 ''')
for row in cursor:        
    print('{0}: {1} : {2}'.format(row[0], row[1], row[2]))
db.commit()

# Update student grade where student id == 55.
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id = ?''',
               (65, 55))
db.commit()
print("Carl Davis's grade has been updated.")

# Remove student id 66 from python programming table.
cursor.execute('''DELETE FROM python_programming WHERE id = ?''', (66,))
db.commit()

# Update students whose id is between 55 and 80 to 100.
cursor.execute('''UPDATE python_programming SET grade = 80
                   WHERE id > 55''')
db.commit()
print('Student grades have been updated.')

db.close()
