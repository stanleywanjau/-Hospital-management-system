from sqlalchemy import Column, Integer, String,Date,Enum
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy import create_engine
from datetime import datetime

from .Base import Base
engine = create_engine('sqlite:///Hospital.db')
Session = sessionmaker(bind=engine)
session = Session()
class Patient(Base):
  __tablename__ = 'patients'
  
  id= Column(Integer, primary_key=True)
  first_name= Column(String)
  last_name= Column(String)
  sex= Column(Enum('male', 'female'))
  birth_date= Column(Date)
  phone_number = Column(String)
  email=Column( VARCHAR(255))
  addmission_date= Column(Date)
  medication= Column( VARCHAR(255))
  
  appointments = relationship("Appointment",back_populates='patient')
  
  
  def __repr__(self):
    return "<Appointment(id={self.id},first_name={self.first_name},last_name={self.last_name},sex={self.sex},birth_date={self.birth_date},phone_number={self.Phone_number},email={self.email},addmission_date={self.addmission},medication={self.medication})>"
  def add_patient_data(self,first_name,last_name,sex,birth_date,phone_number,email,addmission_date,medication):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date() 
    addmission_date = datetime.strptime(addmission_date, "%Y-%m-%d").date() 
    
    patient=Patient(first_name=first_name,last_name=last_name,sex=sex,birth_date=birth_date,phone_number=phone_number,email=email,addmission_date=addmission_date,medication=medication)
    session.add(patient)
    session.commit()