from sqlalchemy import Column, Integer, String,func
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from tabulate import tabulate
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
  patient= relationship("Patient",secondary='appointments' ,back_populates='doctor',viewonly=True)
  
  def __repr__(self):
    return f"<doctor(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, department={self.department}, phone={self.phone})>"

  
  def full_name(self):
    return f"{self.first_name} {self.last_name}"
  def add_doctor(self,first_name,last_name,department,phone):
    doctor=Doctor(first_name=first_name,last_name=last_name,department=department,phone=phone)
    session.add(doctor)
    session.commit()
  def get_doctors(self):
    doctors = session.query(Doctor).all()
    doctor_data = []

    for doctor in doctors:
            doctor_tuple = (doctor.id, doctor.first_name, doctor.last_name, doctor.department, doctor.phone)
            doctor_data.append(doctor_tuple)

    return doctor_data

  def get_doctor_by_name(self, name):
    return (
            session.query(Doctor)
            .filter(func.lower(Doctor.first_name).ilike(func.lower(f"%{name}%")) | func.lower(Doctor.last_name).ilike(func.lower(f"%{name}%")))
            .first()
        )


  def get_doctor_appointments(self, name):
        doctor = self.get_doctor_by_name(name)

        if doctor:
            appointments = doctor.appointments
            rows = []
            result = f"Appointments for Dr. {doctor.full_name()}:\n"

            for appointment in appointments:
                patient_name = appointment.patient.full_name()
                rows.append([appointment.id, patient_name, appointment.start_time, appointment.end_time, appointment.notes])
            headers = ["Appointment ID", "Patient", "Start Time", "End Time", "Notes"]
            result = tabulate(rows, headers, tablefmt="fancy_grid")

            return print(result)
        else:
            return print(f"Doctor with Name {name} not found.")
        
  
  def delete_doctor(self, name):
    delete_doc= self.get_doctor_by_name(name)
    if delete_doc :
      session.delete(delete_doc)
      session.commit()
      print(f"Doctor with Name {name} deleted successfully.")
    else:
      print(f"Doctor with Name {name} not found.")