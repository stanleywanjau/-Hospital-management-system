import click
from models.Doctor import Doctor
from models.Patient import Patient
from models.Appointment import Appointment

appointments=Appointment()
# click.echo(appointments)

@click.group()
def appointment():
  pass

@click.command()
def list_appointments():
  appointments.get_appointments()
  
@click.command()
@click.option('--doctor_id', required=True,prompt="Enter doctor ID",help="Enter doctor ID that will be see the patient")
@click.option('--patient_id', required=True,prompt="Enter patient ID",help="Enter patient ID that will be see the doctor")
@click.option('--appointment_date',required=True,prompt="Enter appointment date",help="Enter the  date the appointment will be scheduled")
@click.option('--start_time',required=True,prompt="Enter start time of the appiontment",help="Enter the start time of the appointment")
@click.option('--end_time',required=True,prompt="Enter end time of the appiontment",help="Enter the end time of the appointment")
@click.option('--notes',required=True,prompt="enter notes",help="Enter notes for the appointment")
def add(doctor_id,patient_id,appointment_date,start_time,end_time,notes):
  appointments.add_appointment(doctor_id,patient_id,appointment_date,start_time,end_time,notes)
  click.echo('Appointments booked!')

@click.command()
@click.option('--appointment_id', required=True,prompt="Enter appointment id for appointment to be deleted",help="Appointment id for appointment to be deleted")
def delete(appointment_id):
  appointments.delete_appointment(appointment_id)




appointment.add_command(list_appointments)
appointment.add_command(add)
appointment.add_command(delete)

if __name__ == '__main__':
    appointment()
