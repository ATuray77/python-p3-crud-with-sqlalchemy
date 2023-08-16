#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (create_engine, desc, asc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    Index('index_name', 'name')  # helps to speed up the search for name

    #schema setup
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())  #

    # determines the structure of the printour/display
    def __repr__(self):
        return f"\n Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"

# moving stuff into the database
if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db') # engine: the python object that interfaces with the db
    Base.metadata.create_all(engine) 

# create session, student objects
     
    Session = sessionmaker(bind=engine)  # use our engine to configure a 'session' class. wraps around the engine
    session = Session() # use 'Session' class to create 'session' object which interacts with our database proper

    # Creating Records or objects which are instances of a class
    albert_einstein = Student(
        name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14,
        ),
    )

    alan_turing = Student(
        name="Alan_Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23,
        ),
    )

    aruna_turay = Student(
        name="Aruna Turay",
        email="aruna.turayg@sherborne.edu",
        grade=12,
        birthday=datetime(
            year=1977,
            month=3,
            day=1,
        ),

    )

    

#session.add(albert_einstein)  # for single record
    #session.bulk_save_objects([albert_einstein, alan_turing, aruna_turay])  # for multiple of objects
    #session.commit()

    

#students = session.query(Student.name).all() # also valid, but without the names variable
    # names = session.query(Student.name).all()
    # print(names)

    #print([student for student in students])

    # print(f"New student ID is {albert_einstein}.") # no need to use this when using bulk_save
    # print(f"New student ID is {alan_turing}.")

#ordering: using the order_by() method allows us to sort by any column
    # students_by_name = session.query(
    #     Student.name).order_by(
    #     Student.name).all()
    # print(students_by_name)

# we use desc() function from the alchemy module to sort in descending order

    # students_by_grade_desc = session.query(Student.name).order_by(desc(Student.grade)).all()
    # print(students_by_grade_desc)

# Limiting: to limit your result set to the first x records, you can use the limit() method
    # oldest_student = session.query(Student.name, Student.birthday).order_by(asc(Student.grade)).limit(1).all()
    # print(oldest_student)

#using the first() method to execute limit(1) statement and does not require a list interpretation
    # oldest_student = session.query(
    #     Student.name, Student.birthday).order_by(
    #         desc(Student.grade)).first()
    
    # print(oldest_student)

    #func() gives us access to common SQL operations through functioni like sum() and count()
    # student_count = session.query(func.count(Student.id)).first()
    # print(student_count)

    #Filtering: filter() method to filter specific record
    # query = session.query(Student).filter(Student.name.like('%Aruna%'), Student.grade==7).all()
    # print(query)
    

    #Updating Data: Use python directly then commit those sessions through sessions
    # for student in session.query(Student):
    #     student.grade += 1
    
    # session.commit()

    # print([(student.name, student.grade) for student in session.query(Student)])

# this UPDATE method does not need the session.commit() method
    # session.query(Student).update({Student.grade: Student.grade+1})
    # print([(
    #     student.name, 
    #     student.grade
    #     ) for student in session.query(Student)])
    
    

#Deleting Data: calling the delete() method
    # query = session.query(Student).filter(Student.name.like('%Alan%'))
#retrieve first matching record as object
    # alan_turing = query.first()
    # print(alan_turing)
 #delete record
    # session.delete(alan_turing)
    # session.commit()
#try to retrieve deleted record
    # alan_turing = query.first()
    # print(alan_turing)

    #No single object ready for deletion, therefore calling the delete() method from query
    #dangerous method, be careful with it
    # query = session.query(
    #     Student).filter(
    #         Student.name == "Albert Einstein")
    # query.delete()

    # albert_einstein = query.first()
    # print(alan_turing)
        
    