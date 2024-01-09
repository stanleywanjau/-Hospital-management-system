from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# Base = declarative_base()
from .Base import Base
engine = create_engine('sqlite:///Hospital.db')
Session = sessionmaker(bind=engine)
session = Session()

class Doctor(Base):
  __tablename__ = 'doctors'
  
  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  department=Column(String)
  phone = Column(Integer)
  
  appointments = relationship("Appointment",back_populates='doctor')
  
  def __repr__(self):
    return f"<doctor(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, department={self.department}, phone={self.phone})>"

  def add_doctor(self,first_name,last_name,department,phone):
    doctor=Doctor(first_name=first_name,last_name=last_name,department=department,phone=phone)
    session.add(doctor)
    session.commit()
  def get_doctors(self):
    return session.query(Doctor).all()

  def get_doctor_by_name(self, first_name, last_name):
    return session.query(Doctor).filter_by(first_name=first_name, last_name=last_name).first()


  def get_doctor_appointments(self, doctor_id):
    doctor = session.query(Doctor).filter_by(id=doctor_id).first()
    return doctor.appointments
  
  def delete_doctor(self, doctor_id):
    delete_doc=session.query(Doctor).filter_by(id=doctor_id).first()
    if delete_doc :
      session.delete(delete_doc)
      session.commit()
      print(f"Doctor with ID {doctor_id} deleted successfully.")
    else:
      print(f"Doctor with ID {doctor_id} not found.")