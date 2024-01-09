from sqlalchemy import Column, Integer, String,Date,Enum
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session
from sqlalchemy.dialects.mysql import VARCHAR


from .Base import Base

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