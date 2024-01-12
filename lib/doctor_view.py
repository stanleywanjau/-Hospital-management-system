# views/doctor_view.py
import click
from models.Doctor import Doctor
from models.Patient import Patient
from models.Appointment import Appointment

doctor_cls = Doctor()

@click.group()
def doctor():
    pass

@click.command()

@click.option('--first_name', prompt="Enter first name", help='first name of the doctor')
@click.option('--last_name', prompt="Enter last name", help='last name of the doctor')
@click.option('--department', prompt="Enter department", help='the department of the doctor')
@click.option('--phone', prompt="Enter phone number", help='phone number of the doctor')

def add(first_name,last_name,department,phone):
    doctor_cls.add_doctor(first_name,last_name,department,phone)
    click.echo('Doctor added successfully!')

@doctor.command()
def list():
    doctors=doctor_cls.get_doctors()
    for doctor in doctors:
        click.echo(f"Doctor ID: {doctor.id}, Name: {doctor.full_name()} ,department: {doctor.department}")
@click.command()
@click.option('--name', required=True ,help="enter  name" ,prompt="Enter name")
# @click.option('--last_name', required=True ,help="enter last name" ,prompt="Enter last name")
def search_doctor(name):
    doctor =doctor_cls. get_doctor_by_name(name)
    if doctor is not None:
        click.echo(f"found {doctor.full_name()}")
    else:
        click.echo(f"{name} not found")

@click.command()
@click.option('--name',required=True,help="Name of the the doctor",prompt="Name of the doctor")
def get_appointment_for_doc(name):
    doctor=doctor_cls.get_doctor_appointments(name)
    # print(doctor)
    if doctor is not None:
        # patient=doctor.patient
        # print(patient)
        for appointment in doctor:
            print(f"Appointment ID: {appointment}, Name:{appointment.notes} ")
    else:
        print("Doctor not found.")
@click.command()
@click.option('--name',required=True,help="Name of doctor to delete",prompt="Name of doctor to delete")
def delete (name):
    doctor_cls.delete_doctor(name)
    
    
doctor.add_command(list)
doctor.add_command(add)
doctor.add_command(search_doctor)
doctor.add_command(get_appointment_for_doc)
doctor.add_command(delete)
if __name__ == '__main__':
    doctor()

# @doctor.command()
# @click.option('--id', prompt=True, help='ID of the doctor')
# def appointments(id):
#     doctor = doctor_controller.get_doctor_by_name(id)
#     appointments = doctor_controller.get_doctor_appointments(id)
#     click.echo(f"Appointments for Doctor {doctor.name}:")
#     for appointment in appointments:
#         click.echo(f"Appointment ID: {appointment.id}, Patient: {appointment.patient.name}")

