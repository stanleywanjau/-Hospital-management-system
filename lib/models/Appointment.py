from sqlalchemy import Column, Integer, String, ForeignKey,Date,Time,Text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session
from sqlalchemy import create_engine
from datetime import datetime
from .Doctor import Doctor
from tabulate import tabulate


from .Base import Base
engine = create_engine('sqlite:///Hospital.db')
Session = sessionmaker(bind=engine)
session = Session()
class Appointment(Base):
  __tablename__ = 'appointments'
  
  id = Column(Integer, primary_key=True)
  doctor_id = Column(Integer, ForeignKey('doctors.id'))
  patient_id = Column(Integer, ForeignKey('patients.id'))
  Appointment_date= Column(Date)
  start_time=Column(Time)
  end_time=Column(Time)
  notes=Column(Text)
  
  doctor = relationship('Doctor',back_populates='appointments')
  patient = relationship('Patient',back_populates='appointments')
  
  
  def __repr__(self):
    return f"<Appointment(id={self.id},doctor-id={self.doctor_id},patient_id={self.patient_id},start_time={self.start_time},end_time={self.end_time},notes={self.notes})>"
  
    
  
  def get_appointments(self):
    appointments = session.query(Appointment).all()
    records = []

    for appointment in appointments:
      doctor_name = appointment.doctor.full_name()
      patient_name = appointment.patient.full_name()
      record = {
                "Appointment ID": appointment.id,
                "Doctor": doctor_name,
                "Patient": patient_name,
                "Start Time": appointment.start_time,
                "End Time": appointment.end_time,
                "Notes": appointment.notes
              }
      records.append(record)

    return records
  
  
  def add_appointment(self,doctor_id,patient_id,appointment_date,start_time,end_time,notes):
    #conver the date string to python date objects
    appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d").date()
    # Convert the string times to Python time objects
    start_time = datetime.strptime(start_time, "%H:%M:%S").time()
    end_time = datetime.strptime(end_time, "%H:%M:%S").time()
    appointment=Appointment(doctor_id=doctor_id,patient_id=patient_id,Appointment_date=appointment_date,start_time=start_time,end_time=end_time,notes=notes)
    session.add(appointment)
    session.commit()
  def delete_appointment(self,appointment_id):
    appointment_to_delete =session.query(Appointment).filter_by(id=appointment_id).first()
    if appointment_to_delete :
      session.delete(appointment_to_delete)
      session.commit()
      print(f"Appointment with ID {appointment_id} deleted successfully.")
    else:
        print(f"Appointment with ID {appointment_id} not found.") 