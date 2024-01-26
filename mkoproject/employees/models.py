from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base

class Employees(Base):
    __tablename__ = 'Employees'
    EmpID = Column(Integer, primary_key=True)
    FirstName = Column(String(20))
    LastName = Column(String, max_length=20)
    StartDate = Column(Date)
    ExitDate = Column(Date, nullable=True)
    Title = Column(Strin(30))
    Supervisor = Column(String(30))
    ADEmail = Column(String, unique=True)
    EmployeeStatus = Column(String(20))
    EmployeeType = Column(String(20))
    EmployeeClassificationType = Column(String(20))
    TerminationType = Column(String(20))
    TerminationDescription = Column(String(150), nullable=True)
    DepartmentType = Column(String(20))
    Division = Column(String(20))
    DOB = Column(Date)
    State = Column(String(10))
    JobFunctionDescription = Column(String(20))
    GenderCode = Column(String(10))
    LocationCode = Column(Integer)
    RaceDesc = Column(String(10))
    MaritalDesc = Column(String(20))
    PerformanceScore = Column(String(20))
    CurrentEmployeeRating = Column(Integer)