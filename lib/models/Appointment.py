from sqlalchemy import Column, Integer, String, ForeignKey,Date,Time,Text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session


from .Base import Base

class Appointment(Base):
  __tablename__ = 'appointments'
  
  id = Column(Integer, primary_key=True)
  doctor_id = Column(Integer, ForeignKey('doctors.id'))
  patient_id = Column(Integer, ForeignKey('patients.id'))
  Appointment_date= Column(Date)
  start_time=Column(Time)
  end_time=Column(Time)
  notes=Column(Text)
  
  
  def __repr__(self):
    return f"<Appointment(id={self.id},doctor-id={self.doctor_id},patient_id={self.patient_id},start_time={self.start_time},end_time={self.end_time},notes={self.notes})>"
  